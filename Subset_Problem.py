# import random
# L = [-12, -3, -6, 7, 2, -2, 6, 3, 9, -7, -5, -8, 1, 11, -9, -4]
# Ans = []
# for i in range(50):
#     temp = random.sample(L, 5)
#     if(sum(temp) == 0):
#         if(temp not in Ans):
#             Ans.append(temp)

# print(Ans)


import random
L = [-12, -3, -6, 7, 2, -2, 6, 3, 9, -7, -5, -8, 1, 11, -9, -4]
Ans = []
for j in range(3,7):
    for i in range(50):
        temp = random.sample(L, j)
        if(sum(temp) == 0):
            if(temp not in Ans):
                Ans.append(temp)

print(Ans)

