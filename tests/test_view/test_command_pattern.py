from unittest.mock import Mock, patch

import pytest

from details.id_generator import IdGenerator
from views.command import CreatePattern


class TestCreatePattern:

    @patch.object(IdGenerator, 'get_id')
    @pytest.mark.parametrize('command, description', [
        ('create "new task"', 'new task'),
        ('create "do something"', 'do something'),
    ])
    def test_create_pattern(self, _id, command, description):
        creator = CreatePattern(Mock())
        creator._id_generator.get_id.return_value = '12'
        assert creator.respond(command) == f'A new task "{description}" is in_backlog with id 12'
