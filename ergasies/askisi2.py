f = open(“in.txt”, “r”)
i, f=0,c=0,k=0,r=0
x=f.read()
for i in x:
if x[i]==&#39;f&#39;:
f+=1
elif x[i]==&#39;c&#39;:
c+=1
elif x[i]==&#39;k&#39;:
k+=1
elif x[i]==&#39;r&#39;:
r+=1
sum=f+c+k+r
if sum&gt;len(x)-sum
print(&quot;kaki&quot;)
f.close()