from selenium import webdriver
import time
import random
from bs4 import BeautifulSoup


def random_delay():
    time.sleep(random.uniform(2, 5))

def get_soup(url):
    driver = webdriver.Chrome()
    driver.get(url)
    random_delay()
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    driver.quit()
    return soup

def get_image_links(soup):
    image_links = [img['src'] for img in soup.find_all('img', class_='img-fluid')]
    return image_links

def get_username(soup):
    username = soup.find('div', class_='d-inline-flex align-items-center').text.strip()
    return username

def get_generation_params(soup):
    generation_params = soup.find('div', class_='mt-1 text-left card py-3 px-4').text.strip()
    return generation_params

def get_model_used(soup):
    model_used = soup.find('div', class_='mt-1 text-center card py-3 px-4').text.strip()
    return model_used

def get_prompt_used(soup):
    prompt_used = soup.find('a', href='/academy/prompt-engineering-course').text.strip()
    return prompt_used


if __name__ == "__main__":
    first_url = "https://prompthero.com/"
    second_url = "https://prompthero.com/prompt/4ae9caa7ad7"

    soup_first = get_soup(first_url)
    soup_second = get_soup(second_url)

    image_links = get_image_links(soup_second)
    username = get_username(soup_second)
    generation_params = get_generation_params(soup_second)
    model_used = get_model_used(soup_second)
    prompt_used = get_prompt_used(soup_second)

    print("Image Links:", image_links)
    print("Username:", username)
    print("Generation Parameters:", generation_params)
    print("Model Used:", model_used)
    print("Prompt Used:", prompt_used)
