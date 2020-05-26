import pytest
from Pytest_package.class_to_test import SomeClassToTest
#reffer conftest.py and class_to_test.py
@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestReportingDemo():

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.abc = SomeClassToTest(10)

    def test_methodA(self):
        result = self.abc.sumNumbers(2, 8)
        assert result == 20
        print("Running method A")

    def test_methodB(self):
        result = self.abc.sumNumbers(2, 8)
        assert result > 20
        print("Running method B")

#how do we find out the directory path in pycharm ?
#when we run this file like py.test -s -v packagename/filename.py --html=htmlreport.html,
#if we run like that , it can generate one htmlreport.html file ,to open this file ,
#just go to Navigate bar , open pycharm projects .
#when