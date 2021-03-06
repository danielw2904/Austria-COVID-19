# 🇦🇹 Österreich Austria - COVID-19 Cases

[![Automatic update](https://github.com/Ramblurr/Austria-COVID-19/workflows/Automatic%20update/badge.svg)](https://github.com/Ramblurr/Austria-COVID-19/actions?query=workflow%3A%22Automatic+update%22)

Data concerning confirmed cases and recoveries of the novel coronavirus that causes COVID-19.

**Sources**:
  * The Bundesministerium für Soziales, Gesundheit, Pflege und Konsumentenschutz's [update page](https://www.sozialministerium.at/Informationen-zum-Coronavirus/Neuartiges-Coronavirus-(2019-nCov).html)
  * Historical data (before 2020-03-11) was filled in from archive.org's [historical snapshots of the above page](https://web.archive.org/web/*/https://www.sozialministerium.at/Informationen-zum-Coronavirus/Neuartiges-Coronavirus-(2019-nCov).html).


## Current Data

**Last updated at:** ![Last updated at](./images/updated-date.svg)

#### Updates

* 2020-03-20: Austria has stopped reporting recovered cases, so "active" below is not a reliable figure
* 2020-03-13: Austria [announces](https://www.derstandard.at/jetzt/livebericht/2000115687827/neue-massnahmen-sollen-ausbreitung-des-coronavirus-eindaemmen?responsive=false) drastic measures in effort to flatten the curve

#### Data in CSV Format:

* [cases.csv](./data/cases.csv)
* [recovered.csv](./data/recovered.csv)

### Total Confirmed Cases

![total cases](./images/total-cases.svg)

### Total Active Cases

- "active" cases are those which have not recovered or not died

![total active](./images/total-active.svg)

### Total Confirmed Recoveries

![total recovered](./images/total-recovered.svg)

### Total Deaths

![total deaths](./images/total-deaths.svg)

### Total Tests

![total tests](./images/total-tests.svg)

### Bestätigte und aktive Fälle Österreichweit

- "active" cases are those which have not recovered or not died

![active cases](./images/country-cases.svg)

### Neue bestätigte Fälle pro Tag Österreichweit

![new cases per day](./images/country-new-per-day.svg)

### Bisher durchgeführte Testungen in Österreich 

![tests](./images/country-tests.svg)

### Confirmed cases by Bundesland

![Austria bundeslands confirmed cases](./images/states-cases.svg)

![Table Austria bundeslands confirmed cases](./images/states-cases-table.png)

### Forecast of increase in infections

- **Assumes no significant change to mitigation measures**
  - Given [the announcement on 2020-03-13 by the Austrian Government](https://www.derstandard.at/jetzt/livebericht/2000115687827/neue-massnahmen-sollen-ausbreitung-des-coronavirus-eindaemmen?responsive=false), this is not a valid assumption.
- Credit to [Hans Fangohr](https://github.com/fangohr/coronavirus-2020) for the methodology

[table1]: start
<pre>
Forecast for cases in Austria:

Last data point used in forecast from 2020-03-28 00:00:00

Infections in 25 days:   7981 (29 Mar 2020)
Infections in 26 days:   8696 (30 Mar 2020)
Infections in 27 days:   9440 (31 Mar 2020)
Infections in 28 days:  10215 (01 Apr 2020)
Infections in 29 days:  11021 (02 Apr 2020)
Infections in 30 days:  11856 (03 Apr 2020)
Infections in 31 days:  12722 (04 Apr 2020)
Infections in 32 days:  13619 (05 Apr 2020)
Infections in 33 days:  14546 (06 Apr 2020)
Infections in 34 days:  15505 (07 Apr 2020)
Infections in 35 days:  16493 (08 Apr 2020)
Infections in 36 days:  17513 (09 Apr 2020)
Infections in 37 days:  18564 (10 Apr 2020)
Infections in 38 days:  19645 (11 Apr 2020)
Infections in 39 days:  20758 (12 Apr 2020)
Infections in 40 days:  21901 (13 Apr 2020)
Infections in 41 days:  23076 (14 Apr 2020)
Infections in 42 days:  24282 (15 Apr 2020)
Infections in 43 days:  25520 (16 Apr 2020)
Infections in 44 days:  26788 (17 Apr 2020)
Infections in 45 days:  28088 (18 Apr 2020)
Infections in 46 days:  29420 (19 Apr 2020)
Infections in 47 days:  30783 (20 Apr 2020)
Infections in 48 days:  32177 (21 Apr 2020)
Infections in 49 days:  33603 (22 Apr 2020)
Infections in 50 days:  35061 (23 Apr 2020)
Infections in 51 days:  36550 (24 Apr 2020)
Infections in 52 days:  38071 (25 Apr 2020)
Infections in 53 days:  39624 (26 Apr 2020)

Fit parameters: p = 2.075 c = 10.6 t0= -0.000 a0= -446.591
</pre>
[table1]: end


#### Fitting the curve
![increase forecast model](images/infections-with-model-fit.svg)

#### Forecasts for cases in Austria

![forecast infections austria](images/infections-with-forecast.svg)

### How long does it take for the number of infections to double?

- ORF reported on 2020-03-12 that doubling was at 2.5 days
- however the the recent [Lancet paper](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(20)30260-9/fulltext) reports 6.4 days after studiying data from China for Dec 31, 2019, to Jan 28, 2020,
- based on ![n(t') =  2n(t)](https://render.githubusercontent.com/render/math?math=n(t')%20%3D%20%202n(t)), we find ![equation](https://render.githubusercontent.com/render/math?math=t'%20%3D%20%5Cleft%28%282%28t-t_0%29%5Ep%2B%5Cfrac%7Ba_0%7D%7Bc%7D%5Cright%29%5E%5Cfrac%7B1%7D%7Bp%7D%20%2B%20t_0)
- the time for infections or deaths to double is thus given by ![t' - t](https://render.githubusercontent.com/render/math?math=t'%20-%20t)
- **Assumes no significant change to mitigation measures**
- Credit to [Hans Fangohr](https://github.com/fangohr/coronavirus-2020) for the methodology

**Notably** these findings reproduce the ORFs reporting that in Austria around 2020-03-12 doubling was happening every 2.5 days.

[table2]: start
<pre>
Forecast for infections doubling in austria:

at day  0 (04 Mar 2020), the time to double n is  nan days
at day  2 (06 Mar 2020), the time to double n is  nan days
at day  4 (08 Mar 2020), the time to double n is  nan days
at day  6 (10 Mar 2020), the time to double n is -0.1 days
at day  8 (12 Mar 2020), the time to double n is  1.5 days
at day 10 (14 Mar 2020), the time to double n is  2.7 days
at day 12 (16 Mar 2020), the time to double n is  3.7 days
at day 14 (18 Mar 2020), the time to double n is  4.7 days
at day 16 (20 Mar 2020), the time to double n is  5.6 days
at day 18 (22 Mar 2020), the time to double n is  6.5 days
at day 20 (24 Mar 2020), the time to double n is  7.4 days
at day 22 (26 Mar 2020), the time to double n is  8.2 days
at day 24 (28 Mar 2020), the time to double n is  9.0 days
at day 26 (30 Mar 2020), the time to double n is  9.9 days
at day 28 (01 Apr 2020), the time to double n is 10.7 days

</pre>
[table2]: end

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
Licensed under BSD 3-Clause License

```
Copyright (c) 2020, Hans Fangohr
Copyright (c) 2020, Casey Link
```

Github workflow Copyright (c) 2020 [Alex](https://github.com/alext234). Licensed under Apache 2.0.

**Inspired by:**

* https://github.com/alext234/coronavirus-stats
* https://github.com/fangohr/coronavirus-2020

