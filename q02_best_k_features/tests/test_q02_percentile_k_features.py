from ..build import percentile_k_features
from unittest import TestCase
from inspect import getfullargspec
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')


class TestPercentile_k_features(TestCase):
    def test_percentile_k_features(self):
        # Input parameters tests
		args = getfullargspec(percentile_k_features).args
        args_default = getfullargspec(percentile_k_features).defaults
        self.assertEqual(len(args), 2, "Expected arguments %d, Given %d" % (2, len(args)))
        self.assertEqual(args_default, (20,), "Expected default values do not match given default values")

        # Return data types
        expected = ['OverallQual', 'GrLivArea', 'GarageCars', 'GarageArea', 'TotalBsmtSF', '1stFlrSF', 'FullBath']


        top_features = percentile_k_features(data)
        self.assertIsInstance(top_features, list,
                              "Expected data type for return value is `List`, you are returning %s" % (
                                  type(top_features)))

        # Return values tests
        self.assertEqual(top_features, expected, "Expected list of variables does not match returned list of variables")
