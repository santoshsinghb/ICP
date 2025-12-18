#!/usr/bin/env python3
"""
report_generator.py
Reads Behave JSON (format produced by `behave -f json -o behave_result.json`)
and renders a single-file Allure-like HTML report.

Usage:
  python reports/report_generator.py --input reports/behave_result.json --output reports/beautiful_report.html
"""
import argparse
import json
import os
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

def load_behave_json(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        data = json.load(f)
    return data

def normalize(data):
    """
    Convert Behave JSON (list of features) into flat list of scenarios:
    [
      {
        "feature": <feature_name>,
        "scenario": <scenario_name>,
        "status": passed/failed/skipped,
        "duration": seconds (sum of step durations),
        "tags": [...],
        "steps": [
            {"name":..., "status":..., "duration":...}, ...
        ],
        "location": <feature_file:line>
      },
      ...
    ]
    """
    out = []
    for feature in data:
        feature_name = feature.get("name") or feature.get("keyword") or "Feature"
        elements = feature.get("elements", []) or []
        for elem in elements:
            # Only process scenarios (skip background)
            if elem.get("type") not in ("scenario", "scenario_outline"):
                continue
            scenario_name = elem.get("name") or "Unnamed Scenario"
            tags = [t for t in elem.get("tags", [])] if elem.get("tags") else []
            steps = []
            total = 0.0
            step_entries = elem.get("steps", []) or []
            for s in step_entries:
                res = s.get("result", {}) or {}
                st_status = res.get("status", "skipped")
                st_duration = res.get("duration", 0) or 0
                # ensure float
                try:
                    st_duration = float(st_duration)
                except Exception:
                    st_duration = 0.0
                total += st_duration
                steps.append({
                    "keyword": s.get("keyword"),
                    "name": s.get("name"),
                    "status": st_status,
                    "duration": round(st_duration, 3)
                })

            # scenario-level status: failed if any step failed, else passed/skipped
            scenario_status = "passed"
            for st in steps:
                if st.get("status") == "failed":
                    scenario_status = "failed"
                    break
                if st.get("status") == "skipped" and scenario_status != "failed":
                    scenario_status = "skipped"

            out.append({
                "feature": feature_name,
                "scenario": scenario_name,
                "status": scenario_status,
                "duration": round(total, 3),
                "tags": [t.get("name") if isinstance(t, dict) else t for t in tags],
                "steps": steps,
                "location": elem.get("location")
            })
    return out

def build_summary(scenarios):
    total = len(scenarios)
    passed = sum(1 for s in scenarios if s["status"] == "passed")
    failed = sum(1 for s in scenarios if s["status"] == "failed")
    skipped = sum(1 for s in scenarios if s["status"] == "skipped")
    total_duration = round(sum(s.get("duration", 0) for s in scenarios), 2)
    return {"total": total, "passed": passed, "failed": failed, "skipped": skipped, "total_duration": total_duration}

def render(scenarios, summary, output_path):
    template_dir = os.path.dirname(os.path.abspath(__file__))
    env = Environment(loader=FileSystemLoader(template_dir))
    tpl = env.get_template("template.html")
    html = tpl.render(now=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), scenarios=scenarios, summary=summary)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Report generated:", output_path)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", required=True, help="Path to behave JSON (e.g. reports/behave_result.json)")
    parser.add_argument("--output", "-o", required=True, help="Output HTML path (e.g. reports/beautiful_report.html)")
    args = parser.parse_args()

    data = load_behave_json(args.input)
    scenarios = normalize(data)
    summary = build_summary(scenarios)
    render(scenarios, summary, args.output)

if __name__ == "__main__":
    main()
