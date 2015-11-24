def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ''

def add_to_index(index,keyword,url):

    for i in index:
        if keyword in i:
            i[1].append(url)
            return

    list=[keyword,[url]]
    index.append(list)

def add_page_to_index(index,url,content):
    keywords=content.split()
    for keyword in keywords:
        add_to_index(index,keyword,url)

def lookup(index,keyword):
    for i in index:
        if keyword in i:
            return i[1]
    return []

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

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            union(tocrawl,get_all_links(content))
            crawled.append(page)
    return index

page=get_page("http://www.udacity.com/cs101x/index.html")
print get_all_links(page)

print crawl_web(page)