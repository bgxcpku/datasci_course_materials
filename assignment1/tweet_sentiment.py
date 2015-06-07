import sys
import json

def read_score(fp):
    scores = {} # initialize an empty dictionary
    for line in fp:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores
#   print scores.items() # Print every (term, score) pair in the dictionary

def give_score(fp,scores):
    score_all = []
    for line in fp:
        new = json.loads(line).get('text','')
        new_score = 0
        for word in new.split():
            new_score += scores.get(word, 0) 
        score_all.append(new_score)
    return score_all

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    score_all = give_score(tweet_file,read_score(sent_file))
    print sum(score_all)

    
#    print type(data)
#    print data[1]
#    print type(data[1])
#    print score
#    print data
#    print scores
#    print score

if __name__ == '__main__':
    main()
 