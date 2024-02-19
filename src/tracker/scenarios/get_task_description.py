from abc import ABCMeta, abstractmethod
from dataclasses import dataclass

from entities.task import TaskEntity


@dataclass
class GetTaskDescriptionDataInterface(metaclass=ABCMeta):
    description: str = NotImplemented


@dataclass
class GetTaskDescriptionDto:
    description: str


class GetTaskDescriptionInterface(metaclass=ABCMeta):

    @abstractmethod
    def get_task_description(self, task_id: str) -> GetTaskDescriptionDataInterface: ...


class GetTaskDescriptionInteractor:

    def __init__(self, repository: GetTaskDescriptionInterface):
        self._repository = repository

    def get_task_upper_description(self, task_id: str) -> GetTaskDescriptionDto:
        record = self._repository.get_task_description(task_id)
        return GetTaskDescriptionDto(
            description=record.description.upper()
        )
