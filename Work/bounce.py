# bounce.py
#
# Exercise 1.5
height = 100
bounces = 1

while bounces <= 10:
    height*= 0.6
    print(bounces, round(height, 4))
    bounces+=1
