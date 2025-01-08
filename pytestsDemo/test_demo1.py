import pytest


@pytest.mark.smoke
def test_firstProgram():
    print("Hello")


@pytest.mark.xfail
def test_SecondGreetCreditCard():
    print("Good Morning")

def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])
    print(crossBrowser[2])