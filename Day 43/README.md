🎯 Day 43 — Attention Mechanism

Continuing my 100 Days of Deep Learning journey, today I learned about one of the most important ideas that helped improve Sequence-to-Sequence models: the Attention Mechanism.

The core idea is simple:

Instead of forcing the decoder to rely on a single fixed context vector, attention allows it to focus on the most relevant parts of the input sequence at each step.

📚 What I learned
🔹 Attention Mechanism — allows the model to focus more on the important parts of the input for the current decoding step.
🔹 Context Vector — calculated as a weighted combination of encoder hidden states:
Cᵢ = Σ αᵢⱼ hⱼ
🔹 Attention Weights (αᵢⱼ) — represent the importance of each encoder hidden state for the current decoder step.
🔹 Encoder–Decoder Interaction — the decoder can access information from different encoder states instead of depending only on the final hidden state.
🔹 BLEU Score — studied as a metric for evaluating machine translation quality.
🔹 Sentence Length vs BLEU Score — the graph in my notes helped me understand how translation performance can change as sentence length increases.
💡 Key takeaway

The biggest limitation of the basic Encoder–Decoder architecture was that the entire input sequence had to be compressed into a single representation.

Attention changes this:

Input Sequence → Encoder Hidden States → Attention Weights → Context Vector → Decoder Output

This is an important step in the progression I am following:

RNN → LSTM → Seq2Seq → Attention → Transformers → LLMs

📅 Day 43 | 24/09/2026

🔗 GitHub:
https://github.com/AniketGaikwad18/100-Days-of-Deep-Learning/tree/main/Day%2043

#100DaysOfDeepLearning #DeepLearning #AttentionMechanism #Attention #Seq2Seq #EncoderDecoder #LSTM #RNN #NLP #MachineLearning #ArtificialIntelligence #Transformers #LLM #LearningInPublic #DeepLearningJourney
