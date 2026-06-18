# CLI Fitness & Habit Logger 🏋️‍♂️

A robust, interactive command-line interface application built in Python for tracking daily fitness metrics. Designed with clean architecture, this tool allows users to log bodyweight exercises and track their progress through a 6-day gym split.

## Features
* **Daily Logging:** Track total pushups, plank duration (in seconds), and your current day in a 6-day gym split.
* **Data Persistence:** Automatically serializes data and saves it to a local `workout_logs.json` file with precise ISO-formatted timestamps.
* **Interactive UI:** Utilizes the `rich` library for a beautiful, color-coded terminal experience featuring input validation and formatted data tables.

## Architecture & Code Quality
* **Object-Oriented Design:** Clear separation of concerns between Data Models (`models.py`), Business Logic (`tracker.py`), and the User Interface (`cli.py`).
* **Type Safety:** Heavily utilizes Python Type Hinting and `dataclasses` for predictable behavior and developer experience.
* **Robust Error Handling:** Comprehensive `try/except` blocks to gracefully handle file I/O operations, JSON decoding errors, and unexpected user inputs.

## Prerequisites
* Python 3.9+
* `pip`

## Installation & Setup

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

```bash 
pip install -r requirements.txt
```

```bash 
python -m src.cli
```
