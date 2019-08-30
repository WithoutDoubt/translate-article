#### 0.7版本

librosa.core.stft

```python
librosa.core.stft(
	y,                 # 输入信号（音频时间序列）
    n_fft = 2048,      # FFT窗口大小
    hop_length = None, # STFT列之间的帧数音频。如果未指定，则默认为 win_length/4。
    				   # （卷积的stride）两个分割帧（窗口）的间距，23ms 或 512 采样点						
    win_length = None, # 每个音频帧都由window（）加窗。
                       # 窗口的长度为win_length，然后用零填充以匹配n_fft。
                       # 如果未指定，则默认为win_length = n_fft。
    window = 'hann'    
    
    center = True      # 如果为真，则填充信号y，使得帧D [：，t],以y [t * hop_length]为中心。
                       # 如果为False，则D [：，t]从y [t * hop_length]开始v
    
    dtype  = <class 'numpy.complex64'>
    
    pad_mode = 'reflect' # 如果center = True，则在信号边缘使用填充模式。
                         # 默认情况下，STFT使用反射填充。
    


)

return  D 
# STFT矩阵  shape=(1 + n_fft/2 , t)

# np.abs(D[f, t]) is 是帧 t 处的频率bin f的幅度大小
# np.angle(D[f, t]) is 是帧 t 处的频率bin f的相位
```

librosa.effects.trim

修剪音频信号的前导和尾随静音。

```python
librosa.effects.trim(
	y,
    top_db = 60  # 低于参考的阈值（以分贝为单位）视为静音
    ref=<function amax at 0x7f3faa085bf8>, 
    # 参考功率。       
    # 默认情况下，它使用np.max并与信号中的峰值功率进行比较。
    frame_length=2048,   # 每个分析框架的样本数
    hop_length = 512     # 分析框架之间的样本数量
    
)
y , _ = librosa.effects.trim(y, top_db=top_db)    
return 
# y
# _
```

librosa.filters.mel

创建一个Filterbank矩阵，将FFT二进制数组合成Mel频率二进制数

```python
librosa.filters.mel(
	sr,                       # 输入信号的采样率
    n_fft,                    # FFT组件的数量
    n_mels = 128,             # 要生成的Mel波段数
    fmin = 0.0,               # 最低频率（Hz）
    fmax = None,              # 最高频率（Hz）。如果为None，请使用fmax = sr / 2.0
    htk = False,              # 使用HTK公式代替Slaney
    norm = 1,                 # 如果为1，则将三角形mel权重除以mel band的宽度（面积归一化）。
							  # 否则，将所有三角形保留为峰值1.0
    dtype = <class 'numpy.float32'>

)

return  M        # shape(n_mels , 1 + n_fft/2)
                 # 梅尔变换矩阵         
```

