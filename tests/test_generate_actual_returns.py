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

from challenge.custom_functions import generate_actual_returns

# test csv import and calculation of closing price actual returns
def test_generate_actual_returns():

    input_csv = Path('../Resources/emerging_markets_ohlcv.csv')
    checker_csv = Path('../Resources/test_results_generate_actual_returns.py')

    input_df = pd.read_csv(
        input_csv,
        index_col='date',
        infer_datetime_format=True,
        parse_dates=True
        )

    checker_df = pd.read_csv(
        checker_csv_
        index_col='date',
        infer_datetime_format=True,
        parse_dates=True
        )


    attempt generate_actual_returns(input_df,,True) == checker_df

