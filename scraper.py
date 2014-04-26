###################################################################################
# Twitter scraper - designed to be forked and used for more interesting things
###################################################################################

import scraperwiki
import simplejson
import urllib2
import datetime

# Change QUERY to your search term of choice. 
# Examples: 'newsnight', 'from:bbcnewsnight', 'to:bbcnewsnight'
# Enter your search term in here. Surround it by quotes ' and if you want a store for a hastag include # e.g. '#ddj'
QUERY = 'diabetes OR #diabetes'
RESULTS_PER_PAGE = '100'
LANGUAGE = 'en'
NUM_PAGES = 1000 

for page in range(1, NUM_PAGES+1):
    base_url = 'http://search.twitter.com/search.json?q=%s&rpp=%s&lang=%s&page=%s' \
         % (urllib2.quote(QUERY), RESULTS_PER_PAGE, LANGUAGE, page)
    try:
        results_json = simplejson.loads(scraperwiki.scrape(base_url))
        #print results_json
        for result in results_json['results']:
            #print result
            data = {}
            data['id'] = result['id']
            data['text'] = result['text'].replace("&quot;", "'")
            data['user_name'] = result['from_user_name']
            data['date'] = result['created_at']
            scraperwiki.sqlite.save(["id", "date"], data) 
    except:
        print 'Scrape failure %s' % base_url
        break
        
    