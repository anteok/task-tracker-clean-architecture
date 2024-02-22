from datetime import datetime

import pytest

from entities.task import TaskEntity, TaskStatus
from repositories.in_memory import InMemoryRepository, NoTaskFoundInRepo, TaskWithIdAlreadyExists
from scenarios.update_status import UpdateStatusDto


class TestInMemoryRepository:

    @pytest.fixture
    def repository(self) -> InMemoryRepository:
        repo = InMemoryRepository()
        repo._tasks['11'] = TaskEntity(
            task_id='11',
            status=TaskStatus.in_review,
            create_time=datetime(2020, 10, 8),
            update_time=datetime(2020, 10, 9),
            description='basic task',
        )
        return repo

    def test_get_task_success(self, repository):
        assert repository.get_task('11') == TaskEntity(
            task_id='11',
            status=TaskStatus.in_review,
            create_time=datetime(2020, 10, 8),
            update_time=datetime(2020, 10, 9),
            description='basic task',
        )

    def test_get_task_fail(self, repository):
        with pytest.raises(NoTaskFoundInRepo):
            repository.get_task('1')

    def test_delete_task_that_does_not_exist(self, repository):
        repository.delete_task('12')
        assert repository._tasks

    def test_delete_task_that_exists(self, repository):
        repository.delete_task('11')
        assert not repository._tasks

    def test_update_task_that_does_not_exist(self, repository):
        with pytest.raises(NoTaskFoundInRepo):
            repository.update_task(update_dto=UpdateStatusDto(
                task_id='12',
                status=TaskStatus.done,
                update_time=datetime(2020, 10, 10)
            ))

    def test_update_task_that_exists(self, repository):
        repository.update_task(update_dto=UpdateStatusDto(
            task_id='11',
            status=TaskStatus.done,
            update_time=datetime(2020, 10, 10)
        ))
        assert repository._tasks['11'] == TaskEntity(
            task_id='11',
            status=TaskStatus.done,
            create_time=datetime(2020, 10, 8),
            update_time=datetime(2020, 10, 10),
            description='basic task',
        )

    def test_create_task_already_exists(self, repository):
        with pytest.raises(TaskWithIdAlreadyExists):
            repository.create_task(TaskEntity(
                task_id='11',
                status=TaskStatus.done,
                create_time=datetime(2020, 10, 8),
                update_time=datetime(2020, 10, 9),
                description='new task',
            ))

    def test_create_task_that_does_not_exist(self, repository):
        repository.create_task(TaskEntity(
            task_id='12',
            status=TaskStatus.done,
            create_time=datetime(2020, 10, 8),
            update_time=datetime(2020, 10, 9),
            description='new task',
        ))
        assert repository._tasks['12'] == TaskEntity(
            task_id='12',
            status=TaskStatus.done,
            create_time=datetime(2020, 10, 8),
            update_time=datetime(2020, 10, 9),
            description='new task',
        )
