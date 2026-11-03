from heart_simulation import Heart


def test_beat_alternates_phase():
    heart = Heart()
    first = heart.beat()
    second = heart.beat()
    assert first["phase"] == "systole"
    assert second["phase"] == "diastole"


def test_beat_count_increments():
    heart = Heart()
    heart.simulate(5)
    assert heart.beat_count == 5


def test_simulate_returns_requested_number_of_beats():
    heart = Heart()
    results = heart.simulate(10)
    assert len(results) == 10


def test_pressures_match_phase():
    heart = Heart(systolic_pressure=120, diastolic_pressure=80)
    results = heart.simulate(4)
    assert results[0]["pressure_mmHg"] == 120
    assert results[1]["pressure_mmHg"] == 80
