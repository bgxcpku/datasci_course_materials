import sys
import json

def term_freq(fp): 
    freq = {}
    for line in fp:
        new = json.loads(line).get('text','')
        term_local = []
        for word in new.split():
            if word in freq.keys():
                freq[word] += 1
            else:
                freq[word] = 1 
    freq_all = sum([y for (x,y) in freq.items()])
    freqs = map(lambda (x,y): { x: float(y)/freq_all }, freq.items())
               
    return freq

def main():
    tweet_file = open(sys.argv[1])
    freq = term_freq(tweet_file)
    print freq

    
if __name__ == '__main__':
    main()
