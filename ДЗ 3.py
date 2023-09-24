## Задача 3
def pack_backpack(items, max_weight):
    possible_items = []
    for item, weight in items.items():
        if weight <= max_weight:
            possible_items.append(item)
            max_weight -= weight
    return possible_items

items = {'tent': 5, 'water': 3, 'food': 4, 'clothes': 2, 'first aid kit': 1}
max_weight = 10
print(pack_backpack(items, max_weight)) 

## Задача 1
def find_duplicates(lst):
    return list(set([x for x in lst if lst.count(x) > 1]))

lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(find_duplicates(lst))

## Задача 2
import re
from collections import Counter

def top_10_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words).most_common(10)

text = """Два кота, два друга, шли как-то по тропинке в лесу. Шли два кота, шли, пока не ушли с тропинки и не дошли
до деревни. Два кота решили не идти дальше и остаться жить в деревне"""
print(top_10_words(text))
