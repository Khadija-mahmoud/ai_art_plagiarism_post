import os
import re
from PIL import Image

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def modify_image_tags(markdown_content, desired_width=600):
    img_pattern = r'<img src="(.*?)" alt="(.*?)" width="(\d+)" height="(\d+)">'

    def modify_image_tag(match):
        img_src, alt_text, _, img_height = match.groups()
        return f'<img src="{img_src}" alt="{alt_text}" width="{desired_width}" height="{img_height}">'

    return re.sub(img_pattern, modify_image_tag, markdown_content)

def resize_images(markdown_content, input_md_file, output_md_file, img_width=600):
    img_pattern = r'!\[.*?\]\((.*?)\)'
    img_links = re.findall(img_pattern, markdown_content)

    resized_image_dir = 'resized_images'
    os.makedirs(resized_image_dir, exist_ok=True)

    for img_link in img_links:
        try:
            img_path = os.path.join(os.path.dirname(input_md_file), img_link)
            with Image.open(img_path) as img:
                img_height = int(img.height * img_width / img.width)
                resized_img = img.resize((img_width, img_height), Image.ANTIALIAS)

            resized_img_path = os.path.join(resized_image_dir, os.path.basename(img_path))
            resized_img.save(resized_img_path)

            markdown_content = markdown_content.replace(img_link, os.path.relpath(resized_img_path, os.path.dirname(output_md_file)))

        except Exception as e:
            print(f"Error processing image '{img_link}': {str(e)}")

    return markdown_content

if __name__ == '__main__':
    input_md_file = r'C:\Users\khadija\PycharmProjects\ai_art_plagiarism_post\Part_1.md'
    output_md_file = input_md_file

    # Read Markdown file
    markdown_content = read_file(input_md_file)

    # Modify image tags
    modified_content = modify_image_tags(markdown_content, desired_width=600)

    # Resize images
    final_content = resize_images(modified_content, input_md_file, output_md_file, img_width=600)

    # Write the final content to the output file
    write_file(output_md_file, final_content)
