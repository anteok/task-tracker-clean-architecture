from abc import ABCMeta, abstractmethod

from entities.task import TaskEntity, TaskStatus


class WrongStatusForDeletionException(Exception):
    ...


class IDeleteTaskRepository(metaclass=ABCMeta):

    @abstractmethod
    def get_task(self, task_id) -> TaskEntity: ...

    @abstractmethod
    def delete_task(self, task_id: str) -> None: ...


class DeleteTaskInteractor:

    def __init__(self, repository: IDeleteTaskRepository):
        self._repository = repository

    def delete_task(self, task_id: str) -> None:
        task = self._repository.get_task(task_id)
        if task.status is not TaskStatus.done:
            raise WrongStatusForDeletionException(f'Task in status "{task.status.name}" cannot be deleted')

        self._repository.delete_task(task_id)
