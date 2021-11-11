from ld_code_exam.exercise_03 import solution


def test_solution():
    assert solution(["gift1", "gift2", "gift3"]) == 3

    assert solution(["gift1", "gift1", "gift1"]) == 1

    assert solution(["gift1", "gift2", "gift1"]) == 2

    assert solution(["gift1", "gift1", "gift1", "gift2", "gift1", "gift3"]) == 3

    assert solution(["Gift3", "Gift5", "Gift3", "Gift2", "Gift1", "Gift3", "Gift4", "Gift2"]) == 6

    assert solution(["Gift1", "Gift3", "Gift1", "Gift2", "Gift1", "Gift4", "Gift3", "Gift1"]) == 4
