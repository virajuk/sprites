import cv2

image = cv2.imread("graphics/man_with_axe_ass.png")
print(image.shape)

for idx in range(7):
    cropped_image = image[0:64, idx*64:(idx+1)*64]
    print(cropped_image.shape)

    cv2.imwrite(f"graphics/sprites/{idx}.png", cropped_image)
