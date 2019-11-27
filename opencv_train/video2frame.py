#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 15:24:09 2019

@author: gomesfellipe
"""
import os
os.getcwd()

# Converter de mov para mp4 as positivase negativas (no terminal):
# ffmpeg -i /Users/gomesfellipe/Documents/opencv_train/convert_mov2mp4/positive.MOV /Users/gomesfellipe/Documents/opencv_train/convert_mov2mp4/positive.mp4
# ffmpeg -i /Users/gomesfellipe/Documents/opencv_train/convert_mov2mp4/negative.MOV /Users/gomesfellipe/Documents/opencv_train/convert_mov2mp4/negative.mp4

import cv2
  
def get_imagem_from_mp4(img):
    vidcap = cv2.VideoCapture('convert_mov2mp4/'+img+'.mp4')
    success,image = vidcap.read()
    count = 0
    while success:
      cv2.imwrite(img+"_images/frame%d.jpg" % count, image)     # save frame as JPEG file      
      success,image = vidcap.read()
      print('Read a new frame: ', success)
      count += 1 
      
get_imagem_from_mp4(img='positive')
get_imagem_from_mp4(img='negative')