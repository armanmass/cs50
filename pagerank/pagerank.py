import os
import random
import re
import sys

import numpy as np
import pandas as pd

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    trans_dict = {}

    N = 1/len(corpus)
    for k in corpus.keys():
        trans_dict[k] = (1-damping_factor) * N

    norm = len(corpus[page])
    for k in corpus[page]:
        trans_dict[k] += damping_factor / norm
    
    return trans_dict 


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    samples = {}
    current_page = random.choice(list(corpus.keys()))
    samples[current_page] = 1

    for _ in range(1, n):
        trans_model = transition_model(corpus, current_page, damping_factor)
        current_page = random.choices(list(trans_model.keys()), weights=list(trans_model.values()))[0]
        samples[current_page] = samples.get(current_page, 0)+1
    
    samples = {key: value / n for key, value in samples.items()}

    return samples

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pagerank = {}

    N = 1/len(corpus)
    for k in corpus.keys():
        pagerank[k] = N

    reverse_corpus = {}

    for k, v in corpus:
        for page in v:
            reverse_corpus[page] = reverse_corpus.get(page, set()).add(k)

    #links on page i in original corpus len(v)
    #


    return pagerank
    raise NotImplementedError


if __name__ == "__main__":
    main()
