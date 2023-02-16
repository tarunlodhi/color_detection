import cv2
import numpy as np
import pandas as pd
import os

dir_path = os.path.dirname(__file__)
image_name=input("Input image name with jpg:")

#Reading the image with opencv
try:
    img = cv2.imread(f"{dir_path}\{image_name}.jpg")
except:
    print("invalid formate or image not found")
clicked = False
r = g = b = xpos = ypos = 0

index=["color","color_name","hex","R","G","B"]
csv = pd.read_csv(f'{dir_path}\colors.csv', names=index, header=None)

def getColorName(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname

def draw_function(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)
       
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_function)

while(1):

    cv2.imshow("image",img)
    font = cv2.FONT_HERSHEY_SIMPLEX
    if (clicked):
        cv2.rectangle(img,(20,20), (820,60), (b,g,r), -1)
        text = 'Color Name = ' + str(getColorName(r,g,b)) + ' ,Red = '+ str(r) +  ' ,Green = '+ str(g) +  ' ,Blue = '+ str(b)
        cv2.putText(img, text, (50,50), 0, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
        if(r+g+b>=600):
            cv2.putText(img, text, (50,50), 0, 0.7, (0,0,0), 2, cv2.LINE_AA)
        clicked=False

    #Press 'esc' key to exit
    if cv2.waitKey(20) & 0xFF ==27:
        break
    
cv2.destroyAllWindows()
