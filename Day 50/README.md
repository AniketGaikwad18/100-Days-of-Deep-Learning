🧠 Day 50 — Scaled Dot-Product Attention

Continuing my 100 Days of Deep Learning journey, today I studied one of the core components behind the Transformer architecture — Scaled Dot-Product Attention.

🔹 What I Learned
Attention Mechanism — helps the model determine which words/tokens are important in a sequence.
Query (Q) — represents what the current token is looking for.
Key (K) — helps determine how well another token matches the query.
Value (V) — contains the information that gets passed forward.
Dot Product Similarity — calculates how strongly Query and Key are related.
Scaling — dividing by √dₖ prevents excessively large dot-product values and helps maintain stable gradients.
Softmax — converts similarity scores into attention weights.
Weighted Sum — combines the Value vectors according to their attention weights to produce the contextual output.
🔄 Overall Flow

Q, K, V → QKᵀ → Scale by √dₖ → Softmax → Attention Weights → Weighted Sum of V → Output

📐 Core Formula

Attention(Q, K, V) = Softmax(QKᵀ / √dₖ)V

💡 Key Takeaway

I understood that attention is not simply about finding the most important word. It computes relationships between tokens, converts those relationships into weights, and then uses those weights to combine information from the Value vectors.

This gives the Transformer a way to build context-aware representations without relying on recurrence.

📌 Learn → Write → Revise → Implement → Connect

#100DaysOfDeepLearning #DeepLearning #Transformers #AttentionMechanism #SelfAttention #MachineLearning #ArtificialIntelligence #LearningInPublic #DeepLearningJourney

