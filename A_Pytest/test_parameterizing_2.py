import test_parameterizing_1
import pytest
@pytest.mark.parametrize("text_input,expected_output",[(5,25),(6,36),(7,49)])
def test_calc_square(text_input,expected_output):
    result=test_parameterizing_1.cal_square_value(text_input)
    assert result == expected_output