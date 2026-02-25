shopping=["bag","pen","pencil"]
print(shopping)
#for
for item in shopping:
    print(item)
#append
shopping.append("notebook")
print(shopping)
for item in shopping:
    print(item)
#insert
shopping.insert(2,"whitener")
print(shopping)
for item in shopping:
    print(item)
#function count
n=shopping.count("bag")    
print(n)
#function len()=length
print(len(shopping))