import pytest
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class TestComputerSoftwareOverviewDashboard:
    #dashboard_id = "new dashboard"
    dashboard_id = "ce98c19b-587f-4d76-9c49-2e9acee257d5"
    @pytest.fixture(scope="class")
    def setup_login(self, driver, login):
        login()
        yield driver


    #@pytest.mark.skip(reason="This test isn't working for 2.0 yet")
    def test_host_count(self, setup_login, kibana_url, timeout):
        driver = setup_login
        #dashboard_id = "33f0d3b0-8b8a-11ea-b1c6-a5bf39283f12"
        driver.get(f"{kibana_url}/app/dashboards#/view/{self.dashboard_id}")
        expected_cond = EC.presence_of_element_located((By.CLASS_NAME, "kbnAppWrapper"))
        WebDriverWait(driver, timeout).until(expected_cond)
        panel_title = "Host Count"
        selector = f'div[data-title="{panel_title}"]'
        expected_cond = EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        WebDriverWait(driver, timeout).until(expected_cond)
        panel = driver.find_element(By.CSS_SELECTOR, selector)
        assert "No results found" not in panel.get_attribute("innerHTML")