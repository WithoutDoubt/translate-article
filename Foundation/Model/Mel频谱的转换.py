sr = 24000                                                                                   # Sample rate.           采样率
n_fft = 2048                                                                                 # fft points (samples)   样本点 FFT的计算，样本数取2的整数幂
frame_shift = 0.0125                                                                         # seconds              帧移  12.5ms    
frame_length = 0.05                                                                          # seconds               帧长  50 ms
hop_length = int(sr*frame_shift)          # samples.设置跳跃长度;在22050Hz，512个样本〜= 23ms

win_length = int(sr*frame_length)         # samples.          
                                                                                             # 每个音频帧都由window（）加窗。
                                                                                             # 窗口的长度为win_length，然后用零填充以匹配n_fft。
                                                                                             # 如果未指定，则默认为win_length = n_fft。                                
n_mels = 512                              # Number of Mel banks to generate                   要生成的梅尔bank 数量
power = 1.2                               # Exponent for amplifying the predicted magnitude   用于放大预测幅度的指数
n_iter = 100                              # Number of inversion iterations                    反演迭代次数
preemphasis = .97 # or None                                                                   预加重
max_db = 100                              #                                                   峰值功率
ref_db = 20                               #                                                   参考功率。默认情况下，它使用np.max并与信号中的峰值功率进行比较
top_db = 15                               #                                                   低于参考的阈值（以分贝为单位）视为静音


def get_spectrograms(fpath):
    '''Returns normalized log(melspectrogram) and log(magnitude) from `sound_file`.
    Args:
      sound_file: A string. The full path of a sound file.

    Returns:
      mel: A 2d array of shape (T, n_mels) <- Transposed                           mel：形状为 2d 的数组（T，n_mels）< - 转置
      mag: A 2d array of shape (T, 1+n_fft/2) <- Transposed                        mag：形状为 2d 的数组（T，1 + n_fft / 2）< - 转置
 '''
    # Loading sound file
    y, sr = librosa.load(fpath, sr=sr)

    # Trimming                                                                    修剪音频信号的前导和尾随静音。  hop_length分析框架之间的样本数量
    y, _ = librosa.effects.trim(y, top_db=top_db)                                 # y 为 裁剪过的音频

    # Preemphasis                                                                 # 预加重
    y = np.append(y[0], y[1:] - preemphasis * y[:-1])                             # append(arr , values , axis = None) , arr 和 value重新组合
                                                                                  # y(n) = x(n)-ax(n-1)    
    # stft
    linear = librosa.stft(y=y,                                                    # 短时傅里叶变换
                          n_fft=n_fft,
                          hop_length=hop_length,
                          win_length=win_length)

    # magnitude spectrogram                                                          幅度谱图
    mag = np.abs(linear)                                                          # (1+n_fft//2, t)   np.abs() 绝对值

    # mel spectrogram                                                               Mel谱图    return 梅尔变换矩阵
    mel_basis = librosa.filters.mel(sr, n_fft, n_mels)                            # (n_mels, 1+n_fft//2)
    mel = np.dot(mel_basis, mag)                                                  # (n_mels, t) 矩阵乘法dot

    # to decibel
    # np.maximum：(X, Y, out=None)   X 与 Y 逐位比较取其大者；
    # np.log () 取对数
    # * 是逐个元素相乘
    # dot 是矩阵相乘
    mel = 20 * np.log10(np.maximum(1e-5, mel))
    mag = 20 * np.log10(np.maximum(1e-5, mag))                    

    # normalize                                                                     标准化  np.clip( X , a_min , a_max )
    mel = np.clip((mel - ref_db + max_db) / max_db, 1e-8, 1)                      # clip 是限制 在 a_min , a_max 
    mag = np.clip((mag - ref_db + max_db) / max_db, 1e-8, 1)                      # clip 是限制 在 a_min , a_max

    # Transpose
    mel = mel.T.astype(np.float32)                                                # (T, n_mels)      mel谱
    mag = mag.T.astype(np.float32)                                                # (T, 1+n_fft//2)  幅度谱

    return mel, mag





def melspectrogram2wav(mel):
    "Mel 谱 转为 语音"
    '''# Generate wave file from spectrogram'''
    # transpose                                                                转置
    mel = mel.T

    # de-noramlize                                                             去标准化
    mel = (np.clip(mel, 0, 1) * max_db) - max_db + ref_db

    # to amplitude                                                             幅度谱
    mel = np.power(10.0, mel * 0.05)
    m = _mel_to_linear_matrix(sr, n_fft, n_mels)                             # Mel谱 到 频率谱的转换
    mag = np.dot(m, mel)

    # wav reconstruction                                                        wav 重建
    wav = griffin_lim(mag)                                                   # 幅度谱重建语音

    # de-preemphasis                                                         # 消去去重，使用IIR或FIR滤波器沿一维过滤数据。
    wav = signal.lfilter([1], [1, -preemphasis], wav)

    # trim                                                                   # 剪
    wav, _ = librosa.effects.trim(wav)

    return wav.astype(np.float32)                                            # 

def spectrogram2wav(mag):                                                   # mag 转 语音 
    '''# Generate wave file from spectrogram'''
    # transpose
    mag = mag.T

    # de-noramlize
    mag = (np.clip(mag, 0, 1) * max_db) - max_db + ref_db

    # to amplitude
    mag = np.power(10.0, mag * 0.05)                                       # 10.0 的（mag*0.05）次方

    # wav reconstruction
    wav = griffin_lim(mag)

    # de-preemphasis
    wav = signal.lfilter([1], [1, -preemphasis], wav)

    # trim
    wav, _ = librosa.effects.trim(wav)

    return wav.astype(np.float32)


def _mel_to_linear_matrix(sr, n_fft, n_mels):          # Mel 频率到 linear 频率 刻度的转换
    m = librosa.filters.mel(sr, n_fft, n_mels)
    m_t = np.transpose(m)                              # 矩阵转置
    p = np.matmul(m, m_t)                              # 矩阵相乘，只允许矩阵相乘
    d = [1.0 / x if np.abs(x) > 1.0e-8 else x for x in np.sum(p, axis=0)]
    return np.matmul(m_t, np.diag(d))

def griffin_lim(spectrogram):
    '''Applies Griffin-Lim's raw.                  适用于Griffin-Lim的原始版本
    '''
    X_best = copy.deepcopy(spectrogram)           # 深度复制，就是独立存在一个
    for i in range(n_iter):                       # 反演迭代次数
        X_t = invert_spectrogram(X_best)          # 
        est = librosa.stft(X_t, n_fft, hop_length, win_length = win_length)
        phase = est / np.maximum(1e-8, np.abs(est))  # 估计相位

        X_best = spectrogram * phase                 # 频域里面，复数计算就是使用 相位直接相乘
    X_t = invert_spectrogram(X_best)                 # 重建时域
    y = np.real(X_t)                                 # 返回实部

    return y


def invert_spectrogram(spectrogram):
    '''
    从stft_matrix重建的时域信号
    spectrogram: [f, t] 复数值谱图stft_matrix转换为时间序列y

    返回一个秩为1的数组
    '''
    return librosa.istft(spectrogram, hop_length, win_length=win_length, window="hann")
