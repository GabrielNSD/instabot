from selenium import webdriver
import json
import time

def login(user, password, enter):

    with open('config.json', 'r') as f:
        config = json.load(f)

    user.send_keys(config['user']['name'])
    password.send_keys(config['user']['password'])
    enter.click()

def scroll_box(cosia, element):
    SCROLL_PAUSE_TIME = 1

    driver = cosia
    scr1 = element

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    count=0
    while True:
        if count > 1000:
            SCROLL_PAUSE_TIME = 1.5
        if count > 2000:
            SCROLL_PAUSE_TIME = 2
        # Scroll down to bottom
        #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", scr1)
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        #new_height = driver.execute_script("return document.body.scrollHeight")
        new_height = driver.execute_script("return arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
        if new_height == last_height:
            break
        last_height = new_height  

        count = count + 1

def xPath_generator(n, str1, str2):

    list_xpath = []

    for i in range(1,n+1):
        num = i
        new_x = str1 + str(num) + str2
        list_xpath.append(new_x)

    return list_xpath


chromedriver_location = "./chromedriver"

driver = webdriver.Chrome(chromedriver_location)
driver.get('https://www.instagram.com/')

time.sleep(2)

#xPaths
user_field = '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input'
password_field = '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input'

enter_button = '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button'

seguidores = '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a'
seguindo = '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a'
search_box ='/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div/div'

lista_de_seguidores= '/html/body/div[4]/div/div[2]/ul'
#elements

user_element = driver.find_element_by_xpath(user_field)
password_element = driver.find_element_by_xpath(password_field)
enter_button_element = driver.find_element_by_xpath(enter_button)

login(user_element,password_element, enter_button_element)

time.sleep(5)

driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click() #fechar pop up de notificações

driver.get('https://www.instagram.com/morgsq/')

time.sleep(2)
#driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/a').click() #abrir perfil

time.sleep(2)

str_n_seguidores = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').text
str_n_seguindo = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span').text

n_seguidores = int(str_n_seguidores.replace('.',''))
n_seguindo = int(str_n_seguindo.replace('.',''))
'''
driver.find_element_by_xpath(seguidores).click() #abrir janela de seguidores

time.sleep(3)


followers_box = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')

scroll_box(driver, followers_box) #scroll followers box


lista = driver.find_elements_by_class_name('FPmhX notranslate  _0imsa ')
list_container = '/html/body/div[4]/div/div[2]/ul/div'

xPath_seguidores = xPath_generator(n_seguidores, '/html/body/div[4]/div/div[2]/ul/div/li[', ']/div/div[1]/div[2]/div[1]/a')

list_followers = []

for item in xPath_seguidores:
    list_followers.append(driver.find_element_by_xpath(item).get_attribute("title"))

print(len(list_followers))

with open('followers.txt', 'w') as file:
    for item in list_followers:
        file.write("%s\n" % item)

action = webdriver.common.action_chains.ActionChains(driver)
action.move_to_element_with_offset(followers_box, -50, 0)
action.click()
action.perform()
'''

driver.find_element_by_xpath(seguindo).click() #abrir janela de seguindo

time.sleep(2)

following_box = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')

scroll_box(driver, following_box)

xPath_seguindo = xPath_generator(n_seguindo, '/html/body/div[4]/div/div[2]/ul/div/li[', ']/div/div[1]/div[2]/div[1]/a')

list_following = []

for item in xPath_seguindo:
    list_following.append(driver.find_element_by_xpath(item).get_attribute("title"))

with open('following.txt', 'w') as file:
    for item in list_following:
        file.write("%s\n" % item)

