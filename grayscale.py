from PIL import Image

# Read the input image
img = Image.open("image_1.jpg")

# Convert colour image into grayscale
gray_image = img.convert("L")

# Save the grayscale image
gray_image.save("greyimage.jpg")

# Display the converted image
gray_image.show()

print("Image converted into grayscale successfully!")
