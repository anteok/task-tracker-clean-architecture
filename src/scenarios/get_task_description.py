from abc import ABCMeta, abstractmethod
from dataclasses import dataclass

from entities.task import TaskEntity


class GetTaskDescriptionInterface(metaclass=ABCMeta):

    @abstractmethod
    def get_task(self, task_id: str) -> TaskEntity: ...


class GetTaskDescriptionInteractor:

    def __init__(self, repository: GetTaskDescriptionInterface):
        self._repository = repository

    def get_task_upper_description(self, task_id: str) -> str:
        task = self._repository.get_task(task_id)
        return task.description.upper()
