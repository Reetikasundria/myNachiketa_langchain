from openai import OpenAI
import os
from dotenv import load_dotenv
from PIL import Image
import requests
from io import BytesIO              

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def generate_images(prompts, output_dir="output/images"):
    os.makedirs(output_dir, exist_ok=True)
    paths = []
    for i, prompt in enumerate(prompts):
        response = client.images.generate(model="dall-e-3",prompt=prompt, n=1, size="1024x1024",quality="standard",response_format="url")
        image_url = response.data[0].url 
        img_data = requests.get(image_url).content
        path = os.path.join(output_dir, f"image_{i+1}.png")
        with open(path, 'wb') as f:
            f.write(img_data)
        paths.append(path)
    return paths
