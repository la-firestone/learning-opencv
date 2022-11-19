# OpenCV Sample 7: Displaying video stream
# Last modified: 11-18-22

# Import the necessary library
import cv2

# Create a VideoCapture object assigned to the correct port (in this case "0")
# READ MORE: https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
cap = cv2.VideoCapture(0)

# Create a QR Detector object
detect = cv2.QRCodeDetector()

# Optional: Use this variable to resize the output frame. Improves speed.
div = 1

# Start a loop to repeatedly capture frames and display them
# READ MORE: https://docs.python.org/3/reference/compound_stmts.html#while
while True:

    # Assign 'frame' to a captured frame from VideoCapture object created in line 9
    # 'ret' is a boolean(True/False statement) that indicates if the frame is ready to be shown
    ret, frame = cap.read()

    if ret:

        value, points, rectified = detect.detectAndDecode(frame)

        if points is not None:
            print(value)
            print(points)
            pts = len(points)
            print(pts)
            for i in range(pts):
                nextPointIndex = (i + 1) % pts
                frame = cv2.line(frame, tuple(points[i][0]), tuple(points[nextPointIndex][0]), (255, 0, 0), 5)

        else:
            print("No QR code detected")

        # Returns number of rows (height), columns (width), and channels ("layers")
        # READ MORE: https://docs.opencv.org/4.x/d3/df2/tutorial_py_basic_ops.html
        height, width, channel = frame.shape

        # If div was set to something other than 1, this re-sizes the output frame.
        # If div is odd, int() rounds output to a whole number. No half pixels allowed!
        frame = cv2.resize(frame, (int(width / div), int(height / div)))

        # Show the image frame
        # READ MORE: https://docs.opencv.org/3.1.0/dc/d2e/tutorial_py_image_display.html?highlight=imshow
        cv2.imshow('frame', frame)

    # Show the frame for 1 ms and wait to see if user pressed 'q'
    # READ MORE: https://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html?highlight=waitkey
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # If user presses 'q', exit out of the loop
        break


# Make sure to release the camera
cap.release()

# Close all windows
# READ MORE: https://docs.opencv.org/3.1.0/dc/d2e/tutorial_py_image_display.html?highlight=destroyallwindows
# READ MORE: https://docs.opencv.org/3.1.0/d7/dfc/group__highgui.html#ga6b7fc1c1a8960438156912027b38f481
cv2.destroyAllWindows()






