#Place each type of combination in its own folder
#This progam will make an image combination for each background and image.

from PIL import Image, ImageFilter
from pathlib import Path

def generate_image_layer_combinations(folder_path:Path,named_output=True):
    print(folder_path,named_output)

    front_images=[]
    back_images=[]
    front_back_combinations=[]

    back_images_path = Path(f'{folder_path}/back_images')
    front_images_path=Path(f'{folder_path}/front_images')
    back_image_index=1
    for back_image_file in back_images_path.iterdir():
        front_image_index=1
        front_back_combinations.append([])

        for front_image_file in front_images_path.iterdir():
            try:
                front_img=Image.open(str(front_image_file))
                back_img=Image.open(str(back_image_file))

                min_width=min(front_img.width,back_img.width)
                min_height=min(front_img.height,back_img.height)

                front_img=front_img.resize((min_width,min_height))
                back_img=back_img.resize((min_width,min_height))

                front_img_RGBA=front_img.convert("RGBA")
                back_img_RGBA=back_img.convert("RGBA")
                front_images.append(front_img_RGBA)
                back_images.append(back_img_RGBA)

                combined_image=Image.alpha_composite(back_img_RGBA,front_img_RGBA)
                front_back_combinations.append(combined_image)
                
                output_file_name=f"output/front__{front_image_index}_back_{back_image_index}.png"
                if named_output:
                    output_file_name=f"output/{front_image_file.name}_{back_image_file.name}"
                print(f"Saved {output_file_name}")
                combined_image.save(output_file_name)
            except ValueError:
                print(front_img_RGBA.size)
                print(back_img_RGBA.size)
            finally:
                front_image_index+=1
        back_image_index+=1

if __name__=="__main__":
    generate_image_layer_combinations(Path("input"))