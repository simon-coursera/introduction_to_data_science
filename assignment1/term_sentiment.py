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

def add_score(sentence, sentiment_score,af_scores, new_scores):
    for term in re.split("\s+", sentence):
        term = clean_word(term)
        if term and not af_scores.has_key(term):
            if not new_scores.has_key(term):
                new_scores[term] = [sentiment_score]
            else:
                new_scores[term].append(sentiment_score)   
    
    
def main():
    afinnfile = open(sys.argv[1])
    af_scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        af_scores[term] = int(score)  # Convert the score to an integer.

    new_scores = {}
    with open(sys.argv[2]) as f:
        for line in f:
            content = json.loads(line).get('text', '')
            if content:
                sentiment_score = sentiment(af_scores, content)
                add_score(content, sentiment_score, af_scores, new_scores)
        
    #calculate new score
    for score_key in new_scores.keys():
        score_total = 0
        for score in new_scores[score_key]:
            score_total += score
        score_average = float(score_total) / len(new_scores[score_key]) 
        print("%s %f"%(score_key, score_average))

if __name__ == '__main__':
    main()
