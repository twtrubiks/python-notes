from datetime import date, datetime
from pprint import pprint
import uuid

from marshmallow import Schema, fields, validate, post_load, ValidationError, validates

"""
https://marshmallow.readthedocs.io/en/stable/

https://marshmallow.readthedocs.io/en/stable/examples.html

pip install -U marshmallow

- 反序列化 (Loading)
Deserialize input data to app-level objects.
The reverse of the dump method is load,
which validates and deserializes an input dictionary to an application-level data structure


- 序列化 (Dumping) obj -> dict
Serialize app-level objects to primitive Python types.
The serialized objects can then be rendered to standard formats
such as JSON for use in an HTTP API.
"""


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_at = datetime.now()

    def __repr__(self):
        return "<User(name={self.name!r})>".format(self=self)


class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()

def serializing_objects():
    # Dumping
    user = User(name="Monty", email="monty@python.org")
    schema = UserSchema()
    result = schema.dump(user)
    print('result type:', type(result)) # dict
    pprint(result)

    # You can also serialize to a JSON-encoded string using dumps.
    json_result = schema.dumps(user)
    print('json_result type:', type(json_result)) # str
    pprint(json_result)

def filtering_output():
    user = User(name="Monty", email="monty@python.org")
    summary_schema = UserSchema(only=("name",))
    result = summary_schema.dump(user)
    pprint(result)

def deserializing_objects():
    user_data = {
        "created_at": "2014-08-11T05:26:03.869245",
        "email": "ken@yahoo.com",
        "name": "Ken",
    }
    schema = UserSchema()
    result = schema.load(user_data)
    print('result type:', type(result))
    pprint(result)


    # loads json_string
    user_json = '{"created_at": "2014-08-11T05:26:03.869245", "email": "ken@yahoo.com", "name": "Ken"}'
    result_obj = schema.loads(user_json)
    print('result type:', type(result_obj))
    pprint(result_obj)

def deserializing_post_load_objects():

    class UserSchema2(Schema):
        name = fields.Str()
        email = fields.Email()
        created_at = fields.DateTime()

        @post_load
        def make_user(self, data, **kwargs):
            return User(**data)

    user_data = {"name": "Ronnie", "email": "ronnie@stones.com"}
    schema = UserSchema2()
    result = schema.load(user_data)
    print(result)

def serializing_many_objects():
    user1 = User(name="Mick", email="mick@stones.com")
    user2 = User(name="Keith", email="keith@stones.com")
    users = [user1, user2]
    schema = UserSchema(many=True)
    result = schema.dump(users)  # OR UserSchema().dump(users, many=True)
    pprint(result)

def base_validation():
    try:
        result = UserSchema().load({"name": "John", "email": "foo"})
    except ValidationError as err:
        print(err.messages)  # => {"email": ['"foo" is not a valid email address.']}
        print(err.valid_data)  # => {"name": "John"}

def base_indices_validation():
    class BandMemberSchema(Schema):
        name = fields.String(required=True)
        email = fields.Email()


    user_data = [
        {"email": "mick@stones.com", "name": "Mick"},
        {"email": "invalid", "name": "Invalid"},  # invalid email
        {"email": "keith@stones.com", "name": "Keith"},
        {"email": "charlie@stones.com"},  # missing "name"
    ]

    try:
        BandMemberSchema(many=True).load(user_data)
    except ValidationError as err:
        pprint(err.messages)
        # {1: {'email': ['Not a valid email address.']},
        #  3: {'name': ['Missing data for required field.']}}

def base_validate():
    class UserSchema(Schema):
        name = fields.Str(validate=validate.Length(min=1))
        permission = fields.Str(validate=validate.OneOf(["read", "write", "admin"]))
        age = fields.Int(validate=validate.Range(min=18, max=40))


    in_data = {"name": "", "permission": "invalid", "age": 71}
    try:
        UserSchema().load(in_data)
    except ValidationError as err:
        pprint(err.messages)
        # {'age': ['Must be greater than or equal to 18 and less than or equal to 40.'],
        #  'name': ['Shorter than minimum length 1.'],
        #  'permission': ['Must be one of: read, write, admin.']}

