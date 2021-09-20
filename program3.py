#!/usr/bin/env python3

import sys
from urllib.request import urlopen

### the fetch method ###
def fetch_words(url):
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words

def print_items(items):
    for word in items:
        print(word)

def main(url):
    words = fetch_words(url)
    print_items(words)

if __name__ == '__main__':
    main(url = sys.argv[1])

# python program3.py http://sixty-north.com/c/t.txt