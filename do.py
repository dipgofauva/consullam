def dismiss_settings(self):
    """Dismisses the settings dialog."""
    settings_close = self.driver.find_element_by_id('settings-close')
    settings_close.click()  
