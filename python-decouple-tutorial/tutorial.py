from decouple import config

if __name__ == "__main__":
    DEBUG = config('DEBUG', default=False, cast=bool)
    print('DEBUG', DEBUG)
    '''
    environment variables have precedence over config files.
    os.environ['PATH'] = '/my_path'
    '''
    PATH = config('PATH', cast=str)
    print('PATH', PATH)
