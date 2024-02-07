#import dependencies
import os
import re

from PIL import Image

def modify_image_tags_in_markdown(input_md_file, output_md_file, desired_width=600):
    # Read the Markdown file  # Validate input file paths
    with open(input_md_file, 'r', encoding='utf-8') as md_file:
        markdown_content = md_file.read()

    # Define a regular expression pattern to match image tags in Markdown
    img_pattern = r'<img src="(.*?)" alt="(.*?)" width="(\d+)" height="(\d+)">'

    def modify_image_tag(match):
        img_src = match.group(1)
        alt_text = match.group(2)
        img_width = match.group(3)
        img_height = match.group(4)

        # Update the width attribute to the desired width
        updated_img_tag = f'<img src="{img_src}" alt="{alt_text}" width="{desired_width}" height="{img_height}">'

        return updated_img_tag

    # Modify image tags using the defined function
    modified_markdown_content = re.sub(img_pattern, modify_image_tag, markdown_content)

    # Write the modified Markdown content to the output file
    with open(output_md_file, 'w', encoding='utf-8') as output_file:
        output_file.write(modified_markdown_content)

def resize_images_in_markdown(input_md_file, output_md_file, img_width = 600):
    # Read the Markdown file
    with open(input_md_file, 'r', encoding='utf-8') as md_file:
        markdown_content = md_file.read()

    # Define a regular expression pattern to match image links in Markdown
    img_pattern = r'!\[.*?\]\((.*?)\)'
    img_links = re.findall(img_pattern, markdown_content)

    # Create a directory to store resized images
    resized_image_dir = 'resized_images'
    os.makedirs(resized_image_dir, exist_ok=True)

    # Process each image link
    for img_link in img_links:
        try:
            # Open and resize the image
            img_path = os.path.join(os.path.dirname(input_md_file), img_link)
            img = Image.open(img_path)
           # img_width = 600
            img_height = int(img_height * img_width / img.width)
            img = img.resize((img_width, img_height), Image.ANTIALIAS)

            # Save the resized image to the output directory
            resized_img_path = os.path.join(resized_image_dir, os.path.basename(img_path))
            img.save(resized_img_path)

            # Replace the original image link with the resized image link
            markdown_content = markdown_content.replace(img_link, os.path.relpath(resized_img_path,
                                                                                  os.path.dirname(output_md_file)))

        except Exception as e:
            print(f"Error processing image '{img_link}': {str(e)}")

    # Write the modified Markdown content to the output file
    with open(output_md_file, 'w', encoding='utf-8') as output_file:
        output_file.write(markdown_content)


if __name__ == '__main__':
    input_md_file = r'C:\Users\khadija\PycharmProjects\ai_art_plagiarism_post\Part_1.md'  # Replace with the path to your input Markdown file
    output_md_file = input_md_file # 'output.md'  # Replace with the desired output Markdown file

    #resize_images_in_markdown(input_md_file, output_md_file, img_width = 10)
    modify_image_tags_in_markdown(input_md_file, output_md_file, desired_width= 600)
