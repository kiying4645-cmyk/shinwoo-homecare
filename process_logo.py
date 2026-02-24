from rembg import remove
from PIL import Image
import io
import os

def process_logo(input_path, output_path):
    print(f"Processing {input_path}...")
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found")
        return

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
    print(f"Successfully saved to {output_path}")

if __name__ == "__main__":
    # 프로젝트 루트의 assets 폴더와 현재 작업 경로를 고려하여 경로 설정
    input_file = "assets/logo.png"
    output_file = "assets/logo_transparent.png"
    
    process_logo(input_file, output_file)
