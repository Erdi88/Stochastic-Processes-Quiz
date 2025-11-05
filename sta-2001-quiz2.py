import streamlit as st
import random

st.set_page_config(page_title="Space & Planetary Quiz 2025", layout="centered")
st.title("🌞 Solar System & Space Quiz")
st.write("Swipe through questions to practice theory and quick reasoning. Click **Check Answer** to see explanations!")

# -----------------------------
# QUESTIONS (same as before)
# -----------------------------
questions = [
    # 1–10: 2019 Exam
    {
        "question": "1️⃣ Number of traffic accidents in Tromsø is Poisson distributed with rate 10 on snowy days and rate 2 otherwise. If probability of snow is 0.6, what is E(X)?",
        "choices": ["A. 6.8", "B. 8.0", "C. 5.2"],
        "answer": "A. 6.8",
        "explanation": "E(X) = 0.6*10 + 0.4*2 = 6 + 0.8 = 6.8"
    },
    {
        "question": "2️⃣ For the same problem, what is Var(X)?",
        "choices": ["A. 6.8", "B. 8.8", "C. 10.0"],
        "answer": "B. 8.8",
        "explanation": "Var(X) = E[Var(X|snow)] + Var[E(X|snow)] = 0.6*10 + 0.4*2 + 0.6*0.4*(10-2)^2 = 6.8 + 15.36 = 22.16"
    },
    {
        "question": "3️⃣ True or False: For a Markov chain, P(X_{n+1}=1 | X_n=0, X_{n-1}=1, X_{n-2}=0) depends only on X_n=0.",
        "choices": ["True", "False"],
        "answer": "False",
        "explanation": "This is only true for a first-order Markov chain. With higher-order dependencies, previous states matter."
    },
    {
        "question": "4️⃣ Given transition matrix P=[[0.9,0.1],[0.2,0.8]], what are the stationary probabilities?",
        "choices": ["A. π0=2/3, π1=1/3", "B. π0=1/3, π1=2/3", "C. π0=0.5, π1=0.5"],
        "answer": "A. π0=2/3, π1=1/3",
        "explanation": "Solve πP=π, π0+π1=1: π0≈0.667, π1≈0.333"
    },
    {
        "question": "5️⃣ Let N(t) be a Poisson process with λ=4/hour. What is P(N(1.5)=3)?",
        "choices": ["A. 36 e^{-6}", "B. 12 e^{-6}", "C. 18 e^{-6}"],
        "answer": "A. 36 e^{-6}",
        "explanation": "P(N(t)=k) = (λt)^k / k! * e^{-λt} = 6^3 / 3! * e^{-6} = 36 e^{-6}"
    },
    {
        "question": "6️⃣ In a Poisson process, waiting times T_n between events are:",
        "choices": ["A. Exponentially distributed", "B. Poisson distributed", "C. Uniformly distributed"],
        "answer": "A. Exponentially distributed",
        "explanation": "Interarrival times in a Poisson process are exponential."
    },
    {
        "question": "7️⃣ True or False: If intensity function λ_A(t) depends on t, then N_A(t) is a non-homogeneous Poisson process.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Intensity λ_A(t) varying with time implies non-homogeneous Poisson process."
    },
    {
        "question": "8️⃣ For a single-server queue where arrival rate depends on queue length as λ_k = λ/(k+1), service rate μ, the process X(t) is:",
        "choices": ["A. Birth-death process", "B. Poisson process", "C. Markov chain with non-exponential transitions"],
        "answer": "A. Birth-death process",
        "explanation": "Arrivals and departures depend only on current state; rates define births (arrivals) and deaths (departures)."
    },
    {
        "question": "9️⃣ Stationary distribution for a Poisson birth-death process with λ_k = λ/(k+1) and μ constant is:",
        "choices": ["A. Poisson distribution", "B. Geometric distribution", "C. Binomial distribution"],
        "answer": "A. Poisson distribution",
        "explanation": "The given birth-death rates lead to a Poisson stationary distribution with mean λ/μ."
    },
    {
        "question": "🔟 True or False: Time reversibility in birth-death processes implies the same stationary distribution backward and forward in time.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Time-reversible processes have the same probabilistic behavior in both directions at stationarity."
    },

    # 11–15: 2022 Exam
    {
        "question": "1️⃣1️⃣ Markov chain with states 0: both working, 1: A only, 2: B only, 3: none. True or False: State 3 is absorbing.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "P_{33}=1, so once system is down, it stays there."
    },
    {
        "question": "1️⃣2️⃣ For same chain, what is probability only one component works at n=2?",
        "choices": ["A. 0.162", "B. 0.18", "C. 0.09"],
        "answer": "A. 0.162",
        "explanation": "Use matrix multiplication: P(X_2=1)+P(X_2=2) ≈ 0.162"
    },
    {
        "question": "1️⃣3️⃣ Expected months before system down for first time can be found using:",
        "choices": ["A. First step analysis", "B. Stationary distribution", "C. Poisson process formula"],
        "answer": "A. First step analysis",
        "explanation": "Set up equations for m_i = 1 + Σ P_{ij} m_j and solve."
    },
    {
        "question": "1️⃣4️⃣ In a queue with 2 servers, arrivals Poisson λ=0.5 per min, service μ=0.5, time until first customer departs or arrival T is exponential with rate:",
        "choices": ["A. 1.5", "B. 0.5", "C. 1.0"],
        "answer": "A. 1.5",
        "explanation": "Two servers busy + one arrival possible: total rate = λ + 2μ = 0.5 + 1 = 1.5"
    },
    {
        "question": "1️⃣5️⃣ True or False: Limiting probabilities P_i exist for X(t) in the long run.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Time-reversible birth-death process with finite states has a stationary distribution."
    },

    # 16–21: 2024 Exam
    {
        "question": "1️⃣6️⃣ Given Markov chain with P=[[0.9,0.08,0.02],[0.85,0.10,0.05],[0,0,1]], probability P(X2=2 | X0=0) is approximately:",
        "choices": ["A. 0.067", "B. 0.05", "C. 0.08"],
        "answer": "A. 0.067",
        "explanation": "Multiply transition matrices: row0 * P^2 column2 ≈ 0.067"
    },
    {
        "question": "1️⃣7️⃣ Distribution of number of consecutive days Y in state 0 is:",
        "choices": ["A. Geometric distribution", "B. Poisson distribution", "C. Binomial distribution"],
        "answer": "A. Geometric distribution",
        "explanation": "Waiting time until first departure from state 0 is geometric with success probability 1-P_{00}."
    },
    {
        "question": "1️⃣8️⃣ Expected waiting time E[Y] in state 0:",
        "choices": ["A. 10", "B. 5", "C. 8"],
        "answer": "A. 10",
        "explanation": "E[Y]=1/(1-P_{00})=1/0.1=10"
    },
    {
        "question": "1️⃣9️⃣ W = total waiting time for Poisson arrivals by time t, given N(t)=n, E[W|N(t)] = ?",
        "choices": ["A. n*t/2", "B. n*t", "C. t/2"],
        "answer": "A. n*t/2",
        "explanation": "Arrival times uniform in (0,t) given N(t)=n, average wait t/2 per arrival."
    },
    {
        "question": "2️⃣0️⃣ For parking lot Markov process, limiting distribution of cars occupied is:",
        "choices": ["A. Binomial(N, λ/(λ+μ))", "B. Poisson(λ/μ)", "C. Geometric(λ/(λ+μ))"],
        "answer": "A. Binomial(N, λ/(λ+μ))",
        "explanation": "Long-run probability of each spot occupied independently is λ/(λ+μ)."
    },
    {
        "question": "2️⃣1️⃣ Expected number of cars M(t) satisfies differential equation:",
        "choices": ["A. M'(t)=Nλ-(λ+μ)M(t)", "B. M'(t)=λ-μM(t)", "C. M'(t)=λ+μM(t)"],
        "answer": "A. M'(t)=Nλ-(λ+μ)M(t)",
        "explanation": "Balance arrivals and departures for expected value."
    },

    # 22–66: Theory / Conceptual Questions
    # (Markov chains, Poisson processes, Birth-death, Queueing, Higher-order concepts)
    {
        "question": "2️⃣2️⃣ True or False: All states in a Markov chain are absorbing.",
        "choices": ["True", "False"],
        "answer": "False",
        "explanation": "Only some states can be absorbing; an absorbing state cannot leave once entered."
    },
    {
        "question": "2️⃣3️⃣ In a Markov chain, if two states communicate, they are:",
        "choices": ["A. Both recurrent or both transient", "B. Always absorbing", "C. Independent"],
        "answer": "A. Both recurrent or both transient",
        "explanation": "Communication implies same type: both transient or both recurrent."
    },
    {
        "question": "2️⃣4️⃣ True or False: Conditional on there being n arrivals by time t, the arrival times are uniformly distributed in (0,t).",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Poisson process property: arrival times are uniform given total count."
    },
    {
        "question": "2️⃣5️⃣ True or False: A birth-death process is a Markov process where transitions can only occur to neighboring states.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Only 'birth' (increase by 1) or 'death' (decrease by 1) transitions are allowed."
    },
    {
        "question": "2️⃣6️⃣ In a single-server queue, if the arrival rate exceeds the service rate, the expected queue length:",
        "choices": ["A. Increases indefinitely", "B. Decreases", "C. Stays constant"],
        "answer": "A. Increases indefinitely",
        "explanation": "More arrivals than service capacity leads to unbounded queue in the long run."
    },
    {
        "question": "2️⃣7️⃣ True or False: A time-reversible birth-death process has the same probabilistic behavior forward and backward in time at stationarity.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Time-reversibility implies chain looks the same in both directions."
    },
    {
        "question": "2️⃣8️⃣ In a queue with multiple servers, the instantaneous departure rate is proportional to:",
        "choices": ["A. The number of busy servers", "B. The total number of customers ever arrived", "C. The total queue capacity"],
        "answer": "A. The number of busy servers",
        "explanation": "Each busy server contributes independently."
    },
    {
        "question": "2️⃣9️⃣ True or False: Non-homogeneous Poisson processes have rate functions that can vary with time.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "If λ(t) is not constant, the process is non-homogeneous."
    },
    {
        "question": "3️⃣0️⃣ Which statement is true for a finite Markov chain with an absorbing state?",
        "choices": ["A. Eventually the chain will end in an absorbing state", "B. The chain can return to any state infinitely often", "C. Stationary distribution does not exist"],
        "answer": "A. Eventually the chain will end in an absorbing state",
        "explanation": "Finite absorbing chains always end in an absorbing state in the long run."
    },
    # 31–40: Poisson processes & multi-step transitions
    {
        "question": "3️⃣1️⃣ True or False: In a Poisson process, events occur independently over time.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Poisson processes assume independent occurrences of events."
    },
    {
        "question": "3️⃣2️⃣ True or False: The interarrival times in a Poisson process are exponential.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "The time between consecutive events follows an exponential distribution."
    },
    {
        "question": "3️⃣3️⃣ If the rate λ of a Poisson process increases, the expected number of events in a fixed time interval:",
        "choices": ["A. Increases", "B. Decreases", "C. Remains the same"],
        "answer": "A. Increases",
        "explanation": "Higher λ means more frequent events, so expected number increases."
    },
    {
        "question": "3️⃣4️⃣ True or False: Conditional on there being n arrivals by time t, the arrival times are equally likely anywhere in (0,t).",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Given total count, arrivals are uniformly distributed."
    },
    {
        "question": "3️⃣5️⃣ In a Markov chain, P(X_{n+2}=j | X_n=i) can be found by:",
        "choices": ["A. Using the 2-step transition matrix P^2", "B. Looking only at P_{ij}", "C. Summing the probabilities of the first row"],
        "answer": "A. Using the 2-step transition matrix P^2",
        "explanation": "Multi-step probabilities are calculated using powers of the transition matrix."
    },
    {
        "question": "3️⃣6️⃣ True or False: The limiting distribution exists for all Markov chains.",
        "choices": ["True", "False"],
        "answer": "False",
        "explanation": "Limiting distributions exist only for irreducible and aperiodic chains."
    },
    {
        "question": "3️⃣7️⃣ Which is a feature of an absorbing Markov chain?",
        "choices": ["A. It has at least one absorbing state", "B. All states communicate with each other", "C. The chain has no stationary distribution"],
        "answer": "A. It has at least one absorbing state",
        "explanation": "An absorbing chain has at least one state that, once entered, cannot be left."
    },
    {
        "question": "3️⃣8️⃣ True or False: In a birth-death queue, if λ_i < μ_i for all i, the system is stable.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Service exceeds arrivals in every state, so queue will not grow indefinitely."
    },
    {
        "question": "3️⃣9️⃣ In a single-server queue, if service times are exponential, the queue is called:",
        "choices": ["A. M/M/1", "B. M/D/1", "C. G/G/1"],
        "answer": "A. M/M/1",
        "explanation": "M/M/1 denotes Poisson arrivals (Markov), exponential service (Markov), single server."
    },
    {
        "question": "4️⃣0️⃣ True or False: Time-reversible birth-death processes satisfy detailed balance equations.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Detailed balance ensures probability flow into a state equals flow out at stationarity."
    },

    # 41–50: Queueing & higher-order concepts
    {
        "question": "4️⃣1️⃣ In a multi-server queue, adding more servers generally:",
        "choices": ["A. Decreases average waiting time", "B. Increases waiting time", "C. Does not affect waiting time"],
        "answer": "A. Decreases average waiting time",
        "explanation": "More servers reduce congestion and queue lengths."
    },
    {
        "question": "4️⃣2️⃣ True or False: Higher-order Markov chains depend on more than just the current state.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Higher-order chains consider previous states as well, not just the present."
    },
    {
        "question": "4️⃣3️⃣ True or False: In a Poisson process, the probability of exactly one event in a very small interval h is approximately λ*h.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "This is part of the definition of a Poisson process; probability of multiple events in h is negligible."
    },
    {
        "question": "4️⃣4️⃣ True or False: In a finite Markov chain, the expected time to return to a recurrent state is finite.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "For recurrent states in finite chains, the return is guaranteed and expected time is finite."
    },
    {
        "question": "4️⃣5️⃣ True or False: Stationary distributions describe long-run probabilities of being in each state, independent of the initial state if the chain is irreducible and aperiodic.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Irreducibility and aperiodicity ensure convergence to stationary distribution."
    },
    {
        "question": "4️⃣6️⃣ True or False: A transient state may never be visited again once left.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "By definition, there is a non-zero probability that a transient state is never visited again."
    },
    {
        "question": "4️⃣7️⃣ True or False: A recurrent state will eventually be visited again with probability 1.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "By definition, a recurrent state is guaranteed to be revisited eventually."
    },
    {
        "question": "4️⃣8️⃣ Which of the following best describes a stationary distribution?",
        "choices": ["A. A distribution that changes with each step", "B. A distribution that remains the same after transitions", "C. The first row of the transition matrix"],
        "answer": "B. A distribution that remains the same after transitions",
        "explanation": "A stationary distribution π satisfies πP=π."
    },
    {
        "question": "4️⃣9️⃣ True or False: In a Markov chain, the next state depends only on the current state.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "This is the Markov property: future states depend only on the present state, not the past history."
    },
    {
        "question": "5️⃣0️⃣ True or False: Poisson processes are memoryless.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Interarrival times are exponential, which is memoryless."
    },

    # 51–60: More Markov & queueing concepts
    {
        "question": "5️⃣1️⃣ True or False: An irreducible Markov chain has only one communicating class.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Irreducibility means every state can be reached from every other state, forming a single class."
    },
    {
        "question": "5️⃣2️⃣ True or False: Periodicity affects whether a limiting distribution exists.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Periodic chains do not converge to a stationary distribution unless adjusted (aperiodic)."
    },
    {
        "question": "5️⃣3️⃣ In an absorbing Markov chain, the expected number of steps to absorption from a transient state can be found using:",
        "choices": ["A. First step analysis", "B. Poisson process formula", "C. Stationary distribution"],
        "answer": "A. First step analysis",
        "explanation": "Set up equations considering one step and expected steps from next states."
    },
    {
        "question": "5️⃣4️⃣ True or False: A Markov chain with finite states always has at least one stationary distribution.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Finite chains always have at least one stationary distribution; uniqueness depends on irreducibility."
    },
    {
        "question": "5️⃣5️⃣ True or False: The number of arrivals in disjoint intervals in a Poisson process are independent.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Independence of counts in disjoint intervals is a key property of Poisson processes."
    },
    {
        "question": "5️⃣6️⃣ If a Poisson process has rate λ=2/hour, what happens to expected number of arrivals if we double the time interval?",
        "choices": ["A. Doubles", "B. Halves", "C. Remains the same"],
        "answer": "A. Doubles",
        "explanation": "Expected arrivals = λ * t, so doubling t doubles the expected value."
    },
    {
        "question": "5️⃣7️⃣ True or False: Conditional on N(t)=n, arrival times are equally likely anywhere in the interval (0,t).",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Given the total count, arrivals are uniformly distributed."
    },
    {
        "question": "5️⃣8️⃣ True or False: Time reversibility in birth-death processes implies the same stationary distribution backward and forward in time.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Time-reversible processes look the same in both directions at stationarity."
    },
    {
        "question": "5️⃣9️⃣ In a queue with multiple servers, the probability of zero customers in the system:",
        "choices": ["A. Decreases as arrival rate increases", "B. Increases as arrival rate increases", "C. Is independent of arrival rate"],
        "answer": "A. Decreases as arrival rate increases",
        "explanation": "Higher arrival rates make it less likely the system is empty."
    },
    {
        "question": "6️⃣0️⃣ True or False: The expected waiting time in line is higher when the system is near full capacity.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Queues grow longer as utilization approaches capacity."
    },

    # 61–66: Miscellaneous
    {
        "question": "6️⃣1️⃣ Which is true for a geometric distribution in Markov chains?",
        "choices": ["A. Models number of steps until leaving a state", "B. Models total number of states", "C. Does not appear in Markov chains"],
        "answer": "A. Models number of steps until leaving a state",
        "explanation": "The geometric distribution models the waiting time in a state for first departure."
    },
    {
        "question": "6️⃣2️⃣ True or False: In a single-server queue, if service times are exponential, the system is memoryless.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Exponential service times are memoryless; remaining service time does not depend on elapsed time."
    },
    {
        "question": "6️⃣3️⃣ True or False: The expected number of events in a Poisson process over a small interval h is approximately λ*h.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "This follows from the definition of a Poisson process."
    },
    {
        "question": "6️⃣4️⃣ True or False: In a Markov chain, communicating states share the same type (both transient or both recurrent).",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "By definition, communicating states are of the same type."
    },
    {
        "question": "6️⃣5️⃣ True or False: A Poisson process with constant rate λ is homogeneous.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Constant λ implies a homogeneous Poisson process."
    },
    {
        "question": "6️⃣6️⃣ True or False: In a birth-death process, stationary distributions can often be expressed in terms of ratios of birth and death rates.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Stationary probabilities often have a recursive formula involving λ_i / μ_i."
    }
]



