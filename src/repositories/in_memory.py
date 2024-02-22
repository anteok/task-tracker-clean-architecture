from entities.task import TaskEntity
from scenarios.create_task import ICreateTaskRepository
from scenarios.delete_task import IDeleteTaskRepository
from scenarios.get_task_description import IGetTaskDescriptionRepository
from scenarios.update_status import IUpdateStatusRepository, UpdateStatusDto


class InMemoryRepoException(Exception):
    ...


class NoTaskFoundInRepo(InMemoryRepoException):
    ...


class TaskWithIdAlreadyExists(InMemoryRepoException):
    ...


class InMemoryRepository(
    ICreateTaskRepository,
    IGetTaskDescriptionRepository,
    IDeleteTaskRepository,
    IUpdateStatusRepository,
):

    def __init__(self):
        self._tasks: dict[str, TaskEntity] = {}

    def get_task(self, task_id: str) -> TaskEntity:
        if task_id not in self._tasks:
            raise NoTaskFoundInRepo
        return self._tasks[task_id]

    def delete_task(self, task_id: str) -> None:
        if task_id in self._tasks:
            self._tasks.pop(task_id)

    def update_task(self, update_dto: UpdateStatusDto) -> None:
        if update_dto.task_id not in self._tasks:
            raise NoTaskFoundInRepo
        self._tasks[update_dto.task_id].status = update_dto.status
        self._tasks[update_dto.task_id].update_time = update_dto.update_time

    def create_task(self, entity: TaskEntity) -> None:
        if entity.task_id in self._tasks:
            raise TaskWithIdAlreadyExists
        self._tasks[entity.task_id] = entity
