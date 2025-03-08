import pagerank

corpus = {"1.html": {"2.html", "3.html"}, "2.html": {"3.html"}, "3.html": {"2.html"}}

page = "1.html"

print(pagerank.transition_model(corpus, page, .85))