import sys
import json

def read_score(fp): # to read the scores 
    scores = {} # initialize an empty dictionary
    for line in fp:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores
#   print scores.items() # Print every (term, score) pair in the dictionary

def give_score(fp,scores): 
    score_all = []
    new_score = 0
    term = {}
    for line in fp:
        new = json.loads(line).get('text','')
        term_local = []
        new_score = 0
        for word in new.split():
        	if scores.get(word, 0) != 0:
        		new_score += scores.get(word) 
        	else:
        		term_local.append(word)
        for t in term_local:
        	if t in term.keys():
        		term[t] += new_score
        	else:
        		term[t] = new_score
    print term

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    score_all = give_score(tweet_file,read_score(sent_file))

    
if __name__ == '__main__':
    main()
 