# May Pena
# This program uses graphics in order to apply different filters
# to a picture that is inputed by the user. 

from graphics import *

def andyWarhol( img ):
    """saturate the colors of the image"""
    for x in range( WIDTH ):
        for y in range( HEIGHT ):
            # get the R, G, B values for the pixel at (x,y)
            red, green, blue = img.getPixel( x, y )
            if blue < 125:
                blue = 0
            else:
                blue = 255
            if red < 125:
                red = 0
            else:
                red = 255
            if green < 125:
                green = 0
            else:
                green = 255               
            # set the R, G, B values of the pixel at (x,y)
            # to different values (here we set red to 255)
            img.setPixel( x, y, color_rgb(red, green, blue ) )


def blackAndWhite( img, win ):
    """transforms the image to a black and white image"""
  
    for y in range( HEIGHT - 1, -1 , -1):
        win.update()
        for x in range( WIDTH ):
            red, green, blue = img.getPixel( x, y )
            grey  = int( 0.3 * red +0.6 * green +0.11 * blue )
            color = color_rgb( grey, grey, grey )
            img.setPixel( x, y, color )

def sideBW( img, win ):
    """transforms the bottom half of the image into gray along a
        diagonal line """
    for y in range( HEIGHT ):
        win.update()
        for x in range( y ):
            if x < WIDTH:
                 red, green, blue = img.getPixel( x, y )
                 grey  = int( 0.3 * red +0.6 * green +0.11 * blue )
                 color = color_rgb( grey, grey, grey )
                 img.setPixel( x, y, color )


def addBorders( img, win, color ):
    """adds a border to the image and updates the window"""   
    #set color
    color = color

    #add top border
    for x in range(WIDTH):
        win.update()
        for y in range(6):
            img.setPixel(x, y, color)

    #add bottom border
    for x in range(WIDTH):
        win.update()
        for y in range(HEIGHT-5, HEIGHT):
            img.setPixel(x, y, color)

    #add left border
    for y in range(HEIGHT):
        win.update()
        for x in range(5):
            img.setPixel(x, y, color)

    #add right border           
    for y in range(HEIGHT):
        win.update()
        for x in range(WIDTH-5, WIDTH):
            img.setPixel(x, y, color)


def pixelation(img, win):
    """ covers the image with circles that have the colors of the
        pixel on which each circle is centered"""
    img.undraw()

    for y in range(0, HEIGHT, 10):
        win.update()
        for x in range(0, WIDTH, 10):
            red, green, blue = img.getPixel(x, y)
            color = color_rgb(red, green, blue)

            radius = 5
            c = Circle(Point(x, y), radius)
            c.setFill(color)
            c.draw(win)

        
def flip(img, win):
    """this function flips the image vertically"""
    for y in range(HEIGHT):
        win.update()
        for x in range(WIDTH//2):
            red, green, blue = img.getPixel(x, y)
            color = color_rgb(red, green, blue)
            img.setPixel(WIDTH - 1 - x, y, color)



def addFog(img, win):
    """adds a white "fog" to the image
       the fog is proportional to the rows in the image
       the heaviest fog is at the bottom and gets lighter as the
       y value of the pixel decreases"""

    for y in range(HEIGHT):
        win.update()
        for x in range( WIDTH ):
            proportion = y/HEIGHT
            red, green, blue = img.getPixel(x, y)
            r = int(red + ((255 - red) * proportion))
            b = int(blue + ((255 - blue) * proportion))
            g = int(green + ((255 - green) * proportion))

            img.setPixel(x, y, color_rgb(r, g, b))
                

    
def main():
    global WIDTH, HEIGHT
    
    # ask user for image
    print( "Input the name of your picture, for example: catHat.gif")
    print( "Transformations might take a minute or two depending" )
    print( "on the size of your image." )
    picture = input( "\nFile name: " )

    # create an image with its center corresponding to the center
    # of the window.  
    img = Image( Point(200, 200), picture )
    WIDTH  = img.getWidth()
    HEIGHT = img.getHeight()
    img = Image( Point( WIDTH//2 , HEIGHT//2), picture )
    
    # open the graphic window
    win = GraphWin( "Playing With Filters", WIDTH, HEIGHT)

    # make the image appear in the window
    img.draw( win )
    
    # un-comment any of the filters to see the magic!
    
    #blackAndWhite( img, win )
    #andyWarhol( img ) 
    #sideBW( img, win )
    #addBorders( img, win, "yellow" )
    #pixelation(img, win)
    #flip(img, win)
    #addFog(img, win)
    
    # close the window when the user clicks on it
    win.getMouse( )
    win.close()

main()
