import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imshow
from skimage import transform

chessImg = imread('input.jpg')
imshow(chessImg)

area_of_interest = np.loadtxt('src-matrix.txt')
area_of_projection = np.loadtxt('dst-matrix.txt')


def project_transform(image, src, dst):
    x_dst = [val[0] for val in dst] + [dst[0][0]]
    y_dst = [val[1] for val in dst] + [dst[0][1]]
    tform = transform.estimate_transform('projective', np.array(src), np.array(dst))
    transformed = transform.warp(image, tform.inverse)
    plt.figure(figsize=(15,18))
    plt.imshow(transformed)
    plt.savefig("output.jpg")
    plt.plot(x_dst, y_dst)
    
project_transform(chessImg, area_of_interest, area_of_projection)
