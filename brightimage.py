from PIL import Image, ImageEnhance

# Open the original dark image
img = Image.open("image_1.jpg")

# Increase image brightness
enhancer = ImageEnhance.Brightness(img)
bright_image = enhancer.enhance(1.8)

# Save the bright image
bright_image.save("bright_image.jpg")

# Display original and bright images
img.show()
bright_image.show()

print("Dark image converted into bright image successfully!")
