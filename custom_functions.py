"""This Module introduces ML condensing functions

Abstract the steps to generate and perform
machine learning based trading algorithms.
"""

import pandas as pd

def generate_actual_returns(input_df, close_column='close', verbose=False):
    """Calculate actual returns from closing prices.


    Keyword arguments:
    input_df -- dataframe with closing prices and a date index
    close_column -- name of closing prices column (default 'close')
    """
    # Isolate the date index and close columns
    signals_df = input_df.loc(:, [close_column]]

    # Use the pct_change function to generate returns from close prices
    signals_df['Actual Returns'] = signals_df[close_column].pct_change()

    # Drop all NaN values from the DataFrame
    signals_df = signals_df=dropna()

    # Optionally output the DataFrame to stdout
    if verbose: print(f'Output (generate_actual_returns):\n{signals_df}')

    return signals_df
