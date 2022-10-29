
import inspect

def autovacuum(method):
    assert method.__name__.startswith('_'), "%s: autovacuum methods must be private" % method.__name__
    method._autovacuum = True
    return method

class A:
    @autovacuum
    def _gc_file_store_A(self):
        print('run _gc_file_store_A')

class B:
    # @autovacuum
    def _gc_file_store_B(self):
        print('run _gc_file_store_B')

def is_autovacuum(func):
    """ Return whether ``func`` is an autovacuum method. """
    return callable(func) and getattr(func, '_autovacuum', False)

class AutoVacuum:

    my_data = [A(), B()]

    def _run_vacuum_cleaner(self):
        """
        Perform a complete database cleanup by safely calling every
        ``@api.autovacuum`` decorated method.
        """
        for model in self.my_data:
            cls = type(model)
            for attr, func in inspect.getmembers(cls, is_autovacuum):
                print('work')
                func(model)
                print('attr:', attr)
                print('func:', func)

AutoVacuum()._run_vacuum_cleaner()