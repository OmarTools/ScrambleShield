from PIL import Image
import os
import random
import string
import multiprocessing

def generate_random_names(length, num_names):
    # Generate a list of random strings of uppercase letters and digits
    letters_and_digits = string.ascii_uppercase + string.digits
    random_names = []
    for _ in range(num_names):
        random_name = ''.join(random.choice(letters_and_digits) for _ in range(length))
        random_names.append(random_name)
    return random_names

def process_part(image, part_index, i, j, part_width, part_height, output_dir, random_names):
    # Calculate the starting and ending coordinates for each part
    left = j * part_width
    upper = i * part_height
    right = (j + 1) * part_width
    lower = (i + 1) * part_height

    # Extract the part from the image
    part = image.crop((left, upper, right, lower))

    # Randomly rotate the part
    rotation_degrees = random.choice([0, 90, 180, 270])
    part = part.rotate(rotation_degrees, expand=True)

    # Generate a random name for the part
    random_name = random_names[part_index]
    part_filename = f'{random_name}.jpg'

    # Save the part in memory
    part_path = os.path.join(output_dir, part_filename)
    part.save(part_path)

    # Return part information
    return part_path, f'({part_filename},{i}_{j},rotation:{rotation_degrees})\n'

def split_image(image_path, num_parts, output_dir):
    # Open the image
    image = Image.open(image_path)

    # Get the dimensions of the image
    width, height = image.size

    # Calculate the size of each part
    part_width = width // num_parts
    part_height = height // num_parts

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Generate random names for the parts
    random_names = generate_random_names(8, num_parts * num_parts)

    # Split the image into parts
    parts = []
    part_info = []
    if __name__ == '__main__':
        with multiprocessing.Pool() as pool:
            results = []
            for i in range(num_parts):
                for j in range(num_parts):
                    part_index = i * num_parts + j
                    results.append(pool.apply_async(process_part, (image, part_index, i, j, part_width, part_height, output_dir, random_names)))

            for result in results:
                part_path, info = result.get()
                parts.append(part_path)
                part_info.append(info)

    # Write part information to the text file
    with open(os.path.join(output_dir, 'part_info.txt'), 'w') as info_file:
        info_file.writelines(part_info)

    return parts


image_path = 'dcr.jpeg'
num_parts = 20
output_dir = 'C:\\Users\\youruser\\Downloads\\'

if __name__ == '__main__':
    image_parts = split_image(image_path, num_parts, output_dir)