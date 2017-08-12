import configparser

# ref. https://docs.python.org/3/library/configparser.html
config = configparser.ConfigParser()
config.read("config.ini")

print(config['DEFAULT']['Compression'])

# Note also that keys in sections are case-insensitive and stored in lowercase
print(config['DEFAULT']['ServerAliveInterval'])
print(config['DEFAULT']['serveraliveinterval'])

print(config['bitbucket.org']['User'])
