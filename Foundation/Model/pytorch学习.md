```python
# pytorch 实现 LeNet网络, 基本的前向传输网络

# LeNet 输入图像为 32 * 32
# 第一层 6个卷积核，5*5，stride = 1 ， 输出为（32-5）/1 +1 = 28,通道为6
# 激活，然后，2*2池化，28/2=14,6个14*14图

# 第二层 16个卷积核，卷积核5*5，输出为 (14-5)+1=10,通道为16
# 激活，池化层2*2,10/2=5，16个


import torch.nn as nn
import torch.nn.functional as F

# nn.Module 子类的函数必须在构造函数中执行父类的构造函数
class Net(nn.Module):
    def __init__(self):  
        super(Net,self).__init__() # 等价于nn.Module.__init__(self)
        
        # '1'表示输入图片为单通道，'6'表示输出通道数，'5'表示卷积核为 5*5
        self.conv1 = nn.Conv2d(1,6,5)
        
        # 卷积层
        self.conv2 = nn.Conv2d(6,16,5)
        
        # 全连接层 y =  Wx + b
        self.fc1 = nn.Linear(16*5*5,120)
        self.fc2 = nn.Linear(120,84)
        self.fc3 = nn.Lineaar(84,10)
        
    def forward(self,x):
        # 卷积 -> 激活 -> 池化
        x = F.max_pool2d(F.relu((self.conv1(x)),(2,2))
        x = F.max_pool2d(F.relu(self.conv2(x)),2) 
        
        # 改变维度 , -1为自适应, x.size(0)是batch size
        # 比如原来的数据一共12个，batch size为2                【?】
        # 就会view成2*6，batch size为4,就会就会view成4*3      【?】         
        x = x.view(x.size()[0],-1)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))   
        x = self.fc3(x)
        return x
net = Net()        
print(net)        
        
        
```

