from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from helpers import load_image, save_image, allowed_file
from histogram_match import match_histograms
from style_transfer import apply_style_transfer

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'
PROCESSED_FOLDER = 'static/processed/'

# Ensure folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "content" not in request.files or "style" not in request.files:
            return "Missing files", 400

        content_file = request.files["content"]
        style_file = request.files["style"]

        if not (content_file and allowed_file(content_file.filename) and 
                style_file and allowed_file(style_file.filename)):
            return "Invalid file type", 400

        content_path = os.path.join(UPLOAD_FOLDER, content_file.filename)
        style_path = os.path.join(UPLOAD_FOLDER, style_file.filename)

        content_file.save(content_path)
        style_file.save(style_path)

        content_img = load_image(content_path)
        style_img = load_image(style_path)

        processed_img = match_histograms(content_img, style_img)

        output_path = os.path.join(PROCESSED_FOLDER, "processed.jpg")
        save_image(processed_img, output_path)

        return redirect(url_for("processed", filename="processed.jpg"))

    return render_template("index.html")

@app.route("/processed/<filename>")
def processed(filename):
    return send_from_directory(PROCESSED_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)
