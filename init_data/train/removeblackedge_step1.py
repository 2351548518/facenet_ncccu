import cv2
import os
import shutil

datapath = "data"
data_remove_edge_path = "data_remove_edge"
def main(datapath):
    filedirs = os.listdir(datapath) # name
    for filepath in filedirs:
        resultimg_path = os.path.join(data_remove_edge_path, filepath)
        if not os.path.exists(resultimg_path):
            os.makedirs(resultimg_path)

        resultimg_a = RemoveBlackEdge(os.path.join(datapath,filepath,"a.jpg"))
        cv2.imwrite(os.path.join(data_remove_edge_path,filepath,"a.jpg"), resultimg_a)
        resultimg_b = RemoveBlackEdge(os.path.join(datapath,filepath,"b.jpg"))
        cv2.imwrite(os.path.join(data_remove_edge_path,filepath,"b.jpg"), resultimg_b)


def RemoveBlackEdge(imgpath):
    image = cv2.imread(imgpath)

    b = cv2.threshold(image, 15, 255, cv2.THRESH_BINARY)  # 调整裁剪效果
    binary_image = b[1]  # 二值图--具有三通道
    binary_image = cv2.cvtColor(binary_image, cv2.COLOR_BGR2GRAY)

    row = binary_image.shape[0]  # row指行，第几行，也就是height
    # print("高度x=",x)
    column = binary_image.shape[1]  # column指列，第几列，也就是width
    # print("宽度y=",y)
    edges_row = []
    edges_column = []

    for i in range(row):  # 逐个判断
        for j in range(column):

            if binary_image[i][j] == 255:  # 255表示白色
                # print("横坐标",i)
                # print("纵坐标",j)
                edges_row.append(i)
                edges_column.append(j)
    # print(edges_x)
    # print(edges_y)
    bottom = min(edges_row)  # 底部
    # print(bottom)
    top = max(edges_row)  # 顶部
    # print(top)

    left = min(edges_column)
    # print(left)         #左边界
    right = max(edges_column)
    # print(right)                #右边界

    pre2_picture = image[bottom:top, left:right]
    return pre2_picture

main(datapath)