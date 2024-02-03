from google.cloud import vision_v1


# Create a Vision client with service account credentials
client = vision_v1.ImageAnnotatorClient.from_service_account_file('serviceAccountToken.json')

print(client)


def extract_text_from_image(image_path):
    # Open the image using Pillow
    with open(image_path, 'rb') as image_file:
        content = image_file.read()

    # Use Vision API to perform OCR on the image
    image = vision_v1.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    # Print the extracted text
    for text in texts:
        print(text.description)

# Example usage
image_path = 'kk.png'
extract_text_from_image(image_path)