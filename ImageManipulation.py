import cv2

image = cv2.imread(r"C:\Users\user\Desktop\After class projects\Enhanced Chatbot\All of them\ProjectMaterial.jpg")

grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite(r"C:\Users\user\Desktop\After class projects\Enhanced Chatbot\All of them\gray.jpg", grayscale_image)

Cropped_image=image[100:300,200:500]
cv2.imwrite(r"C:\Users\user\Desktop\After class projects\Enhanced Chatbot\All of them\Cropped.jpg",Cropped_image)

Rotated_image=cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite(r"C:\Users\user\Desktop\After class projects\Enhanced Chatbot\All of them\Rotated.jpg",Rotated_image)

Bright_image=cv2.convertScaleAbs(image,alpha=1,beta=25)
cv2.imwrite(r"C:\Users\user\Desktop\After class projects\Enhanced Chatbot\All of them\Brighter.jpg",Bright_image)


cv2.imshow("GrayScale image",grayscale_image)
cv2.imshow("CroppedImage",Cropped_image)
cv2.imshow("Rotated image",Rotated_image)
cv2.imshow("Bright image",Bright_image)
cv2.waitKey(0)
cv2.destroyAllWindows()



