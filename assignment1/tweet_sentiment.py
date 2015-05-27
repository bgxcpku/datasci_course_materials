import sys
import json

def lines(fp):
    print str(len(fp.readlines()))

def sent_lib(fp):
    scores = {} # initialize an empty dictionary
    for line in fp:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores
#   print scores.items() # Print every (term, score) pair in the dictionary

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    data = []
    score = []
    scores = sent_lib(sent_file)
    for line in tweet_file:
        new = json.loads(line).get('text','')
        new_score = 0
        for word in new.split():
            new_score+= scores.get(word, 0) 
        data.append(new)
        score.append(new_score)
    print type(data)
    print data[1]
    print type(data[1])
#    print score
#    print data
#    print scores
    print sum(score)
#    print score
    print scores.get("cool",0)
    print word
if __name__ == '__main__':
    main()
 