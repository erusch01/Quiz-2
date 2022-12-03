#Emily Rusch
import math
def formula(a,b,c):
    w = 2*math.pi*a**3
    x = 3*math.sin(b)
    z = 530.27*math.sqrt(c+34)
    y = w + x + z
    print("The formula equals", y)

formula(20,0,30)
