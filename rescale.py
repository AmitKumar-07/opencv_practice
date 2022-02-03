import cv2 as cv

def rescaleFrame(frame,scale=0.2):
    #it method work for photos,videos,live videos
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

#reading image and displaying 
img = cv.imread('Photos/img1.jpeg')
image_resized=rescaleFrame(img)

cv.imshow('Cat', image_resized)
cv.waitKey(0) 


# Reading Videos and displaying
capture = cv.VideoCapture('videos/2.mp4')

while True:
    isTrue, frame = capture.read() 
    frame_resized=rescaleFrame(frame)
    if isTrue:   
        cv.imshow('Video', frame) #original video
        cv.imshow('Video Resized',frame_resized) #resized video
        if cv.waitKey(20) & 0xFF==ord('d'):
            break            
    else:
        break

capture.release()
cv.destroyAllWindows()