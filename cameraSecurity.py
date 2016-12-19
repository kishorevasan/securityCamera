import cv2
from datetime import datetime
import numpy as np

camera_port = 0
#frames relapse for 2 second gap 33fps
ramp_frames = 66

#Sets up the video to capture
camera = cv2.VideoCapture(camera_port)


"""
Function that takes as input one rgb image array and returns a grayscale image. It applies 
the following transform:
    .. math::
		I_{gray} = 0.2989I_r + 0.5870I_g + 0.1140I_b
	Args:
		rgb: ``numpy ndarray`` of a four-dimensional image batch of the form 
	Returns:
		numpy ndarray: gray
"""
def rgb2gray(rgb):
	r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
	gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
	return gray

#returns the image at the current frame
def get_image():
    retval, im = camera.read()
    return im

print "You are protected now."

#gets into an infinite loop 
while True:
    a = np.asarray(rgb2gray(get_image()))
    for i in xrange(ramp_frames):
        temp = get_image()
    b= np.asarray(rgb2gray(get_image()))
    c = np.abs(a-b)
    d = np.zeros(c.shape)
    d[c>25] = 1
    change_percent = 100*np.sum(d)/np.prod(d.shape)
    print change_percent
    if(change_percent>20):
        temp = datetime.now().strftime('%Y_%m_%d %H_%M_%S')
        cv2.imwrite(temp+".jpg",a)
        cv2.imwrite(temp+"(1).jpg",b)

del(camera)
