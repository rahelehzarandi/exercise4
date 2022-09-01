print("enter numbers , if you want to stop enter empty:")
#num1=0
numlist=[]
num2=0
while  num2 !='':
    num2=(input())
    if num2 !='':
       numlist.append(num2)
print(f'min:{min(numlist)}')
print(f'max:{ max(numlist)}')
print(sorted(numlist))