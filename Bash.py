import re

text = "The ghost that says boo haunts the loo"
w = re.findall(".oo", text, re.IGNORECASE)

print(w)