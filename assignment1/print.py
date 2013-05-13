'''
Created on May 13, 2013

@author: simon
'''
import urllib
import json

if __name__ == '__main__':
    url = "http://search.twitter.com/search.json?q=microsoft&page=%d"
    
    for i in range(1,11):
        response = urllib.urlopen(url%(i))
        print json.load(response)