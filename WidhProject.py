import cv2
image=cv2.imread(r"C:\Users\user\Desktop\After class projects\Enhanced Chatbot\Image_Width_Annotaion_Project.py\Waterfall.jpg")

height, width = image.shape[:2]

# Position for arrows
y = height // 2

# Left arrow pointing right
cv2.arrowedLine(image, (0, y), (width//2, y), (0, 255, 0), 2)

# Right arrow pointing left
cv2.arrowedLine(image, (width, y), (width//2, y), (0, 255, 0), 2)

# Width text at midpoint
text = f"Width = {width} px"
cv2.putText(image, text, (width//2 - 100, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

# Save output
cv2.imwrite("Annotatedimage.jpg", image)