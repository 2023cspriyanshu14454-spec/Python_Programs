from PIL import Image   # ✔ Correct import

# Enter image path
image_path = input("Enter the image file path: ")   # ✔ Correct input

try:
    # Open the image
    img = Image.open(image_path)   # ✔ Correct method
    
    # Get resolution
    width, height = img.size   # ✔ Correct way to get resolution
    
    print("Image Resolution:")
    print("Width:", width, "pixels")
    print("Height:", height, "pixels")
    print("Resolution:", width, "x", height)

except FileNotFoundError:   # ✔ Correct error handling
    print("Error: Image file not found.")
except Exception as e:      # ✔ Good practice
    print("Error:", e)
