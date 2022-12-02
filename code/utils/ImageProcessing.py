import cv2  # opencv库
import cv2
import os


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


def imageprocess(imgpath):
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

    # 双边滤波
    img = cv2.bilateralFilter(pre2_picture, 9, 75, 75)
    # img = cv2.GaussianBlur(img, (5, 5), 0)
    # 均值滤波
    img = cv2.blur(img, (5, 5))
    # 非局部均值
    res_img = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 3, 21)

    return res_img

