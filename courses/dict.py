#post
#user_id = 103
#message = "D5 E5 C5 C4 G4"
#language = "Englist"
#datetime = "20230215T124231Z"
#location = (44.590533, -104.715556)

#dict={keys: values}

post = {"user_id": 103,
        "message": "D5 E5 C5 C4 G4",
        "location": "Englisn",
        "datetime": "20230215T124231Z",
        "location":(44.590533, -104.715556)}

print(type(post))

post2 = dict(message="SS Cotpaxi",
         language="Englisn")

post2["user_id"] = 209
post2["datetime"] = "19771116T093001Z"

print(post)
print(post2['message'])


try:
    print(post2['locatin'])
except KeyError:
    print("The post doesn't have a locatin key")


print(dir(post2))

print(help(post2.get))

loc = post2.get('location')
print(loc)

for key, value in post.items():
    print(key, "=", value)

post.pop("location")
print(post)
