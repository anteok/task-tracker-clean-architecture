import pytest

from details.id_generator import IdGenerator


class TestIdGenerator:

    @pytest.fixture(scope='module')
    def generator(self):
        return IdGenerator()

    @pytest.mark.parametrize('_id', range(10))
    def test_new_id(self, _id, generator):
        assert generator.get_id() == str(_id)
