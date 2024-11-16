import cv2
import numpy as np
import base64

def resize_and_apply_colormap(row):
    image = np.array(row[1:]).reshape(1, -1).astype(np.uint8)
    resized_image = cv2.resize(image, (150, 1), interpolation=cv2.INTER_CUBIC)
    colored_image = cv2.applyColorMap(resized_image, cv2.COLORMAP_JET)
    
    _, buffer = cv2.imencode('.jpg', colored_image)
    image_bytes = buffer.tobytes()
    base64_string = base64.b64encode(image_bytes).decode('utf-8')

    return base64_string, colored_image.shape
