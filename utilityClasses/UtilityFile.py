from datetime import datetime


class CommonFunction:

    #Author Name: Sanjay
    # This method is used to capture the screenshot of the current page and save it in the Screenshots folder with the test name and current date & time.
    @staticmethod
    def captureSS(driver, test_name):
        # Current date & time
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        # Screenshot file name
        screenshot_path = f".\\Screenshots\\{test_name}_{current_time}.png"

        driver.save_screenshot(screenshot_path)
