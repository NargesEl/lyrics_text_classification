from bs4 import BeautifulSoup
import pandas as pd
import os
 
path = "/Users/Narges/desktop/spiced/Week_4/project/queen_lyrics/"
artist = 'Queen'
titles = os.listdir(path)
 
data = []

def lyrics_to_dataframe(path:str, artist):
    """
    This function extracts the lyrical text and the title of the song from the html text in the txt files. 
    It will then create dataframes for each artist.
    The path to the txt files is needed as a parameter as well as the name of the artist.
    This must be run for each artist.
    """
    for lyric in titles:
        if lyric.endswith('txt'):
            soup = BeautifulSoup(open(path + lyric))
            try:
                cl = soup.find(attrs={'class':'lyric-body'}).text.replace('\n', ' ')
                ct = soup.find(attrs = {'class':'lyric-title'}).text
                ca = artist
                data.append((cl, ct, ca))
            except AttributeError: 
                print(f'skipping {lyric}')
                pass
pd.DataFrame(data, columns=['Lyric', 'Title', 'Artist']).to_csv(artist+".csv")

