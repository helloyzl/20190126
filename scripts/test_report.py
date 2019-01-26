import pytest,allure
class Test_01:
    @allure.step(title='这是第一个测试方法')
    def test_01(self):
        print('--test_01--')
        assert True

    @allure.step(title='这是第二个测试方法')
    def test_02(self):
        print('--test_02---')
        assert False

