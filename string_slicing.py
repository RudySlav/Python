# Slicing = Create a substring by extracting elements from another string
#           indexing [] or slice ()
#           [start:stop:step]

name = "Krzysztof Mendel"

# Indexing
first_name = name[0:9] # You can leave 0 blank and python will auto assume
last_name = name[10:]
funky_name = name[0::2]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

# Slicing
website = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4)

print(website[slice])
print(website2[slice])