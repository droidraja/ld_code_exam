from ld_code_exam.exercice_01 import solution


def test_solution():
    assert solution(None) == []
    assert solution([]) == []
    assert solution([1, 1, 1]) == [1]
    assert solution([1, 2, 3, ]) == [1, 2, 3]
    assert solution([1, 1, 1, 2, 2, 3]) == [1]
