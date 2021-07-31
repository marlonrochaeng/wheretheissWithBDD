from behave import given, then
import json
from utils.utils import Utils

@given(u'I retrieve all satellites positions with valid timestamps')
def step_impl(context):
    context.positions = context.satellites.get_positions(25544, [1436029892, 1436029902, 1446019305, 1448019409], 'miles')


@then(u'I should see the status code "{code:d}"')
def step_impl(context, code):
    context.positions['code'] == code


@then(u'the information should be valid and same as expected')
def step_impl(context):
    data_under_test = json.load(open('data/satellite_positions.json'))
    assert data_under_test['request_info'] == context.positions['request_info']


@given(u'I retrieve all satellites positions with invalid id')
def step_impl(context):
    context.positions_wrong_id = context.satellites.get_positions(13512, [1436029892, 1436029902, 1446019305, 1448019409], 'miles')


@then(u'I should a status code "{code:d}" and an error message')
def step_impl(context, code):
    error_msg = {'error': 'satellite not found', 'status': 404}
    assert context.positions_wrong_id['code'] == code
    assert context.positions_wrong_id['request_info'] == error_msg


@given(u'I retrieve all satellites positions with valid id and timestamp')
def step_impl(context):
    timestamp_list = [1436029892, 1436029902, 1446019305, 1448019409]
    context.positions = context.satellites.get_positions(25544, timestamp_list, 'miles')

    
@then(u'I should see the same quantity of information')
def step_impl(context):
    assert len(context.positions['request_info']) == 4


@given(u'I retrieve all satellites positions with valid id and wrong units')
def step_impl(context):
    timestamp_list = [1436029892, 1436029902, 1446019305, 1448019409]
    context.positions = context.satellites.get_positions(25544, timestamp_list, 'teste')


@then(u'I the endpoint should work fine and don\'t display error')
def step_impl(context):
    assert context.positions['code'] == 200