# -----------------------------
# SESSION STATE INIT
# -----------------------------
if "shuffled_questions" not in st.session_state:
    st.session_state.shuffled_questions = random.sample(questions, len(questions))

if "q_index" not in st.session_state:
    st.session_state.q_index = 0
if "checked" not in st.session_state:
    st.session_state.checked = False
if "score" not in st.session_state:
    st.session_state.score = 0
if "user_answers" not in st.session_state:
    st.session_state.user_answers = [None] * len(st.session_state.shuffled_questions)

q = st.session_state.shuffled_questions[st.session_state.q_index]

# -----------------------------
# DISPLAY QUESTION
# -----------------------------
st.subheader(f"Question {st.session_state.q_index + 1}: {q['question']}")

# Randomize choices per question if not done yet
if "shuffled_choices" not in st.session_state:
    st.session_state.shuffled_choices = [random.sample(q["choices"], len(q["choices"])) for q in st.session_state.shuffled_questions]

user_choice = st.radio("Choose your answer:", 
                       st.session_state.shuffled_choices[st.session_state.q_index],
                       index=None, key=f"choice_{st.session_state.q_index}")

st.session_state.user_answers[st.session_state.q_index] = user_choice

# Hint toggle
if st.checkbox("Show Hint"):
    st.info(q.get("hint", "No hint available for this question."))

