# stochastic_quiz.py
import streamlit as st
import random

st.set_page_config(page_title="STA-2001 Stochastic Processes Quiz", layout="centered")

st.title("🎲 STA-2001 Stochastic Processes Quiz")
st.write("Test your knowledge from the first four weeks — probability, conditioning, Markov chains, Poisson processes, and more!")

# -----------------------
# QUIZ DATABASE
# -----------------------

questions = [
    {
        "question": "In a fair coin toss, what is the sample space?",
        "options": ["{H}", "{T}", "{H,T}", "{HH, TT}"],
        "answer": 2
    },
    {
        "question": "If two events A and B are independent, then:",
        "options": [
            "P(A ∩ B) = P(A) + P(B)",
            "P(A ∩ B) = P(A)P(B)",
            "P(A|B) = 1",
            "P(A|B) = P(B)"
        ],
        "answer": 1
    },
    {
        "question": "For a discrete random variable X, the expectation E[X] is:",
        "options": [
            "E[X] = ∫ x f(x) dx",
            "E[X] = Σ x² p(x)",
            "E[X] = Σ x p(x)",
            "E[X] = Σ p(x)/x"
        ],
        "answer": 2
    },
    {
        "question": "If X ~ Poisson(λ), then Var(X) equals:",
        "options": ["λ²", "1/λ", "λ", "√λ"],
        "answer": 2
    },
    {
        "question": "The exponential distribution is:",
        "options": [
            "Discrete, for number of trials until success",
            "Continuous, with memoryless property",
            "Uniform over finite outcomes",
            "Continuous, symmetric around mean"
        ],
        "answer": 1
    },
    {
        "question": "Bayes’ theorem relates:",
        "options": [
            "Joint and marginal probabilities",
            "Conditional and unconditional probabilities",
            "Discrete and continuous probabilities",
            "Posterior and likelihood probabilities"
        ],
        "answer": 3
    },
    {
        "question": "For a Markov chain, the Markov property states:",
        "options": [
            "Future depends on entire past",
            "Future is independent of past given present",
            "Present is independent of past",
            "Transitions are deterministic"
        ],
        "answer": 1
    },
    {
        "question": "The n-step transition matrix of a Markov chain is given by:",
        "options": ["Pⁿ", "nP", "P + nI", "Pn/P"],
        "answer": 0
    },
    {
        "question": "A state i is absorbing if:",
        "options": [
            "Pii = 0",
            "Pii < 1",
            "Pii = 1",
            "It can reach all other states"
        ],
        "answer": 2
    },
    {
        "question": "For a Poisson process with rate λ, inter-arrival times are:",
        "options": [
            "Uniform(0, λ)",
            "Bernoulli(p)",
            "Exponential(λ)",
            "Gamma(λ,1)"
        ],
        "answer": 2
    },
    {
        "question": "E[X] = E[E[X|Y]] is known as:",
        "options": [
            "Law of large numbers",
            "Tower property / law of total expectation",
            "Central limit theorem",
            "Conditional variance formula"
        ],
        "answer": 1
    },
    {
        "question": "Var(X) = E[Var(X|Y)] + Var(E[X|Y]) expresses:",
        "options": [
            "Conditional independence",
            "Law of total variance",
            "Bayesian updating",
            "Markov chain balance equations"
        ],
        "answer": 1
    },
    {
        "question": "In a birth–death process, transitions occur:",
        "options": [
            "Only to neighboring states",
            "To any state with equal probability",
            "Instantly between all states",
            "In batches of size ≥ 2"
        ],
        "answer": 0
    },
    {
        "question": "Stationary distribution π satisfies:",
        "options": [
            "π = Pπ",
            "π = πP",
            "πP = 0",
            "Pπ = 0"
        ],
        "answer": 1
    },
    {
        "question": "For an Exponential(λ) distribution, E[X] = ?",
        "options": ["λ", "1/λ", "λ²", "√λ"],
        "answer": 1
    },
    {
        "question": "If N(t) ~ Poisson(λt), then P(N(t)=k) = ?",
        "options": [
            "λt/k!",
            "e^{-λt}(λt)^k/k!",
            "tλ/k!",
            "1/(λt)"
        ],
        "answer": 1
    },
    {
        "question": "A chain is ergodic if it is:",
        "options": [
            "Aperiodic and positive recurrent",
            "Irreducible and transient",
            "Absorbing and deterministic",
            "Reversible only"
        ],
        "answer": 0
    },
    {
        "question": "In simulation, the inverse transform method is used to:",
        "options": [
            "Generate random variables from uniform(0,1) inputs",
            "Invert Markov matrices",
            "Find stationary distributions",
            "Estimate λ from data"
        ],
        "answer": 0
    }
]

random.shuffle(questions)

# -----------------------
# QUIZ LOGIC
# -----------------------

score = 0
st.markdown("---")

for i, q in enumerate(questions):
    st.subheader(f"Question {i+1}: {q['question']}")
    choice = st.radio("Choose one:", q["options"], key=f"q{i}")
    if st.button(f"Check {i+1}"):
        if q["options"].index(choice) == q["answer"]:
            st.success("✅ Correct!")
            score += 1
        else:
            correct_ans = q["options"][q["answer"]]
            st.error(f"❌ Incorrect. Correct answer: {correct_ans}")
    st.markdown("---")

st.write("🧮 Tip: refresh to reshuffle questions each time!")

