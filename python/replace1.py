a = "I am superman and I am here to save the world"
a_new =a.split(" ")
b=[]
for i in a_new:
    if i == "superman":
        b.append("batman")
    else:
        b.append(i)
print(" ".join(b))
