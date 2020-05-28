import random

sym = ["*","#","@"]
num = ["1","2","3", "4", "5", "6", "7", "8", "9", "0"]
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def very_sec():
    pw = random.choice(alpha) + random.choice(num) + random.choice(alpha) + random.choice(num)+ random.choice(alpha) + random.choice(sym) + random.choice(num) + random.choice(sym)
    return pw

def reas_sec():
    pw = random.choice(alpha) + random.choice(alpha) + random.choice(alpha) + random.choice(num) + random.choice(num) + random.choice(sym)
    return pw

def les_sec():
    pw = random.choice(alpha) + random.choice(alpha) + random.choice(num) + random.choice(num)+  random.choice(sym)
    return pw

print(les_sec())
