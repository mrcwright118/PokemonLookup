import pytest
from PokemonLookup import find


def test_get_name_positivie():
    name = find.name(1)
    assert name == "bulbasaur"
    # assert True