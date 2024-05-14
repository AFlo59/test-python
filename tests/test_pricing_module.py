import pytest
from source.pricing_module import *
from unittest.mock import patch

def test_calculate_tax():
    with patch('source.pricing_module.fetch_product_price', return_value=100.0) as mock_fetch:
        assert calculate_tax(2) == 20.0  # 20% de 100.0
        mock_fetch.assert_called_once_with(2)

def test_calculate_tax_high_value():
    with patch('source.pricing_module.fetch_product_price', return_value=10000.0) as mock_fetch:
        assert calculate_tax(1) == 2000.0
        mock_fetch.assert_called_once_with(1)

def test_calculate_tax_zero():
    with patch('source.pricing_module.fetch_product_price', return_value=0.0) as mock_fetch:
        assert calculate_tax(1) == 0.0
        mock_fetch.assert_called_once_with(1)

def test_calculate_tax_api_failure():
    with patch('source.pricing_module.fetch_product_price', side_effect=requests.exceptions.RequestException) as mock_fetch:
        with pytest.raises(requests.exceptions.RequestException):
            calculate_tax(1)
        mock_fetch.assert_called_once_with(1)



