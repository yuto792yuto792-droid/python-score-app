from score_app import calculate_stats

def test_calculate_stats():
    average, highest, lowest = calculate_stats([80, 90, 70])

    assert average == 80
    assert highest == 90
    assert lowest == 70