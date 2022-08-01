from math import *
import string
import random
import hashlib


##from youtubesearchpython import *
##
##
##
##def search_ez(Title):
##    customSearch = VideosSearch(Title, limit = 1)
##    link = customSearch.result()['result'][0]['link']
##    return link
##
##
##print(search_ez("The Blocks we Loved"))

##
##
##import urllib.request
##from bs4 import BeautifulSoup
##
##textToSearch = 'hello world'
##query = urllib.parse.quote(textToSearch)
##url = "https://www.youtube.com/results?search_query=" + query
##response = urllib.request.urlopen(url)
##html = response.read()
##soup = BeautifulSoup(html, 'html.parser')
##for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
##    print('https://www.youtube.com' + vid['href'])


#### O(n) solution for FirstNonRepeatingChar (Amazon)
def firstNonRepeatingCharacter(s):
    Hashmap = {}

    for char in s:
        if char in Hashmap:
            Hashmap[char] += 1
        else:
            Hashmap[char] = 1
    print(Hashmap) 
    for char in s:
        if Hashmap[char] == 1:
            return char


    return '_'


###########Tests###############
print(firstNonRepeatingCharacter("geeksforgeeks"))

print(floor(2))

def encryptFlag(msg, shared_secret):
    sha512 = hashlib.sha512()
    sha512.update(str(shared_secret).encode('ascii'))
    key = sha512.digest()[:len(msg)]
    return bytes([i[0] ^ i[1] for i in zip(key, msg)])
##
##with open('encrypted_flag', 'rb') as f:
##    contents = f.read()

#print(encryptFlag(contents, "stethy cherubimical nontarnishing achoke bechirp"))

random.seed(10052)
p = random.randint(1 << 2047, 1 << 2048) #check random package ;0
q = random.randint(1 << 2047, 1 << 2048)

print(p)
print(q)
print(p == q)
