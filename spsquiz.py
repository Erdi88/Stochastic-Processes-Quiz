import streamlit as st
import random

st.set_page_config(page_title="Database Systems Quiz 2025", layout="centered")

# -----------------------------
# QUESTIONS (same as before)
# -----------------------------
questions = [
     {
        "question": "Asteroid families describe asteroids with:",
        "choices": [
            "A: Similar composition",
            "B: Similar orbital parameters, inclination and semi-major axis",
            "C: Similar size and bulk density"
        ],
        "answer": "B",
        "explanation": "Asteroid families are groups of asteroids sharing similar orbits, likely formed from the breakup of a parent body."
    },
    {
        "question": "Pluto is not classified as a planet anymore because:",
        "choices": [
            "A: It turned out its shape is not spherical",
            "B: It turned out it does not have an atmosphere",
            "C: It does not clear its orbital region from other objects"
        ],
        "answer": "C",
        "explanation": "Pluto does not dominate its orbit, which is one of the criteria for full planet classification under IAU rules."
    },
    {
        "question": "How was the first extra-solar planet around a main-sequence star discovered?",
        "choices": [
            "A: By transit observation",
            "B: By Doppler shift observation",
            "C: By thermal emission observation"
        ],
        "answer": "B",
        "explanation": "The first exoplanet around a main-sequence star was detected using the Doppler shift in the host star's spectrum caused by the planet’s gravitational pull."
    },
    {
        "question": "Which of the following parameters most affected the bulk density of solar system planets at present?",
        "choices": [
            "A: Element compositions in the protoplanetary disk",
            "B: Condensation temperatures in the protoplanetary disk",
            "C: Self-gravity of the planets"
        ],
        "answer": "A",
        "explanation": "The initial elemental composition of the protoplanetary disk determines whether a planet becomes rocky, icy, or gaseous, which strongly affects its density."
    },
    {
        "question": "Several different observations of the Sun are made to monitor the progress of its 11-year cycle; which of the listed parameters is NOT typically used to monitor the solar cycle?",
        "choices": [
            "A: Sunspot number",
            "B: Solar flux at radio wavelength",
            "C: Solar neutrino flux"
        ],
        "answer": "C",
        "explanation": "Solar neutrino flux is not typically used to monitor the solar cycle because neutrino production in the Sun's core remains relatively constant; sunspots and radio flux vary with the cycle."
    },
    {
        "question": "The Sun follows a periodic change of activity of approximately 11 years. Which of the following parameters is commonly used to measure this cycle?",
        "choices": [
            "A: Sunspot number",
            "B: Solar neutrino flux",
            "C: Orbital eccentricity of planets"
        ],
        "answer": "A",
        "explanation": "The number of sunspots is the primary observable used to track the Sun's 11-year cycle, as it directly reflects solar magnetic activity."
    },
    {
        "question": "Despite the observation of dark sunspots during solar maximum, why is the Earth's atmosphere found to be slightly warmer during solar maximum than during solar minimum?",
        "choices": [
            "A: Increased solar radiation in other wavelengths",
            "B: Increased reflection from sunspots",
            "C: Decrease in solar wind velocity"
        ],
        "answer": "A",
        "explanation": "Sunspots themselves are cooler, but the overall solar output increases due to bright regions called faculae, which increases the total solar energy reaching Earth."
    },
    {
        "question": "Which object is used to estimate the flux of interplanetary meteoroids at Mars?",
        "choices": [
            "A: Crater counts on Mars and its moons",
            "B: Orbital period of Mars",
            "C: Solar rotation period"
        ],
        "answer": "A",
        "explanation": "Meteor flux estimates are derived from crater counts on Mars, Phobos, and Deimos, as well as direct meteor observations."
    },
    {
        "question": "Which of the following best describes a Sun-synchronous orbit?",
        "choices": [
            "A: An orbit where the spacecraft always passes over the same solar longitude at the same local solar time",
            "B: An orbit where the spacecraft remains stationary relative to the Sun",
            "C: An orbit where the spacecraft stays at a fixed distance from the Earth"
        ],
        "answer": "A",
        "explanation": "A Sun-synchronous orbit precesses so that the spacecraft passes over any given point on the Sun (or Earth) at the same local solar time, useful for continuous observations."
    },
    {
        "question": "A spacecraft travels from Earth to Mars using a Hohmann transfer orbit. Which of the following statements is correct?",
        "choices": [
            "A: It follows an elliptical path tangent to Earth's and Mars' orbits",
            "B: It follows a circular path at constant speed",
            "C: It requires instantaneous acceleration at the midpoint of the orbit"
        ],
        "answer": "A",
        "explanation": "A Hohmann transfer orbit is an elliptical trajectory tangent to the departure and arrival orbits, optimized for minimum energy transfer."
    },
    {
        "question": "When estimating the flux of interplanetary objects from crater counts on Mars, Phobos, and Deimos, why could the crater counts lead to different estimates?",
        "choices": [
            "A: Differences in surface gravity affect crater formation",
            "B: Differences in surface age and geological activity",
            "C: Differences in atmospheric presence or absence",
            "D: All of the above"
        ],
        "answer": "D",
        "explanation": "Crater counts vary due to differences in surface gravity (affecting crater size), surface age or erosion (older surfaces accumulate more craters), and presence or absence of atmosphere (which can burn up meteoroids before impact). Therefore, all these factors can cause different flux estimates on Mars, Phobos, and Deimos."
    },
    {
        "question": "Which of the products of the reactions in the interior of the Sun reaches the Earth?",
        "choices": [
            "A: Neutrinos",
            "B: Atomic nuclei in the solar wind",
            "C: Photons from the solar light"
        ],
        "answer": "A",
        "explanation": "Neutrinos interact very weakly with matter and can escape the Sun’s core almost immediately, reaching Earth directly. Photons from the core take thousands of years to reach the surface, and atomic nuclei in the solar wind originate from the Sun’s outer layers, not its core fusion reactions."
    },
    {
        "question": "The first exoplanet around a main-sequence star was discovered by:",
        "choices": [
            "A: Its thermal emission brightness",
            "B: The Doppler shift in the spectrum of its host star",
            "C: Its transit reducing the brightness of the host star"
        ],
        "answer": "B",
        "explanation": "The first exoplanet around a main-sequence star was detected using Doppler spectroscopy, observing the wobble of the star caused by the planet's gravitational pull."
    },
    {
        "question": "Which of the following parameters most affected the bulk density of solar system planets at present?",
        "choices": [
            "A: Element compositions in the protoplanetary disk",
            "B: Condensation temperatures in the protoplanetary disk",
            "C: Self-gravity of the planets"
        ],
        "answer": "A",
        "explanation": "The bulk density of planets is primarily determined by their elemental composition, which depends on the materials present in the protoplanetary disk during formation."
    },
    {
        "question": "With few exceptions the planets and other solar system objects orbit the Sun in the same direction. What concept of classical physics explains this observation?",
        "choices": [
            "A: Conservation of energy",
            "B: Conservation of angular momentum",
            "C: Kepler’s laws"
        ],
        "answer": "B",
        "explanation": "The conservation of angular momentum from the rotating protoplanetary disk causes most objects to orbit in the same direction around the Sun."
    },
    {
        "question": "What is the main difference when solar element abundance and element abundance of a primitive meteorite are compared?",
        "choices": [
            "A: The meteorite contains aminoacids",
            "B: The meteorite contains less He because the Sun is enriched in He",
            "C: The meteorite contains smaller amounts of the volatile elements"
        ],
        "answer": "C",
        "explanation": "Meteorites typically have fewer volatile elements compared to the Sun, which loses some of these elements during formation and evolution."
    },
    {
        "question": "The moons of the solar system planets are typically located:",
        "choices": [
            "A: Inside the Roche limit of the planet",
            "B: Inside the Hill sphere of the planet",
            "C: Inside the Jeans radius"
        ],
        "answer": "B",
        "explanation": "Moons orbit within the Hill sphere, which defines the region where a planet’s gravity dominates over the Sun’s, allowing stable satellite orbits."
    },
    {
        "question": "Asteroid families describe asteroids with:",
        "choices": [
            "A: Similar composition",
            "B: Similar orbital parameters, inclination and semimajor axis",
            "C: Similar size and bulk density"
        ],
        "answer": "B",
        "explanation": "Asteroid families are identified based on clustering in orbital parameters, such as semimajor axis, eccentricity, and inclination, often indicating a common origin from a parent body."
    },
    {
        "question": "Explain what the differential equation of hydrostatic equilibrium (∇P = -gρ) means for a planetary atmosphere.",
        "choices": [
            "A: It describes the balance between pressure gradient and gravitational force in the atmosphere",
            "B: It calculates the temperature profile of the atmosphere",
            "C: It describes the chemical composition of the atmosphere"
        ],
        "answer": "A",
        "explanation": "Hydrostatic equilibrium states that the upward pressure gradient force balances the downward gravitational force, maintaining atmospheric stability."
    },
    {
        "question": "Which assumptions were made to derive the hydrostatic equilibrium equation from the full momentum equation?",
        "choices": [
            "A: Neglecting viscosity and acceleration, assuming steady-state conditions",
            "B: Assuming the atmosphere is incompressible",
            "C: Ignoring gravitational effects"
        ],
        "answer": "A",
        "explanation": "Deriving hydrostatic equilibrium assumes a steady-state, negligible viscosity, and small vertical accelerations compared to gravity."
    },
    {
    "question": "The Giant planets grew in the protoplanetary disk by:",
    "choices": [
        "A: collecting smaller planets",
        "B: accumulation of planetesimals, dust, and gas",
        "C: gravitational collapse"
    ],
    "answer": "B",
    "explanation": "Giant planets formed by gradually accumulating solids and gas from the protoplanetary disk, not by collecting other planets or direct collapse."
    },
    {
        "question": "Light emitted from the Sun reaches Earth within about 8 minutes. The solar wind emitted at the same time reaches Earth:",
        "choices": [
            "A: at the same time",
            "B: earlier",
            "C: later"
        ],
        "answer": "C",
        "explanation": "Solar wind particles travel much slower than light, so they reach Earth later than photons from sunlight."
    },
    {
        "question": "The blackbody temperature of the Earth's moon is:",
        "choices": [
            "A: significantly higher because the moon is exposed to the solar wind and Earth is not",
            "B: significantly lower because the moon's radius is less than 1/3 of Earth's radius",
            "C: the same because both are at the same distance from the Sun"
        ],
        "answer": "C",
        "explanation": "The Moon and Earth are at nearly the same distance from the Sun, so their equilibrium blackbody temperatures are approximately the same."
    },
    {
        "question": "The blackbody temperature of Venus is:",
        "choices": [
            "A: higher than that of the Earth",
            "B: lower than that of the Earth",
            "C: about the same, because both planets have about the same size"
        ],
        "answer": "A",
        "explanation": "Venus is hotter than Earth due to its thick CO2 atmosphere, which traps heat via the greenhouse effect."
    },
    {
        "question": "The solar system comets contain dust and ice because:",
        "choices": [
            "A: they are fragments of the outer icy planets",
            "B: they formed outside of the ice line in the protoplanetary cloud",
            "C: they formed in the cold interstellar medium"
        ],
        "answer": "B",
        "explanation": "Comets formed beyond the ice line in the protoplanetary disk where temperatures were low enough for ices to condense, along with dust."
    },
    {
        "question": "Most of the solar wind particles that reach the Earth are:",
        "choices": [
            "A: absorbed in the Earth's atmosphere",
            "B: deflected by the Earth's magnetic field",
            "C: reach the surface of the Earth without interaction"
        ],
        "answer": "B",
        "explanation": "Earth's magnetic field deflects most solar wind particles, protecting the surface from direct impact."
    },
    {
        "question": "The term 'habitable zone' is used in astronomy to describe the:",
        "choices": [
            "A: region in the solar system that is within the ice line",
            "B: region around a star where Earth-like planets can have liquid water on the surface",
            "C: region in the Milky Way where main sequence stars exist"
        ],
        "answer": "B",
        "explanation": "The habitable zone is defined as the orbital region around a star where temperatures allow liquid water to exist on a planet's surface."
    },
    {
        "question": "The ring systems of planets were discovered in the 20th century. There is one exception:",
        "choices": [
            "A: Saturn’s rings are so massive that they are visible even with small telescopes",
            "B: Uranus’ rings were known by astronomers for centuries because they occult stars",
            "C: Jupiter’s rings are easily observed because Jupiter is the giant planet closest to Earth"
        ],
        "answer": "A",
        "explanation": "Saturn's rings are visible even with small telescopes, unlike the faint rings of other planets which required modern observations."
    },
    {
        "question": "Which of these objects is/are located in Lagrange points of the Sun–Earth system:",
        "choices": [
            "A: the Jupiter trojans",
            "B: ESA’s Solar Heliospheric Observatory spacecraft: SOHO",
            "C: the Mars trojans"
        ],
        "answer": "B",
        "explanation": "SOHO is located near the Sun–Earth L1 Lagrange point to continuously monitor the Sun."
    },
    {
        "question": "What is the main process of heat transfer from Sun to planets:",
        "choices": [
            "A: diffusion",
            "B: convection",
            "C: radiation"
        ],
        "answer": "C",
        "explanation": "Energy from the Sun reaches planets primarily via radiation, not conduction or convection."
    },
    {
        "question": "Long-period comets are observed when they approach the vicinity of the Sun from:",
        "choices": [
            "A: Oort cloud",
            "B: planetary nebula",
            "C: molecular cloud"
        ],
        "answer": "A",
        "explanation": "Long-period comets originate from the distant Oort cloud and are seen when they enter the inner solar system."
    }
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
        
        # Extract the letter from the choice before comparing
        choice_letter = choice.split(":")[0].strip()  # "A: Oort cloud" -> "A"
        
        if choice_letter == q["answer"]:
            st.session_state.feedback = f"✅ Correct! {q['explanation']}"
            st.session_state.score += 1
        else:
            st.session_state.feedback = f"❌ Incorrect. Correct: {q['answer']}. {q['explanation']}"


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






