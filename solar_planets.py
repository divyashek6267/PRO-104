import cv2

img = cv2.imread("solar-system.jpg")

cv2.imshow("output",img)

cv2.putText(img,"Sun",(80,90),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255))

cv2.putText(img,"Mercury",(130,200),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255))

cv2.putText(img,"Venus",(210,200),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255))

cv2.putText(img,"Earth",(290,180),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255))

cv2.putText(img,"Mars",(370,180),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255))

cv2.putText(img,"Jupiter",(560,150),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255))

cv2.putText(img,"Saturn",(730,150),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255))

cv2.putText(img,"Uranus",(940,150),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255))

cv2.putText(img,"Neptune",(1100,150),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255))




cv2.imwrite('Solar_systemwithname.jpg',img)

cv2.waitKey(0)
