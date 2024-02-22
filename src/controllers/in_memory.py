from repositories.in_memory import InMemoryRepository
from scenarios.create_task import CreateTaskInteractor
from scenarios.delete_task import DeleteTaskInteractor
from scenarios.get_task_description import GetTaskDescriptionInteractor
from scenarios.update_status import UpdateStatusInteractor


class InMemoryController:
    def __init__(self, repository: InMemoryRepository):
        self._repository = repository


class CreateTaskController(InMemoryController):

    def execute(self, task_id: str, description: str) -> None:
        CreateTaskInteractor(self._repository).create_task(task_id, description)


class DeleteTaskController(InMemoryController):

    def execute(self, task_id: str) -> None:
        DeleteTaskInteractor(self._repository).delete_task(task_id)


class GetTaskDescriptionController(InMemoryController):

    def execute(self, task_id) -> str:
        return GetTaskDescriptionInteractor(self._repository).get_task_upper_description(task_id)


class UpdateStatusController(InMemoryController):

    def execute(self, task_id: str, status: str) -> None:
        UpdateStatusInteractor(self._repository).update_status(task_id, status)