# Howdy!
## Bullet sales data challenge
Prepared by Steve Iannaccone - May 2017

Objectives: given historical sales data, project future sales for the next 12 months.

## Table of Contents:

* [Background](README.md#background)
* [Remington Forecasts:](README.md#remington-forecasts)
    * [52fxl](README.md#52fxl)
    * [53fxl](README.md#53fxl)
    * [54fxl](README.md#54fxl)
    * [55fxl](README.md#55fxl)
    * [56fxl](README.md#56fxl)
    * [57fxl](README.md#57fxl)
    * [58fxl](README.md#58fxl)
    * [59fxl](README.md#59fxl)
    * [60fxl](README.md#60fxl)
    * [61fxl](README.md#61fxl)
* [Henry-Lever:](README.md#henry-lever-forecasts)
    * [80fxl](README.md#80fxl)
    * [81fxl](README.md#81fxl)
    * [82fxl](README.md#82fxl)
    * [83fxl](README.md#83fxl)
    * [84fxl](README.md#84fxl)
* [Aggregated Forecasts](README.md#aggregated-forecasts)
* [Drawbacks](README.md#drawbacks)
* [Future Work](README.md#future-work)




## Background

We have been given sales data for several handgun models from two manufactures
_(Remington and Henry-Lever)_ and we need to forecast the sales for those models,
as well as the sales aggregated by manufacturer, for the following year.

## EDA
Look at data (negative values)

Split and clean data

Negative values - reset to zero

look for seasonality

## Forecasting Approach
Exponential smoothing - trend seasonality

ARIMA - moving average good for data with sudden spikes

Monte Carlo Markov Chain - gets confidence intervals

clean up negative and fractional predicted sales values


## Remington Forecasts

### 52fxl

Forecast model plot:

![52fxl forecast plot](report/Remington_52fxl_forecast.png?raw=true "52fxl forecast plot")

Trend and seasonality plot:

![52fxl seasonality plot](report/Remington_52fxl_seasonality.png?raw=true "52fxl seasonality plot")

Cleaned forecast:

| datetime   | bullets |
|------------|---------|
| 1817-01-01 | 5.0     |
| 1817-02-01 | 6.0     |
| 1817-03-01 | 6.0     |
| 1817-04-01 | 7.0     |
| 1817-05-01 | 6.0     |
| 1817-06-01 | 0.0     |
| 1817-07-01 | 23.0    |
| 1817-08-01 | 5.0     |
| 1817-09-01 | 16.0    |
| 1817-10-01 | 0.0     |
| 1817-11-01 | 7.0     |
| 1817-12-01 | 7.0     |


### 53fxl
Forecast model plot:

![53fxl forecast plot](report/Remington_53fxl_forecast.png?raw=true "53fxl forecast plot")

Trend and seasonality plot:

![53fxl seasonality plot](report/Remington_53fxl_seasonality.png?raw=true "53fxl seasonality plot")

Cleaned forecast:

| datetime   | bullets |
|------------|---------|
| 1817-01-01 | 4.0     |
| 1817-02-01 | 4.0     |
| 1817-03-01 | 6.0     |
| 1817-04-01 | 8.0     |
| 1817-05-01 | 5.0     |
| 1817-06-01 | 0.0     |
| 1817-07-01 | 24.0    |
| 1817-08-01 | 4.0     |
| 1817-09-01 | 8.0     |
| 1817-10-01 | 5.0     |
| 1817-11-01 | 3.0     |
| 1817-12-01 | 6.0     |




### 54fxl
Forecast model plot:

![54fxl forecast plot](report/Remington_54fxl_forecast.png?raw=true "54fxl forecast plot")

Trend and seaonality plot:

![54fxl seasonality plot](report/Remington_54fxl_seasonality.png?raw=true "54fxl seasonality plot")

Cleaned forecast:

| datetime   | bullets |
|------------|---------|
| 1817-01-01 | 8.0     |
| 1817-02-01 | 9.0     |
| 1817-03-01 | 2.0     |
| 1817-04-01 | 6.0     |
| 1817-05-01 | 4.0     |
| 1817-06-01 | 0.0     |
| 1817-07-01 | 25.0    |
| 1817-08-01 | 31.0    |
| 1817-09-01 | 10.0    |
| 1817-10-01 | 0.0     |
| 1817-11-01 | 100.0   |
| 1817-12-01 | 7.0     |


### 55fxl
Forecast model plot:
![55fxl forecast plot](report/Remington_55fxl_forecast.png?raw=true "55fxl forecast plot")

Trend and seasonality plot:

![55fxl seasonality plot](report/Remington_55fxl_seasonality.png?raw=true "55fxl seasonality plot")

Cleaned forecast:

| datetime   | bullets |
|------------|---------|
| 1817-01-01 | 0.0     |
| 1817-02-01 | 0.0     |
| 1817-03-01 | 0.0     |
| 1817-04-01 | 0.0     |
| 1817-05-01 | 1.0     |
| 1817-06-01 | 1.0     |
| 1817-07-01 | -0.0    |
| 1817-08-01 | 4.0     |
| 1817-09-01 | 6.0     |
| 1817-10-01 | 0.0     |
| 1817-11-01 | 31.0    |
| 1817-12-01 | -0.0    |


### 56fxl
Forecast model plot:
![56fxl forecast plot](report/Remington_56fxl_forecast.png?raw=true "56fxl forecast plot")
Trend and seasonality plot:
![56fxl seasonality plot](report/Remington_56fxl_seasonality.png?raw=true "56fxl seasonality plot")
Cleaned forecast:

| datetime   | bullets |
|------------|---------|
| 1817-01-01 | 0.0     |
| 1817-02-01 | 10.0    |
| 1817-03-01 | 0.0     |
| 1817-04-01 | 30.0    |
| 1817-05-01 | 5.0     |
| 1817-06-01 | 12.0    |
| 1817-07-01 | 0.0     |
| 1817-08-01 | 0.0     |
| 1817-09-01 | 0.0     |
| 1817-10-01 | 133.0   |
| 1817-11-01 | 0.0     |
| 1817-12-01 | 0.0     |

### 57fxl
Forecast model plot:
![57fxl forecast plot](report/Remington_57fxl_forecast.png?raw=true "57fxl forecast plot")
Trend and seasonality plot:
![57fxl seasonality plot](report/Remington_57fxl_seasonality.png?raw=true "57fxl seasonality plot")
Cleaned forecast:

| datetime   | bullets |
|------------|---------|
| 1817-01-01 | 0.0     |
| 1817-02-01 | 59.0    |
| 1817-03-01 | 32.0    |
| 1817-04-01 | 34.0    |
| 1817-05-01 | 4.0     |
| 1817-06-01 | 3.0     |
| 1817-07-01 | 1.0     |
| 1817-08-01 | 18.0    |
| 1817-09-01 | 14.0    |
| 1817-10-01 | 49.0    |
| 1817-11-01 | 25.0    |
| 1817-12-01 | 76.0    |

### 58fxl
Forecast model plot:
![58fxl forecast plot](report/Remington_58fxl_forecast.png?raw=true "58fxl forecast plot")
Trend and seasonality plot:
![58fxl seasonality plot](report/Remington_58fxl_seasonality.png?raw=true "58fxl seasonality plot")
Cleaned forecast:

| datetime   | bullets |
|------------|---------|
| 1817-01-01 | 8.0     |
| 1817-02-01 | 8.0     |
| 1817-03-01 | 14.0    |
| 1817-04-01 | 13.0    |
| 1817-05-01 | 12.0    |
| 1817-06-01 | 9.0     |
| 1817-07-01 | 3.0     |
| 1817-08-01 | 14.0    |
| 1817-09-01 | 14.0    |
| 1817-10-01 | 5.0     |
| 1817-11-01 | 48.0    |
| 1817-12-01 | 2.0     |

### 59fxl
Forecast model plot:
![59fxl forecast plot](report/Remington_59fxl_forecast.png?raw=true "59fxl forecast plot")
Trend and seasonality plot:
![59fxl seasonality plot](report/Remington_59fxl_seasonality.png?raw=true "59fxl seasonality plot")
Cleaned forecast:

| datetime   | bullets |
|------------|---------|
| 1817-01-01 | 0.0     |
| 1817-02-01 | 64.0    |
| 1817-03-01 | 45.0    |
| 1817-04-01 | 21.0    |
| 1817-05-01 | 5.0     |
| 1817-06-01 | 0.0     |
| 1817-07-01 | 33.0    |
| 1817-08-01 | 0.0     |
| 1817-09-01 | 17.0    |
| 1817-10-01 | 44.0    |
| 1817-11-01 | 57.0    |
| 1817-12-01 | 55.0    |

### 60fxl
Forecast model plot:
![60fxl forecast plot](report/Remington_60fxl_forecast.png?raw=true "60fxl forecast plot")
Trend and seasonality plot:
![60fxl seasonality plot](report/Remington_60fxl_seasonality.png?raw=true "60fxl seasonality plot")
Cleaned forecast:

| datetime   | bullets |
|------------|---------|
| 1817-01-01 | 0.0     |
| 1817-02-01 | 2.0     |
| 1817-03-01 | 0.0     |
| 1817-04-01 | 18.0    |
| 1817-05-01 | 10.0    |
| 1817-06-01 | 6.0     |
| 1817-07-01 | 17.0    |
| 1817-08-01 | 0.0     |
| 1817-09-01 | 0.0     |
| 1817-10-01 | 0.0     |
| 1817-11-01 | 103.0   |
| 1817-12-01 | 0.0     |

### 61fxl
Forecast model plot:
![61fxl forecast plot](report/Remington_61fxl_forecast.png?raw=true "61fxl forecast plot")
Trend and seasonality plot:
![61fxl seasonality plot](report/Remington_61fxl_seasonality.png?raw=true "61fxl seasonality plot")
Cleaned forecast:

| datetime   | bullets |
|------------|---------|
| 1817-01-01 | 5.0     |
| 1817-02-01 | 5.0     |
| 1817-03-01 | 7.0     |
| 1817-04-01 | 7.0     |
| 1817-05-01 | 6.0     |
| 1817-06-01 | 6.0     |
| 1817-07-01 | 7.0     |
| 1817-08-01 | 7.0     |
| 1817-09-01 | 6.0     |
| 1817-10-01 | 8.0     |
| 1817-11-01 | 16.0    |
| 1817-12-01 | 16.0    |

## Henry-Lever Forecasts

### 80fxl
Forecast model plot:
![80fxl forecast plot](report/Henry_Lever_80fxl_forecast.png?raw=true "80fxl forecast plot")
Trend and seasonality plot:
![80fxl seasonality plot](report/Remington_80fxl_seasonality.png?raw=true "80fxl seasonality plot")
Cleaned forecast:

| datetime   | bullets |
|------------|---------|
| 1817-01-01 | 7.0     |
| 1817-02-01 | 0.0     |
| 1817-03-01 | 0.0     |
| 1817-04-01 | 4.0     |
| 1817-05-01 | 0.0     |
| 1817-06-01 | 16.0    |
| 1817-07-01 | 0.0     |
| 1817-08-01 | 0.0     |
| 1817-09-01 | 0.0     |
| 1817-10-01 | 0.0     |
| 1817-11-01 | 0.0     |
| 1817-12-01 | -0.0    |

### 81fxl
Forecast model plot:
![81fxl forecast plot](report/Henry_Lever_81fxl_forecast.png?raw=true "81fxl forecast plot")
Trend and seasonality plot:
![81fxl seasonality plot](report/Remington_81fxl_seasonality.png?raw=true "81fxl seasonality plot")
Cleaned forecast:

| datetime   | bullets |
|------------|---------|
| 1817-01-01 | 0.0     |
| 1817-02-01 | 1.0     |
| 1817-03-01 | 0.0     |
| 1817-04-01 | 3.0     |
| 1817-05-01 | 0.0     |
| 1817-06-01 | 7.0     |
| 1817-07-01 | 0.0     |
| 1817-08-01 | 0.0     |
| 1817-09-01 | 0.0     |
| 1817-10-01 | 0.0     |
| 1817-11-01 | 1.0     |
| 1817-12-01 | 0.0     |


### 82fxl
Forecast model plot:
![82fxl forecast plot](report/Henry_Lever_82fxl_forecast.png?raw=true "82fxl forecast plot")
Trend and seasonality plot:
![82fxl seasonality plot](report/Remington_82fxl_seasonality.png?raw=true "82fxl seasonality plot")
Cleaned forecast:

| datetime   | bullets |
|------------|---------|
| 1817-01-01 | 1.0     |
| 1817-02-01 | 1.0     |
| 1817-03-01 | 0.0     |
| 1817-04-01 | 2.0     |
| 1817-05-01 | 0.0     |
| 1817-06-01 | 8.0     |
| 1817-07-01 | 0.0     |
| 1817-08-01 | 0.0     |
| 1817-09-01 | 0.0     |
| 1817-10-01 | -0.0    |
| 1817-11-01 | 0.0     |
| 1817-12-01 | 0.0     |


### 83fxl
Forecast model plot:
![83fxl forecast plot](report/Henry_Lever_83fxl_forecast.png?raw=true "83fxl forecast plot")
Trend and seasonality plot:
![83fxl seasonality plot](report/Remington_83fxl_seasonality.png?raw=true "83fxl seasonality plot")
Cleaned forecast:

| datetime   | bullets |
|------------|---------|
| 1817-01-01 | 5.0     |
| 1817-02-01 | 7.0     |
| 1817-03-01 | 3.0     |
| 1817-04-01 | 0.0     |
| 1817-05-01 | 4.0     |
| 1817-06-01 | 6.0     |
| 1817-07-01 | 8.0     |
| 1817-08-01 | 8.0     |
| 1817-09-01 | 12.0    |
| 1817-10-01 | 0.0     |
| 1817-11-01 | 12.0    |
| 1817-12-01 | 11.0    |


### 84fxl
Forecast model plot:
![84fxl forecast plot](report/Henry_Lever_84fxl_forecast.png?raw=true "84fxl forecast plot")
Trend and seasonality plot:
![84fxl seasonality plot](report/Remington_84fxl_seasonality.png?raw=true "84fxl seasonality plot")
Cleaned forecast:

| datetime   | bullets |
|------------|---------|
| 1817-01-01 | 2.0     |
| 1817-02-01 | 7.0     |
| 1817-03-01 | 1.0     |
| 1817-04-01 | 3.0     |
| 1817-05-01 | 3.0     |
| 1817-06-01 | 6.0     |
| 1817-07-01 | 3.0     |
| 1817-08-01 | 2.0     |
| 1817-09-01 | 3.0     |
| 1817-10-01 | 4.0     |
| 1817-11-01 | 2.0     |
| 1817-12-01 | 4.0     |



## Aggregated Results

**Aggregated Henry-Lever Sales Forecast**

| datetime   | bullets |
|------------|---------|
| 1817-01-01 | 15.0    |
| 1817-02-01 | 16.0    |
| 1817-03-01 | 4.0     |
| 1817-04-01 | 12.0    |
| 1817-05-01 | 7.0     |
| 1817-06-01 | 43.0    |
| 1817-07-01 | 11.0    |
| 1817-08-01 | 10.0    |
| 1817-09-01 | 15.0    |
| 1817-10-01 | 4.0     |
| 1817-11-01 | 15.0    |
| 1817-12-01 | 15.0    |

**Aggregated Remington Sales Forecast**

| datetime   | bullets |
|------------|---------|
| 1817-01-01 | 30.0    |
| 1817-02-01 | 167.0   |
| 1817-03-01 | 112.0   |
| 1817-04-01 | 144.0   |
| 1817-05-01 | 58.0    |
| 1817-06-01 | 37.0    |
| 1817-07-01 | 133.0   |
| 1817-08-01 | 83.0    |
| 1817-09-01 | 91.0    |
| 1817-10-01 | 244.0   |
| 1817-11-01 | 390.0   |
| 1817-12-01 | 169.0   |

## Drawbacks
Underestimates sudden jumps in sales

## Future Work
Other models

RNN - will probably need more granular data for this to work well
