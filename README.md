LabVIEW code for ETH Mike hardware.

This version supports ETH Mike #1, #2, #3, #4 and #5 and is only compatible with front-end versions from commit [d6a0dc5646e02c838503b3ed04430bde3b3fe736](https://gitlab.ethz.ch/RELab/eth-mike/eth-mike-front-end/-/commit/d6a0dc5646e02c838503b3ed04430bde3b3fe736) onwards.

**Please make sure the correct robot model is selected before building/deploying** (at the left end of the MAIN_All_In_One.vi diagram).

## Installation
During LabView installation, add the `myRIO software bundle` or select `Real-Time module` & `myRIO toolkit` package to the installation. If the installation crashes during the installation of the VI package manager, try this tip [here](https://knowledge.ni.com/KnowledgeArticleDetails?id=kA03q000000ww5ZCAQ&l=de-CH).

## LabView Programming
You can find a good introduction to LabView [here](https://youtu.be/ZHNlKyYzrPE).

## How to run or deploy the code
This is described [here](Docs/HowToRunTheLabviewProgram.md).

## How to support new Hardware 
This is described [here](Docs/HowToSupportNewMikeHardwareInLabviewCode.md).
