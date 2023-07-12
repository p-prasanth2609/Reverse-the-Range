a=list(map(int,input().split()))
b=int(input())
c=int(input())
d=a[:b]
e=a[b:c+1][::-1]
print(d+e)
