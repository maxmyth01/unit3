#Max Low
#10/5/17
#warmup10.py -- making some dots


from ggame import *


red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)

blackOutline = LineStyle(5,black)
redRectangle = RectangleAsset(200,100,blackOutline,red)
blackTriangle = PolygonAsset([(0,0), (200,0), (100,-75)], blackOutline, black)
blueWindow = RectangleAsset(30,30,blackOutline,blue)
blackDoor = RectangleAsset(30,75,blackOutline, black)

for j in range(3):# prints the row 10 times
    for i in range(5):# prints one row of dots
        Sprite(redRectangle,(50+200*i,100+j*175))
        Sprite(blackTriangle,(50+200*i,100+j*175))
        Sprite(blueWindow,(175+200*i,125+j*175))
        Sprite(blackDoor,(100+200*i,125+j*175))

App().run()

