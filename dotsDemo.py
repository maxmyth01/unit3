#Max Low
#10/5/17
#dotsDemo.py -- making some dots


from ggame import *

red = Color(0xFF0000,1)

dot = CircleAsset(20,LineStyle(1,red),red)

for i in range(20):
    Sprite(dot,(20+45*i,20))
App().run()
