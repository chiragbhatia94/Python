def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ''

def add_to_index(index,keyword,url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword]=[url]

def add_page_to_index(index,url,content):
    keywords=content.split()
    for keyword in keywords:
        add_to_index(index,keyword,url)

def lookup(index,keyword):
    if keyword in index:
        return index[keyword]
    return None

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

def compute_ranks(graph):
    d=0.8 #damping factor
    numloops=10

    ranks={}
    npages=len(graph)
    for page in graph:
        ranks[page]=1.0/npages

    for i in range(numloops):
        newranks={}
        for page in graph:
            newrank=(1-d)/npages


            newranks[page]=newrank
        ranks=newranks
    return ranks

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = {}
    graph = {}
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            outlinks=get_all_links(content)
            graph[page]=outlinks
            union(tocrawl,outlinks)
            crawled.append(page)
    return index, graph

page=get_page("http://www.udacity.com/cs101x/index.html")
print get_all_links(page)

print crawl_web(page)