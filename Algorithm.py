from collections import Counter
from collections import defaultdict

def count_characters(string):
    count_dict= {}
    for c in string:
        if c in count_dict:
            count_dict[c] += 1
        else:
            count_dict[c] = 1

    print(count_dict)

def count_defaultdict(string):
    count_defaultdict = defaultdict(int)
    for C in string:
        count_defaultdict[C] += 1

    print(count_defaultdict)

count_characters("Dynasty")

count_defaultdict("Dynasty")

print(Counter("Dynasty"))