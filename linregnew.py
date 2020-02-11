import os
import matplotlib.pyplot as plt
l1 = []
l2 = []
n = int(input("Enter the number of values for X and Y"))
i=0
for i in range(0,n):
    print("Enter the ",i,"th value of X")
    el = int(input())
    l1.append(el)
for i in range(0,n):
    print("Enter the ",i,"th value of Y")
    ele = int(input())
    l2.append(ele)
print("Values of X are")
print(l1)
print("Values of Y are")
print(l2)
sx=sy=sxy=sqx=sqy=0
mlxy = []
sqlx = []
sqly = []
for i in range(0,n):
          sx = l1[i] + sx
          sy = l2[i] + sy
          mlxy.append(l1[i]*l2[i])
          sqlx.append(l1[i]*l1[i])
          sqly.append(l2[i]*l2[i])
          sqx = sqlx[i] + sqx
          sqy = sqly[i] + sqy
          sxy = mlxy[i] + sxy
a = ((sy*sqx) - (sx*sxy))/((n*sqx) - (sx*sx))
b = ((n*sxy) - (sx*sy))/((n*sqx) - (sx*sx))
print("The LINEAR REGRESSION EQUATION of X and Y is : Y = ",a,"+",b,"X")
x = np.linspace(-5,-5,100)
y = a + b*x
plt.plot(x, y, '-r', label='y=a+bx')
plt.title('Graph of y=a+bx')
plt.xlabel('x', color='#1C2833')
plt.ylabel('y', color='#1C2833')
plt.grid()
plt.show()
