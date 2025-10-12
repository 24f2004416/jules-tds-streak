import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_no_positive_numbers():
    """Test that a list with no positive numbers returns a streak of 0."""
    assert longest_positive_streak([-1, -2, 0, -5]) == 0

def test_single_streak():
    """Test a simple case with a single streak of positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_multiple_streaks():
    """Test that the function returns the length of the longest streak."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_streaks_of_equal_length():
    """Test that if there are multiple streaks of the same max length, it returns that length."""
    assert longest_positive_streak([1, 2, 0, 4, 5]) == 2

def test_streak_at_the_end():
    """Test that a streak at the end of the list is correctly identified."""
    assert longest_positive_streak([-1, 0, 1, 2, 3]) == 3

def test_streak_at_the_beginning():
    """Test that a streak at the beginning of the list is correctly identified."""
    assert longest_positive_streak([1, 2, 3, 0, -1]) == 3

def test_list_with_zeros():
    """Test that zeros correctly break a streak."""
    assert longest_positive_streak([1, 2, 0, 3, 4, 5]) == 3

def test_list_with_negatives():
    """Test that negative numbers correctly break a streak."""
    assert longest_positive_streak([1, 2, -5, 3, 4, 5]) == 3

def test_long_list():
    """Test with a longer list to ensure performance is not an issue."""
    assert longest_positive_streak([1] * 100 + [-1] + [1] * 50) == 100

def test_all_ones():
    """Test a simple case with all ones."""
    assert longest_positive_streak([1, 1, 1]) == 3
