Day 31 — Dogs vs Cats 🐶🐱 | Practical CNN Implementation

Day 31 of my #100DaysOfDeepLearning journey — today I moved from understanding CNN concepts to actually implementing a CNN on a real image-classification problem.

I worked with the Dogs vs Cats dataset and built the complete pipeline from dataset preparation to inference.

🔨 What I implemented today:
📥 Downloaded the dataset using the Kaggle API
🗂️ Organized the dataset into training and testing directories
🖼️ Loaded images using Keras' image_dataset_from_directory
🔄 Resized images to 256 × 256
📊 Normalized pixel values from [0, 255] → [0, 1]
🧠 Built a CNN with multiple Convolution + Batch Normalization + MaxPooling blocks
🔗 Used Flatten and Dense layers for classification
🛡️ Added Dropout to help reduce overfitting
🎯 Used Sigmoid activation for binary classification
⚙️ Compiled the model with Adam + Binary Cross-Entropy
📈 Monitored training/validation accuracy and loss
🔍 Performed inference on a new image and predicted Cat or Dog

The data-loading approach follows Keras' directory-based image pipeline, where class labels can be inferred from the folder structure and images are loaded in batches.

💡 Biggest takeaway

This was an important step in my learning because I wasn't just studying Convolution, Pooling, Batch Normalization, Dropout, and Sigmoid individually anymore.

I was finally seeing how all these concepts come together in a complete CNN pipeline:

Dataset → Preprocessing → CNN → Training → Evaluation → Prediction

This is exactly the kind of learning I want from this journey — understand the concept first, then implement it on a real problem.

🔗 My Day 31 Notes & Code:
https://github.com/AniketGaikwad18/100-Days-of-Deep-Learning/tree/main/Day%2031

From learning CNNs on paper → to teaching a CNN to distinguish between 🐶 and 🐱. 🚀

#DeepLearning #CNN #ComputerVision #ImageClassification #TensorFlow #Keras #MachineLearning #AI #DogsVsCats #100DaysOfDeepLearning #LearningByBuilding
