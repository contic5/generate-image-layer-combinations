from PIL import Image

# Open the source images
img1 = Image.open('image1.jpg')
img2 = Image.open('image2.jpg')

# 1. Horizontal Combination (Side-by-Side)
# Calculate the total width and the maximum height
total_width = img1.width + img2.width
max_height = max(img1.height, img2.height)

# Create a blank background image
horizontal_merge = Image.new('RGB', (total_width, max_height), color=(255, 255, 255))

# Paste the images into place
horizontal_merge.paste(img1, (0, 0))
horizontal_merge.paste(img2, (img1.width, 0)) # Offset by the width of the first image

# Save the result
horizontal_merge.save('horizontal_combined.jpg')


# 2. Vertical Combination (Stacked)
total_height = img1.height + img2.height
max_width = max(img1.width, img2.width)

vertical_merge = Image.new('RGB', (max_width, total_height), color=(255, 255, 255))
vertical_merge.paste(img1, (0, 0))
vertical_merge.paste(img2, (0, img1.height)) # Offset by the height of the first image

vertical_merge.save('vertical_combined.jpg')