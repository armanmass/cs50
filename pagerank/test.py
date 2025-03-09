import pagerank

#corpus = {"1.html": {"2.html", "3.html"}, "2.html": {"3.html"}, "3.html": {"2.html"}}
corpus = {'1': {'2'}, '2': {'1', '3'}, '3': {'4', '2'}, '4': {'2'}}

print(pagerank.iterate_pagerank(corpus, .85))