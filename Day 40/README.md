🔄 Day 40 — Bidirectional RNN

Continuing my 100 Days of Deep Learning journey with Bidirectional RNNs.

Today, I learned how an RNN can understand a sequence by processing it in both directions — from past to future and from future back to past.

📚 What I learned
🔹 A Bidirectional RNN uses two separate RNNs:
Forward RNN → processes the sequence from left to right
Backward RNN → processes the sequence from right to left
🔹 At each time step, the hidden states from both directions are combined to generate the output.
🔹 Understanding the output equation:
yₜ = σ(U[h⃗ₜ, h⃖ₜ] + b)
🔹 Applications:
NER (Named Entity Recognition)
POS Tagging
Machine Translation
🔹 Drawbacks include increased complexity, training time, and the possibility of overfitting.

The key idea I learned today:

Sometimes understanding a word requires knowing not only what came before it, but also what comes after it.

For example, in a sentence like “Amazon is beautiful rivers”, the surrounding context can help a model understand the meaning of a word more effectively.

I’m continuing my approach of:

Concept → Handwritten Notes → Architecture → Equations → Implementation

📅 Day 40 | 21/09/2026

🔗 GitHub:
https://github.com/AniketGaikwad18/100-Days-of-Deep-Learning/tree/main/Day%2040

#100DaysOfDeepLearning #DeepLearning #RNN #BidirectionalRNN #BiRNN #NeuralNetworks #MachineLearning #ArtificialIntelligence #NLP #LearningInPublic #DeepLearningJourney #BuildInPublic
