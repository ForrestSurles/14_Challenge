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
from pathlib import Path
from challenge.custom_functions import generate_actual_returns

# test function - generate_actual_returns
def test_generate_actual_returns():
    input_csv = Path('../Resources/emerging_markets_ohlcv.csv')
