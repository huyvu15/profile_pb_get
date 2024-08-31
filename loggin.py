import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from colored import fg, attr  # pip install colored
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Webdriver
try:
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
except:
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

def FacebookLogin():
    try:
        # Enter Your Email ID And Password
        user = input("Enter your email: ")
        password = input("Enter your password: ")

        # Opening Facebook.
        driver.get('https://www.facebook.com/')
        print(f"{fg('yellow_1')}Facebook Opened!{attr('reset')}")
        time.sleep(1)

        # Entering Email and Password
        username_box = driver.find_element(By.ID, "email")
        username_box.send_keys(user)
        print(f"{fg('yellow_1')}Email entered{attr('reset')}")
        time.sleep(1)

        password_box = driver.find_element(By.ID, "pass")
        password_box.send_keys(password)
        print(f"{fg('yellow_1')}Password entered{attr('reset')}")

        # Pressing The Login Button
        login_box = driver.find_element(By.NAME, "login")
        login_box.click()
        time.sleep
        print(f"{fg('yellow_1')}Logged in successfully{attr('reset')}")

        # Wait for the profile picture link to be clickable and click on it
        profile_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mount_0_0_i4"]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/div[1]/ul/li[1]/div/a/div[1]/div[2]/div'))
        )
        profile_link.click()
        print(f"{fg('yellow_1')}Profile page opened{attr('reset')}")

        # Get the HTML content of the profile page
        time.sleep(5)  # Wait for profile page to load
        profile_html = driver.page_source
        print(f"{fg('green_1')}Profile HTML content retrieved{attr('reset')}")

        # Save HTML content to a file (optional)
        with open('profile_page.html', 'w', encoding='utf-8') as file:
            file.write(profile_html)
        print(f"{fg('green_1')}Profile HTML content saved to profile_page.html{attr('reset')}")

        input(f"{fg('green_1')}Press anything to quit{attr('reset')}")
        driver.quit()
        print(f"{fg('green_1')}Finished{attr('reset')}")
    except Exception as e:
        print(f"{fg('red_1')}Failed to execute script: {e}{attr('reset')}")

FacebookLogin()
