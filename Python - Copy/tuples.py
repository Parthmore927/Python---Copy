# TUPPLES ARE IMMUTABLE LIKE STRINGS
a = (1,4,6,2,"harry",'A',"shiro")
print(type(a))
# a = (1,) -> tupple with only 1 element
# counting to find frequency of a item using count()
print(a.count(4))
# returns index of the searched item using index()
print(a.index(4))
# returns true or false for searched item in the tupple using  "in"
print(4 in a)