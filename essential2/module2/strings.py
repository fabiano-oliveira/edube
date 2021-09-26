
print("A", ord("A"))
print("a", ord("a"))
print("c", ord("c"))
print("ç", ord("ç"))
print(chr(945))

word = "Fabiano"
print(word[::2])
print(word[::-1])
print(word[5:2:-1])

print(min("aAbBcC"))

print(word.find("z"))
print(word.count("a"))


s1 = "12.8"
i = int(s1)
s2 = str(i)
f = float(s2)
print(s1 == s2)