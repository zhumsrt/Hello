import pytest
import allure
class Test_ABC:

    def setup_class(self):
        print(">>>>>>>setup_class")
    def teardown_class(self):
        print(">>>>>>>teardown_class")
    @pytest.mark.run(order=-1)
    @allure.issue('https://www.baidu.com/')
    @allure.testcase('https://www.baidu.com/')
    def test_a(self):
        print(">>>>>>test_a")
        assert False
    def test_b(self):
        print(">>>>>>>test_b")
        assert True