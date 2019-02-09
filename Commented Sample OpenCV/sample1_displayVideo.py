#OpenCV Sample 1: Displaying video stream
#Last modified: 04-09-18

#Import the necessary library
import cv2

#Create a VideoCapture object assigned to the correct port (in this case "0")
#READ MORE: https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
cap = cv2.VideoCapture(0)

#Start a loop to repeatedly capture frames and display them
#READ MORE: https://docs.python.org/3/reference/compound_stmts.html#while
while (1):

    #Assign 'frame' to a captured frame from VideoCapture object created in line 9
    #'ret' is a boolean(True/False statement) that indicates if the frame is ready to be shown
    ret, frame = cap.read()

    #Show the image frame
    #READ MORE: https://docs.opencv.org/3.1.0/dc/d2e/tutorial_py_image_display.html?highlight=imshow
    cv2.imshow('frame', frame)

    #Show the frame for 1 ms and wait to see if user pressed 'q'
    #READ MORE: https://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html?highlight=waitkey
    if cv2.waitKey(1) & 0xFF == ord('q'):
        #If user presses 'q', exit out of the loop
        break


#Make sure to release the camera
cap.release()

#Close all windows
#READ MORE: https://docs.opencv.org/3.1.0/dc/d2e/tutorial_py_image_display.html?highlight=destroyallwindows
#READ MORE: https://docs.opencv.org/3.1.0/d7/dfc/group__highgui.html#ga6b7fc1c1a8960438156912027b38f481
cv2.destroyAllWindows()