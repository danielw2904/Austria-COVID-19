# 🇦🇹 Österreich Austria - COVID-19 Cases

![Automatic update](https://github.com/Ramblurr/Austria-COVID-19/workflows/Automatic%20update/badge.svg)

Data concerning confirmed cases and recoveries of the novel coronavirus that causes COVID-19.

**Sources**:
  * The Bundesministerium für Soziales, Gesundheit, Pflege und Konsumentenschutz's [update page](https://www.sozialministerium.at/Informationen-zum-Coronavirus/Neuartiges-Coronavirus-(2019-nCov).html)
  * Historical data (before 2020-03-11) was filled in from archive.org's [historical snapshots of the above page](https://web.archive.org/web/*/https://www.sozialministerium.at/Informationen-zum-Coronavirus/Neuartiges-Coronavirus-(2019-nCov).html).


## Current Data

Last updated at: ![Last updated at](./images/updated-date.svg)

### Total Confirmed Cases

![total cases](./images/total-cases.svg)

### Total Confirmed Recoveries

![total recovered](./images/total-recovered.svg)

### Total Tests

![total tests](./images/total-tests.svg)

### Total Deaths

![total deaths](./images/total-deaths.svg)

### Confirmed cases by Bundesland

![Austria bundeslands confirmed cases](./images/states-cases.png)

![Table Austria bundeslands confirmed cases](./images/states-cases-table.png)

## Developer

#### Setup your virtualenv

```console
virtualenv -p $(which python3) venv
source venv/bin/activate
```

#### Update the csvs

```console
pip install -r requirements.txt
python -m parsers.austria
```

#### Update the plots

```console
jupyter nbconvert --execute --inplace *.ipynb
```

## License

Code and notebooks Copyright 2020 Casey Link. Licensed under the AGPL v3 or later.

Github workflow Copyright 2020 [Alex](https://github.com/alext234). Licensed under Apache 2.0.

Inspired by https://github.com/alext234/coronavirus-stats
