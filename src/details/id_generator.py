from abc import ABCMeta


class IdGenerator(metaclass=ABCMeta):
    __last_id = 0

    def get_id(self) -> str:
        _id = str(self.__last_id)
        self.__last_id += 1
        return _id
