class CommonEqualityMixin(object):

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)


class Foo(CommonEqualityMixin):

    def __init__(self, item):
        self.item = item


class Bar(Foo):

    def __init__(self, item):
        self.item = item


def test_equality():
    foo = Foo('item')
    bar = Bar('item')
    print(foo == bar)
    print(bar == foo)


if '__main__' == __name__:
    test_equality()
