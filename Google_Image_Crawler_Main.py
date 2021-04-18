from selenium import webdriver
import time


if __name__ == "__main__":
    SCROLL_PAUSE_TIME = 2
    LOADING_PAUSE_TIME = 2
    print("What do you want to search?:")
    search = input()
    driver = webdriver.Chrome()
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

    driver.close()

    print(len(images))
