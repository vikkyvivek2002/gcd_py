a= int(input())
b= int(input())
if(a>b):
    num=b
else:
    num=a
n=1
gcd =0
while(n<=num):
    if(a%n==0 and b%n==0):
        gcd =n
    n=n+1
print(gcd)
