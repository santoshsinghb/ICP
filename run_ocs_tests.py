import os
import subprocess

# Ensure the report directory exists
os.makedirs("Reports/PCS/allure-results", exist_ok=True)

# Run behave with allure formatter and output to Reports/PCS/allure-results
subprocess.run([
    "behave",
    "features/PCS",
    "-f", "allure_behave.formatter:AllureFormatter",
    "-o", "Reports/PCS/allure-results"
])
