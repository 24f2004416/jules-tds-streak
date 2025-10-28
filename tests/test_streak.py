import pytest
from streak import longest_positive_streak

def test_longest_positive_streak_empty_list():
    """Test with an empty list, expecting 0."""
    assert longest_positive_streak([]) == 0

def test_longest_positive_streak_multiple_streaks():
    """Test with multiple positive streaks, ensuring the longest is returned."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_longest_positive_streak_with_zeros():
    """Test that zeros correctly break a streak."""
    assert longest_positive_streak([1, 2, 0, 3, 4, 5, 0, 1]) == 3

def test_longest_positive_streak_with_negatives():
    """Test that negative numbers correctly break a streak."""
    assert longest_positive_streak([1, -5, 2, 3, -10, 4, 5, 6, 7]) == 4

def test_longest_positive_streak_all_positive():
    """Test a list containing only positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_longest_positive_streak_all_non_positive():
    """Test a list with no positive numbers."""
    assert longest_positive_streak([-1, -2, 0, -5, -10]) == 0

def test_longest_positive_streak_single_element_positive():
    """Test a list with a single positive number."""
    assert longest_positive_streak([42]) == 1

def test_longest_positive_streak_single_element_non_positive():
    """Test a list with a single non-positive number."""
    assert longest_positive_streak([-42]) == 0
    assert longest_positive_streak([0]) == 0

def test_longest_positive_streak_at_beginning():
    """Test when the longest streak is at the beginning."""
    assert longest_positive_streak([5, 6, 7, -1, 2, 3]) == 3

def test_longest_positive_streak_at_end():
    """Test when the longest streak is at the end."""
    assert longest_positive_streak([-1, 2, 3, 5, 6, 7]) == 5