def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ''

def bad_hash_string(keyword,buckets):
    return ord(keyword[0])%buckets

def test_hash_function(func, keys, size):
    results=[0]*size
    keys_used=[]
    for w in keys:
        if w not in keys_used:
            hv=func(w,size)
            results[hv]+=1
            keys_used.append(w)
    return results

def hash_string(keyword,buckets):
    b=0
    for i in keyword:
        b=(b+ord(i))%buckets
    return b

def make_hashtable(nbuckets):
    hash=[]
    for i in range(nbuckets):
        hash.append([])
    return hash

def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword,len(htable))]

def hashtable_add(htable,key,value):
    # your code here
    hashtable_get_bucket(htable,key).append([key,value])
    return htable

def hashtable_lookup(htable,key):
    bucket=hashtable_get_bucket(htable,key)
    for i in bucket:
        if i[0]==key:
            return i[1]
    return None

def hashtable_update(htable,key,value):
    bucket = hashtable_get_bucket(htable,key)
    for i in bucket:
        if i[0]==key:
            i[1]=value
            return htable
    hashtable_add(htable,key,value)
    return htable

table = [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]],
[['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]

hashtable_update(table, 'Bill', 42)
hashtable_update(table, 'Rochelle', 94)
hashtable_update(table, 'Zed', 68)
print table
#>>> [[['Ellis', 11], ['Francis', 13]], [['Zed', 68]], [['Bill', 42],
#>>> ['Zoe', 14]], [['Coach', 4]], [['Louis', 29], ['Nick', 2],
#>>> ['Rochelle', 94]]]