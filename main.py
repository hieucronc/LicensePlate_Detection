import cv2
from ultralytics import YOLO
import easyocr
import matplotlib.pyplot as plt

model = YOLO('/content/best.pt')  # Load the trained model
input_image_path = '/content/0000_08244_b.jpg'

# Function to detect the license plate and crop it from the image
def getLicensePlate(imgPath):
    # Load the image
    image = cv2.imread(imgPath)
    if image is None:
        print(f"Could not read image {imgPath}")
        return None

    # Detect objects in the image
    results = model(image)

    # Extract bounding boxes and crop the license plate
    detections = results[0].boxes.xyxy
    if len(detections) > 0:
        bbox = detections[0]  # only one object is detected
        x1, y1, x2, y2 = map(int, bbox[:4])
        cropped_image = image[y1:y2, x1:x2]  # Crop the license plate
        return cropped_image
    else:
        print("No license plate detected.")
        return None

def display(image):
    if image is None:
        print("No image to display")
        return
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.axis('off')
    plt.show()

def extractText(image):
    reader = easyocr.Reader(['en'])
    results = reader.readtext(image)
    return results


LP = getLicensePlate(input_image_path)

if LP is not None:
    # Display the cropped image
    display(LP)

    # Extract text from the cropped image
    ocrText = extractText(LP)

    # for (bbox, text, prob) in text:
    #     print(f"Detected text: {text} (Confidence: {prob:.2f})")
    lp_text = " ".join([text for (bbox, text, prob) in ocrText])
    print(f"License plate: {lp_text}")
