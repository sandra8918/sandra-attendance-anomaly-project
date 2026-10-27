"""Employee Attendance Anomalies.

Author: Sandra Otubushin
Date: 2026-10
"""

import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md("""
    # Employee Attendance Anomaly Detection

    This app identifies employee attendance records that may need review.

    Use the controls below to adjust the anomaly thresholds.
    """)


@app.cell
def _(Path, load_attendance_data):
    project_root = Path(__file__).resolve().parents[2]
    data_path = project_root / "data" / "attendance_data.csv"
    df = load_attendance_data(data_path)
    return (df,)


@app.cell
def _(mo):
    minimum_hours = mo.ui.slider(
        start=20,
        stop=40,
        value=32,
        label="Minimum worked hours",
    )

    minimum_late_days = mo.ui.slider(
        start=0,
        stop=7,
        value=3,
        label="Minimum late days",
    )

    minimum_absence_days = mo.ui.slider(
        start=0,
        stop=7,
        value=2,
        label="Minimum absence days",
    )

    mo.vstack(
        [
            minimum_hours,
            minimum_late_days,
            minimum_absence_days,
        ]
    )
    return minimum_absence_days, minimum_hours, minimum_late_days


@app.cell
def _(
    detect_attendance_anomalies,
    df,
    minimum_absence_days,
    minimum_hours,
    minimum_late_days,
):
    anomalies_df = detect_attendance_anomalies(
        df,
        minimum_worked_hours=minimum_hours.value,
        minimum_late_days=minimum_late_days.value,
        minimum_absence_days=minimum_absence_days.value,
    )
    return (anomalies_df,)


@app.cell
def _(anomalies_df, df, mo):
    mo.md(f"""
    ## Results

    **{anomalies_df.height} of {df.height} attendance records**
    were flagged as anomalies.
    """)


@app.cell
def _(anomalies_df, mo):
    mo.ui.table(anomalies_df)


@app.cell
def _(mo):
    mo.md("""
    ## Interpretation

    A flagged record is a signal for review. It does not automatically
    indicate a policy violation.

    [View the project documentation](https://sandra8918.github.io/sandra-attendance-anomaly-project/)
    """)


if __name__ == "__main__":
    app.run()
