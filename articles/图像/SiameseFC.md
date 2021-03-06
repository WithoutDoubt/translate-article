- Abstract

  任意对象跟踪的问题传统上都是通过专门在线学习对象外观的模型来解决的，使用视频本身作为唯一的训练数据。尽管这些方法很成功，他们的在线学习的方式固有的限制了他们可以学习的模型的丰富性。最近，近年来，人们对深层卷积网络的表现力进行了尝试。然而，如果事先不知道要跟踪的对象，则需要在线执行随机梯度下降，以适应网络的权重，严重影响系统的速度。在这篇文章中，我们在ILSVRC 15数据集上配置了一种全新的完全卷积暹罗网络，用于视频中的目标检测。我们的跟踪器以超过实时的帧速率运行，尽管它非常简单，却在多个基准中实现了最先进的性能。

- Introduction

  我们考虑视频中任意目标的跟踪问题，其中目标仅由第一帧中的一个矩形来识别。由于该算法可能被要求跟踪任何任意对象，因此不可能已经收集到数据并训练了特定的检测器。

  几年来，这个场景最成功的范例是使用从视频本身提取的示例来学习对象的在线外观模型[1]。这在很大程度上归功于TLD[2]、SIM[3]和KCF[4]等方法的能力。然而，使用目前视频中的数据的一个明显缺陷是，只能学习相对简单的模型。尽管计算机视觉中的其他问题越来越普遍地采用由大型监督数据集训练的深卷积网络(conv-net)，但监督数据的缺乏。同时，实时操作的限制也阻止了深度学习在这种学习每个视频检测器的范式中的简单应用。

  最近的工作都是为了克服这一局限，它使用了一个预先训练过的深层控制网，它是为不同但相关的任务而学习的。这些方法要么应用“浅层”方法(例如相关滤波器)，利用网络的内部表示作为特征[5，6]，要么执行SGD(随机梯度下降)对微调多层网络[7，8，9]。虽然浅层方法的使用并没有充分利用端到端学习的好处，但是在跟踪过程中应用sgd以获得最先进的结果的方法却无法做到实时操作。

  我们提倡另一种方法，即对深层conv-net进行训练，以便在初始离线阶段解决更普遍的相似学习问题，然后在跟踪过程中对此函数进行在线评估。本文的主要贡献是证明了该方法在现代跟踪基准中以远远超过帧速率要求的速度获得了非常有竞争力的性能。具体来说，我们训练一个暹罗网络来在一个更大的搜索图像中定位一个样本图像。另一个贡献是一种新颖的暹罗建筑，它对于搜索图像来说是全卷积的：通过一个双线性层来计算两个输入的互相关，从而实现密集和高效的滑动窗口评估。

  我们假设相似性学习方法相对被忽略了，因为跟踪社区无法访问大量的标记数据集。事实上，直到最近，可用的数据集只有几百个带注释的视频。然而，我们认为，ILSVRC数据集用于视频中的对象检测[10](从此以后，ImageNet视频)的出现使得训练这样一个模型成为可能。此外，使用同一领域的视频进行跟踪的深度模型的培训和测试是否公平也是一个争议的问题，因为最近vot委员会禁止这样做。我们表明，我们的模型从ImageNet视频域推广到ALOV/OTB/vot[1，11，12]域，使跟踪基准的视频能够保留用于测试目的。

  - 基于深度相似学习的跟踪

    学习跟踪任意对象可以通过相似性学习来解决。我们提出学习一个函数$f(z，x)$，它将样本图像 $z$ 与相同大小的候选图像 $x$ 进行比较，如果两幅图像描述相同的对象，则返回高分。否则，返回低得分。为了找到对象在新图像中的位置，我们可以对所有可能的位置进行详尽的测试，并选择与对象的过去外观最大相似的候选对象。在实验中，我们将简单地使用对象的初始外观作为样本。函数 $f$ 将从带有标记对象轨迹的视频数据集中学习。

    鉴于他们在计算机视觉方面的广泛成功[13，14，15，16]，我们将使用深度卷积网络作为函数 $f$。使用深层卷积的相似学习通常使用暹罗架构[17，18，19]。暹罗网络对两个输入都应用相同的转换 $ϕ$ , 然后根据$f (z、x) = g(ϕ(z),ϕ(x))$ 结合其使用另一个函数 $g$ 表示. 当函数 $g$ 是一个简单的距离或相似度量时，函数 $ϕ$ 可以被认为是嵌入函数。深层连网已经应用于人脸验证[18，20，14]，键盘描述符学习[19，21]和一次字符识别[22]等任务。

    ![](https://img-blog.csdn.net/20180820103808360?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Z6cDk1/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

    <center><font color = red>图1：完全卷积的暹罗建筑。对于搜索图像x，我们的体系结构是完全卷积的。输出是一个 [ 标量值记分图 ]，其维数取决于搜索图像的大小。这使得在一个评估中能够计算搜索图像中所有已转换的子窗口的相似性函数。在本例中，分数图中的红色和蓝色像素包含对应子窗口的相似之处。最好用颜色来观察。</center></font>

  - 全卷积Siamese 结构

    我们提出了一种关于候选图像x的完全卷积的Siamese结构。**我们说，如果一个函数是转换函数，它是完全卷积的. (We say that a function is fully-convolutional if it commutes with translation)**，给出一个更精确的定义，引入$Lτ$ 表示转换算子 $(L_τx)[u]=x[u-τ]$，如果对于任何平移 $τ$, $h(L_{kτ}x) = L_τh(x)$ , 那将信号映射到信号的函数 $h$ 是整数步长 $k$ 的完全卷积函数。（当x是有限信号时，这只需要保持输出的有效区域。)

    全卷积网络的优点是，我们可以为网络提供更大的搜索图像，而不是相同大小的候选图像。以及它将在单个评估中计算密集网格上所有转换子窗口的相似性。为此，我们使用卷积嵌入函数 $ϕ$，并使用互相关层组合生成的特征映射。
    $$
    f(z,x)=\varphi(z)*\varphi(x)+b_1
    $$
    其中 $b_1$ 表示在每个位置取值 $b∈R$ 的信号。这个网络的输出不是单个分数，而是定义在有限网格$D⊂Z^2$上的分数映射，如图1所示.注意，嵌入函数的输出是一个具有空间支持的特征映射，而不是普通的向量。同样的技术已经应用于当代立体匹配的研究[23]。

    在跟踪过程中，我们使用以目标先前位置为中心的搜索图像。相对于得分图中心的最大得分的位置，乘以内标的跨距。给出目标从一个帧到另一个帧的位移。在一个单一的前进通道中，通过组装一小批缩放图像来搜索多个尺度.

    将使用互相关的特征映射组合起来，并在较大的搜索图像上对网络进行一次评估，在数学上等同于利用内部积组合特征映射和评估。网络上的每个子窗口独立翻译. 然而，互相关层提供了一种非常简单的方法，可以在现有的深度卷积库框架内有效地实现这一操作。虽然这显然是有用的在测试中，也可以在训练过程中加以利用。

  - 大搜索图像的训练

    我们采用区分性的方法，对网络进行正对和负对的训练，并采用逻辑损失法。
    $$
    l(y,v) = log(1+exp(-yv))
    $$
    其中v是单个样本候选对的实值分数，$y∈\{+1；-1\}$ 是它的基本真理标号。在训练过程中，我们利用网络的全卷积特性，使用由样本图像和更大的搜索图像组成的对。这将生成分数 $v:D→R$ 的映射，有效地生成每对对的许多示例。我们将得分图的损失定义为单个损失的平均值。
    $$
    L(y,v) = \frac{1}{|D|}\sum_{u\in D}l(y[u],v[u])
    $$
    对于分数图中的每个位置，都需要一个真正的标签$y[u]∈\{+1,-1\}$。将随机梯度下降(Sgd)应用于该问题，得到了深度卷积 $θ$ 的参数。
    $$
    arg min_{\theta}n E_{(z,x,y)}L(y,x;\theta)
    $$
    通过提取以目标为中心的样本和搜索图像，从注释化视频的数据集中获得对，如图2所示。这些图像是从两个视频帧中提取出来的，这两个帧都包含该对象，并且至多是 $T$ 帧之间的间隔。在训练期间，对象的类将被忽略。对象在每个图像中的比例是标准化的，而不会破坏图像的纵横比。如果得分图的元素在中心的半径R内(代表网络的跨径k)，则被认为属于一个正的例子。
    $$
    y[u]=+1  \quad if \quad k||u-c||\le R \\
    y[u]=-1 \quad otherwise
    $$
    对分数图中的正负两个例子的损失进行加权，以消除阶级不平衡。

    由于我们的网络是完全卷积的，所以它没有学习到在中心子窗口的偏差的风险。我们认为考虑以目标Beca为中心的搜索图像是有效的。使用最困难的子窗口，以及对跟踪器性能影响最大的，很可能是与目标相邻的子窗口。

    注意，由于网络是对称的 $f(z，x)=f(x，z)$，它实际上也是完全卷积的。虽然这允许我们在理论上对不同的对象使用不同大小的样本图像，但是我们假设相同的大小，因为它简化了小型批处理实现。然而，这一假设可能未来要放松。

  - 用于跟踪的ImageNet视频

    2015年版的ImageNet大规模视觉识别挑战[10](ILSVRC)引入了ImageNet视频数据集，作为从视频挑战中检测新对象的一部分。参与者必须对来自30种不同类别的动物和车辆的物体进行分类和定位。培训和验证集共包含近4500个视频，总共有超过一百万个带注释的帧.如果与VOT[12]、ALOV[1]和OTB[11]中的标记序列相比，这一数字尤其令人印象深刻，这些序列加起来总共不到500个视频。我们认为，这个数据集不仅由于其庞大的大小，而且还因为它描述的场景和对象不同于在规范跟踪基准中发现的场景和对象。因此，它可以安全地用于训练用于跟踪的深模型，而无需过度拟合这些基准中使用的视频领域。

  - **实际问题**

    - [ ] **数据集管理** : 在训练过程中，我们采用127×127的样本图像和255×255像素的搜索图像。图像的缩放使得边框，加上上下文的附加边距，有一个固定的区域。更准确地说，如果紧包围框有大小 $(w，h)$ 且上下文边距为 $p$ ,然后选择缩放因子s，使缩放矩形的面积等于一个常数。
      $$
      s(w+2p)\times s(h+2p)=A
      $$
      我们使用样本图像的面积 $A=1272$ ，并将上下文的数量设置为平均维数 $p=(W)/4 $ 的一半。每个帧的样本和搜索图像都是离线提取的，以避免在训练期间图像大小调整。在这项工作的初步版本中，我们采用了一些启发式方法来限制从其中提取训练数据的帧数。在本文的实验中，我们使用了图像网络视频中的4417个视频，这些视频占了200多万标签包围盒。

    - [ ] **网络（体系）结构** : 嵌入函数 $ϕ$ 的体系结构类似于Krizhevsky等人网络的卷积阶段 [16]。参数和激活的尺寸如表1所示。在前两个卷积层之后使用Maxpool。除了最后一层外，每个卷积层都有非线性关系。在训练过程中，在每个线性层之后立即插入批归一化[24]。最后表示的步幅是8。**设计的一个重要方面是没有在网络中引入填充。虽然这是图像分类中的一种常见做法，但它违背了方程的全卷积性.1.**

    - [ ] **跟踪算法** : 因为我们的目的是证明我们的完全卷积的暹罗网络的有效性。在对ImageNet视频进行训练时，我们使用了一种非常简单的算法来进行跟踪。与更复杂的跟踪器不同，我们不更新模型，也不保存过去外观的记忆。我们不包括额外的线索，如光流或颜色直方图，我们也不完善我们的预测与边界框回归。然而，尽管它很简单，但是当使用我们的离线学习的相似性度量时，跟踪算法取得了令人惊讶的好结果。

      <center> 表1：卷积嵌入函数的体系结构</center>

      它类似于Krizhevsky等人网络的卷积阶段[16]。通道映射属性描述每个卷积层的输出和输入信道数。



      在网上，我们确实包含了一些基本的时间限制：我们只在一个区域内搜索约四倍于以前大小的物体，并在分数图中添加一个余弦窗口来惩罚大位移。通过缩放空间跟踪是通过处理多个缩放版本的搜索图像。任何规模的变化都会受到惩罚，当前比额表的更新也会受到影响。
    
    - [ ] 

