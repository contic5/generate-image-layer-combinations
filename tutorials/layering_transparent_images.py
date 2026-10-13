from PIL import Image

# Open images and ensure they are in RGBA mode for transparency
base_layer = Image.open('background.png').convert('RGBA')
top_layer = Image.open('character.png').convert('RGBA')

# Optional: Resize top layer to match the base layer if they differ
if base_layer.size != top_layer.size:
    top_layer = top_layer.resize(base_layer.size)

# Composite them together
combined_layers = Image.alpha_composite(base_layer, top_layer)

# Save as PNG to preserve transparency, or convert to RGB to save as JPEG
combined_layers.save('layered_output.png')