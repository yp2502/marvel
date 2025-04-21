

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

file_path = "/content/time_series_covid19.csv"
df = pd.read_csv(file_path)

date_columns = df.columns[11:]

time_series = df[date_columns].sum(axis=0)

time_series.index = pd.to_datetime(time_series.index)

def plot_series(series, title="Time Series"):
    plt.figure(figsize=(12, 5))
    plt.plot(series, label="Total Cases")
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Total Cases")
    plt.legend()
    plt.show()

plot_series(time_series, title="COVID-19 Cases Over Time")

def adf_test(series):
    result = adfuller(series)
    print(f'ADF Statistic: {result[0]}')
    print(f'p-value: {result[1]}')
    if result[1] < 0.05:
        print("Series is stationary")
    else:
        print("Series is NOT stationary")

adf_test(time_series)

diff_series = time_series.diff().dropna()
plot_series(diff_series, title="Differenced Time Series")

adf_test(diff_series)

def plot_acf_pacf(series):
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))
    plot_acf(series, ax=ax[0])   # Identifies MA (q) component
    plot_pacf(series, ax=ax[1])  # Identifies AR (p) component
    plt.show()

plot_acf_pacf(diff_series)

model = ARIMA(time_series, order=(2, 1, 2))
model_fit = model.fit()

print(model_fit.summary())

forecast = model_fit.forecast(steps=30)

def plot_forecast(time_series, forecast):
    plt.figure(figsize=(12, 5))
    plt.plot(time_series, label="Actual Cases")
    plt.plot(pd.date_range(start=time_series.index[-1], periods=30, freq="D"), forecast, label="Forecast", color="red")
    plt.title("COVID-19 Cases Forecast")
    plt.xlabel("Date")
    plt.ylabel("Total Cases")
    plt.legend()
    plt.show()

plot_forecast(time_series, forecast)