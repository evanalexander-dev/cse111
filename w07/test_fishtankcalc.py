import pytest

from fishtankcalc import (
    check_tank_size,
    check_fish_compatibility,
    check_fish_school_size,
    check_fish_quantity_in_tank
)

def test_check_tank_size():
    fish_data = {
        "Fish1": {"min-tank-size": 5},
        "Fish2": {"min-tank-size": 10},
        "Fish3": {"min-tank-size": 15}
    }
    fish_in_tank = {
        "Fish1": 1,
        "Fish2": 1,
        "Fish3": 1
    }
    assert check_tank_size(fish_data, fish_in_tank, 5) == ["Fish2", "Fish3"]
    assert check_tank_size(fish_data, fish_in_tank, 10) == ["Fish3"]
    assert check_tank_size(fish_data, fish_in_tank, 15) == []

def test_check_fish_compatibility():
    fish_data = {
        "Fish1": {"incompatible": ["Fish2"]},
        "Fish2": {"incompatible": ["Fish1"]},
        "Fish3": {"incompatible": ["Fish1"]}
    }
    assert check_fish_compatibility(fish_data, {"Fish1": 1, "Fish2": 1, "Fish3": 1}) == [["Fish1", "Fish2"], ["Fish3", "Fish1"]]
    assert check_fish_compatibility(fish_data, {"Fish1": 1, "Fish3": 1}) == [["Fish3", "Fish1"]]
    assert check_fish_compatibility(fish_data, {"Fish1": 1, "Fish2": 1}) == [["Fish1", "Fish2"]]

def test_check_fish_school_size():
    fish_data = {
        "Fish1": {"min-quantity": 5, "max-quantity": 10},
        "Fish2": {"min-quantity": 1, "max-quantity": -1},
        "Fish3": {"min-quantity": 2, "max-quantity": 3}
    }
    assert check_fish_school_size(fish_data, {"Fish1": 4, "Fish2": 1, "Fish3": 3}) == [[-1, "Fish1"]]
    assert check_fish_school_size(fish_data, {"Fish1": 11, "Fish2": 1, "Fish3": 1}) == [[1, "Fish1"], [-1, "Fish3"]]
    assert check_fish_school_size(fish_data, {"Fish1": 5, "Fish2": 1, "Fish3": 2}) == []


def test_check_fish_quantity_in_tank():
    fish_data = {
        "Fish1": {"max-length": 8},
        "Fish2": {"max-length": 5},
        "Fish3": {"max-length": 3}
    }
    fish_in_tank = {
        "Fish1": 1,
        "Fish2": 1,
        "Fish3": 1
    }
    assert check_fish_quantity_in_tank(fish_data, fish_in_tank, 20) is False
    assert check_fish_quantity_in_tank(fish_data, fish_in_tank, 16) is False
    assert check_fish_quantity_in_tank(fish_data, fish_in_tank, 10) is True


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
