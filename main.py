import re


def extract_image_links(html_text):
    img_pattern = r'<img [^>]*src=["\'](https?://[a-zA-Z0-9./_-]+\.(?:jpg|jpeg|png|gif))["\']'

    image_links = re.findall(img_pattern, html_text, re.IGNORECASE)

    return image_links


if __name__ == '__main__':
    sample_html = ("<img src='https://example.com/image1.jpg'> "
                   "<img src='http://example.com/image2.png'> "
                   "<img src='https://example.com/image3.gif'>")

    image_links = extract_image_links(sample_html)
    if image_links:
        for image_link in image_links:
            print(image_link)
    else:
        print("Нет ссылок с картинками в HTML тексте.")
