#Lyrics Classification Project

In this project, I created a text classification model on song lyrics by Queen and The Beatles. To do this I needed to first build a corpus of the lyrics. Using Regular Expressions,  I downloaded an HTML page with links to the songs of the artists and extracted the hyper links of each song. Then, I downloaded and extrcted the song lyrics. Using the Bag of Words method I vectorized the text. After that I trained a classifcication model that predicts the artist from a text sample.

Lyrics by other artists can be used by running the function web_scrapping in lyrics_scrapping.py and putting in the url from lyrics.com of that artist. (example https://www.lyrics.com/artist/Queen). The artist's name will also replace 'Queen' in the extraction_fo_lyrics_to_csv.py as well as feature_engineering_and_training_the_model.py .

###End
