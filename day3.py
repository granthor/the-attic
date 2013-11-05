customer_1 = {"name":"nick","age":14}
customer_2 = {"name":"nick","age":14,"eyes":"i dont remember"}
print customer_1 
print customer_2
print type (customer_1)
print customer_1.keys()
print customer_1.values()
print customer_1.items()
print customer_1["name"]
print customer_1["age"]
#print customer_1.items()[0] # what it prints is random
if "eyes" in customer_1.keys():
    print customer_1["eyes"]
else:
    print "no eyes"
if "eyes" in customer_2:
    print customer_2["eyes"]
else:
    print "no eyes"
#Hi i am a comment.

