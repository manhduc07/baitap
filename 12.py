import string,random
M=dict()
n=random.randrange(1,20)
G=random.choice(string.ascii_uppercase)
H=G+''.join(random.choice(string.ascii_lowercase) for i in range(n-1))
M['Tên']=H
A=random.randrange(1,100)
M['Tuổi']=A
print("Random Dictionary: ",M)