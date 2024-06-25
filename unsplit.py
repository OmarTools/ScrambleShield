from PIL import Image
import os
import math

def reconstruct_image(part_info_file, output_dir):
    # Read the part information from the text file
    with open(part_info_file, 'r') as info_file:
        part_info = info_file.readlines()

    # Get the first part filename and rotation from the part information
    first_part_info = part_info[0].strip()
    part_filename, position_info, rotation_info = first_part_info.split(',')
    position = tuple(map(int, position_info.split('_')))
    rotation = int(rotation_info.split(':')[1][:-1])  # Fix to remove ')' from the rotation value
    part_filename = part_filename.strip('(')  # Fix to remove '(' from the filename

    # Open the first part image
    part_path = os.path.join(output_dir, part_filename)
    part_image = Image.open(part_path)

    # Rotate the first part image
    rotated_part = part_image.rotate(-rotation, expand=True)

    # Calculate the dimensions of the rotated part
    part_width, part_height = rotated_part.size

    # Calculate the dimensions of the reconstructed image
    image_width = part_width * (len(part_info)//int(math.sqrt(len(part_info))))
    image_height = part_height * (len(part_info)//int(math.sqrt(len(part_info))))

    # Create a new blank image for reconstruction
    reconstructed_image = Image.new('RGB', (image_width, image_height))

    # Iterate over the part positions and paste the rotated part onto the reconstructed image
    for info in part_info:
        info = info.strip()
        part_filename, position_info, rotation_info = info.split(',')
        position = tuple(map(int, position_info.split('_')))
        rotation = int(rotation_info.split(':')[1][:-1])  # Fix to remove ')' from the rotation value
        part_filename = part_filename.strip('(')  # Fix to remove '(' from the filename

        # Open the part image
        part_path = os.path.join(output_dir, part_filename)
        part_image = Image.open(part_path)

        # Rotate the part
        rotated_part = part_image.rotate(-rotation, expand=True)

        # Calculate the coordinates for pasting the part onto the reconstructed image
        left = position[1] * part_width
        upper = position[0] * part_height
        right = left + part_width
        lower = upper + part_height

        # Paste the rotated part onto the reconstructed image
        reconstructed_image.paste(rotated_part, (left, upper, right, lower))

    # Save the reconstructed image
    reconstructed_image.save(os.path.join(output_dir, 'reconstructed_image.jpg'))

    # Calculate the original size of the image after rotating the parts
    original_width = image_width
    original_height = image_height

    return original_width, original_height


part_info_file = 'C:\\Users\\youruser\\Downloads\\New folder\\part_info.txt'
output_dir = 'C:\\Users\\\youruser\\Downloads\\New folder'

original_width, original_height = reconstruct_image(part_info_file, output_dir)
print(f"The original size of the image after rotating the parts is {original_width} x {original_height}.")