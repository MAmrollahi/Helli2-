import turtle

n = int(input())
zaviye_dakheli = ((n-2)*180)//n
zaviye_kharegi = 180 - zaviye_dakheli

for i in range (3):
   for i in range (4):
      for i in range (n):
         turtle.backward(40)
         turtle.right(zaviye_kharegi)
         
      turtle.penup()
      turtle.forward(n+50)
      turtle.pendown()
   turtle.penup()
   turtle.backward((n*4)+200)
   turtle.right(90)
   turtle.forward(n+40)
   turtle.left(90)
   turtle.pendown()