- 相关工作

  最近的一些工作寻求训练递归神经网络(RNNS)的目标跟踪问题。GaN等人[25]训练RNN来预测目标在每一帧和Kahou等人中的绝对位置[26]。类似地，使用可区分的注意机制训练RNN进行跟踪。这些方法还没有表现出对现代基准的竞争结果，然而，这无疑是未来研究的一个有前景的途径。我们注意到，我们注意到，在这种方法和我们的方法之间可以有一个有趣的平行，通过将一个暹罗网络解释为一个展开的RNN，对长度为2的序列进行训练和评估。因此，对于一个反复出现的模型。暹罗网络可以起到强大的初始化作用。

  Denil等人[27]用粒子滤波器跟踪物体，该过滤器使用学习的距离度量将当前外观与第一帧的外观进行比较。然而，他们的距离度量与我们的大不相同。它们不是比较整个对象的图像，而是计算固定点之间的距离(对象的边界框中的小区域的凹凸不平的一瞥)。为了学习一种距离度量，他们训练一个受限的Boltzmann机器(RBM)，然后对两个固定点使用隐藏激活之间的欧几里德距离。尽管RBM是不受监督的，但他们建议在要检测的对象的中心图像中对RBM进行随机固定训练。这要么是在线执行的，要么是在了解要跟踪的对象的脱机阶段执行的。跟踪一个物体时，他们学习一种随机策略来选择特定于该对象的固定物，使用不确定性作为奖励信号。该方法除了合成MNIST数字序列外，仅对人脸和人的跟踪问题进行了定性的论证。

  对于每一个新的视频，从零开始训练一个深网是不可行的，但一些工作已经探讨了在测试时根据预先训练的参数进行微调的可行性。因此dlt[7]和mdnet[9]都在离线阶段为类似的检测任务训练卷积网络。然后在测试时，使用SGD来学习一个检测器，其中包含从视频本身提取的示例，就像在传统的跟踪作为检测器学习范式中那样。在许多实例中，由于评估正向和向后通过的计算负担，这些方法不能以帧速率操作。利用Conv-网进行跟踪的另一种方法是应用传统的浅层方法，使用预先训练的卷积网络的内部表示作为特征。而这种类型的跟踪器，如DeepSRDCF[6]，Ma等。[5]和fcnt[8]都取得了很好的效果，但由于维数相对较高，无法实现帧速率运算。网络表示法。

  在我们自己的工作的同时，其他一些作者也提出了通过学习图像对的函数来进行目标跟踪的Conv-网。Hitt等人[28]引入GOTURN，其中对Conv-net进行训练，使其从两幅图像直接回归到第一幅图像中所示对象的第二幅图像中的位置。预测一个矩形而不是一个位置具有这样的优点，即不需要进行详尽的评估，就可以处理比例和纵横比的变化。然而，他们的方法的一个缺点是对第二个图像的翻译不具有内在的不变性。这意味着网络必须显示在所有位置的例子，这是通过大量数据集增强实现的。Chen等人[29]训练一个将样本和更大的搜索区域映射到响应地图的网络。然而，由于最后一层是完全连通的，它们的方法对第二层图像的平移也缺乏不变性。类似于Holdet al.，这是低效的，因为培训集必须表示所有对象的所有平移。他们的方法被命名为YCNN，因为网络的Y形状。与我们的方法不同，它们不能在训练后动态地调整搜索区域的大小。陶等人[30]建议培训一个暹罗网络，以识别与初始目标外观匹配的候选图像位置，称呼方法为Sint(暹罗实例搜索跟踪器)进行配音。与我们的方法相反，他们没有采用一种对搜索图像完全卷积的架构。相反，在测试的时候，他们在不同半径的圆圈上均匀地采样包围盒，就像在[3]中一样。此外，它们结合光流和包围盒回归来改进结果。为了提高系统的计算速度，它们采用感兴趣区域(ROI)池来有效地检测多个重叠子窗口。尽管有这样的优化，以每秒2帧的速度，整个系统仍然远远不是实时的.

  所有以上的视频序列训练方法(MDNet[9]，Sint[30]，GOTURN[28])，使用属于基准使用的相同ALOV / OTB / VOT域的训练数据。这种做法已被禁止在VOT的挑战，因为担心过分适合的场景和对象的基准。因此，我们的工作的一个重要贡献是证明一个conv-net可以被训练为有效的目标跟踪，而不需要使用与测试集相同分布的视频。

