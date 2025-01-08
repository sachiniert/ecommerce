import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will be executing last")

@pytest.fixture()

def dataLoad():
    print("User profile data is being created")
    return ["Rahul","Sachin","yadav"]

@pytest.fixture(params=[("chrome","Rahul","Shetty"),("Firefox","Shetty"),("IE","SS")])
def crossBrowser(request):
    return request.param