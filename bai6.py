import random

manh = []
n=int(input("nhập số phần tử muốn tạo :)) "))
#Tạo một List gồm các số thực (tạo ngẫu nhiên bằng hàm random với số lượng phần tử của list là số n nhập vào từ bàn phím)
for i in range(n):
    manh.append(int(random.randrange(-30000,30000,1)))
print(manh)
#tìm phần tử lớn nhất của list
manh.sort(reverse=True)

print("phần tử lớn nhất là: ",manh[0])