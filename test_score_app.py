from score_app import calculate_stats


def test_calculate_stats_basic():
    average, highest, lowest = calculate_stats([80, 90, 70])

    assert average == 80
    assert highest == 90
    assert lowest == 70


def test_calculate_stats_all_100():
    average, highest, lowest = calculate_stats([100, 100, 100])

    assert average == 100
    assert highest == 100
    assert lowest == 100


def test_calculate_stats_all_0():
    average, highest, lowest = calculate_stats([0, 0, 0])

    assert average == 0
    assert highest == 0
    assert lowest == 0


def test_calculate_stats_varied():
    average, highest, lowest = calculate_stats([80, 55, 92, 70])

    assert average == 74.25
    assert highest == 92
    assert lowest == 55