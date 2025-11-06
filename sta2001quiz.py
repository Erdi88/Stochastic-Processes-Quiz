import streamlit as st
import random

st.set_page_config(page_title="Space Quiz 2025", layout="centered")

# -----------------------------
# QUESTIONS (same as before)
# -----------------------------


stochastic_quiz = [
    {
        "question": "The number of accidents tomorrow depends on whether it snows. This model is an example of what type of distribution?",
        "choices": ["A. Simple Poisson", "B. Mixture distribution", "C. Binomial", "D. Normal"],
        "answer": "B. Mixture distribution",
        "explanation": "Because the Poisson rate λ depends on a random condition (snow or not), the overall model is a mixture of two Poisson distributions."
    },
    {
        "question": "In a mixed Poisson model, E(X) is found using which rule?",
        "choices": ["A. Bayes’ theorem", "B. Law of total expectation", "C. Poisson addition property", "D. Moment generating function"],
        "answer": "B. Law of total expectation",
        "explanation": "The expected value is computed by conditioning on each possible scenario and summing weighted by their probabilities."
    },
    {
        "question": "What does P(X=0) represent in a Poisson model of accidents?",
        "choices": ["A. Probability of no accidents", "B. Expected number of accidents", "C. Mean rate of accidents", "D. Variance of accidents"],
        "answer": "A. Probability of no accidents",
        "explanation": "P(X=0) gives the probability that zero accidents occur on that day."
    },
    {
        "question": "The process {Xₙ} where Xₙ indicates if a patient is hospitalized forms what type of stochastic process?",
        "choices": ["A. Independent trials", "B. Markov chain", "C. Renewal process", "D. Poisson process"],
        "answer": "B. Markov chain",
        "explanation": "Each year’s state depends only on the previous year, fulfilling the Markov property."
    },
    {
        "question": "For a two-state Markov chain, stationary probabilities are found by solving what equation?",
        "choices": ["A. π = πP", "B. P = ππ", "C. P = PP", "D. πP = Pπ"],
        "answer": "A. π = πP",
        "explanation": "Stationary probabilities satisfy π = πP, meaning they remain unchanged under one transition."
    },
    {
        "question": "What does it mean for a state to be recurrent in a Markov chain?",
        "choices": ["A. It is absorbing", "B. It can never be reached again", "C. It will be visited infinitely often", "D. It has no stationary probability"],
        "answer": "C. It will be visited infinitely often",
        "explanation": "A recurrent state is one that the process will eventually return to with probability 1."
    },
    {
        "question": "The time between goals in a Poisson process follows what distribution?",
        "choices": ["A. Normal", "B. Uniform", "C. Exponential", "D. Binomial"],
        "answer": "C. Exponential",
        "explanation": "Interarrival times in a Poisson process are exponentially distributed."
    },
    {
        "question": "The waiting time until the 3rd goal in a football match follows what distribution?",
        "choices": ["A. Exponential", "B. Gamma", "C. Uniform", "D. Binomial"],
        "answer": "B. Gamma",
        "explanation": "The sum of n exponential variables (time until nth event) follows a Gamma distribution."
    },
    {
        "question": "If the Poisson rate λ depends on time, the process is called a:",
        "choices": ["A. Non-homogeneous Poisson process", "B. Stationary process", "C. Renewal process", "D. Deterministic process"],
        "answer": "A. Non-homogeneous Poisson process",
        "explanation": "A Poisson process with time-varying rate λ(t) is non-homogeneous."
    },
    {
        "question": "In a birth-death process, what does 'birth rate' refer to?",
        "choices": ["A. Rate of leaving a state", "B. Rate of increasing by one state", "C. Total rate of arrivals", "D. Death rate inverse"],
        "answer": "B. Rate of increasing by one state",
        "explanation": "The birth rate λₖ defines the rate at which transitions occur from state k to k+1."
    },
    {
        "question": "A stationary distribution in a Markov chain represents:",
        "choices": ["A. Long-run average probabilities", "B. Transition rates", "C. Absorbing state probabilities", "D. Variance of state durations"],
        "answer": "A. Long-run average probabilities",
        "explanation": "The stationary distribution gives the long-run proportion of time the process spends in each state."
    },
    {
        "question": "A process is time reversible if:",
        "choices": ["A. The reverse-time process satisfies detailed balance", "B. All states are transient", "C. λ > μ", "D. It has no stationary distribution"],
        "answer": "A. The reverse-time process satisfies detailed balance",
        "explanation": "Time reversibility requires that πᵢpᵢⱼ = πⱼpⱼᵢ for all i, j."
    },
    {
        "question": "In a Markov chain describing a mechanical system, which state is absorbing?",
        "choices": ["A. System fully functional", "B. One component failed", "C. Both components failed", "D. Repair state"],
        "answer": "C. Both components failed",
        "explanation": "Once both components fail, the system remains down, making the state absorbing."
    },
    {
        "question": "When an absorbing Markov chain allows repair transitions (P₃₀ = 1), what happens?",
        "choices": ["A. It becomes transient", "B. It becomes recurrent", "C. It becomes irreducible and ergodic", "D. It stops evolving"],
        "answer": "C. It becomes irreducible and ergodic",
        "explanation": "Allowing repair creates transitions between all states, enabling a steady-state distribution."
    },
    {
        "question": "In queueing theory, 'time reversibility' implies:",
        "choices": ["A. Past and future are statistically identical", "B. The process stops changing", "C. The queue is infinite", "D. Arrivals exceed departures"],
        "answer": "A. Past and future are statistically identical",
        "explanation": "A time-reversible process has the same probabilistic behavior when viewed backward in time."
    },
    {
        "question": "If λ = μ in an M/M/2 queue, utilization per server equals:",
        "choices": ["A. 0", "B. 0.5", "C. 1", "D. 2"],
        "answer": "B. 0.5",
        "explanation": "When λ = μ, each server is busy half the time on average."
    },
    {
        "question": "In an M/M/2 system, what does the state X(t) represent?",
        "choices": ["A. Waiting time", "B. Number of customers in system", "C. Service rate", "D. Interarrival time"],
        "answer": "B. Number of customers in system",
        "explanation": "X(t) counts both customers being served and those waiting in line."
    },
    {
        "question": "In the 2024 exam’s 3-state Markov chain, which state is absorbing?",
        "choices": ["A. State 0", "B. State 1", "C. State 2", "D. None"],
        "answer": "C. State 2",
        "explanation": "The transition matrix has 1 on the diagonal of state 2, making it absorbing."
    },
    {
        "question": "If Y is the number of consecutive days the chain stays in state 0, what distribution does Y follow?",
        "choices": ["A. Binomial", "B. Geometric", "C. Poisson", "D. Normal"],
        "answer": "B. Geometric",
        "explanation": "The number of consecutive successes before failure in a Bernoulli process follows a geometric distribution."
    },
    {
        "question": "The expected value of a geometric random variable with success probability p is:",
        "choices": ["A. 1/p", "B. p", "C. 1−p", "D. p/(1−p)"],
        "answer": "A. 1/p",
        "explanation": "For geometric(p), the expected count of trials before success is 1/p."
    },
    {
        "question": "What does T = min{n ≥ 0 : Xₙ = 2} represent in a Markov chain?",
        "choices": ["A. Time to absorption", "B. Stationary time", "C. Probability of return", "D. Expected duration"],
        "answer": "A. Time to absorption",
        "explanation": "T is the hitting time, i.e., the first time the chain reaches state 2."
    },
    {
        "question": "Given N(t) arrivals by time t in a Poisson process, why are arrival times uniformly distributed?",
        "choices": ["A. Independence property", "B. Stationarity of increments", "C. Memoryless property", "D. Random ordering property"],
        "answer": "D. Random ordering property",
        "explanation": "Conditional on N(t)=n, arrival times are random and equally likely across (0, t)."
    },
    {
        "question": "In a Poisson process, E[W|N(t)] = N(t)t/2 follows from what rule?",
        "choices": ["A. Linearity of expectation", "B. Bayes' theorem", "C. Conditional independence", "D. Uniform scaling"],
        "answer": "A. Linearity of expectation",
        "explanation": "Expectation is additive and independent of distribution details once conditioned on N(t)."
    },
    {
        "question": "In the parking lot model, λ and μ represent what?",
        "choices": ["A. Arrival and service rates", "B. Weather rates", "C. Power and failure rates", "D. Probability weights"],
        "answer": "A. Arrival and service rates",
        "explanation": "λ is the parking (arrival) rate, and μ is the leaving (departure) rate."
    },
    {
        "question": "In the same model, the stationary distribution of the number of cars is:",
        "choices": ["A. Poisson", "B. Binomial", "C. Normal", "D. Uniform"],
        "answer": "B. Binomial",
        "explanation": "The long-run number of occupied spots follows Binomial(N, λ/(λ+μ))."
    },
    {
        "question": "The expected number of parked cars as t → ∞ equals:",
        "choices": ["A. Nλ/(λ+μ)", "B. λ+μ", "C. N/2", "D. 0"],
        "answer": "A. Nλ/(λ+μ)",
        "explanation": "In steady state, the mean equals the expected proportion occupied times N."
    },
    {
        "question": "In the equation M(t)=A+B·e^{−(λ+μ)t}, the exponential term represents:",
        "choices": ["A. Stationary mean", "B. Transient decay", "C. Probability of failure", "D. Binomial coefficient"],
        "answer": "B. Transient decay",
        "explanation": "The exponential term shows how fast the system approaches steady-state."
    },
    {
        "question": "In the urn model with 2 white and 2 black balls, what does the state number i represent?",
        "choices": ["A. Number of total balls", "B. Number of white balls in urn 1", "C. Number of draws made", "D. Number of black balls in urn 2"],
        "answer": "B. Number of white balls in urn 1",
        "explanation": "Each state i corresponds to how many white balls are currently in the first urn."
    },
    {
        "question": "When you swap one ball between urns at each step, what type of process describes the system?",
        "choices": ["A. Random walk", "B. Discrete-time Markov chain", "C. Poisson process", "D. Renewal process"],
        "answer": "B. Discrete-time Markov chain",
        "explanation": "The next state depends only on the current configuration, satisfying the Markov property."
    },
    {
        "question": "In a Markov chain, what is the Chapman-Kolmogorov equation used for?",
        "choices": ["A. Finding mean waiting times", "B. Computing multi-step transition probabilities", "C. Checking stationarity", "D. Calculating variance"],
        "answer": "B. Computing multi-step transition probabilities",
        "explanation": "It relates Pⁿ⁺ᵐ to the product of shorter transitions: Pⁿ⁺ᵐ = PⁿPᵐ."
    },
    {
        "question": "If a state in a Markov chain can reach itself in multiple ways, what does this affect?",
        "choices": ["A. Its variance", "B. Its period", "C. Its absorption", "D. Its reversibility"],
        "answer": "B. Its period",
        "explanation": "The number of steps it takes to return defines the period of that state."
    },
    {
        "question": "For a two-state Markov chain with states 0 and 1, when do stationary probabilities exist?",
        "choices": ["A. Always", "B. Only if transition matrix is symmetric", "C. Only if the chain is irreducible and aperiodic", "D. Only if P(0→1)=1"],
        "answer": "C. Only if the chain is irreducible and aperiodic",
        "explanation": "Both conditions ensure convergence to steady-state probabilities."
    },
    {
        "question": "In a Poisson process with λ=30/hour, what is the expected number of arrivals in 10 minutes?",
        "choices": ["A. 5", "B. 10", "C. 0.5", "D. 30"],
        "answer": "A. 5",
        "explanation": "Expected arrivals = λ × t = 30 × (10/60) = 5."
    },
    {
        "question": "The waiting time until the next event in a Poisson process is exponentially distributed. Which property follows?",
        "choices": ["A. Memoryless property", "B. Stationarity", "C. Uniform arrivals", "D. Markov dependence"],
        "answer": "A. Memoryless property",
        "explanation": "The exponential distribution has no memory: future waiting time is independent of the past."
    },
    {
        "question": "If a Poisson rate depends on time, what is the process called?",
        "choices": ["A. Homogeneous", "B. Non-homogeneous", "C. Stationary", "D. Renewal"],
        "answer": "B. Non-homogeneous",
        "explanation": "A non-homogeneous Poisson process has λ(t) varying with time."
    },
    {
        "question": "The function λ(t) = 2 + 2e^{-t} indicates what about arrivals?",
        "choices": ["A. Increasing intensity", "B. Decreasing intensity", "C. Constant intensity", "D. Random intensity"],
        "answer": "B. Decreasing intensity",
        "explanation": "As t increases, e^{-t} decreases, lowering λ(t)."
    },
    {
        "question": "In a non-homogeneous Poisson process, how is E[N(t)] found?",
        "choices": ["A. λ × t", "B. ∫₀ᵗ λ(u) du", "C. Var[N(t)]", "D. log(λt)"],
        "answer": "B. ∫₀ᵗ λ(u) du",
        "explanation": "The expected number of events equals the integrated intensity over time."
    },
    {
        "question": "What is the main difference between homogeneous and non-homogeneous Poisson processes?",
        "choices": ["A. Whether they are discrete or continuous", "B. Whether rate λ is constant", "C. Whether arrivals are independent", "D. Whether arrivals are Poisson"],
        "answer": "B. Whether rate λ is constant",
        "explanation": "Homogeneous: λ constant. Non-homogeneous: λ(t) varies over time."
    },
    {
        "question": "In a birth-death process, which equation defines the stationary probabilities?",
        "choices": ["A. π = πP", "B. πₖμₖ = πₖ₋₁λₖ₋₁", "C. λ = μ", "D. π₀ = 1"],
        "answer": "B. πₖμₖ = πₖ₋₁λₖ₋₁",
        "explanation": "The detailed balance equations relate consecutive stationary probabilities."
    },
    {
        "question": "For an M/M/1 queue, which parameter defines the utilization rate?",
        "choices": ["A. λ+μ", "B. λμ", "C. λ/μ", "D. μ/λ"],
        "answer": "C. λ/μ",
        "explanation": "The ratio λ/μ gives the proportion of time the server is busy."
    },
    {
        "question": "What is the stationary probability that the server is idle in an M/M/1 queue?",
        "choices": ["A. 1", "B. ρ", "C. 1−ρ", "D. λμ"],
        "answer": "C. 1−ρ",
        "explanation": "Idle time probability = 1−(λ/μ)."
    },
    {
        "question": "In a continuous-time Markov chain, the diagonal elements of the Q-matrix represent:",
        "choices": ["A. Transition rates", "B. Leaving rates (negative)", "C. Absorption rates", "D. Arrival intensities"],
        "answer": "B. Leaving rates (negative)",
        "explanation": "qᵢᵢ = −vᵢ, the total rate of leaving state i."
    },
    {
        "question": "Kolmogorov’s forward equations are used to describe:",
        "choices": ["A. Long-run equilibrium", "B. Short-term time evolution of probabilities", "C. Variance", "D. Expected waiting time"],
        "answer": "B. Short-term time evolution of probabilities",
        "explanation": "They are differential equations governing Pᵢⱼ(t) over time."
    },
    {
        "question": "In a Markov chain, two states belong to the same class if:",
        "choices": ["A. They have same transition probability", "B. Each is reachable from the other", "C. They are recurrent", "D. They are periodic"],
        "answer": "B. Each is reachable from the other",
        "explanation": "Mutual reachability defines communication classes."
    },
    {
        "question": "Which condition ensures a unique stationary distribution in a finite Markov chain?",
        "choices": ["A. Chain is reducible", "B. Chain is irreducible and aperiodic", "C. Chain has absorbing states", "D. Chain has infinite states"],
        "answer": "B. Chain is irreducible and aperiodic",
        "explanation": "Those conditions ensure convergence to a unique stationary distribution."
    },
    {
        "question": "In a Poisson process, what does 'stationary increments' mean?",
        "choices": ["A. The mean stays constant", "B. Probabilities depend only on time difference", "C. Events happen regularly", "D. No memory"],
        "answer": "B. Probabilities depend only on time difference",
        "explanation": "The number of arrivals in an interval depends only on its length, not on the start time."
    },
    {
        "question": "In a DNA mutation Markov model, what property makes it a Markov chain?",
        "choices": ["A. Mutations are independent of position", "B. Next state depends only on current state", "C. Nucleotides mutate periodically", "D. Transitions depend on entire history"],
        "answer": "B. Next state depends only on current state",
        "explanation": "The system satisfies the Markov property because each generation depends only on the current configuration."
    },
    {
        "question": "What does it mean for a Markov chain to be time reversible?",
        "choices": ["A. It always returns to start", "B. The forward and backward processes have the same probability structure", "C. It is periodic", "D. It is absorbing"],
        "answer": "B. The forward and backward processes have the same probability structure",
        "explanation": "In reversible chains, πᵢpᵢⱼ = πⱼpⱼᵢ for all i, j."
    },
    {
        "question": "In a Poisson process, given N(t)=n, the n arrival times are distributed as:",
        "choices": ["A. Exponential", "B. Uniform over (0, t)", "C. Normal", "D. Binomial"],
        "answer": "B. Uniform over (0, t)",
        "explanation": "Conditional on n arrivals, arrival times are uniformly distributed within the interval."
    },
    {
        "question": "In a birth-death process, λᵢ represents:",
        "choices": ["A. Rate of death", "B. Rate of birth (transition up by one state)", "C. Stationary probability", "D. Mean lifetime"],
        "answer": "B. Rate of birth (transition up by one state)",
        "explanation": "λᵢ gives the rate of moving from i to i+1."
    },
    {
        "question": "In a repair model where machine A has priority, what happens if A fails while B is being repaired?",
        "choices": ["A. B continues repair", "B. A is repaired first", "C. Both repaired simultaneously", "D. The system stops"],
        "answer": "B. A is repaired first",
        "explanation": "Priority means repair immediately switches to the more important machine."
    },
    {
        "question": "In an exponential model, the mean time to failure equals:",
        "choices": ["A. 1/λ", "B. λ", "C. log(λ)", "D. λ²"],
        "answer": "A. 1/λ",
        "explanation": "Expected value of exponential(λ) = 1/λ."
    },
    {
        "question": "If a Poisson process has λ = 7 per year, what is E[N(1)]?",
        "choices": ["A. 1", "B. 7", "C. 14", "D. 0.7"],
        "answer": "B. 7",
        "explanation": "Expected number of arrivals in one year equals λt = 7×1 = 7."
    },
    {
        "question": "In a mixed Poisson process with random rate Y, what is E[N(1)]?",
        "choices": ["A. E(Y)", "B. Var(Y)", "C. 1/E(Y)", "D. λ²"],
        "answer": "A. E(Y)",
        "explanation": "By the law of total expectation, E[N(1)] = E(E[N(1)|Y]) = E(Y)."
    },
    {
        "question": "The variance of a mixed Poisson process is larger than a simple Poisson because:",
        "choices": ["A. Randomness in Y adds extra variation", "B. Poisson processes have no variance", "C. Y is constant", "D. λ is fixed"],
        "answer": "A. Randomness in Y adds extra variation",
        "explanation": "Var(N) = E(Var(N|Y)) + Var(E(N|Y)) = E(Y) + Var(Y)."
    },
    {
        "question": "In a birth-death process with λ=μ, the stationary probabilities follow what shape?",
        "choices": ["A. Increasing", "B. Uniform", "C. Decreasing geometric", "D. Random"],
        "answer": "B. Uniform",
        "explanation": "When λ=μ, all states are equally likely in steady state (for finite chains)."
    },
    {
        "question": "In a Markov chain, what does 'time-homogeneous' mean?",
        "choices": ["A. Transition probabilities change with time", "B. Transition probabilities remain constant over time", "C. States depend on multiple previous steps", "D. It has continuous time steps"],
        "answer": "B. Transition probabilities remain constant over time",
        "explanation": "A time-homogeneous Markov chain has transition probabilities that do not depend on the step number n."
    },
    {
        "question": "In a discrete-time Markov chain, if all states communicate, what does that imply?",
        "choices": ["A. The chain is reducible", "B. The chain is irreducible", "C. The chain is transient", "D. The chain is periodic"],
        "answer": "B. The chain is irreducible",
        "explanation": "If every state can be reached from every other, the chain is irreducible."
    },
    {
        "question": "True or False: Every irreducible finite Markov chain has a stationary distribution.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "A finite irreducible Markov chain always has at least one stationary distribution."
    },
    {
        "question": "Which property defines a Poisson process?",
        "choices": ["A. Independent increments", "B. Constant rate", "C. Memoryless interarrival times", "D. All of the above"],
        "answer": "D. All of the above",
        "explanation": "A Poisson process has independent increments, exponentially distributed interarrival times, and constant rate λ."
    },
    {
        "question": "If arrivals follow a Poisson process with rate λ = 10 per hour, what is the expected interarrival time?",
        "choices": ["A. 0.1 hours", "B. 0.5 hours", "C. 0.05 hours", "D. 1/10 hours"],
        "answer": "D. 1/10 hours",
        "explanation": "Expected interarrival time = 1/λ = 0.1 hours."
    },
    {
        "question": "In an M/M/1 queue, what does the ratio ρ = λ / μ represent?",
        "choices": ["A. Average service time", "B. Utilization factor", "C. Mean number of customers", "D. Idle probability"],
        "answer": "B. Utilization factor",
        "explanation": "ρ is the proportion of time the server is busy (utilization)."
    },
    {
        "question": "In an M/M/1 queue, the system is stable if:",
        "choices": ["A. λ = μ", "B. λ > μ", "C. λ < μ", "D. λ ≥ μ"],
        "answer": "C. λ < μ",
        "explanation": "The queue only reaches steady state if arrival rate < service rate."
    },
    {
        "question": "In a birth-death process, what determines the steady-state distribution?",
        "choices": ["A. Initial condition", "B. Birth and death rates", "C. Time step", "D. Transition matrix size"],
        "answer": "B. Birth and death rates",
        "explanation": "The long-run probabilities depend on the balance between birth (λ_i) and death (μ_i) rates."
    },
    {
        "question": "True or False: For a Poisson process, the number of arrivals in disjoint intervals are dependent.",
        "choices": ["True", "False"],
        "answer": "False",
        "explanation": "Poisson process increments are independent in disjoint time intervals."
    },
    {
        "question": "What is the variance of N(t) in a Poisson process with rate λ?",
        "choices": ["A. λt²", "B. λ²t", "C. λt", "D. t/λ"],
        "answer": "C. λt",
        "explanation": "For a Poisson process, Var(N(t)) = λt, equal to the mean."
    },
    {
        "question": "In a time-reversible Markov chain, what must hold for all i and j?",
        "choices": ["A. Pij = Pji", "B. πi Pij = πj Pji", "C. πi = πj", "D. Pij + Pji = 1"],
        "answer": "B. πi Pij = πj Pji",
        "explanation": "The detailed balance equations define time reversibility."
    },
    {
        "question": "Which of the following processes can model customer arrivals with time-varying rates?",
        "choices": ["A. Homogeneous Poisson process", "B. Non-homogeneous Poisson process", "C. Markov chain", "D. Bernoulli process"],
        "answer": "B. Non-homogeneous Poisson process",
        "explanation": "A non-homogeneous Poisson process allows λ(t) to vary with time."
    },
    {
        "question": "If λ(t) = 5 + 2t, what is the mean number of arrivals by time t?",
        "choices": ["A. 7t", "B. 5t + t²", "C. 5 + 2t", "D. 2t²"],
        "answer": "B. 5t + t²",
        "explanation": "E[N(t)] = ∫₀ᵗ λ(s) ds = 5t + t²."
    },
    {
        "question": "Which equation connects n-step transition probabilities in Markov chains?",
        "choices": ["A. Bayes' theorem", "B. Chapman-Kolmogorov equations", "C. Little's law", "D. Kolmogorov forward equations"],
        "answer": "B. Chapman-Kolmogorov equations",
        "explanation": "Pⁿ⁺ᵐ = Pⁿ × Pᵐ defines the Chapman-Kolmogorov relationship."
    },
    {
        "question": "True or False: The expected value of a Poisson-distributed variable equals its variance.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "For X ~ Poisson(λ), both mean and variance are λ."
    },
    {
        "question": "In an absorbing Markov chain, the expected number of steps before absorption is given by:",
        "choices": ["A. Q⁻¹1", "B. (I−Q)⁻¹1", "C. (Q−I)⁻¹", "D. P−Q"],
        "answer": "B. (I−Q)⁻¹1",
        "explanation": "The fundamental matrix (I−Q)⁻¹ gives expected time to absorption."
    },
    {
        "question": "In a two-state continuous-time Markov chain with rates q₀₁ = 2 and q₁₀ = 3, what is the stationary probability of state 0?",
        "choices": ["A. 2/5", "B. 3/5", "C. 1/2", "D. 4/5"],
        "answer": "B. 3/5",
        "explanation": "π₀q₀₁ = π₁q₁₀ → π₀/π₁ = 3/2 → π₀ = 3/5."
    },
    {
        "question": "What does the parameter λ represent in a Poisson process?",
        "choices": ["A. Mean waiting time", "B. Arrival rate per unit time", "C. Probability of one event", "D. System capacity"],
        "answer": "B. Arrival rate per unit time",
        "explanation": "λ is the expected number of events per unit time."
    },
    {
        "question": "For a Poisson process with rate λ, what is the probability of zero arrivals by time t?",
        "choices": ["A. e^(−λt)", "B. 1−e^(−λt)", "C. λt", "D. (λt)e^(−λt)"],
        "answer": "A. e^(−λt)",
        "explanation": "P(N(t)=0) = e^(−λt) because N(t) ~ Poisson(λt)."
    },
    {
        "question": "If X(t) is a continuous-time Markov chain, what does qᵢⱼ represent?",
        "choices": ["A. Transition probability", "B. Rate of transition from i to j", "C. Expected time in state j", "D. Stationary probability"],
        "answer": "B. Rate of transition from i to j",
        "explanation": "qᵢⱼ are instantaneous transition rates between states."
    },
    {
        "question": "In a queueing system, what does Little’s Law state?",
        "choices": ["A. L = λW", "B. L = W/λ", "C. W = Lλ", "D. L = μW"],
        "answer": "A. L = λW",
        "explanation": "Average number in system = arrival rate × average waiting time."
    },
    {
        "question": "True or False: A non-homogeneous Poisson process has constant interarrival times.",
        "choices": ["True", "False"],
        "answer": "False",
        "explanation": "In non-homogeneous processes, interarrival times vary because λ(t) changes."
    },
    {
        "question": "If interarrival times are exponential, what property holds for the process?",
        "choices": ["A. Independence", "B. Stationarity", "C. Memorylessness", "D. Homogeneity"],
        "answer": "C. Memorylessness",
        "explanation": "The exponential distribution is memoryless, a key property of Poisson processes."
    },
    {
        "question": "Which statement about stationary distributions is true?",
        "choices": ["A. It changes over time", "B. It depends on initial state", "C. It satisfies πP = π", "D. It equals the transition matrix"],
        "answer": "C. It satisfies πP = π",
        "explanation": "The stationary distribution remains constant under the Markov transition."
    },
    {
        "question": "In a Markov chain, if a state has period 1, it is:",
        "choices": ["A. Periodic", "B. Aperiodic", "C. Absorbing", "D. Transient"],
        "answer": "B. Aperiodic",
        "explanation": "Aperiodic means the chain can return to the state at irregular intervals."
    },
    {
        "question": "Which function gives the expected number of events in a non-homogeneous Poisson process?",
        "choices": ["A. m(t) = λt", "B. m(t) = ∫₀ᵗ λ(s)ds", "C. m(t) = e^(−λt)", "D. m(t) = λt²"],
        "answer": "B. m(t) = ∫₀ᵗ λ(s)ds",
        "explanation": "The mean value function m(t) integrates the rate over time."
    },
    {
        "question": "True or False: A stationary process has statistical properties that change with time.",
        "choices": ["True", "False"],
        "answer": "False",
        "explanation": "Stationary processes have constant mean and variance over time."
    },
    {
        "question": "What is the primary difference between discrete-time and continuous-time Markov chains?",
        "choices": ["A. Number of states", "B. Timing of transitions", "C. Transition direction", "D. Memory property"],
        "answer": "B. Timing of transitions",
        "explanation": "Discrete-time chains move at fixed steps, continuous-time move randomly in continuous time."
    },
    {
        "question": "In an M/M/2 queue, the probability both servers are busy depends on:",
        "choices": ["A. ρ²", "B. 2ρ", "C. λ/μ²", "D. λ²/(2μ²)"],
        "answer": "D. λ²/(2μ²)",
        "explanation": "For M/M/2, steady-state probability of both busy: (λ²/(2μ²)) * P₀."
    },
    {
        "question": "True or False: A Poisson process can model both arrivals and service completions.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Poisson models can be used for any random arrival or completion process with independent events."
    },
    
]



