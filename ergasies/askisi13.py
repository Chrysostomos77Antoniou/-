sum=0
num=input()
i=16
while num != 0:
m = num % 10
if i%2 != 0
m=m*2
if m&gt;9
m=(m/10)+(m%10)
sum = sum + m
num = num /=10
i-=1
if sum%=10==0:
print(&quot;Valid&quot;)
else:
print(&quot;Not Valid&quot;)