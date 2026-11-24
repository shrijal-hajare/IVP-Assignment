from PIL import Image

# Open the original image
img = Image.open("image_1.jpg")

# Rotate the image by 90 degrees
rotated_img = img.rotate(90)

# Save the rotated image
rotated_img.save("rotated_image.jpg")

# Display the rotated image
rotated_img.show()

print("Image rotated successfully!")
