import pytest

from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score


# --- check_guess -----------------------------------------------------------
# check_guess returns (outcome, message), so compare against the outcome.

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# Regression: hints were backwards (Too High said "Go HIGHER!").
def test_too_high_hint_says_go_lower():
    _, message = check_guess(60, 50)
    assert "LOWER" in message
    assert "HIGHER" not in message


def test_too_low_hint_says_go_higher():
    _, message = check_guess(40, 50)
    assert "HIGHER" in message
    assert "LOWER" not in message


@pytest.mark.parametrize("guess,secret", [(1, 2), (99, 100), (2, 1), (100, 99)])
def test_off_by_one_guesses_are_not_wins(guess, secret):
    outcome, _ = check_guess(guess, secret)
    assert outcome != "Win"


# Regression: app.py cast the secret to str on even attempts, so comparisons
# were done as strings ("9" > "10"). check_guess must compare numerically.
def test_numeric_comparison_not_lexicographic():
    outcome, _ = check_guess(9, 10)
    assert outcome == "Too Low"


# --- get_range_for_difficulty ----------------------------------------------

@pytest.mark.parametrize("difficulty,expected", [
    ("Easy", (1, 20)),
    ("Normal", (1, 50)),
    ("Hard", (1, 100)),
])
def test_range_per_difficulty(difficulty, expected):
    assert get_range_for_difficulty(difficulty) == expected


# Regression: Hard (1-50) used to be a smaller range than Normal (1-100).
def test_ranges_get_wider_with_difficulty():
    sizes = [get_range_for_difficulty(d)[1] for d in ("Easy", "Normal", "Hard")]
    assert sizes == sorted(sizes)
    assert len(set(sizes)) == 3


def test_unknown_difficulty_falls_back_to_default():
    assert get_range_for_difficulty("Impossible") == (1, 100)


# --- parse_guess -----------------------------------------------------------

def test_parse_valid_integer():
    assert parse_guess("42") == (True, 42, None)


def test_parse_strips_whitespace():
    assert parse_guess("  7 ") == (True, 7, None)


def test_parse_decimal_truncates():
    assert parse_guess("3.9") == (True, 3, None)


@pytest.mark.parametrize("raw", [None, "", "   "])
def test_parse_empty_input(raw):
    ok, value, error = parse_guess(raw)
    assert ok is False
    assert value is None
    assert error == "Enter a guess."


@pytest.mark.parametrize("raw", ["abc", "1,5", "12abc", "--3"])
def test_parse_non_numeric(raw):
    ok, value, error = parse_guess(raw)
    assert ok is False
    assert value is None
    assert error == "That is not a number."


@pytest.mark.parametrize("raw", ["inf", "nan", "1e999"])
def test_parse_non_finite_does_not_crash(raw):
    # float("inf") -> int() raises OverflowError, nan raises ValueError.
    ok, value, _ = parse_guess(raw)
    assert ok is False
    assert value is None


# --- update_score ----------------------------------------------------------

def test_win_on_first_attempt_scores_90():
    assert update_score(0, "Win", 1) == 90


def test_win_points_decrease_with_attempts():
    assert update_score(0, "Win", 1) > update_score(0, "Win", 5)


def test_win_points_have_a_floor_of_10():
    assert update_score(0, "Win", 50) == 10


def test_win_adds_to_existing_score():
    assert update_score(25, "Win", 2) == 25 + 80


# Regression: "Too High" used to award a bonus on some attempts.
@pytest.mark.parametrize("outcome", ["Too High", "Too Low"])
@pytest.mark.parametrize("attempt", [1, 2, 3, 4])
def test_wrong_guess_always_costs_5(outcome, attempt):
    assert update_score(50, outcome, attempt) == 45


def test_unknown_outcome_leaves_score_unchanged():
    assert update_score(30, "Whatever", 1) == 30
