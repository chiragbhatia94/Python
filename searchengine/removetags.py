def remove_tags(x):
    while True:
        start=x.find("<")
        if start==-1:
            break
        end=x.find(">",start+1)
        x=x[:start]+" "+x[end+1:]
    list=x.split()
    return list

print remove_tags('This <i>line</i> has <em>lots</em> of <b>tags</b>.')
