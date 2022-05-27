import re

s = "100 north road aroad road"

print(s.replace("road", "ro."))
print(re.sub(r"\broad\b", "ro.", s))

print("*************")
pattern = "^M?M?M?$"
print(re.search(pattern, "MMM"))
