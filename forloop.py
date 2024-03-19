

names = ["Darcy", "Elizabeth", "Bingley", "Jane", "Lydia"]

print( names[0] )
print( names[1] )

names.append("Liya")

print(names)

second_names = ["Aibike"] + names 
print(second_names)

print("-------")
for string in names:
    print(string + "   hello?")
    print(string[0] + "  the first Letter of the name!") # D for "Darcy", "L" for Lizy
    for c in string:
        print(c) 
print("Finished.")


for k in [0, 1, 2, 3, 4, 5]:
    print(k, names[k]) 

# hundnames = [ f"name_{i}" for i in range(100) ]
# print(hundnames)

print("---")
for k in range(6):
    print(k, names[k])

print("---")
for k in range(len(names)):
    print(k, names[k])



