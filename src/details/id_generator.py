from details.singleton import SingletonMeta


class IdGenerator(metaclass=SingletonMeta):
    __last_id = 0

    def get_id(self) -> str:
        _id = str(self.__last_id)
        self.__last_id += 1
        return _id
