"""A very simple heart simulation.

Simulates a beating heart as alternating contraction (systole) and
relaxation (diastole) phases, and computes basic outputs like heart rate
and blood pressure for each beat.
"""


class Heart:
    def __init__(self, resting_bpm=70, systolic_pressure=120, diastolic_pressure=80):
        self.resting_bpm = resting_bpm
        self.systolic_pressure = systolic_pressure
        self.diastolic_pressure = diastolic_pressure
        self.beat_count = 0

    def beat(self):
        """Simulate a single heartbeat, alternating systole/diastole."""
        self.beat_count += 1
        phase = "systole" if self.beat_count % 2 == 1 else "diastole"
        pressure = self.systolic_pressure if phase == "systole" else self.diastolic_pressure
        return {
            "beat_number": self.beat_count,
            "phase": phase,
            "pressure_mmHg": pressure,
        }

    def simulate(self, beats=10):
        return [self.beat() for _ in range(beats)]


if __name__ == "__main__":
    heart = Heart()
    for result in heart.simulate(6):
        print(result)
