- 预处理

  - 生成加噪语音

    - [ ] 使用adddemo.m进行加噪音，对训练和测试用的纯净语音按照不同的信噪比添加噪声。

      ```matlab
      clear
      clc:            % 清除命令窗口的内容，对工作环境中的全部变量无任何影响
      close all       % 关闭所有的Figure窗口
      
      
      %% 噪音文件应该与 加噪文件在同一路径下，直接是 .wav 文件就行
      tt = cell(1,6)
      tt{1} = 'white':
      tt{2} = 'f16':
      tt{3} = 'factory':
      tt{4} = 'pink':
      tt{5} = 'hfchannel':
      tt{6} = 'volvo':
      
      db = [-5 , -3 , 0 , 3 , 5 , 10 , 20] :
      
      for ttl = 1: 6                   % 噪声类型
      	for tt2 = 1:7                % db
      		name = tt{tt1}:
      % clean 语音的数目
      for i = 1:100
      
      % clean语音路径，
      infilename = ['F:\\'num2str(i)'.wav']:         # 
      [speech.clean,fs1] = audioread(infilename1):
      wav1 = speech.clean1:
      
      %
      noisefile = [name '.wav']:
      [clean , noise , x1 , fs1] = addnoise_as1(infilename1,noisefile,db(tt2)):
      
      %生成的文件，路径文件夹需要是 噪声名/信噪比
      infilename1 = ['F:\' name '\' num2str(db(tt2)) '\' num2str(i) '.wav']:
      audiowrite( infilename1 , x1 , fs1):
      
      end
      	end
      end
      
      
      ```

    - [ ] 归一化

    - [ ] 

  - 

- 训练

  - metalstm

    ```
    
    ```

- 测试

- 分析
