import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert  msg == "hi" ," not match "

def test_SecondCreditCard():
    a=4
    b= 5
    assert  a+2 ==6,"Asddition do not match"

@pytest.fixture()
def setup():
    print("I will be executing first")

def test_fixtureDemo(setup):
    print("i will execute steps in fixtureDemo method")


