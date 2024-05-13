from source.my_module_mock import f1,f2
from unittest.mock import patch

def test_f2_with_fixed_f1():
    with patch('source.my_module_mock.f1', return_value=5) as mock_f1:
        assert f2() == 50
        mock_f1.assert_called_once()