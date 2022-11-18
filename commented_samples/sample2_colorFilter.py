#OpenCV Sample 2: Filters a particular color (red) from a frame
#Last modified: 04-09-18

#Import the necessary library
import cv2

#Create a VideoCapture object assigned to the correct port (in this case "0")
#READ MORE: https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
cap = cv2.VideoCapture(0)

#Start a loop to repeatedly capture frames and display them
#READ MORE: https://docs.python.org/3/reference/compound_stmts.html#while
while (1):
    # Assign 'frame' to a captured frame from VideoCapture object created in line 9
    # 'ret' is a boolean(True/False statement) that indicates if the frame is ready to be shown
    ret, frame = cap.read()

    # Show the image frame
    # READ MORE: https://docs.opencv.org/3.1.0/dc/d2e/tutorial_py_image_display.html?highlight=imshow
    cv2.imshow('frame', frame)

    #Convert the captured frame to
    # "Hue Saturation Value" (HSV) color space from "Blue Green Red" (BGR) color space
    #READ MORE: http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html
    #READ MORE: https://en.wikipedia.org/wiki/HSL_and_HSV
    # ***************In OpenCV Hue range is from 0-180 and not from 0 to 360********************
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Uncomment the line below to see the frame in the HSV color space
    #cv2.imshow('hsv', hsv)


    #Create boundary arrays for the dark red we want to filter
    #( Hue 0-180, Saturation 0-255, Value 0-255 )
    redLower = (160, 100, 100)
    redUpper = (180, 255, 255)

    # This returns a binary (black and white) frame and assigns it to 'filtered frame'
    #Any white on the frame is the color we are detecting
    #READ MORE: https://www.pyimagesearch.com/2014/08/04/opencv-python-color-detection/
    filteredFrame = cv2.inRange(hsv, redLower, redUpper)

    #Uncomment the line below to see the binary frame
    #cv2.imshow('filteredFrame', filteredFrame)

    ## This superimposes the black and white frame on top of the original frame to let the desired color through
    # Assigned to a new frame 'colorCutout'
    colorCutout =  cv2.bitwise_and(frame, frame, mask=filteredFrame)
    #Show frame with the color that we want
    cv2.imshow('colorCutout', colorCutout)

    # Show the frame for 1 ms and wait to see if user pressed 'q'
    # READ MORE: https://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html?highlight=waitkey
    if cv2.waitKey(1) & 0xFF == ord('q'):
        #If user presses 'q', exit out of the loop
        break


#Make sure to release the camera
cap.release()

#Close all windows
#READ MORE: https://docs.opencv.org/3.1.0/dc/d2e/tutorial_py_image_display.html?highlight=destroyallwindows
#READ MORE: https://docs.opencv.org/3.1.0/d7/dfc/group__highgui.html#ga6b7fc1c1a8960438156912027b38f481
cv2.destroyAllWindows()