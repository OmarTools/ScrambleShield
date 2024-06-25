from PIL import Image
import os
import random
import string

def generate_random_name(length):
    # Generate a random string of uppercase letters and digits
    letters_and_digits = string.ascii_uppercase + string.digits
    random_name = ''.join(random.choice(letters_and_digits) for _ in range(length))
    return random_name

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

    # Split the image into parts
    parts = []
    with open(os.path.join(output_dir, 'part_info.txt'), 'w') as info_file:
        for i in range(num_parts):
            for j in range(num_parts):
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
                random_name = generate_random_name(8)
                part_filename = f'{random_name}.jpg'

                # Save the part as a separate image file
                part_path = os.path.join(output_dir, part_filename)
                part.save(part_path)

         
                parts.append(part_path)

                # Write part information to the text file
                info = f'({part_filename},{i}_{j},rotation:{rotation_degrees})\n'
                info_file.write(info)

    return parts


image_path = 'dcr.jpeg'
num_parts = 20
output_dir = 'C:\\Users\\username\\folder'

image_parts = split_image(image_path, num_parts, output_dir)
