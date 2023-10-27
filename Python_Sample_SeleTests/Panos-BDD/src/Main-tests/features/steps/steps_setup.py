from behave import *
from utils.lib import logger
from utils.lib import yaml_dictionary
from utils.lib import read_yaml_file as ryaml
from utils.lib.py import Homepage
from utils.lib import functions as fun

@step('Connect to Main Webpage')
def step_impl(context):
    if context.config.userdata['source'] == 'test':
        ...
    # local
    else:
        ...

@step('Navigate to Login using URL')
def step_impl(context):
    loginpath = "path/login"
    path.add_path_to_base_url(context, loginpath, 10)
    context.login_instance = Login(context)
    logger.info("Navigate to Login using URL: SUCCESS")


@step('Login as user using staging environment ({user_input},{credentials})')
def step_impl(context, user_input, credentials):
    context.execute_steps(f'''Then Login user ({user_input},{credentials})''')
    try:
        yaml = ryaml("accounts_yaml.yaml")
        context.username = yaml['USERS'][credentials.replace("@", "")]['username']
        context.password = yaml['USERS'][credentials.replace("@", "")]['password']

    except KeyError:
        logger.info(f"Data not found in yaml for account {user_input}, or account does not exist in yaml")

    logger.info('Login as user using staging environment: SUCCESS')


@step('Validate Homepage and Dashboard')
def step_impl(context):
    context.homepage_instance = Homepage(context)
    context.homepage_instance.validate_test_section()
    context.homepage_instance.validate_latest_locators()
    context.homepage_instance.validate_homagepage_element123()
    logger.info(f"Validate Homepage and Dashboard: SUCCESS")


@step('Logout user')
def step_impl(context):
    context.logout_instance = Logout(context)
    context.logout_instance.logout_method()
    logger.info('Logout user: SUCCESS')


@step('Verify Translations')
def step_impl(context):
    expected_dummy_text = yaml_dictionary('translations.yaml', 'TRANSLATIONS_1')
    translations_dummy = context.vbu_user_list_management_instance.get_breadcrumb_text()
    actual_dummy_text = translations_dummy.replace("\n", " ")
    fun.compare_wordings(context, actual_dummy_text, expected_dummy_text, include_flag=True)
    logger.info("Verify Translations: OK")

