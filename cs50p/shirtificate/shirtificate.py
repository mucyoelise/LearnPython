from fpdf import FPDF  # Import the FPDF library to create PDFs

def main():
    # Get the recipient's name as input
    name = input("Name: ")

    # Generate and save the PDF with the given name
    get_shirtficate(name, "shirtificate.pdf")

def get_shirtficate(name, file_name):
    # Create a new PDF object
    pdf = FPDF()

    # Add a new page to the PDF
    pdf.add_page()

    # Set the font to Helvetica, size 50, and add the title text in the center of the page
    pdf.set_font("helvetica", size=50)
    pdf.cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")

    # Add the CS50 shirt image to the PDF. The image width is set to match the page width (epw)
    pdf.image("shirtificate.png", w=pdf.epw)

    # Set the font size to 30 and text color to white (255, 255, 255) for the recipient's name
    pdf.set_font_size(30)
    pdf.set_text_color(255, 255, 255)

    # Add the recipient's name along with "took CS50" at a specific position on the page
    pdf.text(x=60, y=140, txt=f"{name} took CS50")

    # Save the generated PDF to the file
    pdf.output(file_name)

# Run the main function when the script is executed
if __name__ == '__main__':
    main()