Day 34 — Understanding Recurrent Neural Networks (RNNs)

Continuing my 100 Days of Deep Learning journey, today I started exploring Recurrent Neural Networks (RNNs) — a major step from working with images to working with sequential data.

📚 What I learned today:

🔹 What is an RNN?

Why RNNs are designed for sequential data
How the hidden state acts as memory for previous time steps
Handling variable-length sequences

🔹 RNN Architecture & Forward Propagation

Input \(x_t\), hidden state \(h_t\), and output \(y_t\)
Understanding how information flows from one time step to the next

The basic RNN equations:

$$ h_t=f(W_xx_t+W_hh_{t-1}+b) $$ $$ y_t=g(W_yh_t+b_y) $$

🔹 Representing Text for RNNs

Tokenization
Integer/index encoding
Embeddings
Converting text into numerical vectors that neural networks can process

🔹 Handling Different Sequence Lengths

Padding
Masking
Understanding why padded values should not unnecessarily influence learning

🔹 Practical Example
I used movie review sentiment classification to understand how an RNN can process a sequence of words and predict whether the sentiment is positive or negative.

🔹 Applications

Sentiment Analysis
Sentence Completion
Image Caption Generation
Machine Translation
Question & Answer Systems

One important takeaway from today:

CNNs taught me how neural networks understand spatial patterns. RNNs introduce the idea of understanding information in sequence and context.

Keras' RNN implementation similarly processes inputs across timesteps while maintaining recurrent state, with support for variable-length sequences through masking.

🔗 GitHub:
https://github.com/AniketGaikwad18/100-Days-of-Deep-Learning/tree/main/Day%2034

#100DaysOfDeepLearning #DeepLearning #RNN #RecurrentNeuralNetwork #NLP #NaturalLanguageProcessing #SentimentAnalysis #NeuralNetworks #Keras #TensorFlow #MachineLearning #AI #LearningByBuilding #LearningJourney
