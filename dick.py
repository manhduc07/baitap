#Bài 1
"""
import numpy as np
arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
@@ -10,6 +11,40 @@
print("\nMA trận chuyển vị của tổng 2 ma trận arr1 và arr2 là:\n",chuyen_vi)
"""

import pandas as pd
s = pd.Series([0,1,2,3])
print(s) 
#Bài 2
"""import pandas as pd
import io
import requests
import urllib2
import json
print("Đọc csv từ máy tính")
test = pd.read_csv('./test.csv', encoding='utf-8', header=None, sep=',')
print(test.head(10))
print("\nĐọc csv từ web")
url="https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
s=requests.get(url).content
c=pd.read_csv(io.StringIO(s.decode('utf-8')))
print(c.head(5))
print("\nĐọc Json từ web")
response = urllib2.urlopen('https://api.github.com/users/voduytuan/repos')
data = json.load(response)
print(data)"""

#Bài 3

import matplotlib.pyplot as plt
ex=[0,1,2,6,11,8,15]
week=[1,2,3,4,5,6,7]

"""
#Vẽ đồ thị hình bar
plt.bar(week,ex)
"""

#Vẽ đồ thị hình line
plt.plot(week,ex,marker='.',markersize=10)

plt.show() 