import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    else:
        read_file = sys.argv[1]
        write_file = sys.argv[2]
        modify_files(read_file, write_file)

def modify_files(read_file, write_file):
    extensions = ['.jpg','.jpeg','.png']
    ext1 = read_file[read_file.find('.'):]
    ext2 = write_file[write_file.find('.'):]
    if  not ext1  in extensions:
        sys.exit('Invalid input')

    if not ext2 in extensions:
        sys.exit('Invalid output')
    
    if not ext1 == ext2 :
        sys.exit('Input and output have different extensions')
    
    shirt_img = Image.open('shirt.png')
    img_shirt_size = shirt_img.size
    try:
        with Image.open(read_file) as aFile:
            new_img = ImageOps.fit(image=aFile,size=img_shirt_size)
            new_img.paste(im=shirt_img,box=shirt_img)
            new_img.save(write_file)
    except FileNotFoundError:
        sys.exit('Input does not exist')    
    shirt_img.close()

if __name__ == "__main__":
    main()