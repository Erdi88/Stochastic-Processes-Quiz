import streamlit as st
import random

st.set_page_config(page_title="Database Systems Quiz 2025", layout="centered")

# -----------------------------
# QUESTIONS (same as before)
# -----------------------------
questions = [
     {
        "question": "True or False: Undo phase in recovery rolls back uncommitted transactions.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "Undo restores database to a consistent state by reversing incomplete transactions."
    },
    {
        "question": "Which SQL statement removes specific rows from a table based on a condition?",
        "choices": ["A. DELETE", "B. TRUNCATE", "C. DROP", "D. REMOVE"],
        "answer": "A. DELETE",
        "explanation": "DELETE removes rows matching the WHERE condition."
    },
     {
        "question": "Which type of join returns only rows that match in both tables?",
        "choices": ["A. Inner Join", "B. Left Outer Join", "C. Right Outer Join", "D. Full Outer Join"],
        "answer": "A. Inner Join",
        "explanation": "Inner Join returns only rows where the join condition is satisfied in both tables."
    },
    {
        "question": "True or False: A composite primary key is a primary key consisting of more than one attribute.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "Composite keys combine multiple attributes to uniquely identify a row."
    },
    {
        "question": "Which SQL query lists students who have taken both course INF-1101 and INF-2700?",
        "choices": ["A. Using INTERSECT on two SELECTs", "B. Using UNION on two SELECTs", "C. Using JOIN", "D. Using WHERE IN for one course"],
        "answer": "A. Using INTERSECT on two SELECTs",
        "explanation": "INTERSECT returns only students present in both course queries."
    },
    {
        "question": "True or False: In relational algebra, the projection operation can remove duplicate tuples.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "Projection eliminates duplicate rows, returning a set of distinct tuples."
    },
    {
        "question": "Which type of index is ideal for range queries like BETWEEN or >, < comparisons?",
        "choices": ["A. Hash index", "B. B+-tree", "C. Bitmap index", "D. Clustered index"],
        "answer": "B. B+-tree",
        "explanation": "B+-trees allow efficient range searches by traversing leaf nodes sequentially."
    },
    {
        "question": "True or False: In 3NF, every non-prime attribute is non-transitively dependent on every key.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "3NF removes transitive dependencies to reduce redundancy."
    },
    {
        "question": "Which transaction anomaly occurs when two transactions update the same data simultaneously without isolation?",
        "choices": ["A. Dirty Read", "B. Lost Update", "C. Unrepeatable Read", "D. Phantom Read"],
        "answer": "B. Lost Update",
        "explanation": "A lost update happens when one transaction overwrites another transaction’s changes."
    },
    {
        "question": "Which SQL keyword is used to prevent duplicates in the result of a SELECT query?",
        "choices": ["A. DISTINCT", "B. UNIQUE", "C. GROUP BY", "D. HAVING"],
        "answer": "A. DISTINCT",
        "explanation": "DISTINCT removes duplicate rows from the query result."
    },
    {
        "question": "True or False: A checkpoint allows the database to recover faster after a crash.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "Checkpoints reduce the amount of work during recovery by marking consistent states."
    },
    {
        "question": "Which SQL clause is used to group rows before applying aggregate functions?",
        "choices": ["A. WHERE", "B. HAVING", "C. GROUP BY", "D. ORDER BY"],
        "answer": "C. GROUP BY",
        "explanation": "GROUP BY groups rows for aggregation like COUNT, SUM, AVG."
    },
    {
        "question": "True or False: A foreign key must reference a primary key or a unique key in another table.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "Foreign keys enforce referential integrity by pointing to a unique row in another table."
    },
    {
        "question": "Which type of join would you use to include all students, even if they have not taken any courses?",
        "choices": ["A. Inner Join", "B. Left Outer Join", "C. Right Outer Join", "D. Cross Join"],
        "answer": "B. Left Outer Join",
        "explanation": "Left Outer Join includes all rows from the left table and matches from the right table if they exist."
    },
    {
        "question": "True or False: Undo phase in recovery must be performed before redo phase.",
        "choices": ["A. True", "B. False"],
        "answer": "B. False",
        "explanation": "Redo phase is applied first to ensure committed updates, then undo reverses uncommitted changes."
    },
    {
        "question": "Which normal form eliminates repeating groups?",
        "choices": ["A. 1NF", "B. 2NF", "C. 3NF", "D. BCNF"],
        "answer": "A. 1NF",
        "explanation": "1NF requires each attribute to hold atomic values, removing repeating groups."
    },
    {
        "question": "True or False: In a B+-tree, all records are stored at the leaf nodes.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "B+-tree leaves store all data records; internal nodes only store keys for navigation."
    },
    {
        "question": "Which SQL query finds the highest salary in each department?",
        "choices": ["A. SELECT MAX(salary) FROM Instructor", "B. SELECT dept, MAX(salary) FROM Instructor GROUP BY dept", "C. SELECT dept, salary FROM Instructor WHERE salary = MAX(salary)", "D. SELECT dept, salary FROM Instructor ORDER BY salary DESC"],
        "answer": "B. SELECT dept, MAX(salary) FROM Instructor GROUP BY dept",
        "explanation": "GROUP BY allows aggregation per department."
    },
    {
        "question": "True or False: A schedule is strict if a transaction can read or write uncommitted data from another transaction.",
        "choices": ["A. True", "B. False"],
        "answer": "B. False",
        "explanation": "Strict schedules prevent reading or writing uncommitted data."
    },
    {
        "question": "Which operation in relational algebra selects rows based on a condition?",
        "choices": ["A. Projection", "B. Selection", "C. Join", "D. Union"],
        "answer": "B. Selection",
        "explanation": "Selection (σ) filters tuples satisfying a given predicate."
    },
    {
        "question": "True or False: A dependency-preserving decomposition allows all functional dependencies to be enforced without joins.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "Dependency preservation ensures constraints can be checked on decomposed tables individually."
    },
    {
        "question": "Which SQL command removes a table completely from the database?",
        "choices": ["A. DELETE", "B. TRUNCATE", "C. DROP", "D. REMOVE"],
        "answer": "C. DROP",
        "explanation": "DROP deletes the table schema and all its data permanently."
    },
    {
        "question": "True or False: Hash file organization is better for sequential range queries than B+-tree file organization.",
        "choices": ["A. True", "B. False"],
        "answer": "B. False",
        "explanation": "Hash organization is efficient for equality searches but poor for range queries."
    },
]

# -----------------------------
# SESSION STATE INIT
# -----------------------------
if "q_index" not in st.session_state:
    st.session_state.q_index = 0

if "shuffled_questions" not in st.session_state:
    st.session_state.shuffled_questions = random.sample(questions, len(questions))  # Shuffle questions

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




