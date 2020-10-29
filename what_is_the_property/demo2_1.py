class A:
    def __init__(self, content):
        self._content = content

    def get_content(self):
        if not hasattr(self, '_content'):
            return "content not exists"
        return self._content

    def set_content(self, value):
        self._content = value

    def del_content(self):
        del self._content

    # property(fget=None, fset=None, fdel=None, doc=None)
    content = property(get_content, set_content, del_content, 'my content property')


if __name__ == "__main__":
    a = A('hello')
    print('content:', a.content)  # automatically calls getter
    a.content = 'world'  # automatically calls setter
    print('content:', a.content)
    del a.content  # automatically calls deleter
    print('content:', a.content)  # content not exists
