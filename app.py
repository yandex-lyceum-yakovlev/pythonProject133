from flask import Flask, render_template, send_file, jsonify
import aiohttp
import asyncio
import io
from kandy import generate_image

app = Flask(__name__)

# URL изображения, которое нужно получить
# url = "https://loremflickr.com/640/480"

images = [1, 2, 3]
@app.route('/')
def index():
    return render_template('index.html', images=images)

candies = {'1': "Ворона",
           '2': "Лисица",
           '3': "Сыр"}

@app.route('/get-image/<img_id>')
async def get_image(img_id):
    await generate_image(candies[img_id], f"{img_id}.jpg")
    return send_file(
        f"{img_id}.jpg",
        mimetype='image/jpeg'
    )
if __name__ == '__main__':
    app.run(debug=True)
