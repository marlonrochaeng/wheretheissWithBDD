from behave import fixture


@fixture
def some_config_fixture(context, **kwargs):
    print("Running this part of the fixture before test with SATELLITE tag")

    yield

    print("Running this part of the fixture after test with SATELLITE tag")