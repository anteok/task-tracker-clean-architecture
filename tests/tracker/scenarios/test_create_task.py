from datetime import datetime
from unittest.mock import Mock

import pytest
from freezegun import freeze_time

from entities.task import TaskEntity, TaskStatus
from scenarios.create_task import CreateTaskInteractor


class TestCreateTaskInteractor:

    @pytest.fixture
    def interactor(self) -> CreateTaskInteractor:
        return CreateTaskInteractor(
            repository=Mock(create_task=Mock())
        )

    @freeze_time('2020-10-10')
    def test_create_task(self, interactor):
       interactor.create_task(
           task_id='some',
           description='any',
       )
       interactor._repository.create_task.assert_called_with(
           TaskEntity(
               task_id='some',
               description='any',
               create_time=datetime(2020, 10, 10),
               update_time=datetime(2020, 10, 10),
               status=TaskStatus.in_backlog,
           )
       )
