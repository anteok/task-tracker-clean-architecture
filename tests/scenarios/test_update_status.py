from datetime import datetime
from unittest.mock import Mock

import pytest
from freezegun import freeze_time

from entities.task import TaskStatus
from scenarios.update_status import UpdateStatusDto, UpdateStatusInteractor, WrongStatusCaseException


class TestUpdateStatusDto:

    @freeze_time('2020-10-10')
    @pytest.mark.parametrize('status', [val.name for val in TaskStatus])
    def test_from_request(self, status):
        assert UpdateStatusDto.from_request(task_id='any', status=status) == UpdateStatusDto(
            task_id='any',
            status=TaskStatus[status],
            update_time=datetime(2020, 10, 10)
        )

    def test_wrong_status(self):
        with pytest.raises(WrongStatusCaseException) as exc:
            UpdateStatusDto.from_request(task_id='', status='wrong')
        assert exc.value.args[0] == 'No such value'


class TestUpdateStatusInteractor:

    @pytest.fixture
    def interactor(self) -> UpdateStatusInteractor:
        return UpdateStatusInteractor(
            repository=Mock(update_status=Mock)
        )

    @freeze_time('2020-10-10')
    def test_update_status_success(self, interactor):
        interactor.update_status('any', 'in_backlog')
        interactor._repository.update_task.assert_called_with(task=UpdateStatusDto(
            task_id='any',
            status=TaskStatus.in_backlog,
            update_time=datetime(2020, 10, 10),
        ))

    def test_update_status_failed(self, interactor):
        with pytest.raises(WrongStatusCaseException) as exc:
            interactor.update_status('any', 'wrong')
        assert exc.value.args[0] == 'No such value'
