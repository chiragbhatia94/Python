def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ''

def get_all_links(page):
    url=[]
    start_link=-1
    while(page.find('<a href=',start_link+1)!=-1):
        start_link = page.find('<a href=',start_link+1)
        start_quote=page.find('"',start_link)
        end_quote=page.find('"',start_quote+1)
        url.append(page[start_quote+1:end_quote])
        start_link=end_quote
    return url

"""start with tocrawl = [seed]
crawled = []
while there are more pages tocrawl:
    pick a page from tocrawl
    add that page to crawled
    add all the link targets on this page to tocrawl
return crawled"""

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            union(tocrawl,get_all_links(get_page(page)))
            crawled.append(page)
    return crawled

page=get_page("http://www.udacity.com/cs101x/index.html")
print get_all_links(page)

print crawl_web(page)