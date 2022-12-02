import cv2  # opencv库
import cv2
import os
import shutil

data_remove_edge_path = "data_remove_edge"

data_remove_edge_image_denoisy_path = "data_remove_edge_image_denoisy"


def main(datapath, data_remove_edge_image_denoisy_path):
    filedirs = os.listdir(datapath)  # name
    for filepath in filedirs:
        resultimg_path = os.path.join(data_remove_edge_image_denoisy_path, filepath)
        if not os.path.exists(resultimg_path):
            os.makedirs(resultimg_path)
        print(filepath)

        resultimg_a = imageprocess(os.path.join(datapath, filepath, "a.jpg"))
        cv2.imwrite(os.path.join(data_remove_edge_image_denoisy_path, filepath, "a.jpg"), resultimg_a)
        resultimg_b = cv2.imread(os.path.join(datapath, filepath, "b.jpg"))
        cv2.imwrite(os.path.join(data_remove_edge_image_denoisy_path, filepath, "b.jpg"), resultimg_b)


def imageprocess(imgpath):
    image = cv2.imread(imgpath)
    # 双边滤波
    img = cv2.bilateralFilter(image, 9, 75, 75)
    # img = cv2.GaussianBlur(img, (5, 5), 0)
    # 均值滤波
    img = cv2.blur(img, (5, 5))
    # 非局部均值
    res_img = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 3, 21)

    return res_img


main(data_remove_edge_path, data_remove_edge_image_denoisy_path)
