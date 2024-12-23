from fpdf import FPDF

def main():
    # Get the recipient's name as input
    name = input("Name: ")

    # Generate and save the PDF
    get_shirtficate(name, "shirtificate.pdf")


def get_shirtficate(name, file_name):
    pdf = FPDF() # Creating PDF object
    pdf.add_page() # Adding page on created obj

    # Set font, size, and color for the title
    pdf.set_font("helvetica", size = 50)
    pdf.cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")
    # Add CS50 shirt image
    pdf.image("shirtificate.png", w=pdf.epw)

    # Set font size and color for the text
    pdf.set_font_size(30)
    pdf.set_text_color(255, 255, 255)

    # Add the recipient's name and the course name
    pdf.text(x=60, y=140, txt=f"{name} took CS50")

    # Save the generated PDF
    pdf.output(file_name)

if __name__ == '__main__':
    main()