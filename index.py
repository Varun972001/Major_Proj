#Data:n,p,k
string="Data:180,89,56"
result=[]
result=string.split(":")
result1=[]
result1=result[1].split(",")
print(result1)
sum1=0
sum1=int(result1[0])+int(result1[1])+int(result1[2])
print(sum1)
result2=[]
for item in result1:
    result2.append(round(int(item)/sum1,6))
print(result2)