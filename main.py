from seleniumbase import Driver
from PgFacebook import FacebookClass


driver = Driver(uc=True)
driver.maximize_window()

fb_instance = FacebookClass()
fb_instance.login_to_meta_business(driver)
fb_instance.automate_content_planner(driver)
