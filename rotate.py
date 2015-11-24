def shift_n_letters(letter, n):
    n%=26
    c=ord(letter)
    c=c+n
    if c>ord('z'):
        e=c-ord('z')
        c=ord('a')+e-1
    elif c<ord('a'):
        e=ord('a')-c
        c=ord('z')-e
    return chr(c)

def rotate(s, n):
    res = ""
    for letter in s:
        if letter != ' ':
            res+=shift_n_letters(letter, n)
        else:
            res+=" "
    return res

print rotate ('sarah', 13)
#>>> 'fnenu'
print rotate('fnenu',13)
#>>> 'sarah'
print rotate('dave',5)
#>>>'ifaj'
print rotate('ifaj',-5)
#>>>'dave'
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17)
#>>> ???