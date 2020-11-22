def giaipt():
    print("phuong trinh bac nhat co dang a*x+b=c")
    a= float(input("nhap a="))
    b= float(input("nhap b="))
    c= float(input('nhap c='))
    if a==0:
        print("sai roi :))")
    else:
        print("x =",(c-b)/a)

n=int(input("nhap so lan lap n "))

print("giai pt bang for")
for i in range(n):
    giaipt()
print("ket thuc\n")

print("giai bang while")
while n > 0:
    giaipt()
    n-=1
print("ket thuc while")   