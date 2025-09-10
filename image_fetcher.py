import requests
import os
from urllib.parse import urlparse

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Prompt user for URL
    image_url = input("Please enter the image URL: ").strip()

    # Create directory if it doesn't exist
    folder_name = "Fetched_Images"
    os.makedirs(folder_name, exist_ok=True)

    try:
        # Fetch the image
        response = requests.get(image_url, stream=True)
        response.raise_for_status()  # Check for HTTP errors

        # Extract filename from URL
        parsed_url = urlparse(image_url)
        filename = os.path.basename(parsed_url.path)

        # If filename is empty, generate one
        if not filename:
            filename = "downloaded_image.jpg"

        file_path = os.path.join(folder_name, filename)

        # Save the image in binary mode
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {file_path}\n")

    except requests.exceptions.RequestException as e:
        print(f"✗ Failed to fetch the image. Error: {e}")

    print("Connection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
