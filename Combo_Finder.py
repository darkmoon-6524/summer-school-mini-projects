import random
L = [64,88,152,93,76, 10, 20, 30]
Ans = []
for j in range(len(L)):
    for i in range(50):
        temp = random.sample(L, j)
        if(sum(temp) >= 490 and sum(temp) <= 510):
            if temp not in Ans:
                Ans.append(temp)

print(Ans)
