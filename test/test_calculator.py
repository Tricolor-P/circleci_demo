import calculator
import pytest

addition_lists=(
    [0,0,0],
    [0,10,10],
    [10,0,10],
    [5,5,10])

def func_ids(params):
    return 'Param1={},Param2={}, Result={}'.format(params[0],params[1],params[2])

@pytest.fixture(params=addition_lists,ids=func_ids)
def addition_task(request):
    return request.param

def test_addition_normal(addition_task):
    cal = calculator.Calculator()
    result = cal.addition(addition_task[0],addition_task[1])
    assert result == addition_task[2]
