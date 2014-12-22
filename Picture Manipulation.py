#Alex Herbig, Conor Tanzman, Arshiya Singh
#B04
#aherbig3@gatech.edu, ctanzman@gatech.edu, asingh361@gatech.edu 
#We, Alex Herbig, Conor Tanzman, Arshiya Singh, have worked on this assignment using only this semester's course materials.

from Myro import *
#init("/dev/tty.Fluke2-02A9-Fluke2")
init()
#setPicSize("small")
#p = takePicture()
#turnBy(-90,"deg")
#p2 = takePicture()
#savePicture(p, "robotPic1.jpg")
#savePicture(p2, "robotPic2.jpg")
#p = makePicture("robotPic1.jpg")
#p2 = makePicture("robotPic2.jpg")
#gpic = makePicture("greenscreen_source1.jpeg")
#gpic2 = makePicture("greenscreen_back.jpg")

# Most of the functions that require more than one picture for input will not work if
# The picture are different dimensions.

# This function takes a picture with a greenscreen and replaces the green pixels with pixels from the other picture.
# It examines every pixel. If it is green, then it gets the pixels from 
# the same x and y in picture 2 and replaces it in the greenscreen picture
def greenScreen(greenPic, otherPic):
    for pix in getPixels(greenPic):
        r,g,b = getRGB(pix)
        if g > r and g > b and g > 70:
            x = getX(pix)
            y = getY(pix)
            pixel = getPixel(otherPic,x,y)
            r2, g2, b2 = getRGB(pixel)
            setRGB(pix, (r2,g2, b2))
    show(greenPic)
    savePicture(greenPic, "greenScreen.jpg")


# This function blacks out the corners of the picture.
def cornersOverlay(p):
    height = getHeight(p)
    width = getWidth(p)
    color = makeColor(0,0,0)
    #upper left corner
    for x in range(0,15):
        for y in range(0,30):
            pixel = getPixel(p, x, y)
            setColor(pixel,color)
    for x in range(0,30):
        for y in range(0,15):
            pixel = getPixel(p,x,y)
            setColor(pixel,color)
    
    #lower left corner
    for x in range(0,15):
        for y in range((height-30),height):
            pixel = getPixel(p, x, y)
            setColor(pixel,color)
    for x in range(0,30):
        for y in range((height-15),height):
            pixel = getPixel(p,x,y)
            setColor(pixel,color)

    #upper right corner
    for x in range((width-30),width):
        for y in range(0,15):
            pixel = getPixel(p, x, y)
            setColor(pixel,color)
    for x in range((width-15),width):
        for y in range(0,30):
            pixel = getPixel(p, x, y)
            setColor(pixel,color)
    
    #lower right corner
    for x in range((width-30),width):
        for y in range((height-15),height):
            pixel = getPixel(p, x, y)
            setColor(pixel,color)
    for x in range((width-15),width):
        for y in range((height-30),height):
            pixel = getPixel(p, x, y)
            setColor(pixel,color)
    show(p)
    savePicture(p,"corner-overlay.jpg")


# This tints the entire picture red.
def seeingRed(p):
    for pix in getPixels(p):
        setRed(pix,255)
    show(p)
    savePicture(p, "seeing-red.jpg")


# This takes a picture and makes it darker until it gets to a black screen.
# It saves every step of the way into a list and creates a .gif at the end.
def fade(p):
    aList = []
    for i in range(10):
        for pix in getPixels(p):
            r, g, b = getRGB(pix)
# This makes sure the picture gets darker at a constant rate
            n = (9-i)
            m = (10-i)
            color = makeColor(r*n/m,g*n/m,b*n/m)
            setColor(pix, color)
        copy = copyPicture(p)
        aList.append(copy)
    savePicture(aList, "fade.gif")


# This takes a picture and shakes it around the screen.
# The function takes the picture and centers it on a larger white picture
# Then the picture is moved randomly up, down, side to side, etc
# Each movement is saves into a list, which gets turned into a .gif at the end.
def screenShake(p):
    picList = []
    slides = 10
    width = getWidth(p) + 20
    height = getHeight(p) + 20
    picture = makePicture(width,height)
    for x in range(10,width-10):
        for y in range(10,height-10):
            pix1 = getPixel(p, x-10, y-10)
            pix2 = getPixel(picture, x, y)
            r, g, b = getRGB(pix1)
            color = makeColor(r,g,b)
            setColor(pix2, color)
    default = copyPicture(picture)
    # Setting up random point variations
    shakeList = [(0,0),(10,0),(20,0),(0,10),(20,10),(0,20),(10,20),(20,20)]
    count = 0
    # Creates new pictures, offsets them, and then saves them to the picture list
    while count < slides:
        index = randint(0,7)
        a, c = shakeList[index]
        picture = makePicture(width,height)
        for x in range(a,(width-(20-a))):
            for y in range(c,(height-(20-c))):
                pix1 = getPixel(p, x-a, y-c)
                pix2 = getPixel(picture, x, y)
                r, g, b = getRGB(pix1)
                color = makeColor(r,g,b)
                setColor(pix2, color)
        count += 1
        shake = copyPicture(picture)
        picList.append(shake)
        picList.append(default)
        percent = 100/slides*count
        out = "{:.0f} percent done."
        print(out.format(percent))
        savePicture(picList, "screenShake.gif")


# This function takes 2 pictures and fades from one to the other.
# The color differences are averaged between the pictures and the function slowly changes the pixels on one
# until the picture ends up looking like the sencond picture.
# The pictures are saved into a list and are saved as a .gif.
def crossFade(p1,p2):
    aList = []
    aList.append(p1)
    picChange = copyPicture(p1)
    for d in range(4):
        for x in range(getWidth(p1)):
            for y in range(getHeight(p1)):
                pix1 = getPixel(p1,x,y)
                pix2 = getPixel(p2,x,y)
                pix3 = getPixel(picChange,x,y)
                rChange = getRed(pix2)- getRed(pix1)
                gChange = getGreen(pix2)- getGreen(pix1)
                bChange = getBlue(pix2)- getBlue(pix1)
                rChange = rChange/4
                gChange = gChange/4
                bChange = bChange/4
                r = getRed(pix3)
                g = getGreen(pix3)
                b = getBlue(pix3)
                setRed(pix3, r + rChange)
                setGreen(pix3, g + gChange)
                setBlue(pix3, b +bChange)
        aList.append(copyPicture(picChange))
    aList.append(p2)
    savePicture(aList,"crossfade.gif")

