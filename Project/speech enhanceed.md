#### 记录

先将纯净语音按照不同的信噪比添加噪声，生成噪音文件。



提取特征



15个测试、15个验证

1~270    训练      24个叠加  （不同信噪比）

271 285 验证      24个叠加  （不同信噪比）

286 300 测试





#### 具体

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
      
      db = [-5, 0 , 5 , 10 ] :
      
      for ttl = 1: 6                   % 噪声类型
      	for tt2 = 1:7                % db
      		name = tt{tt1}:
      % clean 语音的数目
      for i = 1:100
      
      % clean语音路径，
      infilename = ['F:\\'num2str(i)'.wav']:         
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

    - [ ] 提取特征，使用teacherstft.m

      - [ ] 提取噪声特征 xx1.mat           270/300
      - [ ] 提取干净特征 yy1.mat           15/300
      - [ ] 提取测试集特征 zz1.mat        15/300

      ```matlab
       %% 提取MFCC语音特征
       
      clear;
      xx = [];
      
      %load jisuanx
      %js=[]
      %js1=[]
       tt=cell(1,6);
      tt{1}='white';
      tt{2}='f16';
      tt{3}='factory';
      tt{4}='pink';
      tt{5}='hfchannel';
      tt{6}='babble';
      
       db=[-5,0,5,10] ;
       for tt1=1:6                        % 类型
           for tt2=1:4                    % db
             name=tt{tt1};
      	   	   
      for i = 1:270       % 只选择前270句作为训练集
       infilename1 = ['F:\Project\噪音\' name '\' num2str(db(tt2)) '\'  num2str(i) '.wav'];            % 噪声地址
       [speech.clean1,nfs] = audioread(infilename1);
       wav1 = speech.clean1;
       wav1=resample(wav1,16000,nfs);  % 采样频率16000
       nfs=16000;
      ttt=i;
      
      
      L = 512; % frame length   帧长
      nfft = 512;% DFT size     数据量的大小，一般为2的n次方，512,1024
      hopfactor = 2;
      inc =256; % frame advance 帧移，一般为帧长的一半
      hopfactor = L/(L-inc);
      InterpMultiple = 1;
      
      
      stopdB =150;
      a       = 0.50;
      b       = -0.50;
      n       = 1:L;
      S       = L/hopfactor; %hop size
      MaxIter = 300;
      
      win     = sqrt(S)/sqrt((4*a^2+2*b^2)*L)*(a+b*cos(2*pi*n/L));
      win     = win(:);
      window  = win;
      
      YY=stft(wav1,window,inc,nfft); % 快速傅里叶变换 从时域数据转变为频域数据，Y = 129 * 354
      Y=abs(YY);%+ 0.000000001*rand(size(Y,1),size(Y,2));
      
        xx = [xx;Y'];                % | 第一种语音信噪比 | 2 | 3 | 4 | 5 |
      end
          end
      
      
      end
      % end
      
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
