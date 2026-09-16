🧠 Day 35 — Backpropagation in RNN

Continuing my 100 Days of Deep Learning journey, today I went deeper into Recurrent Neural Networks (RNNs) by understanding how backpropagation works across multiple time steps.

Until now, I understood how an RNN processes sequential data. Today, the focus was on understanding how the model learns from its errors and updates its weights.

📚 What I learned today:

🔹 Forward Propagation in RNN

How each output depends on the current input and the previous hidden state.
Understanding the flow:
Input → Hidden State → Next Hidden State → Output
Binary classification using sigmoid activation and binary cross-entropy loss.

🔹 Unrolled RNN & Backward Gradient Flow

Unrolling the RNN across different time steps.
Understanding how gradients flow backward through the sequence.
The gradient at one time step can depend on computations from previous time steps.

🔹 Gradient w.r.t. Input Weight \((W_i)\)

Since the input weight is used across the sequence, its gradient considers contributions from all time steps.

🔹 Gradient w.r.t. Recurrent Weight \((W_h)\)

\(W_h\) is reused at every time step.
Therefore, the gradients from different time steps accumulate while calculating its overall gradient.

🔹 Weight Updates
Using Gradient Descent:

$$ W_i = W_i-\eta\frac{\partial L}{\partial W_i} $$ $$ W_h = W_h-\eta\frac{\partial L}{\partial W_h} $$ $$ W_o = W_o-\eta\frac{\partial L}{\partial W_o} $$

🔹 Problems with RNNs

Long-term dependency problem
Gradient-related problems
💡 Key Takeaway

The most important concept I took from today is that RNNs don't just backpropagate through layers — they backpropagate through time steps as well.

Understanding this gradient flow is essential for later understanding why architectures such as LSTM and GRU were developed.

🔗 GitHub:
https://github.com/AniketGaikwad18/100-Days-of-Deep-Learning/tree/main/Day%2035

#100DaysOfDeepLearning #DeepLearning #RNN #RecurrentNeuralNetwork #Backpropagation #NLP #NeuralNetworks #GradientDescent #Keras #TensorFlow #MachineLearning #AI #LearningByBuilding #LearningJourney
