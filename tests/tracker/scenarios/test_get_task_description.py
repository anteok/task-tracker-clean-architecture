from unittest.mock import Mock

import pytest
from freezegun import freeze_time

from tracker.scenarios.get_task_description import GetTaskDescriptionInteractor, GetTaskDescriptionDto


class TestGetTaskDescriptionInteractor:

    @pytest.fixture
    def interactor(self) -> GetTaskDescriptionInteractor:
        return GetTaskDescriptionInteractor(
            repository=Mock(
                get_task_description=Mock(),
            )
        )

    @freeze_time('2020-10-10')
    def test_get_task_upper_description(self, interactor):
        interactor._repository.get_task_description.return_value = Mock(description='some')
        assert interactor.get_task_upper_description(
            task_id='some',
        ) == GetTaskDescriptionDto(
            description='SOME'
        )
