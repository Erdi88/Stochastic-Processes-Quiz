import streamlit as st

st.set_page_config(page_title="STA-2001 Mobile Quiz", layout="wide")
st.title("📊 STA-2001 Stochastic Processes Quiz")
st.write("Answer the questions below. Click **Check Answer** for each question to see if you got it right.")

# ---------------------------
# Define questions
# ---------------------------
questions = [
    # Week 1 - Probability
    {
        "question": "1) If X~Poisson(λ=2), what is P(X=0)?",
        "choices": ["0.135", "0.25", "0.1", "0.5"],
        "answer": "0.135"
    },
    {
        "question": "2) If X~Binomial(n=5, p=0.2), what is E[X]?",
        "choices": ["1", "0.5", "2", "1.2"],
        "answer": "1"
    },
    {
        "question": "3) Conditional expectation formula: E[X] = ?",
        "choices": [
            "E[X|Y] + Var(Y)",
            "E[E[X|Y]]",
            "Var(X|Y)",
            "E[X]*E[Y]"
        ],
        "answer": "E[E[X|Y]]"
    },
    {
        "question": "4) If P(A) = 0.3, P(B) = 0.4 and A,B independent, what is P(A∩B)?",
        "choices": ["0.12", "0.7", "0.1", "0.3"],
        "answer": "0.12"
    },
    # Week 2 - Markov Chains
    {
        "question": "5) For a DTMC, which property defines Markovian behavior?",
        "choices": [
            "Future depends only on present",
            "Future depends on past and present",
            "All states communicate",
            "Chain is reversible"
        ],
        "answer": "Future depends only on present"
    },
    {
        "question": "6) Stationary distribution π satisfies:",
        "choices": ["π = Pπ", "π = πP", "π = P^2", "π = I"],
        "answer": "π = πP"
    },
    # Week 3 - Poisson Process
    {
        "question": "7) N(t)~Poisson(λ=3). E[N(2)] = ?",
        "choices": ["6", "3", "2", "5"],
        "answer": "6"
    },
    {
        "question": "8) Inter-arrival times in a Poisson process are:",
        "choices": ["Exponential", "Uniform", "Normal", "Binomial"],
        "answer": "Exponential"
    },
    # Week 4 - Queueing/Birth-Death
    {
        "question": "9) In a Birth-Death process, transitions occur to:",
        "choices": ["Neighboring states", "Any state", "Absorbing state only", "Random state"],
        "answer": "Neighboring states"
    },
    {
        "question": "10) For a queue with λ=2, μ=1, the stationary probability P0 is proportional to:",
        "choices": ["e^{-2}", "1/2", "2", "1"],
        "answer": "e^{-2}"
    }
        ,
    # Week 1 - Probability & Conditioning
    {
        "question": "11) If X~Geometric(p=0.2), what is E[X]?",
        "choices": ["5", "0.2", "4", "1"],
        "answer": "5"
    },
    {
        "question": "12) If Var(X)=4 and E[X]=3, what is Var(2X+1)?",
        "choices": ["8", "9", "16", "4"],
        "answer": "16"
    },
    {
        "question": "13) If P(A|B)=0.5, P(B)=0.4, what is P(A∩B)?",
        "choices": ["0.2", "0.5", "0.9", "0.4"],
        "answer": "0.2"
    },
    {
        "question": "14) E[X|Y] is a function of:",
        "choices": ["X", "Y", "Both X and Y", "None"],
        "answer": "Y"
    },
    {
        "question": "15) If X~Poisson(λ=3), and Y~Poisson(λ=2), independent, what is E[X+Y]?",
        "choices": ["5", "6", "3", "2"],
        "answer": "5"
    },

    # Week 2 - Markov Chains
    {
        "question": "16) In a DTMC, a state i is absorbing if:",
        "choices": ["Pii = 0", "Pii = 1", "Pi,j = 1 for some j≠i", "Sum of row = 0"],
        "answer": "Pii = 1"
    },
    {
        "question": "17) In first-step analysis, the expected hitting time mi satisfies:",
        "choices": ["mi = sum Pij", "mi = 1 + sum Pij * mj", "mi = Pii", "mi = 0"],
        "answer": "mi = 1 + sum Pij * mj"
    },
    {
        "question": "18) Transient states have the property that:",
        "choices": ["Return with probability 1", "Return with probability <1", "Never leave", "Are always absorbing"],
        "answer": "Return with probability <1"
    },
    {
        "question": "19) Recurrent states have the property that:",
        "choices": ["Return with probability 1", "Return with probability <1", "Never leave", "Are absorbing only"],
        "answer": "Return with probability 1"
    },
    {
        "question": "20) For a 2-state Markov chain with P=[[0.7,0.3],[0.4,0.6]], stationary distribution π0 + π1 = ?",
        "choices": ["1", "0.5", "π0", "π1"],
        "answer": "1"
    },

    # Week 3 - Poisson Process
    {
        "question": "21) If N(t)~Poisson(λ=5), P(N(1)=3) = ?",
        "choices": ["125*e^-5 / 6", "e^-5 / 6", "5*e^-5", "0.125"],
        "answer": "125*e^-5 / 6"
    },
    {
        "question": "22) In a Poisson process, increments over non-overlapping intervals are:",
        "choices": ["Dependent", "Independent", "Always equal", "Zero"],
        "answer": "Independent"
    },
    {
        "question": "23) The waiting time until the first event in a Poisson process is:",
        "choices": ["Uniform", "Exponential", "Poisson", "Normal"],
        "answer": "Exponential"
    },
    {
        "question": "24) If λ=4 per hour, probability no events occur in 30 min?",
        "choices": ["e^-2", "0.5", "e^-4", "0.25"],
        "answer": "e^-2"
    },
    {
        "question": "25) Conditional on N(1)=3, the arrival times are distributed as:",
        "choices": ["Normal", "Uniform order statistics", "Exponential", "Poisson"],
        "answer": "Uniform order statistics"
    },

    # Week 4 - Queueing / Birth-Death
    {
        "question": "26) In a single-server queue with λ<μ, the system is:",
        "choices": ["Stable", "Unstable", "Always empty", "Never empty"],
        "answer": "Stable"
    },
    {
        "question": "27) In an M/M/1 queue, expected number in system L = ?",
        "choices": ["λ/(μ-λ)", "μ/(λ-μ)", "λ+μ", "λ*μ"],
        "answer": "λ/(μ-λ)"
    },
    {
        "question": "28) In a birth-death process, Pi = ?",
        "choices": [
            "Product of μ's over λ's times P0",
            "Sum of λ's times μ's",
            "Pi = 1/i",
            "Pi = 0"
        ],
        "answer": "Product of μ's over λ's times P0"
    },
    {
        "question": "29) Time reversibility occurs if:",
        "choices": ["λi*Pi = μi+1*Pi+1", "All states communicate", "Chain is absorbing", "Sum of row=1"],
        "answer": "λi*Pi = μi+1*Pi+1"
    },
    {
        "question": "30) In a queue with λ=2, μ=1, expected time to empty from state 2 is roughly:",
        "choices": ["(e^2-1)/2", "1", "2", "e^2"],
        "answer": "(e^2-1)/2"
    },
    {
        "question": "31) If X~Bernoulli(p=0.3), Var(X) = ?",
        "choices": ["0.21", "0.3", "0.09", "0.7"],
        "answer": "0.21"
    },
    {
        "question": "32) If X|Y~Binomial(Y,0.5), Y~Poisson(2), what is E[X]?",
        "choices": ["1", "2", "0.5", "4"],
        "answer": "1"
    },
    {
        "question": "33) For independent events A and B, P(A∪B) = ?",
        "choices": ["P(A)+P(B)-P(A)P(B)", "P(A)+P(B)", "P(A)P(B)", "P(A)-P(B)"],
        "answer": "P(A)+P(B)-P(A)P(B)"
    },
    {
        "question": "34) If P(A|B)=0.6, P(B)=0.5, then P(A∩B)=?",
        "choices": ["0.3", "0.1", "0.5", "0.6"],
        "answer": "0.3"
    },
    {
        "question": "35) Conditional variance formula: Var(X) = ?",
        "choices": [
            "Var(E[X|Y]) + E[Var(X|Y)]",
            "E[X|Y]",
            "Var(X|Y)",
            "E[X]*Var(Y)"
        ],
        "answer": "Var(E[X|Y]) + E[Var(X|Y)]"
    },
    {
        "question": "36) Aperiodic Markov chain has:",
        "choices": ["gcd of return times =1", "All states absorbing", "No stationary distribution", "Only one state"],
        "answer": "gcd of return times =1"
    },
    {
        "question": "37) n-step transition probabilities: P^n[i,j] = ?",
        "choices": ["Sum over k of P^n[i,k]*P^m[k,j]", "Pi,j", "Pi,j^2", "P0"],
        "answer": "Sum over k of P^n[i,k]*P^m[k,j]"
    },
    {
        "question": "38) In a 3-state Markov chain, which is true if all states communicate?",
        "choices": ["All states recurrent", "Some states transient", "Some states absorbing", "No stationary distribution"],
        "answer": "All states recurrent"
    },
    {
        "question": "39) Expected hitting time m0= ? in first-step analysis if P0->1=0.3, m1=5",
        "choices": ["1+0.3*5", "5", "0.3+5", "1+5*0.7"],
        "answer": "1+0.3*5"
    },
    {
        "question": "40) In a Markov chain, probability of absorption in state 3 starting from 0 = ?",
        "choices": ["Depends on transition matrix", "Always 0", "Always 1", "0.5"],
        "answer": "Depends on transition matrix"
    },

    # Week 3 - Poisson Process
    {
        "question": "41) If N(2)~Poisson(6), P(N(2)=3)= ?",
        "choices": ["36*e^-6", "6*e^-6", "e^-6 /6", "0.125"],
        "answer": "36*e^-6"
    },
    {
        "question": "42) For N(t)~Poisson(λ), E[N(t)] = ?",
        "choices": ["λ*t", "t/λ", "λ+t", "λ^t"],
        "answer": "λ*t"
    },
    {
        "question": "43) Probability of no arrivals in interval t in Poisson(λ)?",
        "choices": ["e^-λt", "λt", "1-λt", "0"], 
        "answer": "e^-λt"
    },
    {
        "question": "44) Waiting time until nth arrival in Poisson process follows:",
        "choices": ["Gamma(n,λ)", "Exponential(λ)", "Uniform(0,t)", "Binomial(n,p)"],
        "answer": "Gamma(n,λ)"
    },
    {
        "question": "45) Superposition of two independent Poisson processes with rates λ1 and λ2 results in?",
        "choices": ["Poisson(λ1+λ2)", "Poisson(λ1*λ2)", "Exponential(λ1+λ2)", "Binomial(λ1+λ2)"],
        "answer": "Poisson(λ1+λ2)"
    },
    {
        "question": "46) In M/M/1 queue, proportion of time system empty = ?",
        "choices": ["1-ρ", "ρ", "λ/μ", "μ/λ"], 
        "answer": "1-ρ"
    },
    {
        "question": "47) In M/M/1 queue, expected number in queue = ?",
        "choices": ["ρ^2/(1-ρ)", "ρ", "1/ρ", "ρ/(1-ρ)^2"], 
        "answer": "ρ^2/(1-ρ)"
    },
    {
        "question": "48) Birth-death process is a type of:",
        "choices": ["Continuous-time Markov chain", "Discrete-time chain", "Poisson process", "Deterministic process"], 
        "answer": "Continuous-time Markov chain"
    },
    {
        "question": "49) For λi and μi in birth-death, stationary distribution Pi = ?",
        "choices": ["(λ0*λ1*...λi-1)/(μ1*...*μi) * P0", "Sum of λ's", "1/i", "0"], 
        "answer": "(λ0*λ1*...λi-1)/(μ1*...*μi) * P0"
    },
    {
        "question": "50) In an M/M/2 queue with infinite queue, λ=2, μ=1, expected number in system roughly = ?",
        "choices": ["2.5", "2", "3", "4"], 
        "answer": "2.5"
    }

]

# ---------------------------
# Initialize session state for each question
# ---------------------------
for i in range(len(questions)):
    key_choice = f"choice_{i}"
    key_checked = f"checked_{i}"
    if key_choice not in st.session_state:
        st.session_state[key_choice] = None
    if key_checked not in st.session_state:
        st.session_state[key_checked] = False

# ---------------------------
# Display questions with individual Check Answer buttons
# ---------------------------
for i, q in enumerate(questions):
    st.write(f"**Q{i+1}: {q['question']}**")
    key_choice = f"choice_{i}"
    key_checked = f"checked_{i}"
    
    st.radio(
        "",
        q["choices"],
        key=key_choice
    )
    
    if st.button("Check Answer", key=f"btn_{i}"):
        st.session_state[key_checked] = True
    
    if st.session_state[key_checked]:
        user_ans = st.session_state[key_choice]
        correct = user_ans == q["answer"]
        st.markdown(f"**Your answer:** {user_ans} — {'✅ Correct!' if correct else f'❌ Wrong (Correct: {q['answer']})'}")
    
    st.markdown("---")  # separator

