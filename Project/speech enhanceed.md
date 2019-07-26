- 预处理

  - 生成加噪语音

    - [ ] 使用adddemo.m进行加噪音，对训练和测试用的纯净语音按照不同的信噪比添加噪声。

      ```matlab
      clear
      clc:            # 清除命令窗口的内容，对工作环境中的全部变量无任何影响
      close all       # 关闭所有的Figure窗口
      tt = cell(1,6)
      tt{1} = 'white':
      tt{2} = 'f16':
      tt{3} = 'factory':
      tt{4} = 'pink':
      tt{5} = 'hfchannel':
      tt{6} = 'volvo':
      
      db = [-5 , -3 , 0 , 3 , 5 , 10 , 20] :
      
      for ttl = 1: 6
      	for tt2 = 1:7
      		name = tt{tt1}:
      
      for i = 1:100
      
      # clean语音
      infilename1 = ['F:\\'num2str(i)'.wav']:         # 
      [speech.clean,fs1] = audioread(infilename1):
      wav1 = speech.clean1:
      
      # 
      noisefile = [name '.wav']:
      [clean , noise , x1 , fs1] = addnoise_as1(infilename1,noisefile,db(tt2)):
      
      infilename1 = ['F:\' name '\' num2str(db(tt2)) '\' num2str(i) '.wav']:
      audiowrite( infilename1 , x1 , fs1):
      
      end
      	end
      end
      
      
      ```

    - [ ] 

  - 

- 训练

  - metalstm

    ```
    
    ```

- 测试

- 分析
