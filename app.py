from flask import Flask, render_template, send_file, jsonify
import aiohttp
import asyncio
import io
from kandy import generate_image

app = Flask(__name__)

# URL изображения, которое нужно получить
url = "https://loremflickr.com/640/480"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-image')
async def get_image():
    await generate_image("Слон", "image.jpg")
    return send_file(
        "image.jpg",
        mimetype='image/jpeg'
    )
if __name__ == '__main__':
    app.run(debug=True)
