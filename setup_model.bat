@echo off
echo Generating synthetic metrics data...
.\.venv\Scripts\python.exe training\generate_data.py

echo.
echo Training anomaly detection model...
.\.venv\Scripts\python.exe training\train.py

echo.
echo Setup complete.
pause