#Place each type of combination in its own folder
#This progam will make an image combination for each background and image.

from PIL import Image, ImageFilter
from pathlib import Path

backgrounds_path = Path('input/backgrounds')
images_path=Path('input/images')

background_index=1
for background_file in backgrounds_path.iterdir():
    image_index=1
    for image_file in images_path.iterdir():
        try:
            img=Image.open(image_file.absolute())
            background=Image.open(background_file.absolute())

            min_width=min(img.width,background.width)
            min_height=min(img.height,background.height)

            img=img.resize((min_width,min_height))
            background=background.resize((min_width,min_height))

            img_RGBA=img.convert("RGBA")
            background_RGBA=background.convert("RGBA")

            combined_image=Image.alpha_composite(background_RGBA,img_RGBA)
            output_file_name=f"output/image_{image_index}_background_{background_index}.png"
            print(f"Saved {output_file_name}")
            combined_image.save(output_file_name)
        except ValueError:
            print(img_RGBA.size)
            print(background_RGBA.size)
        finally:
            image_index+=1
    background_index+=1