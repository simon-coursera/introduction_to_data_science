import sys
import json
import re

def clean_word(word):
    match = re.search('(\w+)', word)
    if match:
        return match.group().lower()
    else:
        return ''
    
def sentiment(scores, sentence):
    sentiment_score = 0
    
    for term in re.split("\s+", sentence):
        term = clean_word(term)
        if term and scores.has_key(term):
            #print(term)
            sentiment_score += scores[term]
            
    return sentiment_score

def main():
    afinnfile = open(sys.argv[1])
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    
    with open(sys.argv[2]) as f:
        for line in f:
            content = json.loads(line).get('text', '')
            if content:
                print("%f"%(sentiment(scores, content)))
    

if __name__ == '__main__':
    main()
