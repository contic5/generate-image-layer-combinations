#Place each type of combination in its own folder
#This progam will make an image combination for each background and image.

from PIL import Image, ImageFilter
from pathlib import Path

def generate_image_layer_combinations(folder_path:Path,named_output=True):
    print(folder_path)

    backgrounds_path = Path(f'{folder_path}/backgrounds')
    images_path=Path(f'{folder_path}/images')
    background_index=1
    for background_file in backgrounds_path.iterdir():
        image_index=1
        for image_file in images_path.iterdir():
            try:
                img=Image.open(str(image_file))
                background=Image.open(str(background_file))

                min_width=min(img.width,background.width)
                min_height=min(img.height,background.height)

                img=img.resize((min_width,min_height))
                background=background.resize((min_width,min_height))

                img_RGBA=img.convert("RGBA")
                background_RGBA=background.convert("RGBA")

                combined_image=Image.alpha_composite(background_RGBA,img_RGBA)
                output_file_name=f"output/image_{image_index}_background_{background_index}.png"
                if named_output:
                    output_file_name=f"output/{image_file.name}_{background_file.name}"
                print(f"Saved {output_file_name}")
                combined_image.save(output_file_name)
            except ValueError:
                print(img_RGBA.size)
                print(background_RGBA.size)
            finally:
                image_index+=1
        background_index+=1

if __name__=="__main__":
    generate_image_layer_combinations(Path("input"))