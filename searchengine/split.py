
def split_string(source,splitlist):
    list=[]
    atSplit= True
    for char in source:
        if char in splitlist:
            atSplit= True
        else:
            if atSplit:
                list.append(char)
                atSplit=False
            else:
                list[-1]=list[-1]+char
    return list

out = split_string("This is a test-of the,string separation-code!"," ,!-")
print out
#>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = split_string("After  the flood   ...  all the colors came out.", " .")
print out
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
print out
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']

out= split_string('http://this.domain.com/here/there/everywhere.html','/')
print out
#>>>['http:', 'this.domain.com', 'here', 'there', 'everywhere.html']