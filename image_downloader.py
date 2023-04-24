import requests

# URL of the image to download
url = 'https://example.com/image.jpg'

# Send a GET request to the URL to download the image
response = requests.get(url)

# Save the image to a file
with open('image.jpg', 'wb') as f:
    f.write(response.content)

print('Image downloaded successfully!')
