
import re
import urllib
comments=[]
stars=[]
baseurl='https://www.amazon.com/ZYLISS-Susi-Garlic-Press-Need/product-reviews/B007D3V00Q/ref=cm_cr_arp_d_viewopt_sr?ie=UTF8&reviewerType=all_reviews&filterByStar=critical&pageNumber=%d'

for i in range(19):
    fhand=urllib.urlopen(baseurl % (i+1))
    for line in fhand:
        if re.search('review-text">',line):
            comments.append(re.findall('review-text">(.*?)</span>',line)[0])
            if re.search('alt">(.*?) out of 5 stars<',line):
                stars.append(re.findall('alt">(.*?) out of 5 stars<',line)[0])
            else:
                stars.append('99')

import pandas as pd
df=pd.DataFrame({'comments':comments,'stars':stars})
df.to_csv('ZYLISS-Susi_cri.csv')



# Tokenize
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer('\w+')
tokens = tokenizer.tokenize(comments[0])
tokens[:8]

# Lower
words = []
for word in tokens:
    words.append(word.lower())

# Get English stopwords and print some of them
sw = nltk.corpus.stopwords.words('english')
sw[:5]



