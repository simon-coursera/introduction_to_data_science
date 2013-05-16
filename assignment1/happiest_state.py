import sys
import json
import re


US_STATES = ('AL','AK','AZ','AR','CA','CO','CT','DE','DC','FL','GA','HI','ID','IL','IN'
            ,'IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT'
            ,'NE','NV','NH','NJ','NM','NY','NC','ND'
            ,'OH','OK','OR','PA','RI','SC','SD','TN'
            ,'TX','UT','VT','VA','WA','WV','WI','WY'
            ,'AS','GU','MP','PR','VI','UM','FM','MH','PW')


def clean_word(word):
    match = re.search('(\w+)', word)
    if match:
        return match.group().lower()
    else:
        return ''
    
def sentiment(sentence, state_scores, af_scores):
    sentiment_score = 0
    
    for term in re.split("\s+", sentence):
        term = clean_word(term)
        if term and af_scores.has_key(term):
            #print(term)
            sentiment_score += af_scores[term]
            
    return sentiment_score

def get_tweet_state(tweet):    
    _place = tweet.get('place','')
    if _place:
        if _place['country_code'].lower() == u'us':
            return get_state(_place['full_name'])
    
    _user = tweet.get('user','')
    if _user:
        _location = _user.get('location','')
        if _location:
            return get_state(_location) 
    
    return ''

def get_state(full_name):
    names = re.split("\s*,\s*", full_name)
    if len(names) == 2:
        names[1] = names[1].upper()
        if names[1] in  US_STATES:
            return names[1]
        else:
            return ''
    else:
        return ''

def main():
    afinnfile = open(sys.argv[1])
    af_scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        af_scores[term] = int(score)  # Convert the score to an integer.

    state_scores = {}
    
    with open(sys.argv[2]) as f:
        for line in f:
            tweet = json.loads(line)
            _content = tweet.get('text', '')           
            if _content:
                _lang = tweet.get('lang', '')
                if _lang == u"en":
                    _state = get_tweet_state(tweet)                    
                    if _state:
                        #print(_state)
                        _score = sentiment(_content, state_scores, af_scores)
                        if not state_scores.has_key(_state):
                            state_scores[_state] = _score
                        else:
                            state_scores[_state] += _score
    winer_state = ""
    winer_score = -1000000
    for (_state, _score) in state_scores.iteritems():
        #print _state, _score
        if _score > winer_score:
            winer_score = _score
            winer_state = _state
    
    print winer_state

if __name__ == '__main__':
    main()
