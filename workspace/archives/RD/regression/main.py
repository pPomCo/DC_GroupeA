import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import TimeSeriesSplit
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_predict
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor



def main():
    df = pd.read_csv(
        'All-All-2017-09-01_2018-09-01.csv', sep=';',
        header=None,
        nrows=100000
    )

    columnNames = [
        "type",
        "sensor",
        "value",
        "timestamp",
        "unit",
        "location"
    ]
    df.columns = columnNames
    df.timestamp = pd.to_datetime(df.timestamp, format='%Y-%m-%dT%H:%M:%S.%f')

    # print(df.head())
    #
    # print(df.sensor.unique())
    # print(df.unit.unique())
    # print(df.location.unique())

    ilot1Temp = (df.loc[(df['sensor'] == 'u4/302/temperature/ilot1') & (df['type'] == 'temperature')])[['timestamp', 'value']]
    ilot1Temp.timestamp = ilot1Temp.timestamp.map(lambda t: (t - df.timestamp.min()).total_seconds())

    window_size = 50
    # ilot1Temp = ilot1Temp.rolling(window_size)
    # print(ilot1Temp.rolling(window_size).values)
    # print(ilot1Temp[['timestamp', 'value']].iloc[-20:, :])

    data = ilot1Temp.values

    scaler = StandardScaler()
    data = scaler.fit_transform(data)
    # print(a[0,:])

    windows = np.array([data[i-window_size:i].flatten() for i in range(window_size, len(data))])
    X = windows[:,:-1]
    y = windows[:,-1]
    print(X, y)

    # https://stackoverflow.com/a/42258242
    # for i in range(window_size, len(data)):
    #     data[i-window_size:i,:]

    # X = ilot1Temp.timestamp.values[:, np.newaxis]
    # y = ilot1Temp.value.values
    splits=4
    tscv = TimeSeriesSplit(n_splits=splits)
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
    # X_train = X[:round(len(X)*80/100), :]
    # X_test = X[round(len(X)*80/100):, :]
    # y_train = y[:round(len(y)*80/100)]
    # y_test = y[round(len(y)*80/100):]


    # cv_predictions = cross_val_predict(regression, X, y, cv=tscv)
    # print(cv_predictions)


    predictionsRegression = []
    predictionsMLP = []
    i = 0
    fig, axes = plt.subplots(nrows=2, ncols=splits)
    for train_index, test_index in tscv.split(X):
    # #     # print("Train : ", train_index, "Test : ", test_index)
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]

        regression = LinearRegression().fit(X_train, y_train)
        mlp = MLPRegressor(hidden_layer_sizes=(50, 35, 20, 5), alpha=0.0001, shuffle=False, max_iter=500).fit(X_train, y_train)

        X_predict, y_predict = X_train, y_train

        train_predictions_regression = regression.predict(X_train)
        test_predictions_regression = regression.predict(X_test)
        train_predictions_mlp = mlp.predict(X_train)
        test_predictions_mlp = mlp.predict(X_test)

        axes[0][i].plot(data[:,:-1], data[:,-1], 'b-')
        # axes[0][i].plot(X[:,-1], regression.predict(X), 'r-')
        axes[0][i].plot(X_train[:,-1], train_predictions_regression, 'g-')
        axes[0][i].plot(X[len(X_train):,-1], regression.predict(X[len(X_train):,:]), 'r-')

        axes[1][i].plot(data[:,:-1], data[:,-1], 'b-')
        # axes[1][i].plot(X[:,-1], mlp.predict(X), 'r-')
        axes[1][i].plot(X_train[:,-1], train_predictions_mlp, 'g-')
        axes[1][i].plot(X[len(X_train):,-1], mlp.predict(X[len(X_train):,:]), 'r-')
        # axes[1][i].plot(X_train[:,-1], train_predictions_mlp, 'g-')
        # axes[1][i].plot(X_test[:,-1], test_predictions_mlp, 'r-')

        i += 1

    cols = ['Split {}'.format(n) for n in range(1, splits+1)]
    rows = ['{}'.format(model) for model in ['LinearRegression', 'MLP']]

    # fig, axes = plt.sub

    for ax, col in zip(axes[0], cols):
        ax.set_title(col)

    for ax, row in zip(axes[:,0], rows):
        ax.set_ylabel(row, rotation=0, size='large')

    fig.tight_layout()
    # for i, col in enumerate(ax[0]):
    # for i, col in enumerate(ax[1]):
    #     col.plot(X_test, y_test, 'b-')
    #     col.plot(X_test, predictionsMLP[i], 'b-')
    plt.show()


    # print(ilot1Temp.value.mean())
    # print(ilot1Temp.timestamp)

    # ilot1Temp.plot.line()
    # plt.show()


    # sensorSplit = df.sensor.apply(lambda x: x.split(sep='/'))
    # df.sensor = sensorSplit

    # import datetime
    # interval = df.timestamp.iloc[-1] - df.timestamp.iloc[0]
    # print(interval.total_seconds())

    # ilot1Temp.set_index(['timestamp'], inplace=True)
    # ilot1Temp.plot()
    # plt.plot(ilot1Temp.index, ilot1Temp.value)
    # plt.show()


if __name__ == '__main__':
    main()
