from dataclasses import dataclass, asdict
from datetime import datetime

@dataclass
class WorkoutLog:
    """
    Represents a single day's fitness tracking data.
    """
    timestamp: str
    pushups: int
    plank_duration_sec: int
    gym_split_day: int

    @classmethod
    def create(cls, pushups: int, plank_duration_sec: int, gym_split_day: int) -> "WorkoutLog":
        """
        Factory method to create a new log with an automatic timestamp.
        """
        return cls(
            timestamp=datetime.now().isoformat(),
            pushups=pushups,
            plank_duration_sec=plank_duration_sec,
            gym_split_day=gym_split_day
        )

    def to_dict(self) -> dict:
        """Converts the dataclass instance to a dictionary for JSON serialization."""
        return asdict(self)