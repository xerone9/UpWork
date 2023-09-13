import requests


def main():
    def download_image(image):
        image_url = "https://logo.clearbit.com/" + image + ".com"  # Replace with the actual image URL

        response = requests.get(image_url)

        if response.status_code == 200:
            image_data = response.content

            local_path = "brand images/" + image + ".png"  # Replace with your desired local path

            # Write the image data to a local file
            with open(local_path, "wb") as file:
                file.write(image_data)
            print("Image downloaded and saved as", local_path)
        else:
            print("Failed to download image. Status code:", response.status_code)

    with open("brand images/company_names.txt", "r") as file:
        content = file.read().split("\n")
        for logo in content:
            download_image(logo)

































if __name__ == "__main__":
    main()