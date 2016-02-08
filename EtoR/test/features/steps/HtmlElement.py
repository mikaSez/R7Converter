from behave import *

from RevealGenerator import El

use_step_matcher("re")



def before_scenario(context):
    context.el = None

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


@when("i add an attribute")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print("calling i add an attribute")
    context.el.attr("href", "http://www.perdu.com")


@then("this attribute is added to the class")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print(" calling this attribut is added to the class \n")
    assert str(context.el) == '<element href="http://www.perdu.com">content</element>', "content : " + str(context.el)


@given("an element with class attribute")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print("calling an element with class attribute ")
    context.el2 = El("element", "content")
    context.el2.attr("class", "btn")
    print("\n" + str(context.el2))


@when("i add a class attribute")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print("calling i add a class attribute ")
    context.el2.attr("class", "btn-primary")


@then("the element has both attributes")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print(" calling the element has both attributes")
    assert str(context.el2) == '<element class="btn btn-primary">content</element>', "content : " + str(context.el2)