from unittest.mock import Mock

import pytest

from entities.task import TaskStatus
from views.command_pattern import CommandPatternFactory


class TestCommandPatternFactory:

    @pytest.fixture
    def repository(self):
        return Mock(
            get_task=Mock(return_value=Mock(description='do bar', status=TaskStatus.done)),
        )

    @pytest.mark.parametrize('command, response', [
        ('create task "do something"', 'A new task "do something" is in_backlog with id 0'),
        ('what is 12', 'THE TASK WITH ID 12 IS "DO BAR"'),
        ('move task 12 to in_work', 'The task with id 12 was moved to status "in_work"'),
        ('delete task 12', 'The task with id 12 was deleted'),
        ('create task do something', 'Cannot parse command "create task do something"'),
        ('what is love', 'Cannot parse command "what is love"'),
        ('delete task task', 'Cannot parse command "delete task task"'),
        ('move task 12 to random status', 'Cannot parse command "move task 12 to random status"')
    ])
    def test_factory(self, command, response, repository):
        assert CommandPatternFactory.get_response(command, repository) == response
