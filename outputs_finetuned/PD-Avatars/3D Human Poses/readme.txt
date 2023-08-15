There are two folders:
 
outputs_finetuned: 3D poses fine-tuned on our dataset using multi-view cameras.
outputs_pretrained: 3D human poses estimated by a model trained on a public dataset (Human3.6M).


There is a file for each subject. Each file is an numpy array with a shape of [15,3]. Which refers to 15 joint of human body in 3D spaces. 3D poses are relative to the pelvis joint. (Pelvice joint is always zero).

15 Human Joints:

0: pelvis
1: right hip
2:right knee
3: right ankle
4:left hip
5: left knee
6:left ankle
7:neck
8:head
9: right shoulder
10: right elbow
11:right hand
12:left shoulder
13: left elbow
14: left hand