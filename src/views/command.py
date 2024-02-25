from abc import ABCMeta, abstractmethod
from typing import Type, TypeVar, Generic

from controllers.in_memory import InMemoryController, CreateTaskController
from details.id_generator import IdGenerator
from repositories.in_memory import InMemoryRepository

T = TypeVar('T', bound=InMemoryController)


class CommandPattern(Generic[T], metaclass=ABCMeta):
    _start: str
    _controller_class: Type[T]

    def __init__(self, _repository: InMemoryRepository):
        self._controller: T = self._controller_class(_repository)

    @abstractmethod
    def respond(self, command: str) -> str: ...


class CreatePattern(CommandPattern[CreateTaskController]):
    _regex = r'create \"[a-zA-Z\s]*\"'
    _controller_class = CreateTaskController

    def __init__(self, _repository: InMemoryRepository):
        super().__init__(_repository)
        self._id_generator = IdGenerator()

    def respond(self, command: str) -> str:
        new_id = self._id_generator.get_id()
        description = command.split('"')[1]

        self._controller.execute(task_id=new_id, description=description)
        return f'A new task "{description}" is in_backlog with id {new_id}'
