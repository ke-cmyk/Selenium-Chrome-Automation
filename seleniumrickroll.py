import time
from selenium import webdriver

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.set_window_position(-1050, 0)
#driver.maximize_window()
driver.get('http://www.youtube.com/');
driver.switch_to.frame(0) 
time.sleep(1.5) # Let the user actually see something!
search_box = driver.find_element_by_name('search_query') #find search bar
search_box.send_keys('dQw4w9WgXcQ') # lmao
search_box.submit() # Smash enter
video = driver.find_element_by_xpath("//*[@class='yt-simple-endpoint inline-block style-scope ytd-thumbnail']")
video.click()

while True: # Keep trying to find and click skip ad button until it shows up
    try:
        skip = driver.find_element_by_class_name('ytp-ad-skip-button-container')
        skip.click()
        break
    except:
        continue

driver.maximize_window()

time.sleep(5)
driver.quit()