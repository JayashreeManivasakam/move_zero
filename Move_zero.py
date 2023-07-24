lst=list(map(int,input().split()))
for i in range (0,len(lst)-1):
    if lst[i]==0:
        lst.remove(lst[i])
        lst.append(0)
print(lst)
