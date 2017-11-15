import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

from unittest import TestCase
from ..build import rf_rfe
from inspect import getfullargspec


class TestRf_rfe(TestCase):
    def test_rf_rfe(self):

        # Input parameters tests
        args = getfullargspec(rf_rfe).args
        args_default = getfullargspec(rf_rfe).defaults
        self.assertEqual(len(args), 1, "Expected arguments %d, Given %d" % (1, len(args)))
        self.assertEqual(args_default, None, "Expected default values do not match given default values")

        # Return data types
        expected = ['LotFrontage', 'LotArea', 'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'BsmtFinSF1', 'BsmtUnfSF',
                    'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'GrLivArea', 'TotRmsAbvGrd', 'GarageYrBlt', 'GarageArea',
                    'WoodDeckSF', 'OpenPorchSF', 'YrSold']
        top_features = rf_rfe(data)
        self.assertIsInstance(top_features, list,
                              "Expected data type for return value is `List`, you are returning %s" % (
                                  type(top_features)))

        # Return values tests
        self.assertEqual(top_features, expected, "Expected list of variables does not match returned list of variables")
