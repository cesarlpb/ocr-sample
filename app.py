from flask import Flask, render_template, request
from PIL import Image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return 'No image uploaded.', 400

    image = request.files['image']
    img = Image.open(image)

    # Aquí puedes agregar la función que deseas ejecutar
    # cuando se hace clic en el botón

    return 'Image uploaded.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
