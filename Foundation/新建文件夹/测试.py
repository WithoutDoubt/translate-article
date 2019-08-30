sr = 24000         # Sample rate.           采样率
n_fft = 2048       # fft points (samples)   样本点
frame_shift = 0.0125 # seconds              帧移  12.5ms    
frame_length = 0.05  # seconds               帧长  50 ms
hop_length = int(sr*frame_shift)          # samples.设置跳跃长度;在22050Hz，512个样本〜= 23ms

win_length = int(sr*frame_length)         # samples.
n_mels = 512                              # Number of Mel banks to generate  要生成的梅尔银行数量
power = 1.2                               # Exponent for amplifying the predicted magnitude 用于放大预测幅度的指数
n_iter = 100                              # Number of inversion iterations    反演迭代次数
preemphasis = .97 # or None                 预加重
max_db = 100                              # 峰值功率
ref_db = 20                               # 参考功率。默认情况下，它使用np.max并与信号中的峰值功率进行比较
top_db = 15                               # 低于参考的阈值（以分贝为单位）视为静音


def get_spectrograms(fpath):
    '''Returns normalized log(melspectrogram) and log(magnitude) from `sound_file`.
    Args:
      sound_file: A string. The full path of a sound file.

    Returns:
      mel: A 2d array of shape (T, n_mels) <- Transposed                           mel：形状为2d的数组（T，n_mels）< - 转置
      mag: A 2d array of shape (T, 1+n_fft/2) <- Transposed                        mag：形状为2d的数组（T，1 + n_fft / 2）< - 转置
 '''
    # Loading sound file
    y, sr = librosa.load(fpath, sr=sr)

    # Trimming   修剪音频信号的前导和尾随静音。  hop_length分析框架之间的样本数量
    y, _ = librosa.effects.trim(y, top_db=top_db)                                 # y 为 裁剪过的音频

    # Preemphasis                                                                 # 预加重
    y = np.append(y[0], y[1:] - preemphasis * y[:-1])                             # append(arr , values , axis = None) , arr 和 value重新组合
                                                                                  # y(n) = x(n)-ax(n-1)    
    # stft
    linear = librosa.stft(y=y,                                                    # 
                          n_fft=n_fft,
                          hop_length=hop_length,
                          win_length=win_length)

    # magnitude spectrogram                                                          幅度谱图
    mag = np.abs(linear)                                                          # (1+n_fft//2, T)

    # mel spectrogram                                                               Mel谱图    return 梅尔变换矩阵
    mel_basis = librosa.filters.mel(sr, n_fft, n_mels)                            # (n_mels, 1+n_fft//2)
    mel = np.dot(mel_basis, mag)                                                  # (n_mels, t) 矩阵乘法dot

    # to decibel
    mel = 20 * np.log10(np.maximum(1e-5, mel))
    mag = 20 * np.log10(np.maximum(1e-5, mag))

    # normalize                                                                     正则化
    mel = np.clip((mel - ref_db + max_db) / max_db, 1e-8, 1)                      # clip 是限制 在 a_min , a_max 
    mag = np.clip((mag - ref_db + max_db) / max_db, 1e-8, 1)                      # clip 是限制 在 a_min , a_max

    # Transpose
    mel = mel.T.astype(np.float32)    # (T, n_mels)
    mag = mag.T.astype(np.float32)    # (T, 1+n_fft//2)

    return mel, mag