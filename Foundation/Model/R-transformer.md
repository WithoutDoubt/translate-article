#### R

- Abstract

  Recurrent Neural Networks have long been the **dominating** choice for sequence modeling . However, it  severely suffers from two issues: **impotent** in capturing very long-term **dependencies** and unable to **parallelize the sequential computation procedure** . Therefore, many non-recurrent sequence models that **are built on**  convolution and attention operations have been proposed recently. **Notably** , models with multi-head attention such as Transformer have demonstrated extreme **effectiveness** in capturing long-term dependencies in a variety of sequence modeling tasks. Despite their success , however, these models lack necessary components to model **local structures** in sequences and heavily rely on **position embeddings** that have limited effects and require a considerable amount of design efforts . In this paper, we propose the R-Transformer which enjoys the advantages of both RNNs and the multi-head attention mechanism while avoids their **respective** **drawbacks** . The proposed model can effectively capture both local structures and global long-term dependencies in sequences without any use of position embeddings. We evaluate R-Transformer through extensive experiments with data from a wide range of domains and **the empirical results** show that R-Transformer outperforms the state-of-the-art methods by **a large margin** in most of the tasks.

- Introduction

  Recurrent Neural Networks (RNNs) especially its variants such as Long Short-Term Memory (LSTM) and Gated Recurrent Unit (GRU) have achieved great success in a wide range of sequence learning tasks including language modeling , speech recognition , recommendation , etc (). Despite their success , however , the recurrent structure is often troubled by two **notorious** issues. First , it easily suffers from gradient vanishing and exploding problems , which largely limits their ability to learn very long-term dependencies (cite) .**Second , the sequential nature of both forward and backward passes makes it extremely difficult , if not impossible , to parallelize the computation , which dramatically increases the time complexity in  both training and testing procedure.** Therefore , many recently developed sequence learning models have completely **jettisoned** the recurrent structure and only rely on convolution operation or attention mechanism that are easy to parallelize and allow the information flow  at  an arbitrary length , Two representative models that have drawn great attention are Temporal Convolution Networks(TCN) (2018) and Transformer(2017) . In a variety of sequence learning tasks , they have demonstrated comparable or even better performance than that of RNNs()

  - 其次，前向和后向通过的顺序性质使得并行计算极其困难（如果不是不可能的话），这极大地增加了训练和测试过程中的时间复杂度。

- $$
  
  $$
