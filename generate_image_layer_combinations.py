#Place each type of combination in its own folder
#This progam will make an image combination for each background and image.

from PIL import Image, ImageFilter
from pathlib import Path

def make_merged_image(front_images,back_images,front_back_combinations,padding=0):
    image_width=front_images[-1].width
    image_height=back_images[-1].height

    print("Merging Images")
    max_width=(len(front_images)+1)*(image_width)+(len(front_images)+2)*padding
    max_height=(len(back_images)+1)*(image_height)+(len(back_images)+2)*padding
    print(max_width,max_height)

    merged_image = Image.new('RGB', (max_width, max_height), color=(255, 255, 255))
    blank_background=Image.new('RGBA',(image_width,image_height),color=(255,255,255,1))

    for i in range(len(back_images)):
        back_image_plus_background=Image.alpha_composite(blank_background, back_images[i])
        print(f"Back Image {i}")
        y=(i+1)*(image_height)+(i+2)*padding
        merged_image.paste(back_image_plus_background,(padding,y))

    for j in range(len(front_images)):
        front_image_plus_background=Image.alpha_composite(blank_background, front_images[j])
        print(f"Front Image {j}")
        x=(j+1)*(image_width)+(j+2)*padding
        merged_image.paste(front_image_plus_background,(x,padding))
    merged_image.save("example_output/merged_images/merged_images_part_1.png")

    for i in range(len(front_back_combinations)):
        for j in range(len(front_back_combinations[0])):
            x=(j+1)*(image_width)+(j+2)*padding
            y=(i+1)*(image_height)+(i+2)*padding
            merged_image.paste(front_back_combinations[i][j],(x,y))

    merged_image.save("example_output/merged_images/merged_images_part_2.png")
    print("Done")

def find_absolute_min_sizes(back_images_path,front_images_path):
    min_width=99999
    min_height=99999
    for front_image_file in front_images_path.iterdir():
        front_img=Image.open(str(front_image_file))
        min_width=min(front_img.width,min_width)
        min_height=min(front_img.height,min_height)

    for back_image_file in back_images_path.iterdir():
        back_img=Image.open(str(back_image_file))
        min_width=min(back_img.width,min_width)
        min_height=min(back_img.height,min_height)
    return min_width,min_height

def prepare_image(image_file,min_width,min_height):
    img=Image.open(image_file)
    img=img.resize((min_width,min_height))
    img_RGBA=img.convert("RGBA")
    return img_RGBA

def generate_image_layer_combinations(folder_path:Path,named_output=True):
    print(folder_path,named_output)

    #output_path = Path(__file__).resolve().parent / "output"
    #output_path.mkdir(parents=True, exist_ok=True)

    front_images=[]
    back_images=[]
    front_back_combinations=[]

    back_images_path = Path(f'{folder_path}/back_images')
    front_images_path=Path(f'{folder_path}/front_images')
    min_width,min_height=find_absolute_min_sizes(back_images_path,front_images_path)

    back_image_index=1
    for back_image_file in back_images_path.iterdir():
        front_image_index=1
        front_back_combinations.append([])

        for front_image_file in front_images_path.iterdir():
            try:
                front_img=prepare_image(front_image_file,min_width,min_height)
                back_img=prepare_image(back_image_file,min_width,min_height)

                combined_image=Image.alpha_composite(back_img,front_img)
                front_back_combinations[-1].append(combined_image)

                output_file_name=f"example_output/combinations/front__{front_image_index}_back_{back_image_index}.png"
                if named_output:
                    output_file_name=f"example_output/combinations/{front_image_file.stem}_{back_image_file.stem}.png"
                combined_image.save(output_file_name)
                print(f"Saved {output_file_name}")
            except ValueError:
                print(front_img.size)
                print(back_img.size)
            finally:
                front_image_index+=1
        back_image_index+=1

    for front_image_file in front_images_path.iterdir():
        front_img=prepare_image(front_image_file,min_width,min_height)
        front_images.append(front_img)

    for back_image_file in back_images_path.iterdir():
        back_img=prepare_image(back_image_file,min_width,min_height)
        back_images.append(back_img)
    make_merged_image(front_images,back_images,front_back_combinations)

if __name__=="__main__":
    generate_image_layer_combinations(Path("example_input"))