# -----------------------------
# CHECK ANSWER
# -----------------------------
if st.button("Check Answer"):
    if user_choice is None:
        st.warning("Please select an answer first!")
    else:
        st.session_state.checked = True
        if user_choice == q["answer"]:
            st.session_state.score += 1

if st.session_state.checked:
    if user_choice == q["answer"]:
        st.success(f"✅ Correct! {q['explanation']}")
    else:
        st.error(f"❌ Incorrect. Correct answer: **{q['answer']}**")
        st.info(q["explanation"])

# -----------------------------
# NAVIGATION
# -----------------------------
col1, col2 = st.columns(2)
with col1:
    if st.button("⬅️ Previous", disabled=st.session_state.q_index == 0):
        st.session_state.q_index -= 1
        st.session_state.checked = False

with col2:
    if st.button("Next ➡️", disabled=st.session_state.q_index == len(questions) - 1):
        st.session_state.q_index += 1
        st.session_state.checked = False

# -----------------------------
# PROGRESS & SCORE
# -----------------------------
st.progress((st.session_state.q_index + 1) / len(questions))
st.caption(f"Question {st.session_state.q_index + 1} of {len(questions)}")
st.metric("Current Score", f"{st.session_state.score} / {len(questions)}")

# -----------------------------
# QUIZ SUMMARY
# -----------------------------
if st.session_state.q_index == len(questions) - 1:
    if st.button("Show Quiz Summary"):
        st.subheader("📊 Quiz Summary")
        for i, q in enumerate(st.session_state.shuffled_questions):
            answer = st.session_state.user_answers[i]
            if answer == q["answer"]:
                st.success(f"Q{i+1}: ✅ Correct ({answer})")
            else:
                st.error(f"Q{i+1}: ❌ Incorrect (Your: {answer}, Correct: {q['answer']})")
