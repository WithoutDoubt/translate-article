- LPCTron](<https://github.com/alokprasad/LPCTron>)

- [Rnnoise](https://people.xiph.org/~jm/demo/rnnoise/)

- [代码解读](<https://zhuanlan.zhihu.com/p/34757119>)

- [python标准库](<https://blog.csdn.net/qq_41804164/article/details/81448207>)

- [标准](<https://www.pypandas.cn/docs/getting_started/10min.html#%E6%9F%A5%E7%9C%8B%E6%95%B0%E6%8D%AE>)

- [代码解读2](<https://github.com/mozilla/TTS>)

- [语音合成综述](<https://blog.csdn.net/SoundSlow/article/details/82835106>)

- datasets
  - ``__init__``
  - biazzard.py 【大批量】
    - [ ] 
  - datafeeder.py 【】
  - ljspeech.py 【】

- 预处理的代码

- pytorchTTS 【**使用pytorch来运行**】

  - text文件夹
    - [ ] ``__init__.py`` : text文件的预处理，文本预处理代码
      - [ ] 
    - [ ] 
  - hyperparams.py                  
    - [ ] 包括所有需要的超参数。

  - data.py                                  
    - [ ] 加载训练数据并将文本预处理为索引，将wav文件预处理为谱图。
  - mudule.py
    - [ ] 包含所有方法，包括CBHG、高速公路、prenet等。
  - network.py
    - [ ] 包含网络，包括编码器、解码器和后处理网络。
  - train.py
    - [ ] 训练
  - synthesis.py
    - [ ] 用于生成TTS样本。

- 