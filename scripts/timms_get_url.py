"""
Usage:  `python timms_get_url.py <URL>`
Does:   Prints and copies to clipboard the respective video url.
"""

import sys
import pyperclip
from selenium import webdriver

TIMMS_URL_PREFIX    = "https://timms.uni-tuebingen.de/tp/"
PLAYER_URL_PREFIX   = "https://timms.uni-tuebingen.de/Player/EPlayer?id="

def player_extract_video_url(url):
    driver  = webdriver.Firefox()
    driver.get(url)
    result  = driver.execute_script("return TP.SrcFiles[TP.selectedIdx].Url;")
    driver.quit()
    return result

def generate_player_url(url):
    return PLAYER_URL_PREFIX + url[len(TIMMS_URL_PREFIX):]

def timms_get_video_url(url):
    return player_extract_video_url(generate_player_url(url))

def main():
    timms_url   = sys.argv[1]
    video_url   = timms_get_video_url(timms_url)
    pyperclip.copy(video_url)
    print("Copied \'" + video_url + "\' to clipboard.")

if __name__ == "__main__":
    main()

