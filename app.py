from flask import Flask, render_template, request, url_for
from PIL import Image
import os
from ocr import apply_ocr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def allowed_file(filename):
    print(filename.lower()[filename.find("."):])
    return filename.lower()[filename.find("."):] in {'jpg', 'png', 'jpeg'}

@app.route('/', methods=['POST'])
def upload_image():
    image = request.files['image']
    if 'image' not in request.files:
        return 'No image uploaded.', 400
    elif image.filename == '':
        return 'No image selected', 400
    # elif not allowed_file(image.filename):
    #     return 'Invalid file type', 400
    else:
        filename = 'img.jpg'
        tmp_path = os.path.join('./static/input_images', 'tmp.jpg')
        image.save(tmp_path)
        os.replace(tmp_path, os.path.join('./static/input_images', filename))
    
    # return 'Image uploaded successfully'
    # image = request.files['image']
    # img = Image.open(image)

        import re

        ocr_output = apply_ocr("img.jpg")
        # ocr_array = ocr_output.replace(")", "").split("(")
        result = ""
        error = ""
        for item in ocr_output:
            print(item)
            plate, accuracy = item[0], item[1]
            pattern = re.compile(r"\d{4}[A-Z]{1,3}$")
            if pattern.match(plate):
                print(plate, " + ", accuracy)
                result += f"""
                Se ha detectado la matrícula española <strong>{plate}</strong> 
                con una precisión de <strong>{accuracy}</strong>.\n
                """
            else:
                error = """
                No se han detectado matrículas de España en la foto. 
                El formato esperado es <strong>1234ABC</strong>.
                <p>Repite la foto <u>centrando la matrícula</u> y vuelve a probar.<p>
                """


    # Aquí puedes agregar la función que deseas ejecutar
    # cuando se hace clic en el botón
    return render_template('index.html', image_url=url_for('static', filename='input_images/' + filename), result=result, error=error)
    # return 'Image uploaded.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8081)
