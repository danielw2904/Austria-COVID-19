import sys
import csv
import re
import os
import requests
import pandas as pd

from datetime import datetime, timedelta
from lxml import html


url = "https://www.sozialministerium.at/Informationen-zum-Coronavirus/Neuartiges-Coronavirus-(2019-nCov).html"


states = [
    "Burgenland",
    "Kärnten",
    "Niederösterreich",
    "Oberösterreich",
    "Salzburg",
    "Steiermark",
    "Tirol",
    "Vorarlberg",
    "Wien",
]


def get_state(state, text, prefix):
    m = re.search("{}.*{}\s+\((\d+)(?: -.*)*\)".format(prefix, state), text, re.MULTILINE)
    if m is not None:
        return int(m.group(1))
    return 0


def fetch_data(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)

    text = tree.xpath('//div[@class="infobox"]')[0].text_content()
    tests = r".*Bisher durchgeführte Testungen in.*\):\s+([\d\.,]+)"
    summary = r".*Bestätigte (?:Erkrankungsfälle|Fälle),.*Stand\s+(.*),\s+(.*)\s+Uhr:\s+(\d+)\s+Fälle"
    recovered = r".*Genesene Personen,.*Stand\s+(.*),\s+(.*)\s+Uhr:\s+(\d+)"
    deaths = r".*Todesfälle,.*Uhr:\s+([\d\.,]+)"

    m = re.search(summary, text, re.MULTILINE)
    if m is None:
        return None, None
    date, time, total_cases = m.groups()

    m = re.search(tests, text, re.MULTILINE)
    total_tests = None
    if m is not None:
        total_tests = m.groups()[0]
        total_tests = total_tests.replace(",", "").replace(".", "")
    else:
        print("[!] Failed to parse total tests")

    m = re.search(deaths, text, re.MULTILINE)
    total_deaths = 0
    if m is not None:
        total_deaths = m.groups()[0]
        total_deaths = total_deaths.replace(",", "").replace(".", "")

    cases_data = {
        "date": date,
        "time": time,
        "total_cases": total_cases,
        "total_tests": total_tests,
        "total_deaths": total_deaths
    }

    m = re.search(recovered, text, re.MULTILINE)
    has_recovered = False
    recovered_data = None
    if m is not None:
        has_recovered = True
        recovered_date, recovered_time, total_recovered = m.groups()
        recovered_data = {
            "date": recovered_date,
            "time": recovered_time,
            "total_recovered": total_recovered,
        }
    else:
        print("[!] Failed to parse recovered")

    for state in states:
        cases_data[state] = get_state(state, text, "Bestätigte")
        if has_recovered:
            recovered_data[state] = get_state(state, text, "Genesene")

    return cases_data, recovered_data


def wayback(timestamp):
    archive_url = "http://archive.org/wayback/available?url={}&timestamp={}".format(
        url, timestamp
    )
    resp = requests.get(archive_url).json()
    closest = resp["archived_snapshots"]["closest"]
    actual_ts = closest["timestamp"]
    snapshot_url = closest["url"]
    return actual_ts, snapshot_url


index_cols = ["date", "time"]


def clean_data(cases):
    print("PRE CLEAN", cases)
    cases = pd.DataFrame(cases)
    cases.sort_values(by=index_cols, inplace=True)
    cases.drop_duplicates(subset=index_cols, keep="last", inplace=True)
    print("POSTCLEAN", cases)
    return cases


def historical():
    today_cases, today_recovered = fetch_data(url)
    now = datetime.now()
    num_days = 16
    cases = [today_cases]
    recovered = [today_recovered]
    for day in range(1, num_days):
        d = now - timedelta(days=day)
        times = [d.strftime("%Y%m%d080000"), d.strftime("%Y%m%d150000")]
        for ts in times:
            actual_ts, snapshot_url = wayback(ts)
            if actual_ts[0:8] == ts[0:8]:
                print(
                    "Fetching day",
                    "-{}".format(day),
                    "{}-{}".format(ts[6:8], ts[4:6]),
                    "@",
                    ts[8:12],
                    "Uhr",
                )
                past_cases, past_recovered = fetch_data(snapshot_url)
                if past_cases is not None:
                    cases.append(past_cases)
                if past_recovered is not None:
                    recovered.append(past_recovered)

    cases = clean_data(cases)
    recovered = clean_data(recovered)

    cases_csv = os.path.join("data", "cases.csv")
    recovered_csv = os.path.join("data", "recovered.csv")

    cases.to_csv(cases_csv, index=False)
    recovered.to_csv(recovered_csv, index=False)


def current_data():
    today_cases, today_recovered = fetch_data(url)
    today_cases = pd.DataFrame([today_cases])
    today_recovered = pd.DataFrame([today_recovered])
    return today_cases, today_recovered


def data(data_dir):
    cases = pd.read_csv(os.path.join(data_dir, "cases.csv"))
    recovered = pd.read_csv(os.path.join(data_dir, "recovered.csv"))
    return cases, recovered


def template_svg(value, template, out_file):
    with open(template, "r") as f:
        template = f.read()
        new_svg = template.replace("{{VALUE}}", value)
        with open(out_file, "w") as new:
            new.write(new_svg)


def main():
    today_cases, today_recovered = fetch_data(url)
    large_template = "images/value-template.svg"
    small_template = "images/small-template.svg"

    template_svg(
        datetime.now().strftime("%d.%m.%Y %H:%M"),
        small_template,
        "images/updated-date.svg",
    )
    template_svg(today_cases["total_cases"], large_template, "images/total-cases.svg")
    template_svg(
        today_recovered["total_recovered"], large_template, "images/total-recovered.svg"
    )
    template_svg(today_cases["total_tests"], large_template, "images/total-tests.svg")
    template_svg(today_cases["total_deaths"], large_template, "images/total-deaths.svg")
    total_active = int(today_cases["total_cases"]) - int(today_cases["total_deaths"]) - int(today_recovered["total_recovered"])
    template_svg(str(total_active), large_template, "images/total-active.svg")

    cases_csv = os.path.join("data", "cases.csv")
    recovered_csv = os.path.join("data", "recovered.csv")
    cases = pd.read_csv(cases_csv)
    recovered = pd.read_csv(recovered_csv)

    today_cases = pd.DataFrame([today_cases])
    today_recovered = pd.DataFrame([today_recovered])
    cases = clean_data(pd.concat([cases, today_cases]))
    recovered = clean_data(pd.concat([recovered, today_recovered]))

    cases.to_csv(cases_csv, index=False)
    recovered.to_csv(recovered_csv, index=False)


if __name__ == "__main__":
    #main()
    cases, r = data("data")
    print(cases)
    # import requests_cache
    # requests_cache.install_cache("cases_cache")
    # historical()
