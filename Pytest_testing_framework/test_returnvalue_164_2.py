import pytest
from Pytest_testing_framework.test_returnvalue_164_3 import SomeClassToTest
from Pytest_testing_framework.test_returnvalue_164_1 import setUp,oneTimeSetUp

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

