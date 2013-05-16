import sys
import json
import re
from operator import itemgetter

def clean_word(word):
    match = re.search('(\w+)', word)
    if match:
        return match.group().lower()
    else:
        return ''
    
def count_word(sentence, term_dict):
    counter = 0
    
    for term in re.split("\s+", sentence):
        term = clean_word(term)
        if term:
            counter += 1
            if not term_dict.has_key(term):
                term_dict[term] = 1
            else:
                term_dict[term] = term_dict[term] + 1   
    
    return counter
    
def main():
    all_tags = {}
    with open(sys.argv[1]) as f:
        for line in f:
            tweet = json.loads(line)
            _hashtags = tweet.get('entities',{}).get('hashtags','')
            for _hashtag in _hashtags:
                _tag = _hashtag['text']
                #_count = len(_hashtag['indices']) 
                if not all_tags.has_key(_tag):
                    all_tags[_tag] = 1 #_count
                else:
                    all_tags[_tag] += 1 #_count
    
    sorted_hashtags = sorted(all_tags.iteritems(), key=itemgetter(1), reverse=True)
    for i in range(10):
        print("%s %.1f"%(sorted_hashtags[i][0], sorted_hashtags[i][1]))

if __name__ == '__main__':
    main()
