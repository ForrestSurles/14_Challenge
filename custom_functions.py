"""Machine Learning Abstraction Functions

Abstract the steps to generate and perform
machine learning based trading algorithms.

"""

import pandas as pd
from sklearn.preprocessing import StandardScaler

def generate_actual_returns(input_df, close_price='close', verbose=False):
    """Calculate actual returns from closing prices.

    Args:
        input_df (DF): The closing prices with a date index.
        close_price (str): The name of closing price column.

    Returns:
        A DataFrame adding daily percent changes between closing prices.
    """
    # Isolate the date index and close columns
    signals_df = input_df.loc[:, [close_price]]

    # Use the pct_change function to generate returns from close prices
    signals_df['actual_returns'] = signals_df[close_price].pct_change()

    # Drop all NaN values from the DataFrame
    signals_df.dropna(inplace=True)

    # Optionally output the DataFrame to stdout
    if verbose: print(f'Output (generate_actual_returns):\n{signals_df}')

    return signals_df

def generate_trading_signals(
    input_df, close_price='close', actual_returns='actual_returns',
    short_window=20, long_window=100, verbose=False):
    """Calculate strategy returns based upon previous calculations.

    This function applies two SMA (Simple Moving Average) calculations,
    with lengths optionally defined by the user, to the closing prices,
    generates trading signals for a long hold strategy, and lastly
    calculates strategy returns.

    Args:
    input_df (DF): The closing prices with a date index, and actual returns.
    close_price (str): Name of the closing price column.
    actual_returns (str): Name of the actual returns column.
    short_window (int): Length of the rolling short window.
    long_window (int): Length of the rolling long window.

    Returns:
        A DataFrame adding strategy returns and in-progress steps.
    """
    # Introduce new column names
    sma_fast_name = 'sma_fast'
    sma_slow_name = 'sma_slow'
    signal_name = 'signal'
    strategy_returns = 'strategy_returns'

    # Generate fast and slow simple moving averages
    input_df[sma_fast_name] = input_df[close_price] \
            .rolling(window=short_window).mean()
    input_df[sma_slow_name] = input_df[close_price] \
            .rolling(window=long_window).mean()

    # Initialize the new signal column
    input_df[signal_name] = 0

    # Calculate (buy/sell) signal when actual returns (GE/LT) zero
    input_df.loc[(input_df[actual_returns] >= 0), signal_name] = 1
    input_df.loc[(input_df[actual_returns] < 0), signal_name] = -1

    # Optionally output the count of signal values to stdout
    if verbose:
        print(f'Output (raw trade signals):\n{input_df[signal_name].value_counts()}')

    # Calculate the strategy returns
    input_df[strategy_returns] = input_df[actual_returns] \
            * input_df[signal_name].shift()

    # Optionally output the plot of strategy returns to examine performance
    if verbose:
        (1 + input_df[strategy_returns]).cumprod().plot(
                title='Strategy Returns')

    return input_df

def generate_train_test_datasets(X, y, split):
    """Split the data into training and testing datasets.

    Args:
        X (DF): The features DataFrame with SMA fast and slow columns.
        y (Series): The target Series with the 'Signal' column values.
        split (float): Percentage of data used for training vs. testing.

    Returns:
        Four DataFrames of the data split into testing and training sets.
    """
    # Calculate date to split data between training and testing
    split_date_index = len(X.index) - int(round(split * len(X.index), 0))

    # Split features data into train/test datasets
    X_train = X.iloc[:split_date_index]
    X_test = X.iloc[split_date_index:]

    # Split target data into train/test datasets
    y_train = y.iloc[:split_date_index]
    y_test = y.iloc[split_date_index:]

    scaler = StandardScaler()

    # Shape the scaler to the X_train data
    X_scaler = scaler.fit(X_train)

    # Scale the features train/test datasets using the shaped scaler
    X_train_scaled = pd.DataFrame(
        X_scaler.transform(X_train),
        index=X.index[:split_date_index]
    )
    X_test_scaled = pd.DataFrame(
        X_scaler.transform(X_test),
        index=X.index[split_date_index:]
    )

    return X_train_scaled, X_test_scaled, y_train, y_test