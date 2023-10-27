from time import time
from utils.lib import common
from selenium.common.exceptions import NoSuchElementException

def find_element_method(context, find_by, label, inside_element=False):
    unit = context if inside_element else context.driver
    if find_by == 'id':
        element = unit.find_element_by_id("{0}".format(label))
    elif find_by == 'id-multi':
        element = unit.find_elements_by_id("{0}".format(label))
    elif find_by == 'name':
        element = unit.find_element_by_name("{0}".format(label))
    elif find_by == 'xpath':
        element = unit.find_element_by_xpath("{0}".format(label))
    elif find_by == 'xpath-multi':
        element = unit.find_elements_by_xpath("{0}".format(label))
        if len(element) == 0:
            raise NoSuchElementException
    elif find_by == 'css':
        element = unit.find_element_by_css_selector("{0}".format(label))
    elif find_by == 'css-multi':
        element = unit.find_elements_by_css_selector("{0}".format(label))
    elif find_by == 'class':
        element = unit.find_element_by_class_name("{0}".format(label))
    elif find_by == 'class-multi':
        element = unit.find_elements_by_class_name("{0}".format(label))
    elif find_by == 'link-text':
        element = unit.find_element_by_link_text("{0}".format(label))
    elif find_by == 'link-text-partial':
        element = unit.find_element_by_partial_link_text("{0}".format(label))
    elif find_by == 'tag':
        element = unit.find_element_by_tag_name("{0}".format(label))
    elif find_by == 'data-test-id':
        element = unit.find_element_by_xpath('//*[@data-test-id="{0}"]'.format(label))
    elif find_by == 'data-test-id-multi':
        element = unit.find_elements_by_xpath('//*[@data-test-id="{0}"]'.format(label))
    return element

def element_exists_with_locator(context, locator, timeout=10):
    find_by = locator[0]
    label = locator[1]
    return element_exists(context, find_by, label, timeout)

def element_exists(context, find_by, label, timeout=1):
    context.driver.implicitly_wait(1)
    start_time = time.time()
    result = False
    while time.time() - start_time < timeout:
        try:
            result = find_element_method(context, find_by, label)
            break
        except NoSuchElementException:
            result = False
    return result
