from collections import namedtuple


class NetworkAddressClass(object):
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port


if __name__ == "__main__":
    print('=== use namedtuple ===')
    NetworkAddress = namedtuple('NetworkAddress', ['hostname', 'port'])  # write 1
    # NetworkAddress = namedtuple('NetworkAddress', 'hostname port') # write 2
    a = NetworkAddress('localhost', 3306)
    print('a.hostname:', a.hostname)
    print('a.port:', a.port)
    # a.port = 80  # error , tuple read only

    print('=== use class ===')
    b = NetworkAddressClass('localhost', 3306)
    print('b.hostname:', b.hostname)
    print('b.port:', b.port)
    b.port = 80
