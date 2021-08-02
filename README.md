# Ultrafast Lane Detection Inference Pytorch
Example scripts for the detection of lanes using the [ultra fast lane detection model](https://github.com/cfzd/Ultra-Fast-Lane-Detection) in Pytorch.

![!Ultra fast lane detection](https://github.com/ibaiGorordo/Ultrafast-Lane-Detection-Inference-Pytorch-/blob/main/doc/img/detected%20lanes.jpg)
Source: https://www.flickr.com/photos/32413914@N00/1475776461/

# Requirements

 * **OpenCV**, **Scikit-learn** and **pytorch**. **pafy** and **youtube-dl** are required for youtube video inference. 
 
# Installation
```
pip install -r requirements
pip install pafy youtube-dl

```
**Pytorch:** Check the [Pytorch website](https://pytorch.org/) to find the best method to install Pytorch in your computer.

# Pretrained model
Download the pretrained model from the [original repository](https://github.com/cfzd/Ultra-Fast-Lane-Detection) and save it into the **[models](https://github.com/ibaiGorordo/Ultrafast-Lane-Detection-Inference-Pytorch-/tree/main/models)** folder. 

# Ultra fast lane detection - TuSimple([link](https://github.com/cfzd/Ultra-Fast-Lane-Detection))

 * **Input**: RGB image of size 1280 x 720 pixels.
 * **Output**: Keypoints for a maximum of 4 lanes (left-most lane, left lane, right lane, and right-most lane).
 
# Examples

 * **Image inference**:
 
 ```
 python imageLaneDetection.py 
 ```
 
  * **Webcam inference**:
 
 ```
 python webcamLaneDetection.py
 ```
 
  * **Video inference**:
 
 ```
 python videoLaneDetection.py
 ```
 
 # [Inference video Example](https://youtu.be/0Owf6gef1Ew) 
 ![!Ultrafast lane detection on video](https://github.com/ibaiGorordo/Ultrafast-Lane-Detection-Inference-Pytorch-/blob/main/doc/img/laneDetection.gif)
 
 Original video: https://youtu.be/2CIxM7x-Clc (by Yunfei Guo)
 
