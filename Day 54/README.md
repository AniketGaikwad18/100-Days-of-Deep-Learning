🧠 Day 54 — Autoregressive Models & Transformer Decoder
Continuing my 100 Days of Deep Learning journey, today I focused specifically on the Decoder side of the Transformer and understood how it generates output one token at a time.
🔹 What I Learned
- Autoregressive Generation — the model uses previously generated tokens to predict the next token.
  - I → I am → I am learning → I am learning AI
- Masked Self-Attention — prevents the decoder from accessing future tokens, avoiding information leakage during training.
- Cross-Attention — connects the Decoder with the Encoder.
  - Query (Q) → comes from the Decoder
  - Key (K) & Value (V) → come from the Encoder
- Feed-Forward Network (FFN) — applies nonlinear transformations to the representations.
- Add & Norm — combines residual connections with layer normalization.
- Linear + Softmax — converts the decoder output into probabilities for predicting the next token.
🔄 Decoder Flow
Output Embedding + Positional Encoding
↓
Masked Multi-Head Self-Attention
↓
Add & Norm
↓
Cross-Attention with Encoder Outputs
↓
Add & Norm
↓
Feed-Forward Network
↓
Add & Norm
↓
Linear + Softmax
↓
Next Token
💡 Key Takeaway
Today I understood an important connection between Autoregressive Generation, Masked Self-Attention, and Cross-Attention.
The Decoder essentially answers two questions:
“What have I generated so far?” → Masked Self-Attention
“What information from the input should I use?” → Cross-Attention

This helped me understand how the Transformer Decoder can generate a sequence step-by-step while still using the information learned by the Encoder. The original Transformer architecture uses masked decoder self-attention for autoregressive generation and encoder-decoder attention to connect the decoder with encoder representations. arXiv
📌 Learn → Write → Visualize → Connect → Implement
🔗 100 Days of Deep Learning:
https://github.com/AniketGaikwad18/100-Days-of-Deep-Learning
#100DaysOfDeepLearning #Day54 #DeepLearning #Transformers #TransformerDecoder #AutoregressiveModels #MaskedSelfAttention #CrossAttention #AttentionMechanism #NLP #MachineLearning #ArtificialIntelligence #LearningInPublic #DeepLearningJourney
