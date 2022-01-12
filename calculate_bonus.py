from allpairspy import AllPairs


def values_check(salary, review_result, engineer_level):
    if salary is None:
        raise ValueError("Salary empty")
    if review_result is None:
        raise ValueError("Review result empty")
    if engineer_level is None:
        raise ValueError("Engineer level empty")
    if salary < 70000 or salary > 750000:
        raise ValueError("Salary out of range")
    if review_result < 1 or review_result > 5:
        raise ValueError("Review result out of range")
    if engineer_level < 7 or engineer_level > 17:
        raise ValueError("Engineer level out of range")


def calc_level_bonus(salary, engineer_level):
    if engineer_level < 10:
        bonus = salary * 0.05
    elif 10 <= engineer_level < 13:
        bonus = salary * 0.1
    elif 13 <= engineer_level < 15:
        bonus = salary * 0.15
    else:
        bonus = salary * 0.2
    return bonus


def calc_review_result(bonus, review_result):
    if 2 <= review_result < 2.5:
        bonus = bonus + bonus * 0.25
    elif 2.5 <= review_result < 3:
        bonus = bonus + bonus * 0.5
    elif 3 <= review_result < 3.5:
        bonus = bonus + bonus
    elif 3.5 <= review_result < 4:
        bonus = bonus + bonus * 1.5
    elif review_result < 2:
        bonus = bonus
    else:
        bonus = bonus + bonus * 2
    return bonus


def calc_bonus(salary, review_result, engineer_level):
    values_check(salary, review_result, engineer_level)
    return calc_review_result(calc_level_bonus(salary, engineer_level), review_result)


if __name__ == '__main__':
    # salary = 100000
    # review_res = 2
    # eng_level = 17
    # print(calc_bonus(salary, review_res, eng_level))

    # parameters = [
    #     [100000],
    #     [1.0, 2.6, 3.1, 3.6, 5.0],
    #     [7]
    # ]

    parameters = [
        [100000],
        [1],
        [7, 11, 13, 17]
    ]

    print("PAIRWISE:")
    for i, pairs in enumerate(AllPairs(parameters)):
        print(pairs, calc_bonus(pairs[0], pairs[1], pairs[2]))

