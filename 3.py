import random

S = set([])
T = set([])
while len(S) != 10 and len(T) != 10:
    S.add(random.randint(1, 20))
    T.add(random.randint(1, 20))

print(S)
print(T)
print("교집합 : ", end="")
print(S.intersection(T))
print("합집합 : ", end="")
print(S.union(T))
print("차집합 : ", end="")
print(S.difference(T))