- 实验

  - 实施细节

    - [ ] 训练

       通过最小化方程5 求出嵌入函数的参数。使用MatConvNet直接使用SGD [31]。参数的初始值遵循高斯分布，按照改进的Xavier方法[32]进行缩放。训练超过50个epochs，每一个由50000个抽样对组成(根据2.2部分)。每一次迭代的梯度用8的小批次来估计，学习速率在 $10^{-2}$ 到$10^{-5}$之间的每一个时期进行几何退火。

    - [ ] 跟踪

      如前所述，在线阶段是故意最小化的。初始对象外观的嵌入 $ϕ(Z)$ 只计算一次，并与后续帧的子窗口进行卷积比较。我们发现，通过简单的策略(如线性插值)对样本进行在线更新(特征表示)并不能获得很好的性能，因此我们将其固定下来。我们发现，用双三次插值对得分图进行过采样，从17×17到272×272，由于原始地图相对粗糙，使得定位更加精确。为了处理尺度变化，我们还搜索了五个尺度上的对象$1.025^{\{−2，1，0，1，2\}}$，并用线性插值方法更新标度，其因子为0.35以提供阻尼。

      为了使我们的实验结果能够再现，我们与脚本一起共享培训和跟踪代码，以及在http：/www.robots.ox.ac.uk/~Luca/siamese-fc.html上生成管理数据集的脚本。在一台配备了NVIDIA GeForce GTX Titan X和Intel Core i7-4790K、4.0GHz的机器上，当搜索分别超过3和5个比例尺, 我们的完全在线跟踪管道运行在86和58帧每秒，

  - 评估

    我们评估了我们的简单跟踪器的两个变体：SiamFC（SiameseFully Convolutional）和SiamFC3s，它们搜索超过3个尺度而不是5个。

  - OTB-13基准

- 结论

  在本工作中，我们从传统的在线学习方法出发，提出了一种在离线阶段学习强嵌入的替代方法。与它们在分类设置中的使用不同，我们证明，对于跟踪应用，暹罗全卷积深网络有能力更有效地利用现有数据。这既反映在测试时，执行有效的空间搜索，也反映在培训时间，在那里，每个子窗口有效地代表了一个有用的样本，几乎没有额外的成本。实验表明，深度嵌入为在线跟踪器提供了一个自然丰富的特性来源，并使简化的测试时间策略能够很好地执行。我们认为，这种方法是对更复杂的在线跟踪方法的补充，并期望今后的工作能够更彻底地探讨这种关系。

  <center>原始分数，重叠和报告的速度，我们提出的方法和最优秀的15个执行跟踪器的VOT-15挑战。在可用的情况下，我们将与作者报告的速度进行比较，否则(*)我们在efo单元中报告vot-15结果[12]中的值，它大致对应于fps(例如，NCC跟踪器的速度是140 fps和160 efo)。</center>

  - 

- 