import cv2
import os 


def extract_images(path_video, path_out):
    import cv2
    vidcap = cv2.VideoCapture(path_video)
    success,image = vidcap.read()
    count = 0
    while success:
    cv2.imwrite(path_out + "%06d.jpg" % count, image)     # save frame as JPEG file      
    success,image = vidcap.read()
    print('Read a new frame: ', success)
    count += 1


if __name__ == "__main__":
    path_video = "/mnt/c/Users/gardn/Documents/git/data/test.mp4"
    path_out = "/mnt/c/Users/gardn/Documents/git/data/images/"
    extract_images(path_video, path_out)