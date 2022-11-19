import turtle
n = 3


while n <= 5 :
   zaviye_dakheli = ((n-2)*180)//n
   zaviye_kharegi = 180 - zaviye_dakheli
   for i in range (n) :
      turtle.right(zaviye_kharegi)
      turtle.backward(30)
      
   
   turtle.penup()
   turtle.forward(40)
   turtle.pendown()
   n += 1

