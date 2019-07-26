- 网络初始参数借鉴了MSRA何凯明的文章，参数均服从高斯分布，网络的基础结构是AlexNet , 一共5层

| 层   | 卷积核                  | 步长 |
| ---- | ----------------------- | ---- |
| c1   | 96   个 **11 x 11 x 3** | 4    |
| c2   | 256 个 **5 x 5 x 48**   | 1    |
| c3   | 384 个 **3 x 3 x 256**  | 1    |
| c4   | 384 个 **3 x 3 x 192**  | 1    |
| c5   | 256 个 **3 x 3 x 192**  | 1    |

- 3D卷积

​	



- 损失函数

$$
l(y,v) = log(1 + exp(-yp) )\\
L(y,v) = \frac{1}{|D|}\sum_{u\in D} l(y[u],v[u])
$$

 	$u \in D$ 是得分图谱的位置，$v[u]$是这个位置做相关操作后的值$ v = f(z,x;\theta)$ , $y[u]$ 是这个位置的标签，取{+1,-1} 。

​	
$$
\begin{equation}
y[u]=\left\{
\begin{aligned}
+1   && if k||u-c|| \ \cos(t) \\
y & = & \sin(t) \\
z & = & \frac xy
\end{aligned}
\right.
\end{equation}
$$
