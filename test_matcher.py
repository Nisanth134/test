# tests/test_matcher.py
import pytest
from matcher import calculate_match_score, get_best_matches

def test_exact_match():
    assert calculate_match_score(['python', 'flask'], ['Python', 'Flask']) == 100.0

def test_partial_match():
    assert calculate_match_score(['python', 'java'], ['python', 'sql', 'aws']) == 33.33

def test_no_skills_match():
    assert calculate_match_score(['java'], ['python', 'c++']) == 0.0

def test_empty_lists():
    assert calculate_match_score([], ['python']) == 0.0
    assert calculate_match_score(['python'], []) == 100.0

def test_invalid_types_raise_error():
    with pytest.raises(TypeError):
        calculate_match_score("python", ["python"]) # Passing a string instead of a list
