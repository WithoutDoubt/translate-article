**常见库**

- [ ] numpy
- [ ] pandas  pandas 是基于[NumPy](https://baike.baidu.com/item/NumPy/5678437) 的一种工具，该工具是为了解决数据分析任务而创建的，主要是时间序列。
- [ ] Scipy
- [ ] tqdm  进度条美化的基本方法

#### numpy

支持大量的维度数组与矩阵运算，此外针对数组运算提供大量的数学函数库

- [ ] N维数组对象ndarray
- [ ] 广播功能函数
- [ ] 线性代数、傅里叶变换、随机数生成等功能

```python
# 切片，索引
a = np.array( [ [1,2,3],[4,5,6],[7,8,9]  ])
b = a[1:3 , 1:3]  # 取2，3行，       取2，3列
c = a[:,1:3]      # 取1，2，3行      取2，3列
```

```python
numpy.array (object , dtype = None ,copy = True , order = None , subok = False, ndmin = 0)

# object   数组或嵌套的数列 
# dtype    数组元素的数据类型，可选
# copy     对象是否需要复制
# order    创建数组的样式，C为行方向，F为列方向，A为任意方向（默认）
# subok    默认返回一个与基类类型一致的数组
# ndmin    制定生成数组的最小维度
```

- 数据类型

- 数组属性

  - [ ] ``axis=0`` 是按列进行操作，``axis=1`` 是按行进行操作

  | 属性                 |                                                 |
  | -------------------- | ----------------------------------------------- |
  | ``ndarray.ndim``     | 秩，维度                                        |
  | ``ndarray.shape``    | 数组的维度，对于矩阵，n行m列                    |
  | ``ndarray.size``     | 数组元素的总个数，相当于n*m                     |
  | ``ndarray.dtype``    | ``ndarray``对象的元素类型                       |
  | ``ndarray.itemsize`` | ``ndarray``对象中每个元素大的大小，以字节为单位 |
  | ``ndarray.flags``    | ``ndarray``对象的内存信息                       |
  | ``ndarray.real``     | ``ndarray``元素的实部                           |
  | ``ndarray.imag``     | ``ndarray``元素的虚部                           |
  | ``ndarray.data``     | 一般不用                                        |

  ```python
  a = np.arange(24)      
  
  # 返回一个 0~23 的列
  #[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
  
  
  b = a.reshape(2,4,3)   # 调整大小，3维的， 2个  4 行 3 列 的矩阵
  b.ndim                 # 维度为3
  ```

- 创建数组

  ```python
  numpy.empty(shape , dtype = float , order = 'C')  #  C  行优先
  ```

  ```python
  numpy.zeros()
  ```

  ```python
  numpy.ones()      # 全是1
  ```

- 从已有数组创建数组

  ```python
  numpy.asarray()
  ```

- 从数值范围创建数组

  ```python
  numpy.arange(start,stop,step,dtype)
  # 创建一个数列
  
  # 起始值 默认为0
  # 终止值 （不包含）
  # 步长  默认为1
  # 数据类型
  ```

  ```python
  numpy.linspace(start,stop,num=50, endpoint = True , restep = False, dtype = None)
  # 创建一个一位数组，数组是一个等差数列构成的
  
  # start 序列的起始值
  # stop 的终止值，如果endpoint为true,改值包含于数列中
  # num 要生成的等步长的样本数量，默认为50
  # 该值为ture时，数列中包含stop值，反之不包含，默认为true
  # 如果为Ture时，生成的数组中会显示间距，反之不显示
  # ndarray 数据类型
  ```

  ```python
  numpy.logspace(start,stop,num=50, endpoint = True ,base = 10.0, dtype = None)
  # 创建一个等比数列，
  
  # start ，值为 base**start （阶乘）
  # stop ， 值为 base**stop （阶乘）
  # base 为 下标 ， 对数log的底数
  # 
  ```

- 切片和索引

  ```python
  import numpy as np
  
  a = np.arange(10)
  b = a[2:7:2] # 索引从2开始，到7停止（不包括7），间隔为2
  print (b)
  ```

  ``:``  表示索引

  ``…``  来使选择元组的长度和数组的维度相同。【选择全部的意思】

  ```python
  import numpy as np
  a = np.array([[1,2,3],[3,4,5],[4,5,6]])
  print (a[...,1])  #第2列元素
  print (a[1,...])  #第2行元素
  print (a[...,1:]) #第2列及剩下的所有元素
  ```

- numpy高级索引

- numpy广播

- numpy迭代数组

- **numpy数组操作**

  ```python
  numpy.reshape(arr, newshape, order='C')
  # newshape:新的形状
  # order  Column  行  F  列
  ```

  ```python
  numpy.transpose(arr , axes)
  
  np.transpose(a) == a.T   # 示例
  # 转置
  ```

- numpy位运算

- numpy字符串函数

- numpy数学函数

- numpy算术函数

- nuuumpy

#### Scipy （scientific Python）

是一个数学工具包，包括最优化、线性代数、积分、插值、特殊函数、快速傅里叶变换、信号处理和图像处理、常微分方程求解和其他科学与工程中常用的计算

#### Matplotlib

绘图库