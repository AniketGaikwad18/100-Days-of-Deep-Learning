🧠 Day 51 — Visualizing Attention with BertViz

Continuing my 100 Days of Deep Learning journey, today I explored Transformer attention visually using BertViz.

Instead of only understanding attention through equations, I used visualizations to see how different Transformer layers and attention heads connect one token to another.

🔹 What I Explored
BERT + BertViz — loaded bert-base-uncased and extracted its attention weights.
Head View — visualized attention connections for individual attention heads within a layer.
Model View — examined attention patterns across multiple layers and heads.
Neuron View — explored the intermediate Query and Key representations involved in producing attention weights.
Used the sentences:
“The cat sat on the mat”
“The cat lay on the rug”
Observed that different heads and layers can produce different attention patterns, showing that attention is distributed differently throughout the Transformer.

The implementation used BERT with output_attentions=True, tokenized the two sentences, and passed the resulting attention weights to BertViz.

🔍 What the Visualizations Helped Me Understand

The visualizations made the abstract idea of attention much more concrete:

Token → Attention Head → Attention Weights → Relationships between Tokens

In the Head View, line thickness represents the attention value, while different colors represent different attention heads. The Model View gives a broader view across layers and heads, while the Neuron View goes deeper into the Query/Key computations.

💡 Key Takeaway

Attention is not one single pattern inside a Transformer.

Different heads and layers can learn different relationships between tokens, and visualization tools like BertViz make these otherwise hidden computations easier to inspect.

This also connects nicely with what I learned on Day 50 — Scaled Dot-Product Attention: the equations explain how attention is calculated, while BertViz helps me see what those attention patterns actually look like inside BERT.

🔗 GitHub:
https://github.com/AniketGaikwad18/100-Days-of-Deep-Learning

🔗 Reference: Timo Denk's explanation of positional relationships in Transformer positional encoding.

#100DaysOfDeepLearning #DeepLearning #Transformers #BERT #BertViz #AttentionMechanism #SelfAttention #NLP #MachineLearning #ArtificialIntelligence #LearningInPublic
