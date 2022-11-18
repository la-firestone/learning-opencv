#OpenCV Sample 3: Builds upon sample 2, filters a particular color selected using trackbars
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

#Create a window to display the trackbars
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

#Start a loop to repeatedly capture frames and display them
#READ MORE: https://docs.python.org/3/reference/compound_stmts.html#while
while (1):
    # Assign 'frame' to a captured frame from VideoCapture object created in line 9
    # 'ret' is a boolean(True/False statement) that indicates if the frame is ready to be shown
    ret, frame = cap.read()

    # Show the image frame
    # READ MORE: https://docs.opencv.org/3.1.0/dc/d2e/tutorial_py_image_display.html?highlight=imshow
    cv2.imshow('frame', frame)

    # Convert the captured frame to
    # "Hue Saturation Value" (HSV) color space from "Blue Green Red" (BGR) color space
    # READ MORE: http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html
    # READ MORE: https://en.wikipedia.org/wiki/HSL_and_HSV
    # ***************In OpenCV Hue range is from 0-180 and not from 0 to 360********************
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Uncomment the line below to see the frame in the HSV color space
    #cv2.imshow('hsv', hsv)

    # /////////////////////////////

    #Assign values from trackbars to corresponding values to create boundaries
    #READ MORE: https://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html
    hue = cv2.getTrackbarPos('Hue', 'Control Panel')
    sat = cv2.getTrackbarPos('Sat', 'Control Panel')
    val = cv2.getTrackbarPos('Val', 'Control Panel')
    hrange = cv2.getTrackbarPos('Hrange', 'Control Panel')
    srange = cv2.getTrackbarPos('Srange', 'Control Panel')
    vrange = cv2.getTrackbarPos('Vrange', 'Control Panel')


    #Create a boundary for any color that gets updated by trackbars
    #READ MORE: https://www.pyimagesearch.com/2014/08/04/opencv-python-color-detection/
    colorLower = (hue - hrange, sat - srange, val - vrange)
    colorUpper = (hue + hrange, sat + srange, val + vrange)
    #( Hue 0-180, Saturation 0-255, Value 0-255 )
    #EXAMPLE
    #Say the user moves the trackbar and sets the hue to 10 and hrange to 10
    #The lower hue bound will be 10-10 = 0 and upper hue bound will be 10+10=20.

    # /////////////////////////////

    ## This returns a binary (black and white) frame and assigns it to 'filtered frame'
    # Any white on the frame is the color we are detecting
    # READ MORE: https://www.pyimagesearch.com/2014/08/04/opencv-python-color-detection/
    filteredFrame = cv2.inRange(hsv, colorLower, colorUpper)

    # Uncomment the line below to see the binary frame
    # cv2.imshow('filteredFrame', filteredFrame)

    # This superimposes the black and white frame on top of the original frame to let the desired color through
    # Assigned to a new frame 'colorCutout'
    colorCutout =  cv2.bitwise_and(frame, frame, mask=filteredFrame)
    #Show frame with the color that we want
    cv2.imshow('colorCutout', colorCutout)
    # ///////////////////////////////

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