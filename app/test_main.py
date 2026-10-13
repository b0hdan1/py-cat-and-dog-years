import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_human_age",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (100, 100, [21, 17])
    ],
    ids=[
        "return 0 humans years if pets age = 0",
        "boundary 14 pet years should return 0 human year",
        "boundary 15 pet years should return 1 human year",
        "24 pet years should return 2 human years",
        "every 4 cat years after 24 should increase humans age for 1",
        "every 5 dog years after 24 should increase humans age for 1",
        "older ages should return different step of value"
    ]
)
def test_correct_getting_human_age_for_pets(
        cat_age: int,
        dog_age: int,
        expected_human_age: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_human_age


def test_should_raise_error_if_pet_age_is_not_integer() -> None:
    with pytest.raises(TypeError):
        get_human_age("15", 15)
