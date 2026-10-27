from flask import Flask, render_template, request
import os

from utils.image_analyzer import analyze_room
from utils.database import create_database, save_design, get_designs

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create upload folder if it does not exist

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():

    image = request.files.get("room_image")

    room_type = request.form.get("room_type")
    style = request.form.get("style")
    budget = request.form.get("budget")


        # Check if an image was uploaded
    if not image or image.filename == "":
        return "No image uploaded."


        # Save uploaded image
    image_path = os.path.join(
    app.config["UPLOAD_FOLDER"],
    image.filename
    )

    image.save(image_path)


        # Analyze the room using local Ollama + LLaVA
    ai_result = analyze_room(
    image_path,
    room_type,
    style,
    budget
    )


        # Save the design analysis to SQLite database
    save_design(
        image.filename,
        room_type,
        style,
        budget,
        ai_result
    )


        # Display the result page
    return render_template(
        "result.html",
        image_filename=image.filename,
        room_type=room_type,
        style=style,
        budget=budget,
        ai_result=ai_result
    )
@app.route("/generate-design", methods=["POST"])
def generate_design():

    image_filename = request.form.get("image_filename")
    room_type = request.form.get("room_type")
    style = request.form.get("style")
    budget = request.form.get("budget")


    return render_template(
         "result.html",
        image_filename=image_filename,
        room_type=room_type,
        style=style,
        budget=budget,
        ai_result="Design image generation will be connected in the next step."
        )

@app.route("/history")
def history():

                # Get all previous design analyses from database
    designs = get_designs()


                # Display design history page
    return render_template(
        "history.html",
        designs=designs
    )

    if __name__ == "__main__":

                # Create database and table
        create_database()
app.run(debug=True)

