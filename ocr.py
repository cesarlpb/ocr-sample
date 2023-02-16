#%% Importing required methods for inference and visualization.
from paddleocr import PaddleOCR,draw_ocr

#%% Importing required libraries.
import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
# matplotlib inline

#%% Initializing OCR, OCR will automatically download PP-OCRv3 detector, recognizer and angle classifier.
ocr = PaddleOCR(use_angle_cls=True)

# Specifying output path and font path.
out_path = './static/output_images'
# font = './simfang.ttf'

# Applying OCR
img_path = './static/input_images/img.jpg'
result = ocr.ocr(img_path)

#%% Function to plot and save the results.
def save_ocr(img_path, out_path, result, font):
  save_path = os.path.join(out_path, img_path.split('/')[-1].split('.')[0] + '-output.jpg')

  image = cv2.imread(img_path)

  # Extracting boxes, texts and its score from the output list.
  
  boxes = [line[0] for line in result[0]]
#   print(boxes)
  txts = [str(line[1][0]) for line in result[0]]
  scores = [line[1][1] for line in result[0]]
  
  # Plotting the outputs using PaddleOCR in-built function.
  im_show = draw_ocr(image, boxes, txts, scores, font_path=font)
  
  # Saving and displaying the output.
  cv2.imwrite(save_path, im_show)

  img = cv2.cvtColor(im_show, cv2.COLOR_BGR2RGB)
  img_large = cv2.resize(img, dsize=(500, 500), interpolation=cv2.INTER_CUBIC)
  plt.imshow(img)

def apply_ocr(filename="test.jpg"):

    # Cargamos la imagen
    image = cv2.imread(img_path)

    # Convertimos la imagen a formato RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Llamamos al método ocr.ocr()
    result = ocr.ocr(image)
    # print("len:",len(result))

    #%%
    str_ = ""
    for el in result[0]:
        print(el[1])
        str_ += f"{el[1]}\n\n"
    return str_

# str_result = apply_ocr()
# print(str_result)