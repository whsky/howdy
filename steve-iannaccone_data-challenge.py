###########################################################################
###########################################################################
#
# Data Challenge for Pirelli, prepared by
#   Steve Iannaccone -  May, 2017
#
# Objectives: Forecasting bullet sales given
#   historical sales data
#
###########################################################################
###########################################################################

import datetime
from datetime import timedelta
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pylab import rcParams
from fbprophet import Prophet
import os

def read_data_set(filename, parse_date = False, date_col=0):
    """
    INPUT: filepath as string, boolean 'parse_date' to optionally parse
        datetime column specified in 'date_col' to index of DataFrame
    OUTPUT: pandas datframe with data from csv file
    ------------------------------------------------------------------------
    Read in data file as csv to pandas dataframe.
    """
    if parse_date:
        df = pd.read_csv(filename,
                        parse_dates=[date_col],
                        date_parser=dt_parser)
        idx = df.columns.tolist()[date_col]
        df.index = df.pop(idx)
        return df
    else:
        return pd.read_csv(filename)


def dt_parser(x):
    """
    Set up a datetime object parser to interpret datetimes when reading in
        our data from csv files with Pandas. Use as 'date_parser' option
        in read_csv.
    """
    return datetime.datetime.strptime(x, '%Y-%m-%d')

def dt_period(x):
    """
    Convert string of type 'YYYY-MM-DD' to a period object for pandas. Use as
        'date_parser' option in read_csv.
    """
    splt = x.split('-')
    date_int = int(''.join(splt))
    return pd.Period(year=date_int/10000,
                    month=date_int/100 % 100,
                    day=date_int%100,
                    freq='D')

def split_by_brand(df, brand_col = 'brand'):
    """
    INPUT: Pandas DF, column to split on based on category as STR
    OUTPUT: list of pandas DFs (one for each brand category)
    """
    brands = df[brand_col].unique().tolist()
    df_list = []
    for brnd in brands:
        if isinstance(brnd, str):
            df_list.append(df[df[brand_col] == brnd])
    return df_list

def split_by_model(df, model_col = 'handgun_model'):
    """
    INPUT: Pandas DF of bullets sales data, col with handgun model info as STR
    OUTPUT: list of pandas DFs (one for each handgun model)
    """
    models = df[model_col].unique().tolist()
    df_list = []
    for mdl in models:
        df_list.append(df[df[model_col] == mdl])
    return df_list

def make_forecast(ds, data, show_plot=False, save_plot=True,
                    mcmc=False, **kwargs):
    """
    INPUT: str of datetimes, data to predict on, and whether to plot prediction
    OUTPUT: returns Prophet model, and predict object (optionally plot preds,
        either plot to screen and/or savefig to filepath)
    --------------------------------------------------------------------------
    We take in a column of datetime objects as simple strings
        (e.g. '1810-01-01') and a column of data we want to forecast and we
        pass it into Facebook's excellent Prophet module to make predictions
        on future sales. What gets returned is the model and the
        .predict() object.

    The syntax follows suit of sklearn's typical implimentation of .fit(),
        and .predict()

    We use **kwargs to optionally set a filepath to save plots
    """
    y_in = pd.DataFrame()
    y_in['ds'] = ds
    y_in['y'] = data

    if mcmc:
        model = Prophet(mcmc_samples=800)
    else:
        model = Prophet()
    model.fit(y_in)

    future = model.make_future_dataframe(periods=12, freq='M')
    forecast = model.predict(future)

    if save_plot or show_plot:
        plt.close('all')
        model.plot(forecast)
        if save_plot and kwargs is not None:
            plt.savefig('{}_forecast.png'.format(kwargs['filepath']))

        model.plot_components(forecast)
        if save_plot and kwargs is not None:
            plt.savefig('{}_seasonality.png'.format(kwargs['filepath']))
        if show_plot:
            plt.show()
        else:
            plt.show()
            plt.close('all')
    return model, forecast

def clean_forecast(forecast, discretize=True):
    """
    INPUT: raw forcast data, boolean of whether to round to nearest int
    OUTPUT: cleaned forecast data
    --------------------------------------------------------------------------
    Our forecast data may be output with negative values and non-integer
        values. So we can set any negative values to zero, and discretize
        fractional values to the nearest integer (it's hard to sell half
        a bullet).
    """
    yhat = forecast['yhat']

    if discretize:
        yhat = yhat.round(decimals=0)

    yhat[yhat < 0] = 0
    forecast['yhat'] = yhat
    return forecast

def fix_EOM(forecast):
    """
    INPUT: forcast dataframe
    OUTPUT: Dataframe with 'ds' datetime column reset for dates at the
        beginning of the month. We will also set the frequency of the datetime
        object to be monthly.
    --------------------------------------------------------------------------
    Forecasts are return with datestamps set at the end of the month (EOM),
        but we want figures for the beginning of the month. We will use
        timedelta to add a day to each forecasted row in the dataframe.
    """
    new_forecast = forecast[forecast.ds > '1816-12-01']
    new_forecast.ds = new_forecast.ds + timedelta(days=1)
    # pd.DatetimeIndex(new_forecast.ds).to_period('M')
    forecast[forecast.ds > '1816-12-01'] = new_forecast
    return forecast

