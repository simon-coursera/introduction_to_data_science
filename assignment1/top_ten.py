import sys
import json
import re

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
    hashtags = {}
    with open(sys.argv[1]) as f:
        for line in f:
            tweet = json.loads(line)
            _hashtags = tweet.get('entities',{}).get('hashtags','')
            for _hashtag in _hashtags:
                _tag = _hashtag['text']
                _count = len(_hashtag['indices']) 
                if not hashtags.has_key(_tag):
                    hashtags[_tag] = _count
                else:
                    hashtags[_tag] += _count
    
    hashtag_tuples = ()
    for (k,v) in hashtags.iteritems():
        hashtag_tuples += (k,v)
    
    sorted(hashtag_tuples, key=lambda hashtag: hashtag[1])

if __name__ == '__main__':
    main()
