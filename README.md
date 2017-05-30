# Howdy!
## Bullet sales data challenge
Prepared by **Steve Iannaccone** - May 2017

Objectives: given historical sales data, project future sales for the next
12 months.

## Table of Contents:

* [Background](README.md#background)
* [Exploratory Data Analysis](README.md#eda)
* [Forecasting Approach](README.md#forecasting-approach)
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

We have been given sales data for bullets for several handgun models from two
manufactures _(Remington and Henry-Lever)_ and we need to forecast the sales
for those models, as well as the sales aggregated by manufacturer, for the
following year. Sales data for bullets ranges from 1810 - 1816, we need to make
monthly sales forecasts for 1817.

## EDA
After reading in the sales data, we can look at the distributions of values by
calling `df.describe()` on the dataframes. We can see that the bullets sales
data has a minimum value that is negative. So we will need to do some clean-up
before we start modeling. We effectively have two straight forward approaches
here. Firstly, we can just flip the sign of the negative values _(this assumes
that it was simply a clerical error)_. Secondly, we can reset all negative
sales values to zero, this is the safer approach of assuming that bad data
should be removed.

Next, splitting the data by manufacturer and then by handgun model allows us to
look at each model one-by-one. We can also parse the datetime column as a
datetime object when we read in the csv files. This aids in making time series
plots. By looking at the individual sales plots we can see that there are sudden
peaks followed by valleys of no sales. We can also note that these peaks appear
to be regularly spaced.




## Forecasting Approach
These recurrent sales spikes we saw in EDA tip us off on what approach we
should use to begin modeling. Forecasting based on smoothing _(exponential
smoothing, ARIMA, or other moving averages)_ do well with this type of data.
Using additive models also helps us with potential issues with variance in the
sales figures. Recurrent Neural Nets, _(RNNs)_, are excellent at forecasting
data with an underlying pattern. Unfortunately, we only have monthly sales
figures for several years to use for each handgun model. RNNs typically
require more data to effectively train.

This leaves us with additive modeling that will handle seasonality and trend
decomposition. Facebook has recently open-sourced a forecasting tool called
Prophet that does exactly this. It also adds the benefit of being able to pass
forecasting through Monte Carlo Markov Chain _(MCMC)_ algorithms to do Bayesian
inference. This gives us confidence intervals on the predicted values as well
_(in this case, 80% CI)_.

The MCMC portion of forecasting is passed through the python STAN package that
leverages Hamiltonian Monte Carlo modeling _(with Metropolis sampling)_ which
helps to keep our error bounded so using No U-Turn Sampling optimizes quicker.

It also uses Fourier transformation to get seasonality and trend decomposition.
In essence, this removes the seasonality components from the data to look for
underlying trends in changes in sales. The Trend and Yearly plots that follow
illustrate these features. The trend plot shows sales increases over the data
once the recurrent seasonality has been removed. The Yearly plot shows where
the data are suggestion strong seasonal shifts _(up or down)_ in sales based on
our monthly data.

Unfortunately, we cannot set a floor to predictions, so our output of sales
forecasts is occasionally negative. We can clean this up so we can set the
minimum returned value to be zero. This is the data shown in the table.

Lastly, we can replot our original data and add our cleaned forecast data for
1817.

We also need to compile aggregated sales estimates for both manufacturers. For
this I simply took the individual handgun model forecasts for both Remington
and Henry-Lever and added them to get an aggregate forecast.

The next section has these plots and forecast tables for each handgun model
as well as the aggregated forecasts. You can use the Table of Contents to jump
directly to a handgun model or you can access all the data files directly in the
`report` directory of this repo as well.

Code for all of this can be found in the `steve-iannaccone_data-challenge.py`
script file as well.


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

Final forecast plot:

![52fxl forecast plot](report/Remington_52fxl_final_forecast.png?raw=true "52fxl final forecast plot")

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

Final forecast plot:

![53fxl forecast plot](report/Remington_53fxl_final_forecast.png?raw=true "53fxl final forecast plot")

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

Final forecast plot:

![54fxl forecast plot](report/Remington_54fxl_final_forecast.png?raw=true "54fxl final forecast plot")


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

Final forecast plot:

![55fxl forecast plot](report/Remington_55fxl_final_forecast.png?raw=true "55fxl final forecast plot")

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

Final forecast plot:

![56fxl forecast plot](report/Remington_56fxl_final_forecast.png?raw=true "56fxl final forecast plot")

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

Final forecast plot:

![57fxl forecast plot](report/Remington_57fxl_final_forecast.png?raw=true "57fxl final forecast plot")

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

Final forecast plot:

![58fxl forecast plot](report/Remington_58fxl_final_forecast.png?raw=true "58fxl finalforecast plot")

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

Final forecast plot:

![59fxl forecast plot](report/Remington_59fxl_final_forecast.png?raw=true "59fxl final forecast plot")

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

Final forecast plot:

![60fxl forecast plot](report/Remington_60fxl_final_forecast.png?raw=true "60fxl final forecast plot")

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

Final forecast plot:

![61fxl forecast plot](report/Remington_61fxl_final_forecast.png?raw=true "61fxl final forecast plot")


## Henry-Lever Forecasts

### 80fxl
Forecast model plot:

![80fxl forecast plot](report/Henry_Lever_80fxl_forecast.png?raw=true "80fxl forecast plot")

Trend and seasonality plot:

![80fxl seasonality plot](report/Henry_Lever_80fxl_seasonality.png?raw=true "80fxl seasonality plot")

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

Final forecast plot:

![80fxl forecast plot](report/Henry_Lever_80fxl_final_forecast.png?raw=true "80fxl final forecast plot")

### 81fxl
Forecast model plot:

![81fxl forecast plot](report/Henry_Lever_81fxl_forecast.png?raw=true "81fxl forecast plot")

Trend and seasonality plot:

![81fxl seasonality plot](report/Henry_Lever_81fxl_seasonality.png?raw=true "81fxl seasonality plot")

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

Final forecast plot:

![81fxl forecast plot](report/Henry_Lever_81fxl_final_forecast.png?raw=true "81fxl final forecast plot")

### 82fxl
Forecast model plot:

![82fxl forecast plot](report/Henry_Lever_82fxl_forecast.png?raw=true "82fxl forecast plot")

Trend and seasonality plot:

![82fxl seasonality plot](report/Henry_Lever_82fxl_seasonality.png?raw=true "82fxl seasonality plot")

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

Final forecast plot:

![82fxl forecast plot](report/Henry_Lever_82fxl_final_forecast.png?raw=true "82fxl final forecast plot")

### 83fxl
Forecast model plot:

![83fxl forecast plot](report/Henry_Lever_83fxl_forecast.png?raw=true "83fxl forecast plot")

Trend and seasonality plot:

![83fxl seasonality plot](report/Henry_Lever_83fxl_seasonality.png?raw=true "83fxl seasonality plot")

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

Final forecast plot:

![83fxl forecast plot](report/Henry_Lever_83fxl_final_forecast.png?raw=true "83fxl final forecast plot")

### 84fxl
Forecast model plot:

![84fxl forecast plot](report/Henry_Lever_84fxl_forecast.png?raw=true "84fxl forecast plot")

Trend and seasonality plot:

![84fxl seasonality plot](report/Henry_Lever_84fxl_seasonality.png?raw=true "84fxl seasonality plot")

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

Final forecast plot:

![84fxl forecast plot](report/Henry_Lever_84fxl_final_forecast.png?raw=true "84fxl final forecast plot")

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
Like all modeling, there are some drawbacks. Namely, in this approach you can
see that the models frequently underestimate sudden jumps in the sales data
_(e.g. Henry-Lever 81fxl)_. Also, like all additive models, there is a real
risk of overfitting. In our case this is hard to estimate. Because we only have
a little data for each handgun model, the opportunity to run Cross-Validation
to tune parameters, validate, and run the maodel on a test set to check for
robustness is simply not an option. Like nearly all data scientists is history,
I will ask for more data!

## Future Work
Given more time and more data, the next steps would be:

* Check other models
* Aggregate sale data first and then rebuild model _(rather than making model
forecasts first, and then aggregating)_
* Transfoem data ahead of modeling to fix floor problem _(maybe use Box-Cox)_
* With more granular data running a RNN would be interesting
* More data would also mean we could use proper cross-validation approaches
* Use plotly for interactive charts
