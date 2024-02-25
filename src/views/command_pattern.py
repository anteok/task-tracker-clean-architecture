import re
from abc import ABCMeta, abstractmethod
from typing import Type, TypeVar, Generic

from controllers.in_memory import InMemoryController, CreateTaskController, GetTaskDescriptionController, \
    UpdateStatusController, DeleteTaskController
from details.id_generator import IdGenerator
from repositories.in_memory import InMemoryRepository

T = TypeVar('T', bound=InMemoryController)


class CommandPattern(Generic[T], metaclass=ABCMeta):
    regex: str
    _controller_class: Type[T]

    def __init__(self, _repository: InMemoryRepository):
        self._controller: T = self._controller_class(_repository)

    @abstractmethod
    def respond(self, command: str) -> str: ...


class CreatePattern(CommandPattern[CreateTaskController]):
    regex = r'create task \"[a-zA-Z\s]*\"'
    _controller_class = CreateTaskController

    def __init__(self, _repository: InMemoryRepository):
        super().__init__(_repository)
        self._id_generator = IdGenerator()

    def respond(self, command: str) -> str:
        new_id = self._id_generator.get_id()
        description = command.split('"')[1]

        self._controller.execute(task_id=new_id, description=description)
        return f'A new task "{description}" is in_backlog with id {new_id}'


class GetDescriptionPattern(CommandPattern[GetTaskDescriptionController]):
    regex = r'what is (\d{1,3})'
    _controller_class = GetTaskDescriptionController

    def respond(self, command: str) -> str:
        task_id = command.split()[-1]
        description = self._controller.execute(task_id)
        return f'THE TASK WITH ID {task_id} IS "{description}"'


class UpdateStatusPattern(CommandPattern[UpdateStatusController]):
    regex = r'move task (\d{1,3}) to (in_backlog|prioritized|in_work|in_review|done)'
    _controller_class = UpdateStatusController

    def respond(self, command: str) -> str:
        task_id = command.split()[2]
        status = command.split()[-1]
        self._controller.execute(task_id, status)
        return f'The task with id {task_id} was moved to status "{status}"'


class DeleteTaskPattern(CommandPattern[DeleteTaskController]):
    regex = r'delete task (\d{1,3})'
    _controller_class = DeleteTaskController

    def respond(self, command: str) -> str:
        task_id = command.split()[-1]
        self._controller.execute(task_id)
        return f'The task with id {task_id} was deleted'


class CommandPatternFactory:
    @classmethod
    def get_response(cls, command: str, repository: InMemoryRepository) -> str:
        for class_ in CommandPattern.__subclasses__():
            if re.search(class_.regex, command):
                return class_(repository).respond(command)
        return f'Cannot parse command "{command}"'
