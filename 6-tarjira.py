text = "1+56+8+9+0"
print()
s=0
for n in text.split("+"):
    s+=int(n)
print(s)
