import turtle
n = 3
b = int(input())

while n <= b :
   zaviye_dakheli = ((n-2)*180)//n
   zaviye_kharegi = 180 - zaviye_dakheli
   for i in range (n) :
      turtle.right(zaviye_kharegi)
      turtle.backward(20)
      
   
   turtle.penup()
   turtle.forward(40)
   turtle.pendown()
   n += 1

