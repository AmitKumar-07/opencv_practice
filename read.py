import cv2 as cv

#reading image and displaying
img = cv.imread('Photos/img1.jpeg')
cv.imshow('Cat', img)
cv.waitKey(0) #it wait this milisecond amount of time

# Reading Videos and displaying
capture = cv.VideoCapture('videos/2.mp4')

while True:
    isTrue, frame = capture.read() #it is reading frame by frame
    
    # if cv.waitKey(20) & 0xFF==ord('d'):
    # This is the preferred way - if `isTrue` is false (the frame could 
    # not be read, or we're at the end of the video), we immediately
    # break from the loop. 
    if isTrue:    
        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF==ord('d'):
                 break            
    else:
        break

capture.release()
cv.destroyAllWindows()