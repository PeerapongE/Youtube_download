# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 21:35:52 2019

@author: PeerapongE
"""

# pip install youtube-dl
# https://rg3.github.io/youtube-dl/
# https://www.bogotobogo.com/VideoStreaming/YouTube/youtube-dl-embedding.php

# Installation

# pip install youtube-dl


import youtube_dl
import pandas as pd

df = pd.read_excel('input_youtube_download.xlsx')

youtube_url_list = df['url'].tolist()


ydl_opts = {}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(youtube_url_list) # input as list