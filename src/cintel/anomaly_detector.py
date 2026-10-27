"""Employee Attendance Anomalies.

Author: Sandra Otubushin
Date: 2026-10
"""

from pathlib import Path

import polars as pl

from cintel.utils_clinic import (
    detect_attendance_anomalies,
    load_attendance_data,
)


def main() -> None:
    """Run the employee attendance anomaly-detection pipeline."""
    project_root = Path(__file__).resolve().parents[2]
    data_path = project_root / "data" / "attendance_data.csv"
    artifacts_dir = project_root / "artifacts"
    output_path = artifacts_dir / "attendance_anomalies.csv"

    artifacts_dir.mkdir(exist_ok=True)

    df: pl.DataFrame = load_attendance_data(data_path)

    anomalies_df = detect_attendance_anomalies(
        df,
        minimum_worked_hours=32,
        minimum_late_days=3,
        minimum_absence_days=2,
    )

    print(f"Attendance records analyzed: {df.height}")
    print(f"Attendance anomalies found: {anomalies_df.height}")

    anomalies_df.write_csv(output_path)

    print(f"Results saved to: {output_path}")
    print("Attendance anomaly pipeline executed successfully!")


if __name__ == "__main__":
    main()
