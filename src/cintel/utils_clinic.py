"""utils_clinic.py.

Shared helper functions for employee attendance anomaly detection.

Author: Sandra Otubushin
Date: 2026-10
"""

from pathlib import Path

import polars as pl


def load_attendance_data(data_file: Path) -> pl.DataFrame:
    """Read employee attendance records from a CSV file."""
    return pl.read_csv(data_file)


def detect_attendance_anomalies(
    df: pl.DataFrame,
    minimum_worked_hours: float = 32,
    minimum_late_days: int = 3,
    minimum_absence_days: int = 2,
) -> pl.DataFrame:
    """Return employees meeting one or more attendance anomaly conditions."""
    return df.filter(
        (pl.col("worked_hours") <= minimum_worked_hours)
        | (pl.col("late_days") >= minimum_late_days)
        | (pl.col("absence_days") >= minimum_absence_days)
    )
