from allpairspy import AllPairs
import pytest
from calculate_bonus import calc_bonus


list_salary = [None, 50001, 60999]
list_rew_res = [None, 0.9, 6]
list_level = [None, 6, 18]


@pytest.mark.parametrize(
    "salary, review_res, eng_level",
    AllPairs([list_salary, [1], [17]])
)
def test_salary_out_of_range(salary, review_res, eng_level):
    """Check salary value error"""
    with pytest.raises(ValueError) as e:
        calc_bonus(salary, review_res, eng_level)
    assert str(e.value) in [
        "Salary empty",
        "Salary out of range"
    ]


@pytest.mark.parametrize(
    "salary, review_res, eng_level",
    AllPairs([[100000], list_rew_res, [17]])
)
def test_review_res_out_of_range(salary, review_res, eng_level):
    """Check review result value error"""
    with pytest.raises(ValueError) as e:
        calc_bonus(salary, review_res, eng_level)
    assert str(e.value) in [
        "Review result empty",
        "Review result out of range"
    ]


@pytest.mark.parametrize(
    "salary, review_res, eng_level",
    AllPairs([[100000], [1], list_level])
)
def test_engineer_level_out_of_range(salary, review_res, eng_level):
    """Check engineer level value error"""
    with pytest.raises(ValueError) as e:
        calc_bonus(salary, review_res, eng_level)
    assert str(e.value) in [
        "Engineer level empty",
        "Engineer level out of range"
    ]


@pytest.mark.parametrize(
    "review_res, correct_result",
    [(1, 5000),
     (2.6, 7500),
     (3.1, 10000),
     (3.6, 12500),
     (5, 15000)
     ]

)
def test_review_bonus_correct_count(review_res, correct_result):
    """Check correct bonus based on review result"""
    calc = calc_bonus(100000, review_res, 7)
    assert calc == correct_result


@pytest.mark.parametrize(
    "eng_level, correct_result",
    [(7, 5000),
     (11, 10000),
     (13, 15000),
     (17, 20000)
     ]

)
def test_engineer_level_bonus_correct_count(eng_level, correct_result):
    """Check correct bonus based on engineer level"""
    calc = calc_bonus(100000, 1, eng_level)
    assert calc == correct_result