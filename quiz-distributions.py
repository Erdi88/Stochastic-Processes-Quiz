import streamlit as st
import random

st.set_page_config(page_title="Space Quiz 2025", layout="centered")

# -----------------------------
# QUESTIONS (same as before)
# -----------------------------


stochastic_quiz = [
    {
        "question": "When you see a problem mentioning 'events occurring randomly over time' with constant average rate, what model should come to mind first?",
        "choices": ["A. Markov chain", "B. Poisson process", "C. Bernoulli trial", "D. Renewal process"],
        "answer": "B. Poisson process",
        "explanation": "Poisson processes describe random independent events over time with constant rate λ."
    },
    {
        "question": "If a question gives 'exponential waiting times', which process is most likely involved?",
        "choices": ["A. Discrete-time Markov chain", "B. Poisson process", "C. Birth-death process", "D. Brownian motion"],
        "answer": "B. Poisson process",
        "explanation": "Exponential interarrival times imply a Poisson process."
    },
    {
        "question": "You are asked to compute the probability that the next arrival occurs after time t. What function should be used?",
        "choices": ["A. Poisson PMF", "B. Exponential survival function", "C. Geometric PMF", "D. Normal CDF"],
        "answer": "B. Exponential survival function",
        "explanation": "The probability no event occurs by time t is P(T>t)=e^(−λt)."
    },
    {
        "question": "In a continuous-time Markov chain, if a question gives transition rates qᵢⱼ, which system of equations usually defines π?",
        "choices": ["A. πQ=0", "B. PQ=0", "C. πP=π", "D. π=Q⁻¹"],
        "answer": "A. πQ=0",
        "explanation": "Stationary distribution in continuous time satisfies πQ=0 with Σπᵢ=1."
    },
    {
        "question": "If a problem mentions 'expected time until absorption', what matrix do you think of?",
        "choices": ["A. Transition matrix P", "B. Fundamental matrix (I−Q)⁻¹", "C. Generator matrix Q", "D. Covariance matrix"],
        "answer": "B. Fundamental matrix (I−Q)⁻¹",
        "explanation": "The fundamental matrix gives mean steps to absorption for absorbing chains."
    },
    {
        "question": "If an exam question mentions 'long-run proportion of time spent in each state', what are you finding?",
        "choices": ["A. Transient probabilities", "B. Stationary distribution", "C. Hitting probabilities", "D. First passage times"],
        "answer": "B. Stationary distribution",
        "explanation": "Long-run proportions correspond to the stationary distribution π."
    },
    {
        "question": "You are given λ(t)=5t and asked for E[N(2)]. What should you do?",
        "choices": ["A. Use λt", "B. Integrate λ(t) over time", "C. Use exponential CDF", "D. Apply Bayes’ theorem"],
        "answer": "B. Integrate λ(t) over time",
        "explanation": "E[N(t)] = ∫₀ᵗ λ(s)ds = ∫₀²5sds = 10."
    },
    {
        "question": "A question gives a queue with arrival rate λ and service rate μ. If λ≥μ, what should you immediately conclude?",
        "choices": ["A. The system is stable", "B. The queue will grow without bound", "C. Expected number in system is zero", "D. It’s a birth-death process"],
        "answer": "B. The queue will grow without bound",
        "explanation": "For M/M/1 systems, stability requires λ<μ."
    },
    {
        "question": "When asked for 'expected number in the system' in a stable M/M/1 queue, which formula should you recall?",
        "choices": ["A. L=ρ/(1−ρ)", "B. W=1/(μ−λ)", "C. Lq=ρ²/(1−ρ)", "D. P₀=1−ρ"],
        "answer": "A. L=ρ/(1−ρ)",
        "explanation": "Little’s law gives L=λW and for M/M/1, W=1/(μ−λ), so L=ρ/(1−ρ)."
    },
    {
        "question": "In a Markov chain problem, if 'periodic state' is mentioned, what should you check?",
        "choices": ["A. gcd of return step lengths", "B. Expected return time", "C. Stationary probabilities", "D. Eigenvalues of P"],
        "answer": "A. gcd of return step lengths",
        "explanation": "A state’s period is gcd of n such that Pⁿᵢᵢ>0."
    },
    {
        "question": "If you see 'limiting distribution' in an exam, which property ensures it exists?",
        "choices": ["A. Reducibility", "B. Irreducibility and aperiodicity", "C. Absorption", "D. Determinism"],
        "answer": "B. Irreducibility and aperiodicity",
        "explanation": "A limiting distribution exists only if the chain is irreducible and aperiodic."
    },
    {
        "question": "If a question says 'find the expected time until the system empties', it’s usually referring to:",
        "choices": ["A. First passage time", "B. Steady-state probability", "C. Periodic return time", "D. Mean recurrence time"],
        "answer": "A. First passage time",
        "explanation": "It asks for expected hitting time from current state to empty (state 0)."
    },
    {
        "question": "You are asked about a 'two-state on/off process' with exponential durations. What type of model is this?",
        "choices": ["A. Bernoulli process", "B. Continuous-time Markov chain", "C. Renewal process", "D. Discrete-time Markov chain"],
        "answer": "B. Continuous-time Markov chain",
        "explanation": "On/off exponential durations describe a two-state CTMC with rates q₀₁, q₁₀."
    },
    {
        "question": "If a question mentions 'birth rate proportional to state number', what model is that?",
        "choices": ["A. Poisson process", "B. Yule process", "C. M/M/1 queue", "D. Birth-death with constant rates"],
        "answer": "B. Yule process",
        "explanation": "In Yule process, λₙ = nλ, so growth rate is proportional to population size."
    },
    {
        "question": "In a Poisson process, if you are asked for conditional probability given N(t)=n, which distribution applies to event times?",
        "choices": ["A. Uniform(0,t)", "B. Exponential(λ)", "C. Binomial(n,p)", "D. Normal(μ,σ²)"],
        "answer": "A. Uniform(0,t)",
        "explanation": "Given N(t)=n, event times are uniformly distributed in (0,t)."
    },
    {
        "question": "True or False: The exponential distribution is the only continuous distribution with the memoryless property.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "No other continuous distribution satisfies P(T>t+s|T>t)=P(T>s)."
    },
    {
        "question": "If an exam asks 'find E[N(t)] and Var[N(t)] for a Poisson process', what should you remember?",
        "choices": ["A. Both equal λt", "B. Both equal λ", "C. Mean λt, variance λ²t", "D. Mean t/λ, variance λt²"],
        "answer": "A. Both equal λt",
        "explanation": "Poisson process has equal mean and variance λt."
    },
    {
        "question": "When solving Kolmogorov forward equations, what are you usually finding?",
        "choices": ["A. Stationary probabilities", "B. Time-dependent probabilities Pᵢⱼ(t)", "C. Transition matrix eigenvalues", "D. Return times"],
        "answer": "B. Time-dependent probabilities Pᵢⱼ(t)",
        "explanation": "The forward equations describe evolution of state probabilities over time."
    },
    {
        "question": "If you are told a process is reversible and stationary, what simplification can you use in steady-state calculations?",
        "choices": ["A. πP=π", "B. πᵢPᵢⱼ=πⱼPⱼᵢ", "C. P=Q", "D. P²=I"],
        "answer": "B. πᵢPᵢⱼ=πⱼPⱼᵢ",
        "explanation": "Detailed balance allows solving π using pairwise equalities."
    },
    {
        "question": "When asked to simulate a Poisson process, which random variable generator should be used?",
        "choices": ["A. Uniform", "B. Exponential", "C. Normal", "D. Geometric"],
        "answer": "B. Exponential",
        "explanation": "Interarrival times in a Poisson process are exponential."
    },
    {
        "question": "If a question mentions 'absorbing probability starting from state i', what approach do you recall?",
        "choices": ["A. Solve linear equations using Q and R", "B. Compute πQ=0", "C. Use Chapman-Kolmogorov", "D. Integrate λ(t)"],
        "answer": "A. Solve linear equations using Q and R",
        "explanation": "Absorbing probabilities are found from fundamental matrix (I−Q)⁻¹R."
    },
    {
        "question": "You are told to find the expected number of customers in system using Little’s Law. What inputs do you need?",
        "choices": ["A. λ and μ", "B. λ and average waiting time W", "C. W and service rate μ", "D. Arrival count only"],
        "answer": "B. λ and average waiting time W",
        "explanation": "Little’s Law: L=λW, linking mean number, rate, and waiting time."
    },
    {
        "question": "If an exam question mentions 'Kolmogorov backward equations', what are they used for?",
        "choices": ["A. Time evolution of transition probabilities", "B. Expected first passage times", "C. Stationary distribution", "D. Queue stability"],
        "answer": "B. Expected first passage times",
        "explanation": "Backward equations help compute hitting or absorption expectations."
    },
    {
        "question": "If 'number of arrivals until time t' is Poisson(λt), what is 'time until nth arrival'?",
        "choices": ["A. Exponential(λ)", "B. Gamma(n,λ)", "C. Normal(λt)", "D. Geometric(p)"],
        "answer": "B. Gamma(n,λ)",
        "explanation": "Waiting time for nth arrival is Gamma distributed."
    },
    {
        "question": "In a question where arrivals are Poisson and services exponential, which model should you recognize?",
        "choices": ["A. Birth-death process", "B. M/M/1 queue", "C. Renewal process", "D. Bernoulli trial model"],
        "answer": "B. M/M/1 queue",
        "explanation": "M/M/1 queues combine Poisson arrivals with exponential service times."
    },
    {
        "question": "True or False: The expected return time to a recurrent state equals 1/πᵢ.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Mean recurrence time of state i is inverse of its stationary probability."
    },
    {
        "question": "If λ(t)=3e^(−t), how do you find expected total arrivals until time 2?",
        "choices": ["A. Use λ×t", "B. Integrate 3e^(−t) from 0 to 2", "C. Multiply by mean interarrival time", "D. Use λ²t"],
        "answer": "B. Integrate 3e^(−t) from 0 to 2",
        "explanation": "E[N(t)] = ∫₀ᵗ λ(s)ds = 3(1−e^(−2))."
    },
    {
        "question": "When asked about 'expected time in each state before absorption', what are you computing?",
        "choices": ["A. Stationary probabilities", "B. Fundamental matrix entries", "C. Transition rates", "D. Recurrence intervals"],
        "answer": "B. Fundamental matrix entries",
        "explanation": "Each entry (i,j) of (I−Q)⁻¹ gives expected visits to j starting from i."
    },
    # --- POISSON DISTRIBUTION ---
    {
        "question": "Which type of events does the Poisson distribution model?",
        "choices": ["A. Number of random independent events over time", "B. Time between two events", "C. Successes in fixed number of trials", "D. Continuous outcomes"],
        "answer": "A. Number of random independent events over time",
        "explanation": "The Poisson distribution models the count of events in a fixed interval with constant average rate λ."
    },
    {
        "question": "What is the mean and variance of a Poisson(λ) random variable?",
        "choices": ["A. Mean=λ, Var=λ", "B. Mean=λ, Var=√λ", "C. Mean=λt, Var=λ²t", "D. Mean=1/λ, Var=1/λ²"],
        "answer": "A. Mean=λ, Var=λ",
        "explanation": "Both the mean and variance of Poisson(λ) are equal to λ."
    },
    {
        "question": "If a question says 'events occur at rate 3 per hour', what is P(X=0) in 1 hour?",
        "choices": ["A. e^(-3)", "B. 1−e^(-3)", "C. 3e^(-3)", "D. Cannot be determined"],
        "answer": "A. e^(-3)",
        "explanation": "For Poisson(λ), P(X=0)=e^(−λ)."
    },
    {
        "question": "Which condition is required for Poisson model validity?",
        "choices": ["A. Events depend on each other", "B. Constant rate and independent events", "C. Time-varying rate", "D. Equal number of arrivals always"],
        "answer": "B. Constant rate and independent events",
        "explanation": "Poisson requires independent events occurring with constant average rate."
    },

    # --- EXPONENTIAL DISTRIBUTION ---
    {
        "question": "The exponential distribution models:",
        "choices": ["A. Number of arrivals", "B. Waiting time between events", "C. Probability of success", "D. Number of trials"],
        "answer": "B. Waiting time between events",
        "explanation": "The exponential distribution models the continuous time between Poisson events."
    },
    {
        "question": "What is the memoryless property?",
        "choices": ["A. P(T>t+s|T>t)=P(T>s)", "B. E[T]=Var[T]", "C. P(X<n)=1−P(X>n)", "D. Independence of variables"],
        "answer": "A. P(T>t+s|T>t)=P(T>s)",
        "explanation": "The exponential distribution uniquely satisfies the memoryless property."
    },
    {
        "question": "What is the mean of Exponential(λ)?",
        "choices": ["A. 1/λ", "B. λ", "C. λ²", "D. 1/λ²"],
        "answer": "A. 1/λ",
        "explanation": "The exponential mean E[T]=1/λ and variance Var[T]=1/λ²."
    },
    {
        "question": "Which of the following statements about exponential distribution is TRUE?",
        "choices": ["A. It can model discrete time gaps", "B. It models continuous waiting times", "C. It has fixed interval probabilities", "D. It’s symmetric"],
        "answer": "B. It models continuous waiting times",
        "explanation": "The exponential distribution describes continuous positive times between events."
    },

    # --- GEOMETRIC DISTRIBUTION ---
    {
        "question": "What does the geometric distribution model?",
        "choices": ["A. Number of events per hour", "B. Time between events", "C. Number of trials until first success", "D. Continuous waiting time"],
        "answer": "C. Number of trials until first success",
        "explanation": "The geometric distribution counts discrete trials until a success occurs."
    },
    {
        "question": "What is the mean of a Geometric(p) distribution?",
        "choices": ["A. 1/p", "B. p", "C. (1−p)/p", "D. 1/(1−p)"],
        "answer": "A. 1/p",
        "explanation": "The expected number of trials until success is E[X]=1/p."
    },
    {
        "question": "The geometric distribution is the discrete analogue of which continuous distribution?",
        "choices": ["A. Poisson", "B. Exponential", "C. Normal", "D. Uniform"],
        "answer": "B. Exponential",
        "explanation": "Both geometric and exponential distributions share the memoryless property."
    },
    {
        "question": "If a question says 'each trial independent, same probability of success p', which distribution applies?",
        "choices": ["A. Binomial", "B. Geometric", "C. Poisson", "D. Normal"],
        "answer": "B. Geometric",
        "explanation": "The geometric distribution describes repeated Bernoulli trials until the first success."
    },

    # --- BINOMIAL DISTRIBUTION ---
    {
        "question": "What does the binomial distribution model?",
        "choices": ["A. Number of arrivals per interval", "B. Number of successes in fixed n independent trials", "C. Waiting time between events", "D. Continuous growth"],
        "answer": "B. Number of successes in fixed n independent trials",
        "explanation": "Binomial(n,p) counts how many successes occur in n Bernoulli trials."
    },
    {
        "question": "What are the mean and variance of Binomial(n,p)?",
        "choices": ["A. Mean=np, Var=np(1−p)", "B. Mean=n/p, Var=np²", "C. Mean=1/p, Var=1/p²", "D. Mean=λ, Var=λ"],
        "answer": "A. Mean=np, Var=np(1−p)",
        "explanation": "Binomial expectation and variance follow directly from summing Bernoulli trials."
    },
    {
        "question": "Which of the following conditions justifies using binomial distribution?",
        "choices": ["A. Independent trials with constant success probability", "B. Dependent events", "C. Poisson arrivals", "D. Continuous outcomes"],
        "answer": "A. Independent trials with constant success probability",
        "explanation": "Binomial assumptions include independence and constant probability p."
    },
    {
        "question": "If n is large and p is small, which distribution can approximate Binomial(n,p)?",
        "choices": ["A. Poisson(λ=np)", "B. Exponential(λ=p)", "C. Normal(μ=np,σ²=np(1−p))", "D. Uniform"],
        "answer": "A. Poisson(λ=np)",
        "explanation": "The Poisson is a good approximation for large n, small p, with λ=np."
    },

    # --- NORMAL DISTRIBUTION ---
    {
        "question": "What type of variable is modeled by a normal distribution?",
        "choices": ["A. Discrete", "B. Continuous", "C. Binary", "D. Poisson count"],
        "answer": "B. Continuous",
        "explanation": "The normal distribution models continuous real-valued random variables."
    },
    {
        "question": "What are the parameters of a Normal distribution?",
        "choices": ["A. λ only", "B. n and p", "C. μ and σ²", "D. p only"],
        "answer": "C. μ and σ²",
        "explanation": "A Normal(μ,σ²) variable has mean μ and variance σ²."
    },
    {
        "question": "If X~N(μ,σ²), how can you standardize it?",
        "choices": ["A. Z=(X−μ)/σ", "B. Z=(X+μ)/σ²", "C. Z=Xσ/μ", "D. Z=μ/X"],
        "answer": "A. Z=(X−μ)/σ",
        "explanation": "The standard normal variable has mean 0 and variance 1."
    },
    {
        "question": "The normal distribution is often used as an approximation for which discrete distribution when n is large?",
        "choices": ["A. Binomial", "B. Geometric", "C. Poisson", "D. Exponential"],
        "answer": "A. Binomial",
        "explanation": "The normal approximates Binomial(n,p) when n is large (by CLT)."
    },

    # --- UNIFORM DISTRIBUTION ---
    {
        "question": "The continuous uniform distribution assumes:",
        "choices": ["A. Some outcomes more likely", "B. All outcomes equally likely", "C. Exponential timing", "D. Binary outcomes"],
        "answer": "B. All outcomes equally likely",
        "explanation": "Uniform(a,b) assigns equal probability density between a and b."
    },
    {
        "question": "What is the mean of Uniform(a,b)?",
        "choices": ["A. (a+b)/2", "B. a*b", "C. (b−a)", "D. 1/(b−a)"],
        "answer": "A. (a+b)/2",
        "explanation": "The mean is the midpoint, variance is (b−a)²/12."
    },

    # --- GAMMA DISTRIBUTION ---
    {
        "question": "What does the gamma distribution generalize?",
        "choices": ["A. Normal distribution", "B. Waiting time for n events", "C. Discrete success counts", "D. Binomial process"],
        "answer": "B. Waiting time for n events",
        "explanation": "Gamma(n,λ) gives the time until the nth Poisson event occurs."
    },
    {
        "question": "What is the mean of a Gamma(α,λ) distribution?",
        "choices": ["A. α/λ", "B. λ/α", "C. 1/(αλ)", "D. αλ"],
        "answer": "A. α/λ",
        "explanation": "The mean E[X]=α/λ and Var[X]=α/λ²."
    },
    {
        "question": "Which distribution is a special case of Gamma with α=1?",
        "choices": ["A. Normal", "B. Exponential", "C. Uniform", "D. Binomial"],
        "answer": "B. Exponential",
        "explanation": "Gamma(1,λ) = Exponential(λ)."
    },

    # --- BERNOULLI DISTRIBUTION ---
    {
        "question": "The Bernoulli distribution models:",
        "choices": ["A. Continuous random variable", "B. One binary trial (success/failure)", "C. Number of events", "D. Waiting times"],
        "answer": "B. One binary trial (success/failure)",
        "explanation": "Bernoulli(p) describes a single trial with success probability p."
    },
    {
        "question": "What are the mean and variance of a Bernoulli(p) random variable?",
        "choices": ["A. Mean=p, Var=p(1−p)", "B. Mean=1/p, Var=p²", "C. Mean=np, Var=np(1−p)", "D. Mean=λ, Var=λ"],
        "answer": "A. Mean=p, Var=p(1−p)",
        "explanation": "Bernoulli is the basis for Binomial distribution."
    },

    # --- SUMMARY IDENTIFICATION ---
    {
        "question": "Which distribution should you use for 'number of arrivals in 10 minutes'?",
        "choices": ["A. Poisson", "B. Exponential", "C. Geometric", "D. Normal"],
        "answer": "A. Poisson",
        "explanation": "Poisson models counts of arrivals in a fixed time window."
    },
    {
        "question": "Which distribution describes 'time between successive arrivals'?",
        "choices": ["A. Exponential", "B. Poisson", "C. Binomial", "D. Uniform"],
        "answer": "A. Exponential",
        "explanation": "Exponential describes continuous waiting times between Poisson arrivals."
    },
    {
        "question": "Which distribution is appropriate for 'number of trials before success'?",
        "choices": ["A. Geometric", "B. Binomial", "C. Exponential", "D. Poisson"],
        "answer": "A. Geometric",
        "explanation": "Geometric models the count of trials until first success."
    },
    {
        "question": "Which distribution fits 'number of successes out of 20 independent trials with p=0.2'?",
        "choices": ["A. Binomial", "B. Poisson", "C. Normal", "D. Exponential"],
        "answer": "A. Binomial",
        "explanation": "Binomial applies to fixed number of Bernoulli trials."
    },
    {
        "question": "If waiting times between events are exponential, what distribution describes total waiting time for 3 events?",
        "choices": ["A. Gamma(3,λ)", "B. Poisson(λ)", "C. Normal(μ,σ²)", "D. Binomial"],
        "answer": "A. Gamma(3,λ)",
        "explanation": "Sum of 3 independent exponential(λ) variables is Gamma(3,λ)."
    },
    # --- SCENARIO RECOGNITION & MIXED APPLICATIONS ---

    {
        "question": "A help desk receives calls at a constant average rate. What distribution models the number of calls in one hour?",
        "choices": ["A. Poisson", "B. Exponential", "C. Normal", "D. Uniform"],
        "answer": "A. Poisson",
        "explanation": "Independent arrivals over fixed time follow a Poisson distribution."
    },
    {
        "question": "The time between two consecutive calls at the same help desk follows which distribution?",
        "choices": ["A. Exponential", "B. Poisson", "C. Binomial", "D. Geometric"],
        "answer": "A. Exponential",
        "explanation": "Waiting times between Poisson events are exponentially distributed."
    },
    {
        "question": "A factory machine fails on average every 4 days. Which parameter λ should be used for Exponential(λ)?",
        "choices": ["A. λ = 1/4 per day", "B. λ = 4 per day", "C. λ = 0.25 per hour", "D. λ = 0.5 per day"],
        "answer": "A. λ = 1/4 per day",
        "explanation": "λ represents the average rate of failures, which is the reciprocal of mean time between failures."
    },
    {
        "question": "A student guesses answers on a 10-question multiple-choice test with p=0.25 of success each time. Which distribution applies to the number of correct answers?",
        "choices": ["A. Binomial(10,0.25)", "B. Poisson(2.5)", "C. Geometric(0.25)", "D. Normal(0,1)"],
        "answer": "A. Binomial(10,0.25)",
        "explanation": "There are fixed independent Bernoulli trials with success probability p."
    },
    {
        "question": "A computer network logs the number of dropped packets per minute. What model best fits this count?",
        "choices": ["A. Poisson", "B. Normal", "C. Exponential", "D. Uniform"],
        "answer": "A. Poisson",
        "explanation": "Poisson models discrete counts of independent random events in time."
    },
    {
        "question": "A device waits for the first successful transmission, with each attempt independent. Which distribution describes the number of attempts needed?",
        "choices": ["A. Geometric", "B. Binomial", "C. Poisson", "D. Exponential"],
        "answer": "A. Geometric",
        "explanation": "Geometric counts discrete trials until first success."
    },
    {
        "question": "The lifetime of an electronic component is exponentially distributed with mean 500 hours. What is its rate λ?",
        "choices": ["A. 1/500 per hour", "B. 500 per hour", "C. 5 per hour", "D. 0.5 per hour"],
        "answer": "A. 1/500 per hour",
        "explanation": "Mean = 1/λ, so λ = 1/mean."
    },
    {
        "question": "If a process models time until the 4th customer arrival with rate λ, which distribution applies?",
        "choices": ["A. Gamma(4,λ)", "B. Poisson(λ)", "C. Exponential(λ)", "D. Geometric(p)"],
        "answer": "A. Gamma(4,λ)",
        "explanation": "Gamma generalizes exponential to waiting time for n events."
    },
    {
        "question": "Which distribution often approximates a sum of many independent random variables, regardless of the original distribution?",
        "choices": ["A. Normal", "B. Poisson", "C. Geometric", "D. Binomial"],
        "answer": "A. Normal",
        "explanation": "By the Central Limit Theorem, sums of i.i.d. variables tend to normality."
    },
    {
        "question": "Which distribution is appropriate for 'fraction of heads' in 100 fair coin tosses?",
        "choices": ["A. Binomial scaled by n", "B. Poisson", "C. Geometric", "D. Uniform"],
        "answer": "A. Binomial scaled by n",
        "explanation": "The number of heads is Binomial(100,0.5), and the fraction is X/100."
    },
    {
        "question": "If interarrival times are exponentially distributed, what does that imply about event independence?",
        "choices": ["A. Events occur independently", "B. Events are correlated", "C. Events occur in bursts", "D. Depend on last arrival time"],
        "answer": "A. Events occur independently",
        "explanation": "The exponential’s memoryless property implies independence between events."
    },
    {
        "question": "If a question involves 'average number of arrivals per minute' but you must find 'expected waiting time', which distribution links them?",
        "choices": ["A. Exponential", "B. Poisson", "C. Normal", "D. Geometric"],
        "answer": "A. Exponential",
        "explanation": "Waiting time (continuous) is exponential with rate equal to Poisson’s λ."
    },
    {
        "question": "Which distribution would you use for the number of customers waiting in a simple queue with arrivals λ and service μ?",
        "choices": ["A. Geometric or Poisson, depending on queue type", "B. Normal", "C. Exponential", "D. Uniform"],
        "answer": "A. Geometric or Poisson, depending on queue type",
        "explanation": "Discrete counts of customers often follow Poisson or geometric steady-state distributions."
    },
    {
        "question": "A machine produces parts with a 1% defect rate. For 200 parts, the approximate distribution of defective parts is:",
        "choices": ["A. Poisson(λ=2)", "B. Binomial(200,0.01)", "C. Normal(μ=2,σ²≈2)", "D. Any of these (A≈B≈C)"],
        "answer": "D. Any of these (A≈B≈C)",
        "explanation": "Binomial(200,0.01) ≈ Poisson(λ=2) ≈ Normal(μ=2,σ²=2) for large n, small p."
    },
    {
        "question": "If a system has exponentially distributed service times, what does that imply about its memory of past service?",
        "choices": ["A. It has none (memoryless)", "B. It increases with time", "C. It depends on queue length", "D. It oscillates"],
        "answer": "A. It has none (memoryless)",
        "explanation": "The exponential distribution is the only continuous one with no memory."
    },
    {
        "question": "If a question gives 'mean interarrival time = 2 minutes', what is the expected number of arrivals in 10 minutes?",
        "choices": ["A. 5", "B. 10", "C. 20", "D. 2"],
        "answer": "A. 5",
        "explanation": "Rate λ = 1/2 arrivals per minute, so expected count = λ × 10 = 5."
    },
    {
        "question": "When combining two independent Poisson processes with rates λ1 and λ2, what is the resulting rate?",
        "choices": ["A. λ1 + λ2", "B. λ1 − λ2", "C. λ1λ2", "D. max(λ1,λ2)"],
        "answer": "A. λ1 + λ2",
        "explanation": "Independent Poisson processes sum to another Poisson process with total rate equal to the sum of individual rates."
    },
    {
        "question": "If X~Exponential(λ), what is P(X>mean)?",
        "choices": ["A. e^(−1)", "B. 0.5", "C. 1−e^(−1)", "D. Cannot be computed"],
        "answer": "A. e^(−1)",
        "explanation": "P(X>1/λ)=e^(−λ×1/λ)=e^(−1)≈0.3679."
    },
    {
        "question": "Which distribution should you suspect when an event has a 'constant hazard rate' (risk per unit time)?",
        "choices": ["A. Exponential", "B. Weibull", "C. Normal", "D. Binomial"],
        "answer": "A. Exponential",
        "explanation": "A constant hazard rate defines the exponential distribution."
    },
    {
        "question": "Which distribution is most appropriate for modeling 'number of system crashes per week'?",
        "choices": ["A. Poisson", "B. Normal", "C. Binomial", "D. Exponential"],
        "answer": "A. Poisson",
        "explanation": "Discrete counts of rare events per interval are modeled by Poisson."
    },
    {
        "question": "Which distribution fits 'total service time for 5 independent exponential tasks'?",
        "choices": ["A. Gamma(5,λ)", "B. Poisson(5)", "C. Binomial(5,p)", "D. Normal(μ,σ²)"],
        "answer": "A. Gamma(5,λ)",
        "explanation": "Sum of independent exponential(λ) random variables is Gamma(k,λ)."
    },
    {
        "question": "Which distribution is symmetric around its mean?",
        "choices": ["A. Normal", "B. Exponential", "C. Poisson", "D. Geometric"],
        "answer": "A. Normal",
        "explanation": "The normal distribution is symmetric around μ."
    },
    {
        "question": "Which distribution should you think of if the probability of success changes over time?",
        "choices": ["A. Not Binomial (violates constant p)", "B. Binomial", "C. Poisson", "D. Exponential"],
        "answer": "A. Not Binomial (violates constant p)",
        "explanation": "Binomial assumes fixed probability per trial; varying p breaks that assumption."
    },
    {
        "question": "In which case is the geometric distribution not appropriate?",
        "choices": ["A. When success probability varies by trial", "B. When trials are independent", "C. When first success is of interest", "D. When probability is constant"],
        "answer": "A. When success probability varies by trial",
        "explanation": "Geometric requires identical independent trials with constant p."
    },
    {
        "question": "If a variable represents the number of arrivals in 15 seconds and has mean λt=6, what is its standard deviation?",
        "choices": ["A. √6", "B. 6", "C. 1/6", "D. 36"],
        "answer": "A. √6",
        "explanation": "For Poisson, Var(X)=λt, so SD=√(λt)."
    },
    {
        "question": "If the lifetime of components is exponentially distributed, the lifetime of 3 components in parallel is:",
        "choices": ["A. Longer, since max of exponentials", "B. Same as one", "C. Shorter, since min of exponentials", "D. None"],
        "answer": "A. Longer, since max of exponentials",
        "explanation": "Parallel components fail only when all fail; total life is the maximum of exponentials."
    },
    {
        "question": "If the lifetime of components is exponential, the lifetime of 3 in series is:",
        "choices": ["A. Shorter, since min of exponentials", "B. Longer", "C. Unchanged", "D. Constant"],
        "answer": "A. Shorter, since min of exponentials",
        "explanation": "Series system fails when first component fails, which is the minimum of exponentials."
    }
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