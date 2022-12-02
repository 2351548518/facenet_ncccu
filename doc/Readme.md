## Facenet-人脸对比
## 使用大数据与人工智能挑战赛所给数据集进行训练

### 赛题数据分析与预处理

**数据分析** ：比赛所给的数据集中的```a.jpg``` 是含有噪声的数据集，因此首先想办法在尽可能保留图像细节的情况下去除噪声，因此想到了先对所有的图片进行**去除黑边** ，之后对图片**去除噪声** 。然后根据facenet的输入对已经处理好的数据进行划分，生成数据集。facenet所要求的数据集为**在同一个文件夹下是同一个人的人脸的数据** ，因此将```label == "1"``` 的文件夹复制到```datasets``` 中作为训练所用的数据集。

**预处理** ：

- 去除黑边：见代码```init_data/train/removeblackedge_step1.py``` . 
- 去除噪声：见代码```init_data/train/ImageDenoising_step2.py``` .
- 数据文件划分：首先为了方便将```init_data/train/annos.csv``` 中的第一行删除，之后见代码``` init_data/train/split_file.py```.

预处理后的文件夹名为·```datasets``` ,将此文件复制到```init_data``` 目录下，作为数据集，已经处理好的数据集```init_data/train/new_datasets.zip```。

**生成lfw数据进行验证** ：

> 此处参考博客:
>
> [按照lfw pairs.txt的格式生成自己的pairs.txt_Deepcong的博客-CSDN博客](https://blog.csdn.net/DeepCBW/article/details/102698947)
>
> [仿照LFW的pair.txt生成自己数据集的txt文件_WINMI_1627的博客-CSDN博客](https://blog.csdn.net/qq_38702419/article/details/88711327)

需要首先将上一步生成的重命名为 ```init_data/train/new_datasets``` ，之后依次运行以下代码。之后将文件夹再重命名为```init_data/mylfw``` .

代码见：``` init_data/train/createpairs_step1.py``` 和 ``` init_data/train/createpairs_step2.py``` .

至此，数据的预处理结束。

### 模型构建

采用facenet，使用的开源代码来自[bubbliiiing/facenet-pytorch: 这是一个facenet-pytorch的库，可以用于训练自己的人脸识别模型。 (github.com)](https://github.com/bubbliiiing/facenet-pytorch) ，开源时间为```2 years ago``` ，早于比赛开始时间，符合比赛规定。

训练直接运行```code/train.py``` ，训练好的模型保存在``` code/model``` 中。选择训练200epoch的模型进行预测。

### 结果预测

直接运行```run.py``` 文件。

## 整体文件目录

![image-20221201223002783](https://raw.githubusercontent.com/2351548518/images/main/20221201/image-20221201223002783.png)

## Reference

https://github.com/davidsandberg/facenet  
https://github.com/timesler/facenet-pytorch  



