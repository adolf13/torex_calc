from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import inch, mm
from reportlab.lib.utils import ImageReader
import os


def png_to_pdf_with_images_and_text(png_filepath, pdf_filepath, top_text, pagesize=letter):
    """
    Adds images and multiline text to a PNG and converts to PDF.  Handles scaling and placement.

    Args:
        png_filepath: Path to input PNG.
        pdf_filepath: Path to output PDF.
        top_text: Multiline text for top (list of strings).
        bottom_text: Multiline text for bottom (list of strings).
        torex_filepath: Path to the image to add to the top left.
        font_size: Font size.
        pagesize: ReportLab pagesize.
    """

    #png_filepath = 'C:\\Users\\mas13\\PycharmProjects\\Torex_calc\\client\\out_pic.jpg'
    print(png_filepath)
    bottom_text = ["Подпись заказчика        ______________________________", ""]
    torex_filepath = "torex.jpg"
    font_size = 40
    try:
        img = Image.open(png_filepath)
        img_width, img_height = img.size

        try:
            font = ImageFont.truetype("CeraPro-Light.ttf", font_size)
        except IOError:
            font = ImageFont.load_default()
            print("Warning: Arial font not found. Using default font.")

        text_height_per_line = 35  # font.getsize("A")[1]
        top_text_height = len(top_text) * text_height_per_line + 5
        bottom_text_height = len(bottom_text) * text_height_per_line + 5
        total_text_height = top_text_height + bottom_text_height

        # Load and resize the torex image (adjust max_size as needed)
        torex_img = Image.open(torex_filepath)
        max_size = (400, 400)  # Adjust the maximum size of the torex image
        torex_img.thumbnail(max_size)

        # Create a new image with space for all elements
        new_width = img_width + torex_img.width + 10  # 10px spacing
        new_height = max(img_height + total_text_height, torex_img.height + top_text_height + bottom_text_height)
        new_img = Image.new("RGB", (new_width, new_height), "white")

        # Paste torex image
        new_img.paste(torex_img, (1600, 0))  # 10px padding

        # Paste the main image
        new_img.paste(img, (torex_img.width, top_text_height))  # 20px padding

        draw = ImageDraw.Draw(new_img)

        # Draw top text
        y_offset = 0
        for line in top_text:
            draw.text((torex_img.width, y_offset), line, font=font, fill="black")  # Add padding
            y_offset += text_height_per_line

        # Draw bottom text
        y_offset = top_text_height + img_height
        for line in bottom_text:
            draw.text((torex_img.width, y_offset + 30), line, font=font, fill="black")  # Add padding
            y_offset += text_height_per_line

        new_img.save("temp_image.png")

        page_width, page_height = pagesize
        aspect_ratio = img_width / img_height
        scaled_width = min(page_width, new_width)
        scaled_height = scaled_width * new_height / new_width

        c = canvas.Canvas(pdf_filepath, pagesize=pagesize)
        c.drawImage(ImageReader("temp_image.png"), (page_width - scaled_width) / 2 - 70,
                    (page_height - scaled_height) / 2 + 100, width=scaled_width, height=scaled_height)
        c.save()

        print(f"Successfully converted '{png_filepath}' to '{pdf_filepath}' with added images and text.")
        # Clean up temporary image
        os.remove("temp_image.png")

    except FileNotFoundError:
        print(f"Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage:
if __name__ == "__main__":
    png_file = 'C:\\Users\\mas13\\PycharmProjects\\Torex_calc\\client\\out_pic.jpg'

    pdf_file = "output.pdf"
    top_lines = ["Delta PRO PP 950x2050 в наклад, без доп. замка",
                 "Наружная отделка - МДФ 10 мм ПВХ Оскуро",
                 "Внутренняя отделка - МДФ 10 мм ПВХ Оскуро.",
                 "Наличники -НУ1 Оскуро",
                 "Фурнитура черный квадрат",
                 "Цвет металла - Черный графит"]
    torex_image = "torex.jpg"
    bottom_lines = ["Подпись заказчика        ______________________________", ""]
    png_to_pdf_with_images_and_text(png_file, pdf_file, top_lines, A4)
