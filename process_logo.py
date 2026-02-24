import sys
from rembg import remove
from PIL import Image
import io
import os

def process_logo(input_path, output_path):
    print(f"Processing {input_path}...")
    with open(input_path, 'rb') as i:
        input_data = i.read()
    
    # 배경 제거
    output_data = remove(input_data)
    
    # 여백 트리밍
    img = Image.open(io.BytesIO(output_data)).convert("RGBA")
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)
    
    # 저장
    img.save(output_path, "PNG")
    print(f"Saved to {output_path}")

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_dir, "assets", "raw_logo.png")
    output_file = os.path.join(current_dir, "assets", "logo_transparent.png")
    
    if os.path.exists(input_file):
        process_logo(input_file, output_file)
    else:
        print(f"Error: {input_file} not found")
