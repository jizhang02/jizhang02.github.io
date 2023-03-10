---
layout:     post
title:      "Transformer's past and present."
subtitle: "Transformer的前世今生"
date:       2021-09-08 17:16:00
author:     "Jing"
header-img: "img/post-bg.jpg"
tags:
    - Computer Science
    - Deep Learning
    - Transformer
---

### Let you know the principle of AI models from excellent works
This post is an introduction to the Transformer, in terms of its origin, application and development.
![roadmap](/img/20210908_transformer.png)

## ![#60A917](https://via.placeholder.com/60/60A917/FFFFFF?text=2015) RNN 2015
⭐ Sequence to sequence model with attention mechanism, to avoid forgeting too long vectors, compute each vector's weight (correlation) of decoder with all the vectors in encoder. Machine Translation, Natural Language Processing (NLP)    
📄 [Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473), 2015
## ![#1BA1E2](https://via.placeholder.com/60/1BA1E2/FFFFFF?text=2016) RNN 2016    
⭐ Self-Attention model, not limited in sequence to sequence model.   
📄 [Long Short-Term Memory-Networks for Machine Reading](https://arxiv.org/abs/1601.06733), 2016
## ![#6A00FF](https://via.placeholder.com/60/6A00FF/FFFFFF?text=2017) Transformer 2017
⭐ Attention without RNN, in other words, it consists of Attention and Self-Attention layers only.    
📄 [Attention is all you need](https://proceedings.neurips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf), 2017
## ![#FA6800](https://via.placeholder.com/60/FA6800/000000?text=2021) Vision Transformer 2021
⭐ It uses Transformer (encoder part) to do the image classification task. It split the image into small patches as input, and record the position infomation of each patch. It performs well if pretrained on large datasets (more than 100 million). Short for ViT.     
📄 [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](https://arxiv.org/abs/2010.11929), 2021
## ![#0050EF](https://via.placeholder.com/60/0050EF/FFFFFF?text=2021) Vision Transformer in segmentation 2021
⭐ It first uses Transformer to do the image segmentation task. At the same time, it combines the CNN in encoder part to better restore the low level information, in decoder part, it also uses CNN.    
📄 [TransUNet: Transformers Make Strong Encoders for Medical Image Segmentation](https://arxiv.org/abs/2102.04306), 2021-02-08    
📄 [Medical Transformer: Gated Axial-Attention for Medical Image Segmentation](https://arxiv.org/abs/2102.10662), 2021-02-21   
📄 [CoTr: Efficiently Bridging CNN and Transformer for 3D Medical Image Segmentation](https://arxiv.org/abs/2103.03024), 2021-03-04   
📄 [TransBTS: Multimodal Brain Tumor Segmentation Using Transformer](https://arxiv.org/abs/2103.04430), 2021-03-07    
📄 [UNETR: Transformers for 3D Medical Image Segmentation](https://arxiv.org/abs/2103.10504), 2021-03-18    
📄 [Pyramid Medical Transformer for Medical Image Segmentation](https://arxiv.org/abs/2104.14702), 2021-04-29     
📄 [Swin-Unet: Unet-like Pure Transformer for Medical Image Segmentation](https://arxiv.org/abs/2105.05537), 2021-05-12    
📄 [UTNet: A Hybrid Transformer Architecture for Medical Image Segmentation](https://arxiv.org/abs/2107.00781), 2021-07-02    
📄 [DS-TransUNet:Dual Swin Transformer U-Net for Medical Image Segmentation](https://arxiv.org/abs/2106.06716), 2021-07-12    
📄 [TransAttUnet: Multi-level Attention-guided U-Net with Transformer for Medical Image Segmentation](https://arxiv.org/abs/2107.05274), 2021-07-12    
📄 [UCTransNet: Rethinking the Skip Connections in U-Net from a Channel-wise Perspective with Transformer](https://arxiv.org/abs/2109.04335), 2021-09-09   
📄 [nnFormer: Interleaved Transformer for Volumetric Segmentation](https://arxiv.org/abs/2109.03201), 2021-09-07    
📄 [MISSFormer: An Effective Medical Image Segmentation Transformer](https://arxiv.org/abs/2109.07162v1), 2021-09-15              
📄 [Transformer-Unet: Raw Image Processing with Unet](https://arxiv.org/abs/2109.08417), 2021-09-17     
📄 [VT-UNet: A Robust Volumetric Transformer for Accurate 3D Tumor Segmentation](https://arxiv.org/pdf/2111.13300.pdf), 2021-11-26         
📄 [Advances in Medical Image Analysis with Vision Transformers: A Comprehensive Review](https://arxiv.org/pdf/2301.03505.pdf), 2023-01-10, 63 pages!      

👉 Acknowledgements: [Wang Shusen](https://youtu.be/aButdUV0dxI)
