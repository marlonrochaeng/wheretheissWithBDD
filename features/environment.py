from behave import use_fixture
from fixtures import some_config_fixture
from entities.satellites import Satellites

def before_all(context):
    print("---Running before all tests---")

def before_tag(context, tag):
    if tag == "satellites":
        use_fixture(some_config_fixture, context)

def before_feature(context, feature):
    print("---Running before every feature---")

def before_scenario(context, scenario):
    print("---Running before every scenario---")
    context.satellites = Satellites()

def after_all(context):
    print("---Running after all scenarios---")

def after_feature(context, feature):
    print("---Running after every feature---")

def after_scenario(context, scenario):
    print("---Running after every scenario---")