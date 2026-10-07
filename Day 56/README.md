🧠 Day 56 — Scaled Dot-Product Attention: From Intuition to Matrix Representation
Continuing my 100 Days of Deep Learning journey, today I went deeper into Scaled Dot-Product Attention, focusing not only on the formula but also on how attention is actually represented and computed using matrices.
🔹 What I Learned
- Query (Q) — represents what information a token is looking for.
- Key (K) — represents the information available from each token and helps determine relevance.
- Value (V) — contains the actual information that will be retrieved.
- Dot Product (QKᵀ) — calculates similarity between queries and keys.
- Scaling (√dₖ) — keeps the values controlled, helping Softmax maintain useful gradients.
- Softmax — converts similarity scores into attention weights.
- Weighted Sum of V — combines the Value vectors according to those weights to produce the final contextual representation.
The standard Transformer formulation is:
Attention(Q, K, V) = Softmax(QKᵀ / √dₖ)V arXiv
📐 Understanding the Matrix Flow
Today I focused on understanding the complete mathematical pipeline:
Q × Kᵀ
↓
Similarity Scores
↓
Scale by 1/√dₖ
↓
Softmax
↓
Attention Weights
↓
Attention Weights × V
↓
Output
I also connected this with the difference between Self-Attention and Cross-Attention:
- Self-Attention: Q, K and V originate from the same sequence.
- Cross-Attention: Q comes from the Decoder, while K and V come from the Encoder.
This is the core mathematical mechanism behind the attention used in the original Transformer architecture. arXiv
💡 Key Takeaway
One of the biggest things I understood today is that attention is essentially a relevance → weighting → information retrieval process:
Q asks → K finds the relevant information → Softmax decides how important it is → V provides the information.
Rather than treating the attention formula as something to memorize, I'm now focusing on understanding what every matrix multiplication is actually doing.
📌 Learn → Write → Visualize → Implement → Connect
🔗 100 Days of Deep Learning:
https://github.com/AniketGaikwad18/100-Days-of-Deep-Learning
#100DaysOfDeepLearning #Day56 #DeepLearning #Transformers #AttentionMechanism #ScaledDotProductAttention #SelfAttention #CrossAttention #MachineLearning #ArtificialIntelligence #NLP #LearningInPublic #DeepLearningJourney
