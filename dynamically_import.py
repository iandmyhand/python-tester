

def dynamically_import():
    mod = __import__('my_package.my_module', fromlist=['my_class'])
    klass = getattr(mod, 'my_class')


if '__main__' == __name__:
    dynamically_import()