def implement_custom_validate():
    """
    Warning
    Validation occurs on deserialization but not on serialization.
    To improve serialization performance, data passed to Schema.dump() are considered valid.
    """
    def validate_quantity(n):
        if n < 0:
            raise ValidationError("Quantity must be greater than 0.")
        if n > 30:
            raise ValidationError("Quantity must not be greater than 30.")


    class ItemSchema(Schema):
        quantity = fields.Integer(validate=validate_quantity)


    in_data = {"quantity": 31}
    try:
        result = ItemSchema().load(in_data)
    except ValidationError as err:
        print(err.messages)  # => {'quantity': ['Quantity must not be greater than 30.']}

def field_validators_as_methods():
    class ItemSchema(Schema):
        quantity = fields.Integer()

        @validates("quantity")
        def validate_quantity(self, value):
            if value < 0:
                raise ValidationError("Quantity must be greater than 0.")
            if value > 30:
                raise ValidationError("Quantity must not be greater than 30.")

def required_fields():
    class UserSchema(Schema):
        name = fields.String(required=True)
        age = fields.Integer(required=True, error_messages={"required": "Age is required."})
        city = fields.String(
            required=True,
            error_messages={"required": {"message": "City required", "code": 400}},
        )
        email = fields.Email()

    try:
        result = UserSchema().load({"email": "foo@bar.com"})
    except ValidationError as err:
        pprint(err.messages)
        # {'age': ['Age is required.'],
        # 'city': {'code': 400, 'message': 'City required'},
        # 'name': ['Missing data for required field.']}

def partial_loading():
    # skip required validation by passing partial.
    class UserSchema(Schema):
        name = fields.String(required=True)
        age = fields.Integer(required=True)


    result = UserSchema().load({"age": 42}, partial=("name",))
    # OR UserSchema(partial=('name',)).load({'age': 42})

    # marshmallow.exceptions.ValidationError: {'name': ['Missing data for required field.']}
    # result = UserSchema().load({"age": 42})

    print(result)  # => {'age': 42}

def specifying_defaults():
    """
    load_default specifies the default deserialization value for a field. Likewise,
    dump_default specifies the default serialization value.
    """
    class UserSchema(Schema):
        id = fields.UUID(load_default=uuid.uuid1)
        birthdate = fields.DateTime(dump_default=datetime(2017, 9, 29))


    UserSchema().load({})
    # {'id': UUID('337d946c-32cd-11e8-b475-0022192ed31b')}
    UserSchema().dump({})
    # {'birthdate': '2017-09-29T00:00:00+00:00'}

def handling_unknown_field():
    from marshmallow import Schema, INCLUDE
    """
    RAISE (default): raise a ValidationError if there are any unknown fields

    EXCLUDE: exclude unknown fields

    INCLUDE: accept and include the unknown fields
    """


    class UserSchema(Schema):
        class Meta:
            unknown = INCLUDE

    # at instantiation time,
    # schema = UserSchema(unknown=INCLUDE)

    # or when calling load.
    # UserSchema().load(data, unknown=INCLUDE)

def validation_without_deserialization():
    """
    If you only need to validate input data (without deserializing to an object),
    you can use Schema.validate().
    """
    errors = UserSchema().validate({"name": "Ronnie", "email": "invalid-email"})
    print(errors)  # {'email': ['Not a valid email address.']}


if __name__ == "__main__":
    serializing_objects()
    # filtering_output()
    # deserializing_objects()
    # deserializing_post_load_objects()
    # serializing_many_objects()
    # base_validation()
    # base_indices_validation()
    # base_validate()
    # implement_custom_validate()
    # required_fields()
    # partial_loading()
    # specifying_defaults()
    # specifying_defaults()
    # validation_without_deserialization()