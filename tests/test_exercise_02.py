from ld_code_exam.exercise_02 import is_number, solution
import os


def test_is_number():
    assert not is_number("")
    assert is_number("1.23E-7")
    assert not is_number("1 2 3 ")
    assert not is_number("abacsa")
    assert is_number("12312345")
    assert is_number("-123123")
    assert is_number("-1.123E-7")


def test_solution():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    test_file_name = 'test_exercise02_data.txt'
    test_file_path = os.path.join(current_dir, test_file_name)
    assert solution(test_file_path) == ["1", "2.123E-7", "-2000", "3.123"]
