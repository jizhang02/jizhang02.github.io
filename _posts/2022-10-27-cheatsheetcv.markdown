---
layout:     post
title:      "Cheatsheet on CS"
subtitle:   "常用命令速查表"
date:       2022-10-27
author:     "Jing"
header-img: "img/post-bg.jpg"
tags:
    - Computer Science
    - Programming
    - opengate

---


In this article, the author records some commands and codes under Ubuntu, Python, Anaconda and some specific applications. Some sentences are mixed with Chinese language for one's own convienience. It will be updated from time to time.


####  Pytorch
* `torch.cuda.is_available()` 查看是否支持cuda
* 主函数中：
`torch.backends.cudnn.deterministic = True`  用以保证实验的可重复性
#### Conda
* 查看版本 `conda --version`
* 查看环境 `conda env list`
* 安装某个版本 `conda install python==3.6` 
* 复制环境 `conda create -n 新环境名 --clone 旧环境名`
* 删除原环境 `conda remove -n 旧环境名 --all`
* 激活环境 `conda activate 环境名`
* 关闭环境 `conda deactivate`
* 导出环境 到另一个机器 
  * `conda env export > 环境名.yaml`
  * `conda env create -f 环境名.yaml`
#### Python
* 打印版本信息 `print(sys.version)`
* 打印所有文件 `print(glob.glob("path/*.mhd"))`
* 双循环 `for x, y in zip(directory_image, directory_label):`
* 3 interpreters/environments
  * Windows->Anaconda->base Python3.8 _for basics_
  * Windows->Anaconda->pp   Python3.8 _for TODO_
  * Ubuntu->Anaconda->mc    Python3.8 _for opengate_
#### Terminal
* 查看ip地址 `hostname -I`
* 查看ssh `ps -ef | grep ssh`
* 查看python版本 `python --version`
* 查看GPU信息 `nvidia-smi` 
* 列出可用GPU `nvidia-smi -L` 
* 新建文件 `touch test.py`
* 编辑文件 `vi test.py`
* 回到home `cd ~`
* 运行sh文件 `bash xxx.sh`
* 在PyCharm的Terminal输入Ubuntu，进入到Ubuntu的Terminal
* 修改环境变量  `sudo vim /home/jing/.bashrc`
* 使之生效 `source ~/.bashrc`
* 更新算计 `pip install opengate -U`
* 卸载软件 `sudo apt-get remove --auto-remove qtcreator`
#### WSL=Windows subsystom linux
* A good subsitute for vmware virtual machine.
* 动态IP地址设置为静态 [solution](https://github.com/microsoft/WSL/issues/4150#issuecomment-504209723)-> failed.
* version ` wsl -l -v`
#### Opengate
* GitHub https://github.com/OpenGATE/opengate
* Opengate data path _/home/jing/anaconda3/envs/mc/lib/python3.8/site-packages/opengate/tests/data_
* test files _/home/jing/anaconda3/envs/mc/lib/python3.8/site-packages/opengate/tests/src_
* two parts
  * opengate_core -> C++ based
  * opengate -> Python based 
* Units

      millimeter              (mm)        毫米
      nanosecond              (ns)        纳秒
      Mega electron Volt      (MeV)       兆电子伏特
      positron charge         (eplus)     正电子电荷
      degree Kelvin           (kelvin)    温度计量单位
      the amount of substance (mole)      摩尔，物质的量
      luminous intensity      (candela)   坎德拉，发光强度
      radian                  (radian)    弧度
      steradian               (steradian) 球面度
      Becquerel               (Bq)        贝克，放射性活度，每秒衰变的原子个数
* 运行程序前设置环境变量 `sudo vim /home/jing/.bashrc`
* Simulation
  * Geometry
  * Physics
  * Source
  * Actions
* Stats

      NumberOfRun               = 1
      NumberOfEvents            = 20000
      NumberOfTracks            = 103511
      NumberOfSteps             = 726120
      NumberOfGeometricalSteps  = 27558
      NumberOfPhysicalSteps     = 698562
      PPS (Primary per sec)     = 7998.91
      TPS (Track per sec)       = 41398.7
      SPS (Step per sec)        = 290408
