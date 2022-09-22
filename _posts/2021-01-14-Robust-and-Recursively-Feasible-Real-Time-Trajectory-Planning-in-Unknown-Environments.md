---
title: "Robust and Recursively Feasible Real-Time Trajectory Planning in Unknown Environments"
categories:
 - Research
 - Conference
tags:
 - planning
 - feasibility
 - real-time
header:
  teaser: /assets/image/thumbnail/IROS2021.png
conference: IROS
authors: Inkyu Jang, Dongjae Lee, <u>Seungjae Lee</u>, H. Jin Kim
links: 
 - paper: 
   link: https://arxiv.org/abs/2107.06484
   name: "Paper"
 - video:
   link: https://www.youtube.com/watch?v=pqe6jSrH1_w
   name: "Video"
 - bibtex: 
   name: "Bibtex"
---

{% include video id="pqe6jSrH1_w" provider="youtube" %}

**Abstract:** Motion planners for mobile robots in unknown environments face the challenge of simultaneously maintaining both robustness against unmodeled uncertainties and persistent feasibility of the trajectory-finding problem. That is, while dealing with uncertainties, a motion planner must update its trajectory, adapting to the newly revealed environment in real-time; failing to do so may involve unsafe circumstances. Many existing planning algorithms guarantee these by maintaining the clearance needed to perform an emergency brake, which is itself a robust and persistently feasible maneuver. However, such maneuvers are not applicable for systems in which braking is impossible or risky, such as fixed-wing aircraft. To that end, we propose a real-time robust planner that recursively guarantees persistent feasibility without any need of braking. The planner ensures robustness against bounded uncertainties and persistent feasibility by constructing a loop of sequentially composed funnels, starting from the receding horizon local trajectory's forward reachable set. We implement the proposed algorithm for a robotic car tracking a speed-fixed reference trajectory. The experiment results show that the proposed algorithm can be run at faster than 16 Hz, while successfully keeping the system away from entering any dead-end, to maintain safety and feasibility. 

## Bibtex <a id="bibtex"></a>
```
@inproceedings{jang2021robust,
  title={Robust and Recursively Feasible Real-Time Trajectory Planning in Unknown Environments},
  author={Jang, Inkyu and Lee, Dongjae and Lee, Seungjae and Kim, H Jin},
  booktitle={2021 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},
  pages={1434--1441},
  year={2021},
  organization={IEEE}
}
```
