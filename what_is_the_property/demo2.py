class A:
    def __init__(self, content):
        self._content = content

    @property
    def content(self):
        if not hasattr(self, '_content'):
            return "content not exists"
        return self._content

    @content.setter
    def content(self, value):
        self._content = value

    @content.deleter
    def content(self):
        del self._content


if __name__ == "__main__":
    a = A('hello')
    print('content:', a.content)  # automatically calls getter
    a.content = 'world'  # automatically calls setter
    print('content:', a.content)
    del a.content  # automatically calls deleter
    print('content:', a.content)  # content not exists
