import os
import io

from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

def generate_design_image(image_path, room_type, style, budget):

    
    if not HF_TOKEN:
        return None, "Hugging Face token not found."

    prompt = f"""
    

    Edit this existing {room_type} room into a realistic {style} interior design.

    Keep the original room structure, walls, floor, windows, doors and camera
    perspective as much as possible.

    Improve the furniture arrangement, colors, lighting and decorations.

    The available budget is ₹{budget}.

    The result should look like a realistic photograph of the same room after
    interior redesign.

    Do not change the room type.
    Do not make major architectural changes.
    """

    
    try:

        client = InferenceClient(
            provider="fal-ai",
            api_key=HF_TOKEN,
        )

        with open(image_path, "rb") as image_file:
            input_image = image_file.read()

        edited_image = client.image_to_image(
            input_image,
            prompt=prompt,
            model="Qwen/Qwen-Image-Edit",
        )

        output_folder = "static/generated"

        os.makedirs(
            output_folder,
            exist_ok=True
        )

        output_filename = "redesigned_room.png"

        output_path = os.path.join(
            output_folder,
            output_filename
        )

        edited_image.save(output_path)

        return output_filename, None

    except Exception as error:

        return None, str(error)

