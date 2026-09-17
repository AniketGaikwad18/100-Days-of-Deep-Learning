Day 36 — Understanding LSTM (Long Short-Term Memory)

Continuing my 100 Days of Deep Learning journey, today I moved from understanding the limitations of RNNs to learning how LSTM networks handle long-term dependencies in sequential data.

The key idea I focused on today was simple but powerful: how can a neural network decide what information to remember, what to forget, and what to output?

📚 What I learned today:

🔹 Why LSTM?

Limitations of traditional RNNs with long sequences
The problem of losing important information over time
How LSTM introduces a memory cell for maintaining long-term information

🔹 RNN vs LSTM

RNN primarily carries information through the hidden state.
LSTM maintains both:
Hidden state \((h_t)\) → short-term information
Cell state \((C_t)\) → long-term information

🔹 The 3 LSTM Gates

Forget Gate \((f_t)\) → decides what information to remove
Input Gate \((i_t)\) → decides what new information to add
Output Gate \((o_t)\) → decides what information to expose as the hidden state

🔹 Understanding the LSTM Equations
I went through the complete flow of:
Forget → Add new information → Update cell state → Generate hidden state/output

Including the roles of sigmoid, tanh, element-wise multiplication, and vector concatenation.

💡 Key Takeaway

What I found most interesting today is that an LSTM doesn't simply “remember everything.”

It uses gates to control the flow of information — deciding what to forget, what to store, and what to output.

This gave me a much clearer understanding of how LSTMs are designed to handle long-term dependencies and address the gradient problems associated with traditional RNNs.

🔗 GitHub:
https://github.com/AniketGaikwad18/100-Days-of-Deep-Learning/tree/main/Day%2036

#100DaysOfDeepLearning #DeepLearning #LSTM #RNN #RecurrentNeuralNetwork #NLP #NeuralNetworks #MachineLearning #AI #TensorFlow #Keras #DeepLearningJourney #LearningByBuilding #LearningInPublic
