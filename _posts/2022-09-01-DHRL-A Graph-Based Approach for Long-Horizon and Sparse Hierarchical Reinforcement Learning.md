---
title: "DHRL: A Graph-Based Approach for Long-Horizon and Sparse Hierarchical Reinforcement Learning"
categories:
 - Research
 - Conference
tags:
 - reinforcement learning
 - hierarchical RL
 - goal conditioned RL
header:
  teaser: /assets/image/thumbnail/NeurIPS2022.png
conference: Neurips
authors: <u>Seungjae Lee</u>, Jigang Kim, Inkyu Jang, and H. Jin Kim
links:
 - paper:
   link: https://arxiv.org/abs/2210.05150
   name: "Paper"
- code:
   link: https://github.com/jayLEE0301/dhrl_official
   name: "Code"
---
<p style="color:gray;">NeurIPS 2022</p>
**Abstract:** Hierarchical Reinforcement Learning (HRL) has made notable progress in complex control tasks by leveraging temporal abstraction. However, previous HRL algorithms often suffer from serious data inefficiency as environments get large. The extended components, i.e., goal space and length of episodes, impose a burden on either one or both high-level and low-level policies since both levels share the total horizon of the episode. In this paper, we present a method of Decoupling Horizons Using a Graph in Hierarchical Reinforcement Learning (DHRL) which can alleviate this problem by decoupling the horizons of high-level and low-level policies and bridging the gap between the length of both horizons using a graph. DHRL provides a freely stretchable high-level action interval, which facilitates longer temporal abstraction and faster training in complex tasks. Our method outperforms state-of-the-art HRL algorithms in typical HRL environments. Moreover, DHRL achieves long and complex locomotion and manipulation tasks.



## Bibtex <a id="bibtex"></a>
```
@inproceedings{lee2022graph,
  title={DHRL: A Graph-Based Approach for Long-Horizon and Sparse Hierarchical Reinforcement Learning},
  author={Lee, Seungjae and Kim, Jigang and Jang, Inkyu and Kim, H Jin},
  booktitle={Thirty-sixth Conference on Neural Information Processing Systems},
  pages={},
  year={2022},
  organization={}
}
```
