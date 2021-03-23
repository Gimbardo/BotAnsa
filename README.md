# BotAnsa
A python-wrote bot that writes titles and previews of articles on ansa.it in a file.txt, written for a job interview

# Installation
Requirements:
    selenium
Installation guide:
    "pip install selenium" for windows

download from this link chromedriver, based on your chrome version
https://sites.google.com/a/chromium.org/chromedriver/downloads

change line 10 of BotAnsa.py based on where you place your chromedriver.exe

# Manual
python BotAnsa.py    -> to run the bot in his "normal" behaviour: he writes in
                        news.txt the first 5 news on ansa.it

python BotAnsa.py 'filter' 'n_news' 'file'    -> every argument isn't mandatory, but they need to be in order
                                                 (to change 'file', you need to write the other arguments)
                                                 
* filter -> BotAnsa will select only news that contains this filter (default '')
* n_news -> BotAnsa will search only through this number of news (default 5)
* file -> BotAnsa will save articles in a file called this way(default 'news.txt')

BotAnsa.py -> line 10: change this depending on where you place your chromedriver
