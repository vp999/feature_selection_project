import pandas as pd
from unittest import TestCase
from ..build import plot_corr
from inspect import getfullargspec

data = pd.read_csv('data/house_prices_multivariate.csv')


class TestPlot_corr(TestCase):
    def test_plot_corr(self):
        # Input parameters tests
        args = getfullargspec(plot_corr).args
        args_default = getfullargspec(plot_corr).defaults
        self.assertEqual(len(args), 2, "Expected arguments %d, Given %d" % (2, len(args)))
        self.assertEqual(args_default,(11,), "Expected default values do not match given default values")

        # Return type tests
        # Nothing to check here

        # Return value tests
        # Nothing to check here
