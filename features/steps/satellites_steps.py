from behave import given, then


@given(u'I retrieve all satellites list information')
def step_impl(context):
    context.satellite_list = context.satellites.get_satellites()
    assert context.satellite_list['code'] == 200


@then(u'I should see only one satellite')
def step_impl(context):
    assert len(context.satellite_list['request_info']) == 1


@then(u'its name and id are "{name}" and "{id:d}"')
def step_impl(context, name, id):
    context.satellite_list['request_info'][0]['name'] == name
    context.satellite_list['request_info'][0]['id'] == id

@given(u'I retrieve the satellite info by id "{id:d}"')
def step_impl(context, id):
    context.satellite_by_id = context.satellites.get_by_id(id)
    

@then(u'I should verify that its name is "{name}"')
def step_impl(context, name):
    assert context.satellite_by_id['code'] == 200
    assert context.satellite_by_id['request_info']['name'] == name


@then(u'all other information is valid')
def step_impl(context):
    for _, value in context.satellite_by_id['request_info'].items():
        if value is None:
            assert False

@then(u'I should see status code "{code:d}" and an error message')
def step_impl(context, code):
    error_msg = {'error': 'satellite not found', 'status': 404}
    assert context.satellite_by_id['code'] == code
    assert context.satellite_by_id['request_info'] == error_msg
