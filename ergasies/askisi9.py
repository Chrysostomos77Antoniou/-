x=input()
num=3*x+1
while num!=0:
m = num % 10
num = num / 10
sum = sum + m
print(sum)