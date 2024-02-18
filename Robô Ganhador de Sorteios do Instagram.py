import time
from selenium import webdriver
from pynput.keyboard import Key, Controller

# CONFIGURAÇÕES INICIAIS ------- ------- ------- ------- ------- ------- ------- ------- ------- ------- -------

insta_id = 'fugitapedro'                                        # Coloque aqui seu login
insta_pw = 'cor191910'                                          # Coloque aqui sua senha
insta_link = 'https://www.instagram.com/p/CcObXrYLmIl/'         # Coloque aqui o link do post do sorteio
timer = 6                                                       # Tempo em segundos. Aumente se tiver dando pau

# CONSTANTE GLOBAL ------- ------- ------- ------- ------- ------- ------- ------- ------- ------- ------- -------

keyboard = Controller()
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
contador_alphabet = 0
contador = 1
print(contador)

def clint_eastwood():
    global contador
    global contador_alphabet
    global alphabet

    keyboard.press(alphabet[contador_alphabet])
    keyboard.release('b')
    time.sleep(timer)
    for a in range(0, contador):
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        time.sleep(0.1)
    contador = contador + 1
    time.sleep(0.2)


# REALIZANDO O LOGIN

driver = webdriver.Chrome()
driver.get('https://www.instagram.com/');
time.sleep(timer)
id_box = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
id_box.send_keys(insta_id)
pw_box = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
pw_box.send_keys(insta_pw)
time.sleep(timer)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
time.sleep(timer)

# CASO EXISTA A TELA DE CONFIRMAÇÃO DE LOGIN, ELE VERIFICA E SAI DELA
try:
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
except AttributeError:
    print("OK!")
time.sleep(timer)

# IGNORA O MENU DE ATIVAR NOTIFICAÇÕES, CASO EXISTA:
try:
    driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()
except AttributeError:
    print("OK!")
time.sleep(timer)

# VENCENDO O SORTEIO
while contador_alphabet < 26:
    while contador <= 40:
        driver.get(insta_link);
        time.sleep(timer)
        msg_box = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea')
        msg_box.click()
        keyboard.press('@')
        keyboard.release('@')
        clint_eastwood()
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(timer)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    time.sleep(3000)
    contador = 1
    contador_alphabet = contador_alphabet + 1