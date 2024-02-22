from unittest.mock import Mock

import pytest
from freezegun import freeze_time

from scenarios.get_task_description import GetTaskDescriptionInteractor


class TestGetTaskDescriptionInteractor:

    @pytest.fixture
    def interactor(self) -> GetTaskDescriptionInteractor:
        return GetTaskDescriptionInteractor(
            repository=Mock(
                get_task=Mock(),
            )
        )

    @freeze_time('2020-10-10')
    def test_get_task_upper_description(self, interactor):
        interactor._repository.get_task.return_value = Mock(description='some')
        assert interactor.get_task_upper_description(
            task_id='any',
        ) == 'SOME'
