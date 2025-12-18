import os
import time
import json
import logging
from datetime import datetime
from behave.model_core import Status
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from zipfile import ZipFile

# GLOBAL COLLECTORS
html_report_data = []
screenshot_paths = []
log_file_path = None
CUSTOM_JSON_FILE = "reports/behave_result.json"


# ----------------------------------------------------------
# BEFORE ALL
# ----------------------------------------------------------
def before_all(context):
    global log_file_path, logger

    print("\n[BEFORE ALL] Starting PCS automation...\n")

    os.makedirs("logs", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file_path = f"logs/PCS_Execution_{timestamp}.log"

    logger = logging.getLogger("PCS_LOGGER")
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler(log_file_path)
    logger.addHandler(fh)

    logger.info("Execution Started")


# ----------------------------------------------------------
# BEFORE SCENARIO
# ----------------------------------------------------------
def before_scenario(context, scenario):
    scenario._start_time = time.time()
    logger.info(f"Scenario Started: {scenario.name}")


# ----------------------------------------------------------
# BEFORE STEP
# ----------------------------------------------------------
def before_step(context, step):
    step._start_time = time.time()


# ----------------------------------------------------------
# AFTER STEP
# ----------------------------------------------------------
def after_step(context, step):
    step.duration = round(time.time() - step._start_time, 3)
    logger.info(f"Step: {step.name} → {step.status.name} ({step.duration}s)")


# ----------------------------------------------------------
# AFTER SCENARIO → STORE PROPER JSON
# ----------------------------------------------------------
def after_scenario(context, scenario):
    scenario_duration = round(time.time() - scenario._start_time, 3)

    # screenshot if failed
    screenshot_path = None
    if scenario.status == Status.failed and hasattr(context, "driver"):
        os.makedirs("screenshots/PCS", exist_ok=True)
        screenshot_path = f"screenshots/PCS/{scenario.name}.png"
        context.driver.save_screenshot(screenshot_path)
        screenshot_paths.append(screenshot_path)
        attach(open(screenshot_path, "rb").read(), "Failure Screenshot", AttachmentType.PNG)

    # collect steps
    steps = []
    scenario_failed = False

    for step in scenario.steps:
        step_status = step.status.name.lower()
        if step_status == "failed":
            scenario_failed = True

        steps.append({
            "name": step.name,
            "status": step_status,
            "duration": getattr(step, "duration", 0)
        })

    # final scenario status
    final_status = "failed" if scenario_failed else "passed"

    # ADD TO JSON
    html_report_data.append({
        "scenario": scenario.name,
        "status": final_status,
        "duration": scenario_duration,
        "steps": steps,
        "tags": list(scenario.tags),
        "screenshot": screenshot_path
    })


# ----------------------------------------------------------
# AFTER ALL → SAFE JSON WRITE + ZIP
# ----------------------------------------------------------
def after_all(context):
    print("\n[AFTER ALL] Writing final JSON...")

    tmp = CUSTOM_JSON_FILE + ".tmp"

    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(html_report_data, f, indent=4, ensure_ascii=False)

    if os.path.exists(CUSTOM_JSON_FILE):
        os.remove(CUSTOM_JSON_FILE)

    os.rename(tmp, CUSTOM_JSON_FILE)
    print(f"[JSON] Saved → {CUSTOM_JSON_FILE}")

    # ZIP screenshots
    if screenshot_paths:
        zip_name = f"screenshots/PCS/PCS_Screenshots_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
        with ZipFile(zip_name, "w") as z:
            for s in screenshot_paths:
                if os.path.isfile(s):
                    z.write(s, os.path.basename(s))
            if log_file_path:
                z.write(log_file_path, os.path.basename(log_file_path))

        print(f"[ZIP] Created → {zip_name}")

    print("[AFTER ALL] Execution done.\n")
