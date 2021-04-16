# import the necessary module (Here cv2)
import cv2

# Capture the video
video = cv2.VideoCapture("Lane Detection AVI.avi")  # Here I've gave "Lane Detection AVI.avi" inside VideoCapture method since I've included this video in my folder

# Check whether the video is opened or not

while video.isOpened():
    
    is_grabbed, frame = video.read() # Here we're using read() method to read the images of the given video (ie) video is formed by set of images right?
    
    # When we complete the video we need to break out of the video 
    if not is_grabbed:
        break  # if the value of is_grabbed is false means we need to break out of it

    cv2.imshow("Lane detection video",frame) # Since video is a frame by frame image
    if cv2.waitKey(20) & 0xFF == ord('q'): # Here waitKey(20)  detects the speed of the video
        break

video.release()

cv2.destroyAllWindows() 


# And that's it now you know how to open a video using opencv in python
