class A:
    def __init__(self, content):
        self._content = content

    def get_content(self):
        if not hasattr(self, '_content'):
            return "content not exists"
        return self._content

    def set_content(self, value):
        self._content = value

    def delete_content(self):
        del self._content


if __name__ == "__main__":
    a = A('hello')
    print('content:', a.get_content())  # get content
    a.set_content('world')  # set content
    print('content:', a.get_content())
    a.delete_content()  # delete content
    print('content:', a.get_content())  # content not exists
