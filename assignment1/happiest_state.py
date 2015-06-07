import sys
import json
import re
state_mapping = { 
    "alabama": "al",
    "alaska": "ak",
    "arizona": "az",
    "arkansas": "ar",
    "california": "ca",
    "colorado": "co",
    "connecticut": "ct",
    "delaware": "de",
    "florida": "fl",
    "georgia": "ga",
    "hawaii": "hi",
    "idaho": "id",
    "illinois": "il",
    "indiana": "in",
    "iowa": "ia",
    "kansas": "ks",
    "kentucky": "ky",
    "louisiana": "la",
    "maine": "me",
    "maryland": "md",
    "massachusetts": "ma",
    "michigan": "mi",
    "minnesota": "mn",
    "mississippi": "ms",
    "missouri": "mo",
    "montana": "mt",
    "nebraska": "ne",
    "nevada": "nv",
    "new hampshire": "nh",
    "new jersey": "nj",
    "new mexico": "nm",
    "new york": "ny",
    "north carolina": "nc",
    "north dakota": "nd",
    "ohio": "oh",
    "oklahoma": "ok",
    "oregon": "or",
    "pennsylvania": "pa",
    "rhode island": "ri",
    "south carolina": "sc",
    "south dakota": "sd",
    "tennessee": "tn",
    "texas": "tx",
    "utah": "ut",
    "vermont": "vt",
    "virginia": "va",
    "washington": "wa",
    "west virginia": "wv",
    "wisconsin": "wi",
    "wyoming": "wy" }

def read_score(fp): # to read the scores 
    scores = {} # initialize an empty dictionary
    for line in fp:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores
#   print scores.items() # Print every (term, score) pair in the dictionary

def match_state(fp, scores):
    # A list of 2-character abbreviated state names
    abbr_states = set(map(lambda (k,v): v, state_mapping.items()))

    # State scores as a dictionary from state abbreviations
    state_scores = dict.fromkeys(abbr_states, 0)
    state_times = dict.fromkeys(abbr_states, 0)

    list_all = []
    i = 0
    for line in fp:
        i += 1
        new = json.loads(line)
        term_local = []
        new_score = 0
        if new.get('user') != None:
            if (new.get('user')).get('location') !=None:
                if ((((new.get('user')).get('location')).split(','))[0].lower() in state_mapping) or (((new.get('user')).get('location')).lower() in state_mapping):
                    long_name, short_name = (filter(lambda (k,v): ((new.get('user')).get('location')).lower() in (k,v) or (((new.get('user')).get('location')).split(','))[0].lower() == v or (((new.get('user')).get('location')).split(','))[0].lower() == k, state_mapping.items()))[0]
                    #print short_name
                    #list_all.append(new)  
                    for word in new.get('text','').split():
                        if scores.get(word, 0) != 0:
                            new_score += scores.get(word) 
                    state_scores[short_name] += new_score   
                    state_times[short_name] += 1
             
        elif new.get('place') != None:
            if (((new.get('place')).get('full_name')).lower() in state_mapping) or (((new.get('place')).get('full_name').split(','))[0].lower() in state_mapping):
                long_name, short_name = (filter(lambda (k,v): ((new.get('place')).get('full_name')).lower() in (k,v) or (((new.get('place')).get('full_name')).split(','))[0].lower() == v or (((new.get('place')).get('full_name')).split(','))[0].lower() == k, state_mapping.items()))[0]
                #list_all.append(new)
                for word in new.get('text','').split():
                    if scores.get(word, 0) != 0:
                        new_score += scores.get(word) 
                state_scores[short_name] += new_score  
                state_times[short_name] += 1

    #print list_all
    for k in state_scores.keys():
        if state_times[k] != 0:
            state_scores[k] = float(state_scores[k]) / float(state_times[k])

    print state_scores
def main():
    sent_file = open('AFINN-111.txt')
    tweet_file = open('output.txt')
#    score_all = give_score(tweet_file,)
    match_state(tweet_file, read_score(sent_file))
    
if __name__ == '__main__':
    main()

 