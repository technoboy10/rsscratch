import scratch
import feedparser
import time
import webbrowser
feed = "http://wiki.scratch.mit.edu/index.php?title=Special:RecentChanges&feed=rss"
parsed = feedparser.parse(feed)
parsed_article = parsed.entries[0]
print 'PARSED'
s = scratch.Scratch()
s.connect()
print "OK"
article = 0
while True:
  updates = s.receive()
	updates_d = updates[1]
	if 'feed' in updates_d:
		feed = updates_d['feed']
		parsed = feedparser.parse(feed)
		parsed_article = parsed.entries[article]
		print 'PARSED'
	if 'article' in updates_d:
		article = updates_d['article'] - 1
	article_title = parsed_article.title
	article_desc = parsed_article.description
	title_encode = article_title.encode('ascii', 'ignore')
	desc_encode = article_desc.encode('ascii', 'ignore')
	article_url = parsed_article.link
	s.sensorupdate({'article title' : title_encode})
	s.sensorupdate({'article description' : desc_encode})
	s.sensorupdate({'article url' : article_url})
	parsed = feedparser.parse(feed)
	parsed_article = parsed.entries[article]
