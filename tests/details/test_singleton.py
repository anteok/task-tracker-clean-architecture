from details.singleton import SingletonMeta


class TestSingletonMeta:

    def test_singleton(self):
        class AnyClass(metaclass=SingletonMeta): ...

        first = AnyClass()
        second = AnyClass()
        assert first is second
