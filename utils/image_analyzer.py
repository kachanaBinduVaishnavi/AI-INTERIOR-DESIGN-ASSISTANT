import requests
import base64

def analyze_room(image_path, room_type, style, budget):


    # Read the image
    with open(image_path, "rb") as image_file:
        image_data = base64.b64encode(
            image_file.read()
        ).decode("utf-8")


    # Prompt for the AI
    prompt = f"""


    You are an AI interior design assistant.

    Carefully analyze the uploaded room image.

    User selections:

    Room Type: {room_type}
    Interior Style: {style}
    Budget: ₹{budget}

    IMPORTANT IMAGE ANALYSIS RULES:

    * Only describe objects that are clearly visible in the image.
    * Never invent furniture, windows, doors, decorations, colors, or other objects.
    * If something is unclear, say "Not clearly visible in the image."
    * First identify what is actually visible before giving suggestions.
    * If the selected room type does not match the image, clearly mention the mismatch.
    * Suggestions should be practical and suitable for the selected room type, style, and budget.
    * Do not use Markdown formatting.
    * Do not use asterisks.
    * Do not use backslash characters.
    * Start each bullet point with a normal hyphen (-).

    Use exactly these headings:

    1. Room Observations
    2. Existing Furniture
    3. Colors and Lighting
    4. Layout Observations
    5. Problems or Areas That Can Be Improved
    6. Practical Interior Design Suggestions
    7. Furniture and Decor Suggestions
    8. Suggestions That Fit the User's Budget

    Under each heading, provide 3 to 5 short bullet points.
    """


    # Send image and prompt to local Ollama
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llava",
            "prompt": prompt,
            "images": [image_data],
            "stream": False
        }
    )


    # Check for errors
    if response.status_code != 200:
        return "Error connecting to Ollama: " + response.text


    # Get AI response
    result = response.json()

    ai_response = result["response"]
    # Clean unwanted Markdown escape characters
    ai_response = ai_response.replace("\\.", ".")
    ai_response = ai_response.replace("\\-", "-")
    ai_response = ai_response.replace("\\*", "")
    ai_response = ai_response.replace("\\", "")
    ai_response = ai_response.replace("*", "")
    return ai_response

