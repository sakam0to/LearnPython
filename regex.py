# Regression Expression
import re

print(re.findall("abba", "aabbaabbaa"))

print(re.findall("a..a", "aabbaaccaa"))

print(re.findall("^aa..a", "aabbaaccaa"))

print(re.findall("a..aa$", "aabbaaccaa"))

print(re.findall("ac*a", "aabbaaccaa"))

print(re.findall("ab+a", "aabbaaccaa"))

print(re.findall("aa?", "aabbaaccaa"))

print(re.findall("a{2}b{2}a{2}", "aabbaaccaa"))

print(re.findall("[a-z]{2}", "aabbaaccaa"))

print(re.findall("\d{2}", "aa22aaccaa"))

pattern = re.compile("[a-z]{2}\d*a{2}")
lst = ["aabbaaccaa", "aabbaabbaa", "aa22aaccaa"]
for l in lst:
    if pattern.search(l): # search() try to match from any position
        print("find:", l)
        print("match from start:", re.match(pattern, l))
        print("match from any position:", re.search(pattern, l))
        print("match to findall:", pattern.findall(l))
        print("search.group():", pattern.search(l).group(), "\n")

str = "Today is Sep 3rd"
rep = re.sub(r"\drd", "1st", str)
print(rep)

