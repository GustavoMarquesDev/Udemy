# Selenium - Automatizando tarefas no navegador
from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/


# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent
# Caminho para a pasta onde o chromedriver está
CHROME_DRIVER_PATH = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)  # type: ignore

    chrome_service = Service(
        executable_path=CHROME_DRIVER_PATH,
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser


if __name__ == '__main__':
    TIME_TO_SLEEP = 10
    # Example
    # options = '--headless', '--disable-gpu',
    options = ()
    browser = make_chrome_browser(*options)

    # Como antes
    browser.get('https://www.google.com')

    try:
        # Espera para encontrar o elemento
        search_textarea = WebDriverWait(browser, TIME_TO_SLEEP).until(
            EC.presence_of_element_located((By.NAME, 'q'))
        )
        search_textarea.send_keys('Hello world!')
        search_textarea.send_keys(Keys.ENTER)

        results = browser.find_element(By.ID, 'search')
        links = results.find_elements(By.TAG_NAME, 'a')
        links[0].click()

    except Exception as e:
        print('Não consegui encontrar o elemento')

    # Dorme por 10 segundos
    sleep(TIME_TO_SLEEP)
