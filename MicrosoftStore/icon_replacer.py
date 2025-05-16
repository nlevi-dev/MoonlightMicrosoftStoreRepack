import os
from PIL import Image

def resize_and_overlay(template_path, folder_path):
    # Load the template image
    template = Image.open(template_path).convert("RGBA")
    background_color = template.getpixel((0, 0))

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".png"):
            filepath = os.path.join(folder_path, filename)
            
            # Open the target image
            target = Image.open(filepath).convert("RGBA")
            target_size = target.size

            # Resize the template to fit target while preserving aspect ratio
            template_ratio = template.width / template.height
            target_ratio = target_size[0] / target_size[1]

            if template_ratio > target_ratio:
                # Fit to width
                new_width = target_size[0]
                new_height = int(new_width / template_ratio)
            else:
                # Fit to height
                new_height = target_size[1]
                new_width = int(new_height * template_ratio)

            resized_template = template.resize((new_width, new_height), Image.LANCZOS)

            # Create background image with the color from (0, 0)
            background = Image.new("RGBA", target_size, background_color)

            # Paste resized template onto background, centered
            x = (target_size[0] - new_width) // 2
            y = (target_size[1] - new_height) // 2
            background.paste(resized_template, (x, y), resized_template)

            # Save result (overwrite original)
            background.save(filepath)

resize_and_overlay("moonlight_ms300.png", "unpack/Assets")