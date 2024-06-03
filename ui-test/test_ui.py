import page_object.page as page
import page_object.locators as locators

class TestAppUI:
    def test_app_title_matches(self, browser):
        main_page = page.MainPage(browser)

        assert main_page.is_title_matches()

    def test_app_result_is_not_empty(self, browser):
        main_page = page.MainPage(browser)
        main_page.fill_data("1,2;2,3")
        main_page.click_send_button()

        assert len(main_page.get_result()) != 0
    def test_app_from_example_1(self, browser):
        main_page = page.MainPage(browser)
        main_page.fill_data("1,2;2,3;3,4;1,3")
        main_page.click_send_button()

        assert main_page.get_result() == "1"
    def test_app_from_example_2(self, browser):
        main_page = page.MainPage(browser)
        main_page.fill_data("1,2;1,2;1,2")
        main_page.click_send_button()

        assert main_page.get_result() == "2"
    def test_app_from_example_3(self, browser):
        main_page = page.MainPage(browser)
        main_page.fill_data("1,2;2,3")
        main_page.click_send_button()

        assert main_page.get_result() == "0"
    def test_app_data_is_empty(self, browser):
        main_page = page.MainPage(browser)
        main_page.click_send_button()

        assert main_page.get_result() == "empty string"
    def test_app_data_is_not_digits(self, browser):
        main_page = page.MainPage(browser)
        main_page.fill_data("abc")
        main_page.click_send_button()

        assert main_page.get_result() == "only digits , and ; are allowed"
    def test_app_intervals_right_border(self, browser):
        main_page = page.MainPage(browser)
        main_page.fill_data("1,2"+";1,2"*105)
        main_page.click_send_button()

        assert main_page.get_result() == "there must be less than 105 intervals"
    def test_app_two_elements_each_interval(self, browser):
        main_page = page.MainPage(browser)
        main_page.fill_data("1;2,3")
        main_page.click_send_button()

        assert main_page.get_result() == "every interval must have exactly two elements"
    def test_app_second_value_bigger(self, browser):
        main_page = page.MainPage(browser)
        main_page.fill_data("2,1;2,3")
        main_page.click_send_button()

        assert main_page.get_result() == "second value in interval must be bigger than first value"
    def test_app_first_value_left_border(self, browser):
        main_page = page.MainPage(browser)
        value = -5 * 104 - 1
        main_page.fill_data(f"{value},1;2,3")
        main_page.click_send_button()

        assert main_page.get_result() == "values must be between -5 * 104 and -5 * 104"
    def test_app_second_value_right_border(self, browser):
        main_page = page.MainPage(browser)
        value = 5 * 104 - 1
        main_page.fill_data(f"1,{value+1};2,3")
        main_page.click_send_button()

        assert main_page.get_result() == "values must be between -5 * 104 and -5 * 104"