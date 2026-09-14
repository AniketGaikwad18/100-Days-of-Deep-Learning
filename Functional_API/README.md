Additional Work — Functional API & Multi-Output Deep Learning 🧠🏗️

Alongside Day 33, I explored the Keras Functional API and moved beyond simple sequential architectures.

Today I learned how the Functional API allows us to represent a model as a graph of connected layers, making it possible to build architectures with branching, shared layers, and multiple outputs.

🔨 What I worked on:
Understanding Functional API vs Sequential API
Creating models using Input() and Model(inputs, outputs)
Building non-linear / branching architectures
Working with multiple outputs
Understanding shared layers and how information can flow into different prediction branches
Visualizing and inspecting the model architecture using model.summary() and model graphs
Implementing a multi-task Age & Gender Prediction model using ResNet50
Using a pretrained ResNet50 backbone as a feature extractor
Creating separate branches:
👤 Age → Regression
🚻 Gender → Binary Classification
Understanding how different outputs can have their own loss functions and metrics

The architecture I worked with demonstrates an important idea: one shared feature extractor can learn representations that are then used by multiple task-specific heads.

🔗 My Day 33 Code / Additional Work:
https://github.com/AniketGaikwad18/100-Days-of-Deep-Learning/tree/main/Day%2033

From simple layer-by-layer networks → to designing architectures that actually resemble real-world deep learning systems. 🚀

#DeepLearning #Keras #FunctionalAPI #ResNet50 #TransferLearning #MultiTaskLearning #ComputerVision #MachineLearning #AI #NeuralNetworks #100DaysOfDeepLearning #LearningByBuilding