# -----------------------------
# SESSION STATE INIT
# -----------------------------
if "q_index" not in st.session_state:
    st.session_state.q_index = 0

if "shuffled_questions" not in st.session_state:
    st.session_state.shuffled_questions = random.sample(stochastic_quiz, len(stochastic_quiz))  # Shuffle questions

if "user_answers" not in st.session_state:
    st.session_state.user_answers = [None] * len(st.session_state.shuffled_questions)

if "score" not in st.session_state:
    st.session_state.score = 0

if "feedback" not in st.session_state:
    st.session_state.feedback = ""

# -----------------------------
# SHUFFLE CHOICES PER QUESTION
# -----------------------------
if "shuffled_choices" not in st.session_state:
    st.session_state.shuffled_choices = [
        random.sample(q["choices"], len(q["choices"])) for q in st.session_state.shuffled_questions
    ]

# -----------------------------
# DISPLAY CURRENT QUESTION
# -----------------------------
q = st.session_state.shuffled_questions[st.session_state.q_index]
choices = st.session_state.shuffled_choices[st.session_state.q_index]

st.markdown(f"<h3 style='text-align:center'>{q['question']}</h3>", unsafe_allow_html=True)

# -----------------------------
# CSS FOR LARGE BUTTONS AND NAVIGATION
# -----------------------------
st.markdown("""
<style>
.choice-button {
    width: 90%;
    max-width: 500px;
    min-height: 60px;
    font-size: 18px;
    padding: 15px;
    margin: 10px auto;
    display: block;
    text-align: left;
    border-radius: 10px;
    background-color: #f0f0f0;
    border: 2px solid #ccc;
}
.choice-button:hover {
    background-color: #e0e0e0;
}
.nav-container {
    width: 90%;
    max-width: 500px;
    margin: 20px auto 10px auto;
    display: flex;
    justify-content: space-between;
}
.nav-button {
    width: 120px;
    height: 45px;
    font-size: 16px;
}
.feedback {
    text-align:center;
    font-size:16px;
    margin-top:10px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# DISPLAY CHOICES AS LARGE RECTANGULAR BUTTONS
# -----------------------------
for choice in choices:
    if st.button(choice, key=f"{st.session_state.q_index}_{choice}", help="Click to answer"):
        st.session_state.user_answers[st.session_state.q_index] = choice
        if choice == q["answer"]:
            st.session_state.feedback = f"✅ Correct! {q['explanation']}"
            st.session_state.score += 1
        else:
            st.session_state.feedback = f"❌ Incorrect. Correct: {q['answer']}.\n{q['explanation']}"

if st.session_state.feedback:
    st.markdown(f"<div class='feedback'>{st.session_state.feedback}</div>", unsafe_allow_html=True)

# -----------------------------
# NAVIGATION BUTTONS
# -----------------------------
prev_disabled = st.session_state.q_index == 0
next_disabled = st.session_state.q_index == len(st.session_state.shuffled_questions) - 1

st.markdown("<div class='nav-container'>", unsafe_allow_html=True)
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("⬅️ Previous", key="prev", disabled=prev_disabled):
        if st.session_state.q_index > 0:
            st.session_state.q_index -= 1
            st.session_state.feedback = ""
with col2:
    if st.button("Next ➡️", key="next", disabled=next_disabled):
        if st.session_state.q_index < len(st.session_state.shuffled_questions) - 1:
            st.session_state.q_index += 1
            st.session_state.feedback = ""
st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# PROGRESS AND SCORE
# -----------------------------
st.progress((st.session_state.q_index + 1) / len(st.session_state.shuffled_questions))
st.caption(f"Question {st.session_state.q_index + 1} of {len(st.session_state.shuffled_questions)}")
st.metric("Score", f"{st.session_state.score} / {len(st.session_state.shuffled_questions)}")