def generate_report(df, modelname):
    """
    INPUT: DataFrame with sales data, String with modelname info
    OUTPUT: None, we are writing everything to our 'report' folder
    --------------------------------------------------------------------------
    Generate forecast csv and plots for report with one function call
    """
    model, forecast = make_forecast(df.datetime,
                                    df.bullets,
                                    show_plot = False,
                                    save_plot = True,
                                    mcmc = True,
                                    filepath = 'report/{}'.format(modelname))

    forecast = clean_forecast(forecast, discretize = True)
    forecast = fix_EOM(forecast)

    preds = forecast[forecast.ds > '1816-12-01']

    out_df = pd.DataFrame()
    out_df['datetime'] = preds['ds']
    out_df['bullets'] = preds['yhat']

    out_df.to_csv('report/{}_forecast.csv'.format(modelname))

    #Make final forecast plot:
    forecast_plotter(df, out_df, modelname)

def agg_sales(folderpath):
    """
    INPUT: String with folderpath where forecast data has been saved
    OUTPUT: None, saving aggregated sales data to csv
    -------------------------------------------------------------------------
    Read in all csv files in `folderpath` and calculate aggregate sales
        forecast parsed by manufacturer (either Remington or Henry-Lever)
    """
    hl_reports = []
    rem_reports = []
    for f in os.listdir(folderpath):
        if f.endswith('.csv'):
            if f.startswith('Henry'):
                hl_reports.append(f)
            elif f.startswith('Rem'):
                rem_reports.append(f)


    all_rem = pd.concat((pd.read_csv(folderpath + '/' + f, index_col = 1) \
                        for f in rem_reports), axis = 1)

    all_hl = pd.concat((pd.read_csv(folderpath + '/' + f, index_col = 1) \
                        for f in hl_reports), axis = 1)

    rem_agg = pd.DataFrame()
    rem_agg['bullets'] = all_rem.bullets.sum(axis = 1)
    # rem_agg['datetime'] = rem_agg.index
    rem_agg.reset_index(inplace=True)

    hl_agg = pd.DataFrame()
    hl_agg['bullets'] = all_hl.bullets.sum(axis = 1)
    # hl_agg['datetime'] = hl_agg.index
    hl_agg.reset_index(inplace=True)

    rem_agg.to_csv('report/Agg_Remington_forecast.csv')
    hl_agg.to_csv('report/Agg_Henry_Lever_forecast.csv')

def forecast_plotter(df, forecast, modelname):
    """
    INPUT: Pandas dataframe with original sales data, and Pandas dataframe with
        new cleaned forecast sales data
    OUTPUT: saved plot as png
    -------------------------------------------------------------------------
    Make time series plot with original sales data and with cleaned forecast
    data using matplotlib
    """
    #Parse date strings from orignal sales dataframe:
    df.datetime = df.datetime.apply(lambda x: \
                                    datetime.datetime.strptime(x, '%Y-%m-%d'))
    df.index = df.datetime
    forecast.index = forecast.datetime
    plt.plot(df.bullets, alpha=0.6)
    plt.plot(forecast.bullets, alpha=0.6)
    plt.savefig('report/{}_final_forecast.png'.format(modelname))
    plt.show()
    plt.close()


if __name__ == '__main__':


    bullets_df = read_data_set('data/Bullets_sales.csv')
    guns_df = read_data_set('data/Handgun_makers_sales.csv')

    print("-")*40
    print("Head of bullets dataframe:\n")
    print(bullets_df.head())
    print("-")*40
    print("Head of guns dataframe:\n")
    print(guns_df.head())

    #Check DFs for null values:
    print("-")*40
    print("Total number of Null values in bullets df: ")
    print(sum(bullets_df['bullets'].isnull()))
    print("-")*40
    print("Total number of Null values in guns df: ")
    print(sum(guns_df['sales'].isnull()))

    print("-")*40
    print("Description of bullets df:\n")
    print(bullets_df.describe())
    print("-")*40
    print("Description of bullets df:\n")
    print(guns_df.describe())

    #We see some bullet sales are negative...we should fix this. We can assume a
    #   clerical error and fix the sign, or we can assume those datapoints are
    #   bad and reset them to zero. Let's reset to zero:
    bullets_df[bullets_df['bullets'] < 0] = 0

    #Split data by manufacturer:
    bullets_rem = split_by_brand(bullets_df)[0]
    bullets_hl = split_by_brand(bullets_df)[1]

    guns_rem = split_by_brand(guns_df)[0]
    guns_hl = split_by_brand(guns_df)[1]

    #Split out each Remington model into a seperate DF:
    rem_52fxl, rem_53fxl, rem_54fxl, rem_55fxl, rem_56fxl, rem_57fxl,\
        rem_58fxl, rem_59fxl, rem_60fxl, rem_61fxl \
            = split_by_model(bullets_rem)

    #Split out each H-L model into a seperate DF:
    hl_80fxl, hl_81fxl, hl_82fxl, hl_83fxl, hl_84fxl\
        = split_by_model(bullets_hl)


    #Loop through each bullet model DF to generate forecasts and plots
    #   This might take a few minutes...
    gun_models = [rem_52fxl, rem_53fxl, rem_54fxl, rem_55fxl, rem_56fxl,
                    rem_57fxl, rem_58fxl, rem_59fxl, rem_60fxl, rem_61fxl,
                    hl_80fxl, hl_81fxl, hl_82fxl, hl_83fxl, hl_84fxl]

    for gun in gun_models:
        generate_report(gun,
                        '{0}_{1}'.format(gun.brand.tolist()[0],
                                        gun.handgun_model.tolist()[0]))


    agg_sales('report')
