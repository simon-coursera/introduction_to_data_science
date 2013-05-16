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
    term_dict = {}
    term_total = 0
    
    with open(sys.argv[1]) as f:
        for line in f:
            content = json.loads(line).get('text', '')
            if content:
                term_total += count_word(content, term_dict)

    for (term, count) in term_dict.iteritems():
        print("%s %f"%(term, float(count)/term_total))

if __name__ == '__main__':
    main()
