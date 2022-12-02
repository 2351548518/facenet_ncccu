import os, sys
import cv2
import numpy as np
# sys.path.append("..")
from PIL import Image
from facenet import Facenet
from code.utils.ImageProcessing import imageprocess,RemoveBlackEdge



model = Facenet()
def predict(file1,file2):

    # 去除边框和去噪
    img1 = imageprocess(file1)
    # 只去除黑边
    img2 = RemoveBlackEdge(file2)

    image_1 = Image.fromarray(np.uint8(img1))
    image_2 = Image.fromarray(np.uint8(img2))

    probability = model.detect_image(image_1, image_2)
    print(probability)

    return probability

def main(to_pred_dir,result_save_path):
    subdirs = os.listdir(to_pred_dir) # name
    labels = []
    for subdir in subdirs:

        result = predict(os.path.join(to_pred_dir,subdir,"a.jpg"),os.path.join(to_pred_dir,subdir,"b.jpg"))
        labels.append(result)
    fw = open(result_save_path,"w")
    fw.write("id,label\n")
    for subdir,label in zip(subdirs,labels):
        fw.write("{},{}\n".format(subdir,label))
    fw.close()

if __name__ == "__main__":
    to_pred_dir = sys.argv[1]
    result_save_path = sys.argv[2]
    main(to_pred_dir, result_save_path)