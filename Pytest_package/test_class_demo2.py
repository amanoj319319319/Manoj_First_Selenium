import pytest
from Pytest_package.class_to_test1 import SomeClassToTest
#plse reffer conftest.py

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestClassDemo():

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.abc = SomeClassToTest(self.value)

    def test_methodA(self):
        result = self.abc.sumNumbers(2, 8)
        assert result == 20
        print("Running method A")

    def test_methodB(self):
        print("Running method B")

#how do you run this file is ,
#py.test -s -v packagename/filename.py --browser firefox