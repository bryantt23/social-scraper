import time
from selenium import webdriver


# Set the path to your WebDriver (e.g., ChromeDriver)
# Update this path to where your ChromeDriver is located
webdriver_path = '/path/to/chromedriver'

# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Open Tinder
driver.get('https://google.com')

# Keep the browser open for a while (e.g., 10 seconds) to see the result
time.sleep(3)

# Close the browser
driver.quit()
