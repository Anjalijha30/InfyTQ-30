# Assignment 60 


def remove_duplicates(value):
    t=[]
    for i in value:
        if i not in t:
            t.append(i)
    k=''.join(str(i) for i in t)
    return k

print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))
