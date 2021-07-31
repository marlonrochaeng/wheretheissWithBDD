from behave import given, then
import json

@given(u'I retrieve information using correct coordinates')
def step_impl(context):
    context.coordinates = context.satellites.get_position_info([37.795517,-122.393693])


@then(u'I should see status code "{code:d}" and the correct coordinates data')
def step_impl(context, code):
    data_under_test = json.load(open('data/satellite_coordinate.json'))

    assert context.coordinates['code'] == code
    assert context.coordinates['request_info'] == data_under_test['request_info']


@given(u'I retrieve information using incorrect coordinates')
def step_impl(context):
    context.wrong_coordinates = context.satellites.get_position_info([91.795517,-192.393693])


@then(u'I should see status code "{code:d}" and the error message')
def step_impl(context, code):
    error_msg = {'error': 'application error', 'status': 500}
    assert context.wrong_coordinates['code'] == code
    assert context.wrong_coordinates['request_info'] == error_msg