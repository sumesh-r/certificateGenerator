from PIL import Image, ImageFont, ImageDraw

# Global Variables
FONT_FILE = ImageFont.truetype(r'font/PTSans-BoldItalic.ttf', 50)
FONT_COLOR = "#000000"

template = Image.open(r'template.png')
WIDTH, HEIGHT = template.size

def make_certificates(name):
    '''Function to save certificates as a .png file'''

    image_source = Image.open(r't1.png')
    draw = ImageDraw.Draw(image_source)

    # Finding the width and height of the text. 
    name_width, name_height = draw.textsize(name, font=FONT_FILE)

    # Placing it in the center, then making some adjustments.
    draw.text((((WIDTH) - name_width) / 2-200, (HEIGHT - name_height) / 2 -11), name, fill=FONT_COLOR, font=FONT_FILE)

    # Saving the certificates in a different directory.
    image_source.save("./out/" + name +".png")
    print('Saving Certificate of:', name)        

if __name__ == "__main__":
    my_file = open("names.txt", "r")
  
    # reading the file
    data = my_file.read()
  
    # replacing end splitting the text 
    # when newline ('\n') is seen.
    names = data.split("\n")

    names = ['Tushar Nankani',"Full Name", 'Some Long Ass Name Might Not Work']
    # names=['SELVAMUTHUKUMARAN NEELAKANDAN']

    for name in names:
        make_certificates(name)
    my_file.close()

    print(len(names), "certificates done.")

