import turtle

n = int(input())
zaviye_dakheli = ((n-2)*180)//n
zaviye_kharegi = 180 - zaviye_dakheli

for i in range (n):
   turtle.forward(20)
   turtle.right(zaviye_kharegi)
