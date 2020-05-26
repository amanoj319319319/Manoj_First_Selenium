
import pytest
from selenium import webdriver

@pytest.mark.usefixtures("setUp","oneTimeSetUp")
class TestExampleOne():
    @pytest.fixture(autouse=True)
    def test_title(self,oneTimeSetUp):
        pass














        









