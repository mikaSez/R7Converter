

from behave import *

from RevealGenerator import Params


@given('all params with {globalAnswer} as text')
def step_impl(context, globalAnswer):
    """
    :type context: behave.runner.Context
    """
    context.comms = globalAnswer
    context.ctrl = globalAnswer



@when("I init my param class")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.par = Params(context.comms, context.ctrl)



@then("my class anwer only truth")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.ctrl == "oui"
    assert context.comms == "oui"


@given("Usually coms are not translated in EAST")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.comms = "non"
    context.ctrl = "oui"
    pass

@then("my class should have false in comms")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.par.comms == "false"
