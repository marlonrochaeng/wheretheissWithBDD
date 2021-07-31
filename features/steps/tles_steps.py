from behave import given,then

@given(u'I retrieve information using correct information for tles')
def step_impl(context):
    context.tles = context.satellites.get_tles(25544)


@then(u'I should see status code "{code:d}" and a valid data for tles')
def step_impl(context, code):
    assert context.tles['code'] == code
    for _, value in context.tles['request_info'].items():
        if value is None:
            assert False


@given(u'I retrieve information using text parameter for tles')
def step_impl(context):
    context.tles = context.satellites.get_tles(25544, 'text')


@then(u'I should see the text "ISS (ZARYA)" in the response')
def step_impl(context):
    assert 'ISS (ZARYA)' in context.tles['request_info']


@given(u'I retrieve information using incorrect tles info')
def step_impl(context):
    context.tles = context.satellites.get_tles(101)

@then(u'I should see status code "{code:d}" and the error message for tles')
def step_impl(context, code):
    error_msg = {'error': 'satellite not found', 'status': 404}

    assert context.tles['code'] == code
    assert context.tles['request_info'] == error_msg