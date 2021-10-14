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

# test csv import and calculation of closing price actual returns
def test_generate_actual_returns():

    input_csv = Path('./Resources/emerging_markets_ohlcv.csv')
    checker_csv = Path('./Resources/test_results.csv')

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

    # provided input
    output_df = generate_actual_returns(input_df,'close',True)

    check_list = [False, False]

    if len(output_df) == len(checker_df): check_list[0] = True

    if output_df.iloc[0, 0] == checker_df.iloc[0, 0]: check_list[1] =  True

    assert check_list
