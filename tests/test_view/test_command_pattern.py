from unittest.mock import Mock, patch

import pytest

from controllers.in_memory import UpdateStatusController, DeleteTaskController
from details.id_generator import IdGenerator
from views.command_pattern import CreatePattern, GetDescriptionPattern, UpdateStatusPattern, DeleteTaskPattern


class TestCommandPattern:

    @patch.object(IdGenerator, 'get_id')
    @pytest.mark.parametrize('command, description', [
        ('create task "new task"', 'new task'),
        ('create task "do something"', 'do something'),
    ])
    def test_create_pattern(self, _id, command, description):
        creator = CreatePattern(Mock())
        creator._id_generator.get_id.return_value = '12'
        assert creator.respond(command) == f'A new task "{description}" is in_backlog with id 12'

    def test_get_description_pattern(self):
        descriptor = GetDescriptionPattern(
            Mock(get_task=Mock(return_value=Mock(description='do some')))
        )
        assert descriptor.respond('12') == 'THE TASK WITH ID 12 IS "DO SOME"'

    @patch.object(UpdateStatusController, attribute='execute')
    def test_update_status(self, execute_method):
        updater = UpdateStatusPattern(Mock())
        assert updater.respond('move task 12 to prioritized') == 'The task with id 12 was moved to status "prioritized"'
        execute_method.assert_called_with('12', 'prioritized')

    @patch.object(DeleteTaskController, attribute='execute')
    def test_delete_task(self, execute_method):
        deleter = DeleteTaskPattern(Mock())
        assert deleter.respond('delete task 12') == 'The task with id 12 was deleted'
        execute_method.assert_called_with('12')