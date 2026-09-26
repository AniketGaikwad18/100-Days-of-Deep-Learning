Day 45 — Bahdanau Attention & Luong Attention 🧠🔍

Continuing my #100DaysOfDeepLearning journey, today I learned two important attention mechanisms used in RNN-based Seq2Seq models: Bahdanau Attention and Luong Attention.

🔹 Bahdanau Attention — Additive Attention

I learned how the model:

Calculates an alignment score between the decoder state and encoder states
Converts scores into attention weights using Softmax
Creates a context vector as a weighted sum of encoder states
Uses a feed-forward neural network to calculate the alignment scores
🔹 Luong Attention

I studied how Luong Attention calculates attention scores using the relationship between the current decoder state and encoder states, with the notes focusing on the dot-product approach.

The key idea I understood today is that attention allows the decoder to selectively focus on relevant encoder states instead of relying on a single fixed representation of the entire input sequence. This helps sequence models access relevant information from earlier parts of the input.

🔗 My Day 45 Notes & Code:
https://github.com/AniketGaikwad18/100-Days-of-Deep-Learning/tree/main/Day%2045

Understanding attention step by step — from alignment scores to attention weights to the final context vector. 🚀

#DeepLearning #AttentionMechanism #BahdanauAttention #LuongAttention #RNN #Seq2Seq #NLP #MachineLearning #AI #100DaysOfDeepLearning
