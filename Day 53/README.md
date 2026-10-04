🧠 Day 53 — Transformer Architecture: Complete View
Continuing my 100 Days of Deep Learning journey, today I studied the complete Transformer architecture and focused on understanding how the Encoder and Decoder work together.
🔹 What I Learned
- Input Embedding — converts input tokens into vector representations.
- Positional Encoding — provides information about the position of each token.
- Multi-Head Self-Attention — allows tokens to capture relationships with other tokens.
- Masked Self-Attention — prevents the decoder from looking at future tokens during generation.
- Multi-Head Cross-Attention — allows the decoder to use information produced by the Encoder.
- Feed-Forward Network (FFN) — applies nonlinear transformations to the representations.
- Add & Norm — combines residual connections with layer normalization.
- Linear + Softmax — converts the final decoder representation into probabilities for the next token.
🔄 Working Flow
Input → Embedding + Positional Encoding
↓
N Encoder Layers → Encoder Output / Memory
↓
Decoder → Masked Self-Attention + Cross-Attention
↓
N Decoder Layers
↓
Linear + Softmax
↓
Next-Word Probabilities
I also understood that the Transformer architecture can be built by stacking multiple encoder and decoder layers, allowing the model to progressively process and transform the representations. The original Transformer paper introduced this attention-based encoder-decoder architecture without recurrence or convolution. arXiv
💡 Key Takeaway
After learning Scaled Dot-Product Attention → BertViz → Transformer components, this session helped me connect everything into one complete architecture.
The bigger picture is now clearer:
Embedding → Position → Attention → FFN → Add & Norm → Encoder/Decoder → Prediction
I'm focusing on understanding how each component contributes to the final prediction, rather than simply memorizing the Transformer diagram.
📌 Learn → Write → Visualize → Connect → Implement
🔗 100 Days of Deep Learning:
https://github.com/AniketGaikwad18/100-Days-of-Deep-Learning
#100DaysOfDeepLearning #Day53 #DeepLearning #Transformers #TransformerArchitecture #SelfAttention #CrossAttention #NLP #MachineLearning #ArtificialIntelligence #LearningInPublic #DeepLearningJourney
