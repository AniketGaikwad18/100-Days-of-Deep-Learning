Day 33 — Transfer Learning & Pretrained CNNs 🧠🚀

Day 33 of my #100DaysOfDeepLearning journey, and today I explored Transfer Learning — one of the most practical approaches for building image-based deep learning models when training a network completely from scratch may require significant data and resources.

📚 What I learned:
What Transfer Learning is and why knowledge learned from one problem can be reused for a related problem
What Pretrained Models are and why they are useful
VGG16 and its architecture
AlexNet and its major convolution/pooling stages
The ImageNet dataset and its role in training large-scale image classification models
Why early convolutional layers can learn general visual features such as edges, textures and shapes
Two major approaches to transfer learning:
🔹 Feature Extraction — keep the pretrained convolutional base frozen and train new classification layers
🔹 Fine-Tuning — unfreeze some of the later layers and retrain them with a low learning rate

The key idea I understood today is that we don't always need to start learning from zero. A pretrained model can provide a strong foundation, which we can adapt to our own task. Keras describes the typical workflow as freezing the pretrained base, adding new trainable layers, and optionally fine-tuning part of the base model later with a very low learning rate.

This connects directly with the Dogs vs Cats CNN I implemented earlier — instead of building everything from scratch, a pretrained model can be adapted for a similar image-classification task. Keras even demonstrates this type of transfer-learning workflow on cats-vs-dogs classification.

🔗 My Day 33 Notes & Code:
https://github.com/AniketGaikwad18/100-Days-of-Deep-Learning/tree/main/Day%2033

From training a CNN from scratch → to understanding how we can reuse what a model has already learned. 🚀

#DeepLearning #TransferLearning #VGG16 #AlexNet #CNN #ComputerVision #ImageNet #Keras #TensorFlow #MachineLearning #AI #100DaysOfDeepLearning #LearningByBuilding
