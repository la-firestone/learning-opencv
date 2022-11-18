#OpenCV Sample 5: Builds upon sample 4, adds text to the frame with the coordinates of the object
#Last modified: 04-09-18

#Import the necessary library
import cv2

#Create a VideoCapture object assigned to the correct port (in this case "0")
#READ MORE: https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
cap = cv2.VideoCapture(0)

#/////////////////////////////

#This as an "empty function" for a parameter we are not using with the trackbar object
def nothing(x):
    pass


# Create a window for later use
cv2.namedWindow('Control Panel')

#Create track bars for all input values
#READ MORE: https://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html?highlight=createtrackbar#createtrackbar
#Arguments: cv.CreateTrackbar(trackbarName, windowName, value, count, onChange)  None
cv2.createTrackbar('Hue', 'Control Panel', 0, 180, nothing)  # default 0 205 255 69 8 12
cv2.createTrackbar('Sat', 'Control Panel', 205, 255, nothing)
cv2.createTrackbar('Val', 'Control Panel', 255, 255, nothing)
cv2.createTrackbar('Hrange', 'Control Panel', 69, 127, nothing)
cv2.createTrackbar('Srange', 'Control Panel', 69, 127, nothing)
cv2.createTrackbar('Vrange', 'Control Panel', 69, 127, nothing)



#/////////////////////////////
#Define a function that filters the desired color, takes in a frame as an argument
#READ MORE: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
def filterColor(frame):

    # Convert the captured frame to
    # "Hue Saturation Value" (HSV) color space from "Blue Green Red" (BGR) color space
    # READ MORE: http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html
    # READ MORE: https://en.wikipedia.org/wiki/HSL_and_HSV
    # ***************In OpenCV Hue range is from 0-180 and not from 0 to 360********************
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # /////////////////////////////

    # Assign values from trackbars to corresponding values to create boundaries
    # READ MORE: https://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html
    hue = cv2.getTrackbarPos('Hue', 'Control Panel')
    sat = cv2.getTrackbarPos('Sat', 'Control Panel')
    val = cv2.getTrackbarPos('Val', 'Control Panel')
    hrange = cv2.getTrackbarPos('Hrange', 'Control Panel')
    srange = cv2.getTrackbarPos('Srange', 'Control Panel')
    vrange = cv2.getTrackbarPos('Vrange', 'Control Panel')

    # Create a boundary for any color that gets updated by trackbars
    # READ MORE: https://www.pyimagesearch.com/2014/08/04/opencv-python-color-detection/
    colorLower = (hue - hrange, sat - srange, val - vrange)
    colorUpper = (hue + hrange, sat + srange, val + vrange)
    # ( Hue 0-180, Saturation 0-255, Value 0-255 )
    # EXAMPLE
    # Say the user moves the trackbar and sets the hue to 10 and hrange to 10
    # The lower hue bound will be 10-10 = 0 and upper hue bound will be 10+10=20.

    # /////////////////////////////

    # This returns a binary (black and white) frame and assigns it to 'filtered frame'
    # Any white on the frame is the color we are detecting
    # READ MORE: https://www.pyimagesearch.com/2014/08/04/opencv-python-color-detection/
    filteredFrame = cv2.inRange(hsv, colorLower, colorUpper)

    # Uncomment the line below to see the binary frame
    #cv2.imshow('filteredFrame', filteredFrame)

    # This superimposes the black and white frame on top of the original frame to let the desired color through
    # Assigned to a new frame 'colorCutout'
    colorCutout =  cv2.bitwise_and(frame, frame, mask=filteredFrame)
    # show the frame with the color that we want
    cv2.imshow('colorCutout', colorCutout)
    # Note: This function returns the binary (black and white) frame
    return filteredFrame

# Function that returns the array of points for the biggest contour
# Takes in a binary (black and white) frame as its argument
def findBiggestContour(mask):
    # Contours
    # READ MORE: https://docs.opencv.org/3.1.0/d4/d73/tutorial_py_contours_begin.html
    # READ MORE: https://docs.opencv.org/3.1.0/d3/dc0/group__imgproc__shape.html#ga17ed9f5d79ae97bd4c7cf18403e1689a

    # Create an array of contour points
    # READ MORE: https://docs.opencv.org/3.1.0/d3/dc0/group__imgproc__shape.html#ga17ed9f5d79ae97bd4c7cf18403e1689a
    contoursArray = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)[-2]

    # This code will execute if at least one contour was found
    if len(contoursArray) > 0:
        # Find the biggest contour
        biggestCountour = max(contoursArray, key=cv2.contourArea)
        # Returns an array of points for the biggest contour found
        return biggestCountour

#Start a loop to repeatedly capture frames and display them
#READ MORE: https://docs.python.org/3/reference/compound_stmts.html#while
while (1):
    # Assign 'frame' to a captured frame from VideoCapture object created in line 9
    # 'ret' is a boolean(True/False statement) that indicates if the frame is ready to be shown
    ret, frame = cap.read()

    # ////////////////////////////
    # Call our function that we created (line 36) and assign the result to 'mask'
    # Remember that mask is the binary (black and white) frame returned from filterColor()
    mask = filterColor(frame)

    #Call our function that we created (line 85) and assign result to 'biggest contour'
    biggestContour = findBiggestContour(mask)
    # Find the center coordinates, width, and height of a bounding rectangle around the biggest contour
    x, y, w, h = cv2.boundingRect(biggestContour)
    # Assign color to blue
    rectangleColor = (255, 0, 0) #(Blue,Green,Red)
    # Draw rectangle onto the frame using the points of the bounding rectangle from contour
    cv2.rectangle(frame, (x, y), (x + w, y + h), rectangleColor, 2)

    #Choose the font for the text we will display
    font = cv2.FONT_HERSHEY_SIMPLEX

    #Put the text of the values on the screen to the user can see them
    #cv2.putText(frame, "X: " + format(x), (0, 50), font, 0.6, (155, 250, 55), 2, cv2.LINE_AA)
    #cv2.putText(frame, "Y: " + format(y), (0, 100), font, 0.6, (155, 250, 55), 2, cv2.LINE_AA)

    #Put the coordinates of contour on the screen and have them move with the object
    cv2.putText(frame, "X: " + format(x), (int(x), int(y)+50), font, 0.6, (155, 250, 55), 2, cv2.LINE_AA)
    cv2.putText(frame, "Y: " + format(y), (int(x), int(y)+100), font, 0.6, (155, 250, 55), 2, cv2.LINE_AA)

    # ///////////////////////
    #Show final result
    cv2.imshow('frame', frame)

    # Show the frame for 1 ms and wait to see if user pressed 'q'
    # READ MORE: https://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html?highlight=waitkey
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # If user presses 'q', exit out of the loop
        break


# Make sure to release the camera
cap.release()

#Close all windows
#READ MORE: https://docs.opencv.org/3.1.0/dc/d2e/tutorial_py_image_display.html?highlight=destroyallwindows
#READ MORE: https://docs.opencv.org/3.1.0/d7/dfc/group__highgui.html#ga6b7fc1c1a8960438156912027b38f481
cv2.destroyAllWindows()