#truy xuất đến từng phần tử trong List và in giá trị của từng phần tử ra màn hình
smnr= [29,6,30,5,-2002,3,2,12,1,7,-12]

print("phần tử trong list")
for hn in smnr:
    print(hn)
#truy xuất đến từng phần tử trong List và thực hiện tính logarith của từng phần tử và in giá trị đó ra màn hình
import math
print("\ntinh log các giá trị trong list: ")
for hn in smnr:
    if hn <= 0:
        print("số {} không thể tính log".format(hn))
    else:
        print("giá trị log của số {} là {}".format(hn,math.log(hn)))