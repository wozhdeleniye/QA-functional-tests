import pytest

from api_helper import post_page, get_page


class TestHttpBaseChecks:
    def test_http_ok_on_root_page(self):
        assert get_page().status_code == 200

    def test_http_text_non_empty(self):
        assert get_page().text

    def test_http_ok_on_result_page(self):
        assert post_page('1,2').status_code == 200

    def test_form_content_type_text_html(self):
        assert get_page().headers['Content-Type'] == 'text/html; charset=utf-8'

    def test_form_content_type_app_json(self):
        assert post_page('1,2').headers['Content-Type'] == 'application/json'


def intervals_right_bound_valid_string_maker():
    string = "1,2"
    for i in range(1, 105):
        string += ";" + str(i + 1) + "," + str(i + 2)
    return string


def intervals_right_bound_invalid_string_maker():
    string = "1,2"
    for i in range(1, 106):
        string += ";" + str(i + 1) + "," + str(i + 2)
    return string


class TestCheckEraseLogic:
    def test_example_1(self):
        assert post_page('1,2;2,3;3,4;1,3').json()['result'] == 1

    def test_example_2(self):
        assert post_page('1,2;1,2;1,2').json()['result'] == 2

    def test_example_3(self):
        assert post_page('1,2;2,3').json()['result'] == 0

    @pytest.mark.parametrize("data", [
        pytest.param("1,2", id='left_bound'),
        pytest.param(intervals_right_bound_valid_string_maker(), id='right_bound'),
    ])
    def test_solution_intervals_length_valid(self, data):
        assert post_page(data).json()['result'] == 0

    @pytest.mark.parametrize("data", [
        pytest.param("", id='left_bound'),
        pytest.param(intervals_right_bound_invalid_string_maker(), id='right_gt_bound')
    ])
    def test_solution_intervals_length_invalid(self, data):
        assert post_page(data).status_code == 400

    def test_bad_request_empty_string(self):
        assert post_page('').status_code == 400

    def test_bad_request_wrong_chars(self):
        assert post_page('asdASD').status_code == 400

    def test_bad_request_not_two_items_in_interval(self):
        assert post_page('1;2,3').status_code == 400

    def test_bad_request_first_item_bigger(self):
        assert post_page('2,1').status_code == 400

    def test_bad_request_empty_form(self):
        assert post_page('', '').status_code == 400

    @pytest.mark.parametrize("data", [
        pytest.param(str(-5*104) + ",1", id='left_bound'),
        pytest.param("1," + str(5*104), id='right_gt_bound')
    ])
    def test_solution_interval_item_value_valid(self, data):
        assert post_page(data).json()['result'] == 0

    @pytest.mark.parametrize("data", [
        pytest.param(str(-5 * 104 - 1) + ",1", id='left_bound'),
        pytest.param("1," + str(5 * 104 + 1), id='right_gt_bound')
    ])
    def test_solution_interval_item_value_invalid(self, data):
        assert post_page(data).status_code == 400