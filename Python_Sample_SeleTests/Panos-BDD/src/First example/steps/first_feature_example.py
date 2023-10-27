from behave import *

# The first step
@step('The first step')
def step_impl(context):
    print("This is the first step")


# The second step
@step('The second step')
def step_impl(context):
    print("This is the second step")


# The last step
@step('The last step')
def step_impl(context):
    print("This is the step")
