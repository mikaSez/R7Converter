from behave import *

from RevealGenerator import El

use_step_matcher("re")


@given("a new element is created")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.el = El("element", "content")


@then("its name should wrap the content")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert str(context.el) == "<element>content</element>" , "content : " + str(context.el);


@when("i insert another element")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.el.insert(El("second", "text"))


@then("second element is printed inside the first")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert str(context.el) == "<element>content<second>text</second></element>", "content : " + str(context.el)
