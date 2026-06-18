import json
from pathlib import Path
from typing import List, Optional
from .models import WorkoutLog

class FitnessTracker:
    """
    Manages the saving and retrieving of workout logs to/from a local JSON file.
    """
    def __init__(self, filepath: str = "data/workout_logs.json"):
        self.filepath = Path(filepath)
        self._ensure_data_file_exists()

    def _ensure_data_file_exists(self) -> None:
        """Creates the data directory and JSON file if they do not exist."""
        try:
            self.filepath.parent.mkdir(parents=True, exist_ok=True)
            if not self.filepath.exists():
                with open(self.filepath, "w") as f:
                    json.dump([], f)
        except OSError as e:
            raise RuntimeError(f"Failed to initialize data file at {self.filepath}: {e}")

    def load_logs(self) -> List[WorkoutLog]:
        """
        Reads the JSON file and returns a list of WorkoutLog objects.
        """
        try:
            with open(self.filepath, "r") as f:
                data = json.load(f)
                return [WorkoutLog(**item) for item in data]
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"Error reading data: {e}. Returning empty history.")
            return []
        except TypeError as e:
            print(f"Data corruption error: {e}")
            return []

    def save_log(self, log: WorkoutLog) -> bool:
        """
        Appends a new WorkoutLog to the existing JSON history.
        """
        logs = self.load_logs()
        logs.append(log)
        try:
            with open(self.filepath, "w") as f:
                # Convert logs back to dicts with indent for human-readability
                json.dump([l.to_dict() for l in logs], f, indent=4)
            return True
        except OSError as e:
            print(f"Failed to save workout log: {e}")
            return False