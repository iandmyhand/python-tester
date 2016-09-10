class ExceptionBase(Exception):

    code = None
    detail = None

    def __init__(self, code, *args, **kwargs):
        self.code = code
        self.detail = kwargs.pop('detail', None)
        super(ExceptionBase, self).__init__(code, *args, **kwargs)


class ExceptionInheritance(ExceptionBase):

    def __init__(self, code, *args, **kwargs):
        super(ExceptionInheritance, self).__init__(code=code, *args, **kwargs)


e = ExceptionInheritance('TEST', detail='This is a detail message.')
assert(type(e) == ExceptionInheritance)
assert(isinstance(e, ExceptionBase))
assert('TEST' == e.code)
assert('This is a detail message.' == e.detail)
