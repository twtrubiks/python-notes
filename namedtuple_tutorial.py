from collections import namedtuple


class NetworkAddressClass(object):
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port


if __name__ == "__main__":
    print('=== use namedtuple ===')
    NetworkAddress = namedtuple('NetworkAddress', ['hostname', 'port'])  # write 1
    # NetworkAddress = namedtuple('NetworkAddress', 'hostname port') # write 2
    print('NetworkAddress._fields', NetworkAddress._fields)  # _fields is a tuple with the field names of the class

    a = NetworkAddress('localhost', 3306)
    print('a.hostname:', a.hostname)
    print('a.port:', a.port)
    # a.port = 80  # error , tuple read only

    network_address_data = ('hello', 1234)
    na_1 = NetworkAddress._make(network_address_data)  # write 1
    na_2 = NetworkAddress(*network_address_data)  # write 2
    print('na_1', na_1)
    print('na_2', na_2)

    # _asdict() return a collections.OrderedDict
    # That can be used to produce a nice display of data
    print('na_1._asdict()', na_1._asdict())

    print('=== use class ===')
    b = NetworkAddressClass('localhost', 3306)
    print('b.hostname:', b.hostname)
    print('b.port:', b.port)
    b.port = 80
