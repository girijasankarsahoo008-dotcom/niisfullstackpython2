"""#wap take emp salary from keyboard if sal>=5000
da=30% hra=20%

enter basic salary
6000
basic salary
6000
da=1500
hra=1200
total salary=9000


enter basic salary
5000
basic salary
5000
da=1500
hra=1000
total salary=7500


enter basic salary
4000
basic salary
4000
da=0
hra=0
total salary=4000






"""


print("enter basic salary")
sal=float(input())
da,hra=0,0
if sal>=5000:
	da=sal*0.3
	hra=sal*0.2
totalsal=sal+da+hra
print("basic sal=",sal)
print("da=",da)
print("hra=",hra)
print("total salary=",totalsal)







