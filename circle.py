#
# ref: https://www.itread01.com/content/1548357888.html
#      https://chtseng.wordpress.com/2016/12/05/opencv-contour%E8%BC%AA%E5%BB%93/
#
import cv2
import numpy as np

class fisheyeCircle(object):
  def __init__(self, img):
    self.img = img

  def getRadiusCenter(img):
    #self.img = img
    img_shape = img.shape
    h = img_shape[0]
    w = img_shape[1]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    
    _, thresh8 = cv2.threshold(gray , 127, 255, 8)
    cv2.imwrite('gray.png', thresh8)
    ret, thresh = cv2.threshold(cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY) , 127, 255, cv2.THRESH_BINARY_INV)
    contours, hier = cv2.findContours(thresh8, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    r_max = []
    c_max = []

    for c in contours:
      x,y,w,h = cv2.boundingRect(c)
      # calculate center and radius of minimum enclosing circle
      (x,y),radius = cv2.minEnclosingCircle(c)
      # cast to integers
      center = (int(x),int(y))
      radius = int(radius)   
      r_max.append(radius)
      c_max.append(center)
      # draw the circle
      #img = cv2.circle(img,center,radius,(0,255,0),2)
    #cv2.imshow("circle", img)
    #cv2.imwrite('circle.png', img)   

    #print('r',max(r_max))
    #print(c_max[r_max.index(max(r_max))]) 
    return max(r_max), c_max[r_max.index(max(r_max))] 
""" 
img = cv2.imread("rawImage.jpg", cv2.IMREAD_UNCHANGED)
#img = cv2.imread("rewarp.png", cv2.IMREAD_UNCHANGED)

img_shape = img.shape
h = img_shape[0]
w = img_shape[1]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray , 127, 255, 0)
_, thresh1 = cv2.threshold(gray , 127, 255, 1)
_, thresh2 = cv2.threshold(gray , 127, 255, 2)
_, thresh3 = cv2.threshold(gray , 127, 255, 3)
_, thresh4 = cv2.threshold(gray , 127, 255, 4)
_, thresh8 = cv2.threshold(gray , 127, 255, 8)

#cv2.imshow('0', thresh)
#cv2.imshow('1', thresh1)
#cv2.imshow('2', thresh2)
#cv2.imshow('3', thresh3)
#cv2.imshow('4', thresh4)
#cv2.imshow('8', thresh8)

cv2.imwrite('0.png', thresh)
cv2.imwrite('1.png', thresh1)
cv2.imwrite('2.png', thresh2)
cv2.imwrite('3.png', thresh3)
cv2.imwrite('4.png', thresh4)
cv2.imwrite('8_.png', thresh8)

ret, thresh = cv2.threshold(cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY) , 127, 255, cv2.THRESH_BINARY_INV)
contours, hier = cv2.findContours(thresh8, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
r_max = []
c_max = []

for c in contours:
  # find bounding box coordinates
  x,y,w,h = cv2.boundingRect(c)
  cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)

  # find minimum area
  rect = cv2.minAreaRect(c)
  # calculate coordinates of the minimum area rectangle
  box = cv2.boxPoints(rect)
  # normalize coordinates to integers
  box = np.int0(box)
  # draw contours
  #cv2.drawContours(img, [box], 0, (0,0, 255), 3)
  # calculate center and radius of minimum enclosing circle
  (x,y),radius = cv2.minEnclosingCircle(c)
  # cast to integers
  center = (int(x),int(y))
  radius = int(radius)
  
  r_max.append(radius)
  c_max.append(center)

  #print('center,r:',center,radius)
  # draw the circle
  img = cv2.circle(img,center,radius,(0,255,0),2)

print('r',max(r_max))
print(c_max[r_max.index(max(r_max))])

cv2.circle(img,(c_max[r_max.index(max(r_max))]), 10, (0, 255, 0), -1)
cv2.drawContours(img, contours, -1, (25, 0, 0), 1)
cv2.imshow("contours ", img)
cv2.imwrite('8.png', img)

 """
if __name__ == '__main__':

    imgPath = './rawImage.jpg'
    img = cv2.imread(imgPath, cv2.IMREAD_UNCHANGED)
    r,c = fisheyeCircle.getRadiusCenter(img)
    print(r,c)
    img = cv2.circle(img,c,10,(0,0,0),-1)
    text = "center :"+ str(c) + " redius:" +str(r)
    cv2.putText(img, text, c, cv2.FONT_HERSHEY_SIMPLEX,
  1, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imwrite('circle.png', img) 
