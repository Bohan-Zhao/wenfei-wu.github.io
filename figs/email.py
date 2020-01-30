import Image
import ImageDraw
import ImageFont

def getSize(txt, font):
    testImg = Image.new('RGB', (1, 1))
    testDraw = ImageDraw.Draw(testImg)
    return testDraw.textsize(txt, font)

if __name__ == '__main__':

    fontname = "roboto.ttf"
    fontsize = 30   
    text = "wenfeiwu@tsinghua.edu.cn"
    #text = "wenfeiwu@mail.tsinghua.edu.cn"
    text1 = "wenfeiwu@outlook.com"

    colorText = "black"
    colorOutline = "red"
    colorBackground = "white"


    font = ImageFont.truetype(fontname, fontsize)
    width, height = getSize(text, font)
    print width, height
    img = Image.new('RGB', (width+4, 2*height+8), colorBackground)
    d = ImageDraw.Draw(img)
    d.text((2, -5), text, fill=colorText, font=font)
    d.text((2, height-5), text1, fill=colorText, font=font)
    #d.rectangle((0, 0, width+3, height+3), outline=colorOutline)

    img.save("email.png")
