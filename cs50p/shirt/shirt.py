import sys  # To handle command-line arguments
from PIL import Image, ImageOps  # To open, manipulate, and save images

def main():
    # Ensure that exactly two command-line arguments (input and output files) are provided
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')  # Exit if not enough arguments
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')  # Exit if too many arguments
    else:
        # Assign the first argument as the input file and the second as the output file
        read_file = sys.argv[1]
        write_file = sys.argv[2]
        modify_files(read_file, write_file)  # Call function to modify the image

def modify_files(read_file, write_file):
    # Supported file extensions for input and output images
    extensions = ['.jpg', '.jpeg', '.png']
    
    # Extract file extensions from the input and output file names
    ext1 = read_file[read_file.find('.'):].lower()  # Get the file extension of input
    ext2 = write_file[write_file.find('.'):].lower()  # Get the file extension of output

    # Validate if the input file has a valid image extension
    if not ext1 in extensions:
        sys.exit('Invalid input')  # Exit if the input file is not a valid image type

    # Validate if the output file has a valid image extension
    if not ext2 in extensions:
        sys.exit('Invalid output')  # Exit if the output file is not a valid image type
    
    # Check if the input and output have the same file extension
    if not ext1 == ext2:
        sys.exit('Input and output have different extensions')  # Exit if the extensions don't match
    
    # Open the shirt image that will be pasted on top of the input image
    shirt_img = Image.open('shirt.png')  # Load the "shirt" image
    img_shirt_size = shirt_img.size  # Get the size of the "shirt" image to fit the input image

    try:
        # Open the input image file
        with Image.open(read_file) as aFile:
            # Resize the input image to the size of the "shirt" image
            new_img = ImageOps.fit(image=aFile, size=img_shirt_size)
            
            # Paste the "shirt" image on top of the resized input image
            new_img.paste(im=shirt_img, box=(0, 0))  # Position the "shirt" image at the top-left corner

            # Save the modified image to the specified output file
            new_img.save(write_file)

    except FileNotFoundError:
        sys.exit('Input does not exist')  # Exit if the input file is not found

    # Close the shirt image after use to release resources
    shirt_img.close()

if __name__ == "__main__":
    main()  # Run the main function when the script is executed