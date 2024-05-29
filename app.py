from flask import Flask, render_template, send_file, jsonify
import aiohttp
import asyncio
import io

app = Flask(__name__)

# URL изображения, которое нужно получить
url = "https://loremflickr.com/640/480"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-image')
async def get_image():
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                image_data = await response.read()
                return send_file(
                    io.BytesIO(image_data),
                    mimetype='image/jpeg',
                    as_attachment=False,
                    attachment_filename='image.jpg'
                )
            else:
                return jsonify({'error': 'Failed to retrieve image'}), 500

if __name__ == '__main__':
    app.run(debug=True)