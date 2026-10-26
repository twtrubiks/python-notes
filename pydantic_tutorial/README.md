# pydantic 教學

今天來介紹 pydantic, pydantic 完全支援 IDE,

你可能會說已經有內建的 [PEP 484 Type Hints 介紹](https://github.com/twtrubiks/python-notes/tree/master/type-hints-tutorial) 和 [dataclasses_tutorial.py](https://github.com/twtrubiks/python-notes/blob/master/dataclasses_tutorial.py) 了, 為什麼還需要這個 ❓

原因是 pydantic 在處理 json 以及資料驗證上面比較強大 😀

我建議大家還是可以花個時間稍微看一下 😆

安裝

```cmd
pip install pydantic==2.14.1
```

[官網文件](https://docs.pydantic.dev/latest/) 寫的非常豐富,

這邊就寫一些官方的範例給大家看

- [Models](#models)

- [Fields](#fields)

- [JSON Schema](#json-schema)

- [Validators](#validators)

- [Type Adapter](#type-adapter)

- [Performance](#performance)

- [延伸閱讀](#延伸閱讀)

# 教學

## Models

[Basic model usage](https://docs.pydantic.dev/latest/concepts/models/#basic-model-usage)

```python
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str = 'Jane Doe'

# 正確的初始化
user = User(id=3)

# 錯誤的初始化 (因為定義的是 int)
user = User(id='abc')

# 可以使用 model_dump 來完成 serialized
user.model_dump() # {'id': 3, 'name': 'Jane Doe'}
```

建立 [Nested models](https://docs.pydantic.dev/latest/concepts/models/#nested-models)

```python
from typing import List, Optional

from pydantic import BaseModel


class Foo(BaseModel):
    count: int
    size: Optional[float] = None


class Bar(BaseModel):
    apple: str = 'x'
    banana: str = 'y'


class Spam(BaseModel):
    foo: Foo
    bars: List[Bar]

# 以下兩種方法都可以
m = Spam(foo={'count': 4}, bars=[{'apple': 'x1'}, {'apple': 'x2'}])
m1 = Spam(foo=Foo(count=4), bars=[Bar(apple='x1'), Bar(apple='x2')])
print(m)
print(m1)
```

[Error handling](https://docs.pydantic.dev/latest/concepts/models/#error-handling)

```python
from pydantic import BaseModel, ValidationError


class User(BaseModel):
    id: int
    name: str = 'Jane Doe'

data = dict(
    id=['1', 2, 'bad'],
)

try:
    User(**data)
except ValidationError as e:
    print(e)
```

[Generic models](https://docs.pydantic.dev/latest/concepts/models/#generic-models)

```python
from typing import Generic, List, Optional, TypeVar

from pydantic import BaseModel, ValidationError

DataT = TypeVar('DataT')


class DataModel(BaseModel):
    numbers: List[int]
    people: List[str]


class Response(BaseModel, Generic[DataT]):
    data: Optional[DataT] = None


print(Response[int](data=1))
#> data=1
print(Response[str](data='value'))
#> data='value'
print(Response[str](data='value').model_dump())
#> {'data': 'value'}

data = DataModel(numbers=[1, 2, 3], people=[])
print(Response[DataModel](data=data).model_dump())
#> {'data': {'numbers': [1, 2, 3], 'people': []}}
try:
    Response[int](data='value') # 型態錯誤
except ValidationError as e:
    print(e)
```

parametrized generic

```python
from typing import Generic, TypeVar

from pydantic import BaseModel, ValidationError

T = TypeVar('T')


class ResponseModel(BaseModel, Generic[T]):
    content: T


class Product(BaseModel):
    name: str
    price: float


class Order(BaseModel):
    id: int
    product: ResponseModel[Product]


product = Product(name='Apple', price=0.5)
response = ResponseModel[Product](content=product)
order = Order(id=1, product=response)
print(repr(order))

try:
    response = ResponseModel[int](content=product)
except ValidationError as e:
    print(e)
```

[Validation of unparametrized type variables](https://docs.pydantic.dev/latest/concepts/models/#validation-of-unparametrized-type-variables)

```python
from typing import Generic

from typing_extensions import TypeVar

from pydantic import BaseModel, ValidationError

T = TypeVar('T')
U = TypeVar('U', bound=int)
V = TypeVar('V', default=str)


class Model(BaseModel, Generic[T, U, V]):
    t: T
    u: U
    v: V


print(Model(t='t', u=1, v='v'))
#> t='t' u=1 v='v'

try:
    Model(t='t', u='u', v=1)
except ValidationError as exc:
    print(exc)
```

[Faux immutability](https://docs.pydantic.dev/latest/concepts/models/#faux-immutability)

如果 frozen 設定為 False, 是可以動態修改變數的屬性的.

```python
from pydantic import BaseModel, ConfigDict, ValidationError


class FooBarModel(BaseModel):
    model_config = ConfigDict(frozen=True)

    a: str
    b: dict


foobar = FooBarModel(a='hello', b={'apple': 'pear'})

try:
    foobar.a = 'different'
except ValidationError as e:
    print(e)
    """
    1 validation error for FooBarModel
    a
      Instance is frozen [type=frozen_instance, input_value='different', input_type=str]
    """
```

[Required fields](https://docs.pydantic.dev/latest/concepts/models/#required-fields)

以下三種方法都代表必填

```python
from pydantic import BaseModel, Field


class Model(BaseModel):
    a: int
    b: int = ... # emphasize that a field is required
    c: int = Field(..., alias='C') # emphasize that a field is required

model = Model(a=1, b=2, C=3) # 使用 C 是因為設定了 alias
# model = Model(a=1, b=2, c=3) # ValidationError
print(model)
```

[Fields with non-hashable default values](https://docs.pydantic.dev/latest/concepts/models/#fields-with-non-hashable-default-values)

```python
from typing import Dict, List

from pydantic import BaseModel


class Model(BaseModel):
    item_counts: List[Dict[str, int]] = [{}]


m1 = Model()
m1.item_counts[0]['a'] = 1
print(m1.item_counts)
#> [{'a': 1}]

m2 = Model()
print(m2.item_counts)
#> [{}]
```

[Fields with dynamic default values](https://docs.pydantic.dev/latest/concepts/models/#fields-with-dynamic-default-values)

使用 default_factory 建立 default

```python
from datetime import datetime, timezone
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


def datetime_now() -> datetime:
    return datetime.now(timezone.utc)


class Model(BaseModel):
    uid: UUID = Field(default_factory=uuid4)
    updated: datetime = Field(default_factory=datetime_now)


print(Model())
print(Model())
```

[Structural pattern matching](https://docs.pydantic.dev/latest/concepts/models/#structural-pattern-matching)

支援 match_case, 可參考 [match_case_tutorial.py](https://github.com/twtrubiks/python-notes/blob/master/match_case_tutorial.py)

```python
from pydantic import BaseModel


class Pet(BaseModel):
    name: str
    species: str


a = Pet(name='Bones', species='dog') # Bones is a dog
# a = Pet(name='Bones', species='dog1') # No dog matched
print(a)

match a:
    # match `species` to 'dog', declare and initialize `dog_name`
    case Pet(species='dog', name=dog_name):
        print(f'{dog_name} is a dog')

    # default case
    case _:
        print('No dog matched')
```

[Extra fields](https://docs.pydantic.dev/latest/concepts/models/#extra-fields)

正常是可以加入額外的 fields

```python
from pydantic import BaseModel


class Model(BaseModel):
    x: int


m = Model(x=1, y='a')
```

如果你不想要可以加入額外的 fields, 可以這樣設定

```python
from pydantic import BaseModel, ConfigDict, ValidationError


class Model(BaseModel):
    x: int

    model_config = ConfigDict(extra='forbid')


try:
    Model(x=1, y='a')
except ValidationError as exc:
    print(exc)
```

## Fields

[Default values](https://docs.pydantic.dev/latest/concepts/fields/#default-values)

```python
from pydantic import BaseModel, Field


class User(BaseModel):
    name: str = Field(default='John Doe')


user = User()
print(user)
```

或是使用前面介紹的 default_factory 都可以

```python
from uuid import uuid4

from pydantic import BaseModel, Field


class User(BaseModel):
    id: str = Field(default_factory=lambda: uuid4().hex)
```

[Using Annotated](https://docs.pydantic.dev/latest/concepts/fields/#using-annotated)

```python
from uuid import uuid4

from typing_extensions import Annotated

from pydantic import BaseModel, Field


class User(BaseModel):
    id: Annotated[str, Field(default_factory=lambda: uuid4().hex)]
```

[Field aliases](https://docs.pydantic.dev/latest/concepts/fields/#field-aliases)

```python
from pydantic import BaseModel, Field


class User(BaseModel):
    name: str = Field(..., alias='username')


user = User(username='johndoe')
# user = User(name='johndoe') # ValidationError
print(user) # name='johndoe'
print(user.model_dump(by_alias=True)) # {'username': 'johndoe'}
```

[Numeric Constraints](https://docs.pydantic.dev/latest/concepts/fields/#numeric-constraints)/

```python
from pydantic import BaseModel, Field


class Foo(BaseModel):
    positive: int = Field(gt=0) # greater than
    non_negative: int = Field(ge=0) # greater than or equal to
    negative: int = Field(lt=0) # less than
    non_positive: int = Field(le=0) # less than or equal to
    even: int = Field(multiple_of=2) # a multiple of the given number
    love_for_pydantic: float = Field(allow_inf_nan=True) # allow 'inf', '-inf', 'nan' values


foo = Foo(
    positive=1,
    non_negative=0,
    negative=-1,
    non_positive=0,
    even=2,
    love_for_pydantic=float('inf'),
)
print(foo)
```

[String Constraints](https://docs.pydantic.dev/latest/concepts/fields/#string-constraints)

```python
from pydantic import BaseModel, Field


class Foo(BaseModel):
    short: str = Field(min_length=3)
    long: str = Field(max_length=10)
    regex: str = Field(pattern=r'^\d*$')


foo = Foo(short='foo', long='foobarbaz', regex='123')
print(foo)
```

[Decimal Constraints](https://docs.pydantic.dev/latest/concepts/fields/#decimal-constraints)

```python
from decimal import Decimal

from pydantic import BaseModel, Field


class Foo(BaseModel):
    precise: Decimal = Field(max_digits=5, decimal_places=2)


foo = Foo(precise=Decimal('123.45'))
print(foo)
```

[Strict Mode](https://docs.pydantic.dev/latest/concepts/fields/#strict-mode)

```python
from pydantic import BaseModel, Field


class User(BaseModel):
    name: str = Field(strict=True)
    age: int = Field(strict=False)
    c: int = Field(strict=False, default=1)


user = User(name='John', age='42')
user = User(name='John', age='42', c='3')
```

[The computed_field decorator](https://docs.pydantic.dev/latest/concepts/fields/#the-computed_field-decorator)


```python
from pydantic import BaseModel, computed_field


class Box(BaseModel):
    width: float
    height: float
    depth: float

    @computed_field
    @property # 可以不加, 但建議還是加進去
    def volume(self) -> float:
        return self.width * self.height * self.depth


b = Box(width=1, height=2, depth=3)
print(b.model_dump())
#> {'width': 1.0, 'height': 2.0, 'depth': 3.0, 'volume': 6.0}
```

## JSON Schema

[JSON Schema](https://docs.pydantic.dev/latest/concepts/json_schema/)

```python
import json
from enum import Enum

from typing import Annotated

from pydantic import BaseModel, Field
from pydantic.config import ConfigDict


class FooBar(BaseModel):
    count: int
    size: float | None = None


class Gender(str, Enum):
    male = 'male'
    female = 'female'
    other = 'other'
    not_given = 'not_given'


class MainModel(BaseModel):
    """
    This is the description of the main model
    """

    model_config = ConfigDict(title='Main')

    foo_bar: FooBar
    gender: Annotated[Gender | None, Field(alias='Gender')] = None
    snap: int = Field(
        42,
        title='The Snap',
        description='this is the value of snap',
        gt=30,
        lt=50,
    )


main_model_schema = MainModel.model_json_schema()  # (1)!
print(json.dumps(main_model_schema, indent=2))  # (2)!
```

## Validators

[Annotated Validators](https://docs.pydantic.dev/latest/concepts/validators/#annotated-validators)

```python
from typing import Any, List

from typing_extensions import Annotated

from pydantic import BaseModel, ValidationError
from pydantic.functional_validators import AfterValidator


def check_squares(v: int) -> int:
    assert v**0.5 % 1 == 0, f'{v} is not a square number'
    return v


def double(v: Any) -> Any:
    return v * 2


MyNumber = Annotated[int, AfterValidator(double), AfterValidator(check_squares)]


class DemoModel(BaseModel):
    number: List[MyNumber]


print(DemoModel(number=[2, 8])) # number=[4, 16]
try:
    DemoModel(number=[2, 4])
except ValidationError as e:
    print(e)
```

[Field validators](https://docs.pydantic.dev/latest/concepts/validators/#field-validators)

```python
from pydantic import (
    BaseModel,
    ValidationError,
    ValidationInfo,
    field_validator,
)


class UserModel(BaseModel):
    name: str
    id: int

    @field_validator('name')
    @classmethod
    def name_must_contain_space(cls, v: str) -> str:
        if ' ' not in v:
            raise ValueError('must contain a space')
        return v.title()

    # you can select multiple fields, or use '*' to select all fields
    @field_validator('id', 'name')
    @classmethod
    def check_alphanumeric(cls, v: str, info: ValidationInfo) -> str:
        if isinstance(v, str):
            # info.field_name is the name of the field being validated
            is_alphanumeric = v.replace(' ', '').isalnum()
            assert is_alphanumeric, f'{info.field_name} must be alphanumeric'
        return v


print(UserModel(name='John Doe', id=1)) # name='John Doe' id=1

try:
    UserModel(name='samuel', id=1)
except ValidationError as e:
    print(e)

try:
    UserModel(name='John Doe', id='abc')
except ValidationError as e:
    print(e)

try:
    UserModel(name='John Doe!', id=1)
except ValidationError as e:
    print(e)
```

[Model validators](https://docs.pydantic.dev/latest/concepts/validators/#model-validators)

```python
from typing import Any

from typing_extensions import Self

from pydantic import BaseModel, ValidationError, model_validator


class UserModel(BaseModel):
    username: str
    password1: str
    password2: str

    @model_validator(mode='before')
    @classmethod
    def check_card_number_omitted(cls, data: Any) -> Any:
        if isinstance(data, dict):
            assert (
                'card_number' not in data
            ), 'card_number should not be included'
        return data

    @model_validator(mode='after')
    def check_passwords_match(self) -> Self:
        pw1 = self.password1
        pw2 = self.password2
        if pw1 is not None and pw2 is not None and pw1 != pw2:
            raise ValueError('passwords do not match')
        return self


print(UserModel(username='scolvin', password1='zxcvbn', password2='zxcvbn'))
#> username='scolvin' password1='zxcvbn' password2='zxcvbn'
try:
    UserModel(username='scolvin', password1='zxcvbn', password2='zxcvbn2')
except ValidationError as e:
    print(e)

try:
    UserModel(
        username='scolvin',
        password1='zxcvbn',
        password2='zxcvbn',
        card_number='1234',
    )
except ValidationError as e:
    print(e)
```

## Type Adapter

[Type Adapter](https://docs.pydantic.dev/latest/concepts/type_adapter/)

```python
from typing import List

from typing_extensions import TypedDict

from pydantic import TypeAdapter, ValidationError


class User(TypedDict):
    name: str
    id: int


user_list_adapter = TypeAdapter(List[User])
user_list = user_list_adapter.validate_python([{'name': 'Fred', 'id': '3'}])
print(repr(user_list))
#> [{'name': 'Fred', 'id': 3}]

try:
    user_list_adapter.validate_python(
        [{'name': 'Fred', 'id': 'wrong', 'other': 'no'}]
    )
except ValidationError as e:
    print(e)

print(repr(user_list_adapter.dump_json(user_list)))
#> b'[{"name":"Fred","id":3}]'
```

在 Performance 中, nested 的情境底下, 使用 Type Adapter 會比 model 好,

可參考 [Use TypedDict over nested models](https://docs.pydantic.dev/latest/concepts/performance/#use-typeddict-over-nested-models)

## Performance

可參考 [Performance tips](https://docs.pydantic.dev/latest/concepts/performance/)

## 延伸閱讀

* [pydantic-ai-tutorial](https://github.com/twtrubiks/pydantic-ai-tutorial) - pydantic-ai 介紹教學
