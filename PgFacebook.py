from selenium.webdriver.common.by import By
import pyautogui
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta
import os
from seleniumbase.common.exceptions import NoSuchElementException


class FacebookClass:
    def get_info_from_script(self):

        # Get the file path for script
        file_path = os.path.join(
            os.path.expanduser("~"),
            "Desktop",
            "Daily_accounts",
            "bread_fall_daily",
            "Script_bread_fall_daily_youtube.txt",
        )

        info_dict = {}
        try:
            with open(file_path, "r") as file:
                current_key = None
                for line in file:
                    line = line.strip()  # Remove leading/trailing whitespace

                    if ":" in line:
                        current_key, value = line.strip().split(":", 1)
                        info_dict[current_key.strip()] = value.strip()
                    else:
                        # Append to description if same key
                        if current_key == "Description":
                            info_dict[current_key] += "\n" + line
                        else:
                            # Handle unexpected line format (optional)
                            print(f"Warning: Unexpected line format: {line}")

        except FileNotFoundError:
            print(f"Error: File not found at {file_path}")

        return info_dict

    def login_to_meta_business(self, driver):

        # Retrieve information from the file
        info = self.get_info_from_script()

        # access to meta business login page an clicks on the facebook logo to access with a facebook account
        driver.get("https://business.facebook.com/business/loginpage")

        try:
            # Attempt to click on the desired element
            driver.click('[alt="Facebook"]')
        except NoSuchElementException:
            try:
                driver.click("div.x1e0frkt")
            except NoSuchElementException:
                # If both elements are not found, handle the exception
                print("Could not find element using either locator")

        # enter credentials and clicks on log in button
        driver.type("#email", info["Email"])
        driver.type("#pass", info["Password"])
        driver.click("#loginbutton")

    def automate_content_planner(self, driver):

        # navigates to content planner page
        driver.get("https://business.facebook.com/latest/content_calendar")
        driver.sleep(2)

        # Retrieve information from the file
        info = self.get_info_from_script()

        date_str = info["Start_date"]  # Your starting date
        day = "Day"  # Label for day

        # Convert the starting date string to a datetime object
        start_date = datetime.strptime(date_str, "%m/%d/%Y")

        for i in range(int(info["Last_day_uploaded"]), int(info["Upload_until_day"])):
            # Add i days to the starting date
            current_date = start_date + timedelta(days=i)
            # Format the date as desired (e.g., MM/DD/YYYY)
            formatted_date = current_date.strftime("%m/%d/%Y")

            # navigates to reel composer page
            driver.get("https://business.facebook.com/latest/reels_composer")

            # clicks on the "Add Video" button by searching for all elements with
            # the class name "xtwfq29" and clicking on the second one
            driver.wait_for_element("div.xtwfq29")
            option_elements = driver.find_elements(By.CSS_SELECTOR, "div.xtwfq29")
            option_elements[1].click()
            driver.sleep(2)

            # waits 2 seconds before interacting with the computer.
            # Searches for the title of the video and hits ENTER when it is found.
            pyautogui.sleep(2)
            pyautogui.hotkey("`")  # For Mac
            pyautogui.hotkey("command", "f")
            pyautogui.sleep(2)
            pyautogui.typewrite(
                info["Name_of_video"], interval=0.1
            )  # writes name of video
            pyautogui.press("enter")
            pyautogui.sleep(2)
            pyautogui.press("TAB")
            pyautogui.press("TAB")
            pyautogui.hotkey("`")  # For Mac
            pyautogui.press("enter")

            # locates the element for the description of the video
            driver.wait_for_element("div.xjbqb8w.xmls85d")
            driver.click(
                "div.xjbqb8w.xmls85d"
            )  # click on it so the code can send keys (words)

            # we need to use actions so we can write the description of the video
            actions = ActionChains(driver)
            actions.send_keys(
                f"{day} {i+1} " + info["Description"]
            ).perform()  # description of the video
            driver.sleep(2)

            # clicks twice on the button "Next"
            driver.wait_for_element("div.xo1l8bm.x140t73q").click()
            driver.wait_for_element("div.xo1l8bm.x140t73q").click()

            # identifies the "Schedule" button and clicks on it
            driver.wait_for_element(
                "div.x1i10hfl.x1pi30zi"
            )  # locator for "Schedule" button
            option_elements = driver.find_elements(
                By.CSS_SELECTOR, "div.x1i10hfl.x1pi30zi"
            )
            option_elements[1].click()

            # identifies the element to input the date (for some reason we have to click it twice)
            driver.wait_for_element("div.x15x72sd").click()  # locator to input the date
            driver.sleep(2)
            driver.wait_for_element("div.x15x72sd").click()
            driver.sleep(2)

            # send keys to the input date
            actions.key_down(Keys.COMMAND).send_keys("a").key_up(Keys.COMMAND).perform()
            driver.sleep(2)
            actions.send_keys(f"{formatted_date}").send_keys(Keys.ENTER).perform()
            driver.sleep(2)

            # identifies the elements for the Hour, Minute and Time of day (08:00 PM)
            option_elements = driver.find_elements(By.CSS_SELECTOR, "input.x972fbf")

            # takes the Time from the script and divides it in hours, minutes, time_of_day
            time_parts = info["Time"].replace(":", " ").split()
            hours, minutes, time_of_day = time_parts

            # send keys
            option_elements[1].send_keys(hours)  # hours
            option_elements[2].send_keys(minutes)  # minutes
            option_elements[3].send_keys(time_of_day)  # time_of_day
            driver.sleep(2)

            # clicks on the "Publish" button
            driver.wait_for_element("div.xo1l8bm.x140t73q").click()

            # Print the date and day on terminal
            print(f"{formatted_date} - {day} {i+1}")
