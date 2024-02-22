from datetime import datetime
from unittest.mock import Mock

import pytest

from entities.task import TaskStatus, TaskEntity
from scenarios.delete_task import DeleteTaskInteractor, WrongStatusForDeletionException


class TestDeleteTaskInteractor:

    @pytest.fixture
    def interactor(self) -> DeleteTaskInteractor:
        return DeleteTaskInteractor(
            repository=Mock(get_task=Mock(), delete_task=Mock())
        )

    @pytest.mark.parametrize('status', [val for val in TaskStatus if val is not TaskStatus.done])
    def test_delete_task_in_wrong_status(self, interactor, status):
        interactor._repository.get_task.return_value = TaskEntity(
            task_id='any',
            status=status,
            update_time=datetime.now(),
            create_time=datetime.now(),
            description='',
        )
        with pytest.raises(WrongStatusForDeletionException) as exc:
            interactor.delete_task('any')
        assert exc.value.args[0] == f'Task in status "{status.name}" cannot be deleted'

    def test_delete_completed_task(self, interactor):
        interactor._repository.get_task.return_value = TaskEntity(
            task_id='any',
            status=TaskStatus.done,
            update_time=datetime.now(),
            create_time=datetime.now(),
            description='',
        )
        interactor.delete_task('any')
        interactor._repository.delete_task.assert_called_with('any')
