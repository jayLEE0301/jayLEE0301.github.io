---
title: "Outcome-Directed Reinforcement Learning by Uncertainty & Temporal Distance-Aware Curriculum Goal Generation"
categories:
 - Research
 - Conference
tags:
 - reinforcement learning
 - exploration
 - meta learning
header:
  teaser: /assets/image/thumbnail/ICLR2023.png
conference: submitted to ICLR
authors: Daesol Cho*, <u>Seungjae Lee*</u>, and H. Jin Kim (* These authors contributed equally)
---

**Abstract:** Current reinforcement learning (RL) often suffers from solving a challenging exploration problem where the desired outcomes or high rewards are rarely observed. Even though curriculum RL, a framework that solves complex tasks by proposing a sequence of surrogate tasks, shows some reasonable results, most of the previous works still have difficulty in proposing curriculum due to the absence of a mechanism for obtaining calibrated guidance to the desired outcome state without any prior domain knowledge. To alleviate it, given the desired outcome examples, we propose an uncertainty & temporal distance-aware curriculum goal generation method for the outcome-directed RL via solving a bipartite matching problem. It could not only provide precisely calibrated guidance of the curriculum to the desired outcome states but also bring much better sample efficiency and geometry-agnostic curriculum goal proposal capability compared to previous curriculum RL methods. We demonstrate that our algorithm significantly outperforms these methods in a variety of challenging navigation tasks and robotic manipulation tasks in a quantitative and qualitative way.


