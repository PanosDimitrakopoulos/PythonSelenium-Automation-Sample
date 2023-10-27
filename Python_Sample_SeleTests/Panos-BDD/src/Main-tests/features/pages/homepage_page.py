from lib import functions as fun
from lib import logger


class Homepage():
    # Locators
    _xpath_locator = ('xpath', '//locator')
    _data_test_id_locator = ('data-test-id', "locator")
    _class_locator = ('class', '[locator]')
    _

    _dictionary_or_elements = {
        _element_1: "Element 1",
        _element_2: "Element 2",
        _element_3: "Element 3"
    }

    def __init__(self, context):
        self.context = context
        self.landing_page()

    def validate_test_section(self):
        test_section = fun.element_exists_with_locator(self.context, self._xpath_locator)
        assert test_section is not None, "Test section NOT found"
        logger.info("Validated Test section")

    def validate_latest_locators(self):
        self._validate_latest_bills_section()
        self._class_locator()
        logger.info("Validated Latest Locators")

    def _validate_latest_bills_section(self):
        data_test_section = fun.element_exists_with_locator(self.context, self._data_test_id_locator)
        fun.scroll_element_into_view(self.context, data_test_section, alignToTop=False)
        assert data_test_section is not None, "Data Test Section NOT found"

    def _class_locator(self):
        self.class_locator_button = fun.element_exists_with_locator(self.context, self._class_locator, 25)
        assert self.class_locator_button is not None, "Button NOT found"

        sorting_btn = self.class_locator_button[1]
        sorting_btn.click()
        elements = fun.element_exists_locator(self.context, self._dictionary_or_elements, 25)
        assert elements is not None, "Elements NOT found"

    def validate_homagepage_element123(self):
       #lf.

