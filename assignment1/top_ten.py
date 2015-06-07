import sys
import json
import re

def hash_score_stat(fp):
	hash_score = {}
	i = 0
	for line in fp:
		new = json.loads(line)
		#print new.get('entities')
		if new.get('entities') != None:
			print new.get('entities')
  		#if not ((new.get('entities')).get('hashtags')):
  		#	print "good"
  		#	i += 1
	print i



def main():
    tweet_file = open('output.txt')
    hash_score_stat(tweet_file)
    
if __name__ == '__main__':
    main()
