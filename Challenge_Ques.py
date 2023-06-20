L = ["Ram", 1, "Shyam", 2, "Aman", 3]
print(L)

try:
    L.sort()
except:
    L = [str(i) for i in L]
    L.sort()
    try:
        for i in range(len(L)):
            L[i] = int(L[i])
    except:
        pass
        
print(L)
