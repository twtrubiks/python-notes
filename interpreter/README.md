# what is the python interpreter

* [Youtube Tutorial - what is the python interpreter](https://youtu.be/MxS3CoyyIaU)

Many times we open the `.py` file, and the first line at the beginning will show `#!/usr/bin/python3`.

Ever wondered why is this :question:

`#!/usr/bin/python3` is used to specify the interpreter :exclamation: :exclamation:

Why specify an interpreter :question:

For example, many people have both Python2 and Python3 installed on their systems, but 2 and 3 are not compatible.

So you must specify an interpreter when executing `.py`.

For example, `hello.py`

```python
#!/usr/bin/python3

import sys
print(str(sys.version))
```

You will find the output of python3.

The space after `#!` is optional, that is, `#!/usr/bin/python3` and `#! /usr/bin/python3` are both allowed.

If an interpreter is specified, the following instructions can be executed directly, and it will be automatically executed using python3.

Remember to give it execute permissions

( x = executable )

```cmd
chmod +x hello.py
```

```cmd
./hello.py
```

If no interpreter is specified, you can also be added to the terminal during execution.

```cmd
python3 hello.py
```

In short, the goal is to tell the computer which Python version to use :blush:
