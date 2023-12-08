n=int(input())
l=list(map(int,input().split()))
t=[]
for i in range(n):
  t.append(l[i])
k=t
a=[]
r=[]
for i in range(n):
  a.append(l[i])
  k.remove(l[i])
  s=abs(sum(a)-sum(k))
  print(s,end=' ')

# ip:
# 5
# 1 2 3 4 5

# op:
# 13 9 3 5 15