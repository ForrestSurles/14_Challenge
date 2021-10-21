"""
==========================================================================================
VITAL NOTE: to everyone else, and me in 6 months.
==========================================================================================
WHERE YOU RUN 'pytest' FROM WILL MAKE OR BREAK THESE TESTS
SO BE SURE TO HAVE YOUR CURRENT WORKING DIRECTORY BE THE 'tests' SUB-FOLDER
THAT'S LOCATED IN A PRESUMED PARENT FOLDER.
OTHERWISE, YOU'RE GONNA HAVE A BAD TIME.
==========================================================================================
"""
"""Unit tests for custom_functions.py

These units test for errors in the
functions provided by the file.
"""

# Imports
import pandas as pd

from pathlib import Path

from custom_functions import generate_actual_returns
from custom_functions import generate_trading_signals

# Test csv import and calculation of closing price actual returns
def test_generate_actual_returns():

    # Path to input data
    input_csv = Path('./Resources/emerging_markets_ohlcv.csv')

    # Path to known output
    checker_csv = Path('./Resources/generate_actual_returns.csv')

    input_df = pd.read_csv(
        input_csv,
        index_col='date',
        infer_datetime_format=True,
        parse_dates=True
        )

    checker_df = pd.read_csv(
        checker_csv,
        index_col='date',
        infer_datetime_format=True,
        parse_dates=True
        )

    # Generate function output
    output_df = generate_actual_returns(input_df,'close',True)

    # Default answers for tests
    check_list = [False, False]

    # Return True if output dataframes are equal in size
    if len(output_df) == len(checker_df): check_list[0] = True

    # Return True if the first records from each DataFrame are the same
    if output_df.iloc[0, 0] == checker_df.iloc[0, 0]: check_list[1] =  True

    assert all(check_list)

# Test SMA generation, determine trading
# signals, and calculate strategy returns
def test_generate_trading_signals():

    # Hardcoded input variables
    close_price='close'
    actual_returns='actual_returns'
    short_window=20
    long_window=100
    verbose=True

    # Path to input data
    input_csv = Path('./Resources/generate_actual_returns.csv')

    # Path to known output
    checker_csv = Path('./Resources/generate_trading_signals.csv')

    input_df = pd.read_csv(
        input_csv,
        index_col='date',
        infer_datetime_format=True,
        parse_dates=True
        )

    checker_df = pd.read_csv(
        checker_csv,
        index_col='date',
        infer_datetime_format=True,
        parse_dates=True
        )

    # Generate function output
    output_df = generate_trading_signals(
            input_df,
            close_price,
            actual_returns,
            short_window,
            long_window,
            True
            )

    assert input_df.equals(output_df)