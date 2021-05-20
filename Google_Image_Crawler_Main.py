from selenium import webdriver
import os
import urllib.request
import time


if __name__ == "__main__":
    SCROLL_PAUSE_TIME = 2
    LOADING_PAUSE_TIME = 2
    print("What do you want to search?:")
    search = input()
    print("How many images do you want, end result might be less but not more")
    amount = int(input())
    print("Please wait! This will take some Time.")

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")

    driver = webdriver.Chrome('chromedriver', options=options)
    driver.get('https://www.google.de/imghp?hl=de&ogbl/xhtml')

    time.sleep(LOADING_PAUSE_TIME)

    search_field = driver.find_element_by_name('q')
    search_field.send_keys(search)
    search_field.submit()

    time.sleep(LOADING_PAUSE_TIME)

    current = driver.current_url
    driver.get(current+"xhtml")

    time.sleep(LOADING_PAUSE_TIME)

    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    images = driver.find_elements_by_tag_name('img')

    if not os.path.exists(search):
        os.makedirs(search)
    for count, element in enumerate(images):
        url = element.get_attribute('src')
        if url is not None:
            urllib.request.urlretrieve(url, search+'/'+search+str(count)+'.png')
        else:
            count = count - 1
        if count == amount:
            break

    print("Congratulation your images are on your computer")

    driver.close()

