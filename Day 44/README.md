Revision Day 44 — Beam Search 🔍🤖

Today’s Revision Day 44 focused on Beam Search, a decoding technique used in RNN/Seq2Seq models for sequence generation.

I learned how Beam Search explores multiple possible sequences instead of selecting only the most probable word at every timestep.

What I covered:
Greedy Search vs Beam Search
Beam width (k) and how it controls the number of candidate sequences retained
Step-by-step decoding from <SOS> to <EOS>
Sequence probability as the product of individual word probabilities
Using log probabilities to avoid numerical underflow
How increasing beam width increases the search space and computational cost
Advantages and limitations of Beam Search in sequence generation

A key takeaway for me was understanding that k = 1 behaves like Greedy Search, while k > 1 allows the model to keep multiple candidate sequences and compare them later.

🔗 My Deep Learning Journey:
https://github.com/AniketGaikwad18/100-Days-of-Deep-Learning

Revising older concepts while connecting them to sequence generation. One concept at a time. 🚀

#DeepLearning #BeamSearch #RNN #Seq2Seq #NLP #MachineLearning #AI #100DaysOfDeepLearning #LearningInPublic
