from PIL import Image

background = Image.open('canvas.jpg')
overlay = Image.open('logo.png').convert('RGBA') # Smaller image

# Define top-left coordinates where the overlay should go (x, y)
position = (50, 100)

# Paste overlay. Passing 'overlay' as the third argument handles transparency masking
background.paste(overlay, position, overlay)

background.save('overlay_output.jpg')