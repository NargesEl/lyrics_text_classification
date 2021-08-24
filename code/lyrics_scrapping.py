import requests
import re
import time

def web_scrapping(url):
    """ 
    This function scrapes all the lyrics from a base url from lyrics.com (the parameter needed), saves them as .txt files. 
    It pauses between scapes for 3 seconds to provent blacklisting.
    """
    response = requests.get(url)
    links = '(\/lyric.+?)"'
    urls = re.findall(links, response.text)
    for u in urls:
    new_url = 'https://www.lyrics.com' + u
    song = requests.get(new_url)
    filename = u.split("/")[-1]+".txt"
    open(filename, 'w').write(song.text)
    print(new_url, response.status_code)
    time.sleep(3) 


web_scrapping()