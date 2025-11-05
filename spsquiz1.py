import streamlit as st
import random

st.set_page_config(page_title="Space Quiz 2025", layout="centered")

# -----------------------------
# QUESTIONS (same as before)
# -----------------------------
questions = [
    # Example subset, replace with your full list
    {
        "question": "1️⃣ What is the main difference between solar element abundance and primitive meteorite abundance?",
        "choices": [
            "A. Meteorites contain smaller amounts of volatile elements",
            "B. Meteorites contain amino acids",
            "C. Meteorites contain less helium because the Sun is enriched in He"
        ],
        "answer": "A. Meteorites contain smaller amounts of volatile elements",
        "explanation": "Primitive meteorites (like CI chondrites) lost volatiles such as H, He, C, N during condensation. They preserve the solid composition of the solar nebula."
    },
    {
        "question": "2️⃣ Which two elements make up about 98% of the Sun’s mass?",
        "choices": [
            "A. Hydrogen and Helium",
            "B. Oxygen and Carbon",
            "C. Iron and Silicon"
        ],
        "answer": "A. Hydrogen and Helium",
        "explanation": "Hydrogen (~74%) and Helium (~24%) dominate the Sun’s mass. All heavier elements (‘metals’) make up only about 2%."
    },
    {
        "question": "3️⃣ CI chondrites are important because they represent:",
        "choices": [
            "A. The gaseous composition of the Sun",
            "B. The original solid composition of the solar nebula",
            "C. The metallic core of Earth"
        ],
        "answer": "B. The original solid composition of the solar nebula",
        "explanation": "CI chondrites retain the same proportions of non-volatile elements as the Sun, except volatile gases. They act as a chemical reference for the early Solar System."
    },
    {
        "question": "4️⃣ In the Sun, the third most abundant element (after H and He) is:",
        "choices": [
            "A. Oxygen",
            "B. Carbon",
            "C. Iron"
        ],
        "answer": "A. Oxygen",
        "explanation": "After H and He, Oxygen is the most abundant element in the Sun, followed by Carbon, Neon, and Iron."
    },
    {
        "question": "Which two elements make up most of the Sun’s mass?",
        "choices": ["A. Hydrogen and Helium", "B. Oxygen and Iron", "C. Carbon and Silicon", "D. Helium and Nitrogen"],
        "answer": "A. Hydrogen and Helium",
        "explanation": "Hydrogen (~74%) and Helium (~24%) dominate the Sun’s composition; all other elements make up less than 2%."
    },
    {
        "question": "What is the main difference between solar elemental abundance and that of primitive meteorites?",
        "choices": ["A. Meteorites contain smaller amounts of volatile elements", "B. Meteorites have higher hydrogen content", "C. Meteorites contain amino acids", "D. Meteorites are richer in helium"],
        "answer": "A. Meteorites contain smaller amounts of volatile elements",
        "explanation": "Primitive meteorites lost volatile elements like H, He, and C, but preserve refractory element proportions similar to the Sun."
    },
    {
        "question": "What is the dominant energy source of the Sun?",
        "choices": ["A. Gravitational contraction", "B. Nuclear fusion of hydrogen into helium", "C. Radioactive decay", "D. Chemical combustion"],
        "answer": "B. Nuclear fusion of hydrogen into helium",
        "explanation": "The Sun’s energy comes from the proton-proton chain converting hydrogen into helium in its core."
    },
    {
        "question": "Which law relates a planet’s orbital period to its average distance from the Sun?",
        "choices": ["A. Kepler’s third law", "B. Newton’s first law", "C. Stefan–Boltzmann law", "D. Wien’s displacement law"],
        "answer": "A. Kepler’s third law",
        "explanation": "Kepler’s third law states P² ∝ a³, linking orbital period (P) and semi-major axis (a)."
    },
    {
        "question": "The Roche limit defines:",
        "choices": ["A. The distance within which a satellite is torn apart by tidal forces", "B. The distance a planet can retain an atmosphere", "C. The maximum radius of a planet", "D. The escape velocity threshold"],
        "answer": "A. The distance within which a satellite is torn apart by tidal forces",
        "explanation": "Inside the Roche limit, tidal forces exceed self-gravity, disintegrating moons or comets."
    },
    {
        "question": "Which type of meteorite best preserves the original solar system composition (minus gases)?",
        "choices": ["A. CI carbonaceous chondrites", "B. Iron meteorites", "C. Achondrites", "D. Ordinary chondrites"],
        "answer": "A. CI carbonaceous chondrites",
        "explanation": "CI chondrites closely match the Sun’s non-volatile element ratios, making them key for solar composition studies."
    },
    {
        "question": "What does Kepler’s second law (law of areas) state?",
        "choices": ["A. Planets move faster near the Sun and slower when far away", "B. All orbits are circular", "C. The Sun moves around the planets", "D. Planetary speeds are constant"],
        "answer": "A. Planets move faster near the Sun and slower when far away",
        "explanation": "A line between the Sun and a planet sweeps equal areas in equal times—so speed varies with distance."
    },
    {
        "question": "Which force keeps planets in orbit around the Sun?",
        "choices": ["A. Gravitational force", "B. Magnetic force", "C. Centrifugal force", "D. Electromagnetic radiation pressure"],
        "answer": "A. Gravitational force",
        "explanation": "The Sun’s gravity provides the centripetal force needed for orbital motion."
    },
    {
        "question": "What is the escape velocity from a planet of mass M and radius R?",
        "choices": ["A. sqrt(2GM/R)", "B. GM/R²", "C. sqrt(GM/R²)", "D. GM²/R"],
        "answer": "A. sqrt(2GM/R)",
        "explanation": "Escape velocity is derived from equating kinetic and gravitational potential energy: v = √(2GM/R)."
    },
    {
        "question": "What is the approximate temperature of the Sun’s surface (photosphere)?",
        "choices": ["A. 5800 K", "B. 10000 K", "C. 3500 K", "D. 15000 K"],
        "answer": "A. 5800 K",
        "explanation": "The Sun’s visible surface emits like a ~5800 K blackbody."
    },
    {
        "question": "In the solar nebula model, what caused the inner planets to be rocky and outer ones gaseous?",
        "choices": ["A. Temperature gradient in the protoplanetary disk", "B. Solar magnetic field strength", "C. Planetary collisions", "D. Stellar winds"],
        "answer": "A. Temperature gradient in the protoplanetary disk",
        "explanation": "High temperatures near the Sun allowed only refractory materials to condense, forming rocky planets."
    },
    {
        "question": "What are ‘volatile elements’ in planetary science?",
        "choices": ["A. Elements that evaporate easily", "B. Elements that are metallic", "C. Elements with high atomic numbers", "D. Elements that form silicates"],
        "answer": "A. Elements that evaporate easily",
        "explanation": "Volatiles like H, C, N, and noble gases vaporize at low temperatures."
    },
    {
        "question": "Which region of the solar system contains icy bodies beyond Neptune?",
        "choices": ["A. Kuiper Belt", "B. Oort Cloud", "C. Asteroid Belt", "D. Magnetosphere"],
        "answer": "A. Kuiper Belt",
        "explanation": "The Kuiper Belt contains trans-Neptunian icy objects such as Pluto and Eris."
    },
    {
        "question": "Which formula gives the gravitational potential energy between two masses M and m separated by r?",
        "choices": ["A. -GMm/r", "B. GMm/r²", "C. -GMm/r²", "D. Gm/Mr"],
        "answer": "A. -GMm/r",
        "explanation": "Gravitational potential energy is negative, indicating a bound system."
    },
    {
        "question": "The main process forming energy in the Sun’s core is:",
        "choices": ["A. Proton-proton chain fusion", "B. Deuterium burning", "C. Helium capture", "D. Neutron decay"],
        "answer": "A. Proton-proton chain fusion",
        "explanation": "The proton-proton chain dominates energy generation in main-sequence stars like the Sun."
    },
    {
        "question": "Which law describes the flux of radiation from a blackbody?",
        "choices": ["A. Stefan–Boltzmann law", "B. Kepler’s first law", "C. Wien’s displacement law", "D. Planck’s quantum law"],
        "answer": "A. Stefan–Boltzmann law",
        "explanation": "The total energy emitted per unit area is σT⁴."
    },
    {
        "question": "Which statement is TRUE about the asteroid belt?",
        "choices": ["A. It lies between Mars and Jupiter", "B. It lies beyond Neptune", "C. It is made entirely of ice", "D. It has only one large object"],
        "answer": "A. It lies between Mars and Jupiter",
        "explanation": "The asteroid belt is between 2–3 AU, composed mostly of rock and metal."
    },
    {
        "question": "Comets are primarily composed of:",
        "choices": ["A. Ice and dust", "B. Iron and nickel", "C. Silicate rock", "D. Hydrogen gas"],
        "answer": "A. Ice and dust",
        "explanation": "Comets are icy planetesimals; their tails form as ices sublimate near the Sun."
    },
    {
        "question": "Which planet has the highest surface temperature due to the greenhouse effect?",
        "choices": ["A. Venus", "B. Mercury", "C. Mars", "D. Jupiter"],
        "answer": "A. Venus",
        "explanation": "A dense CO₂ atmosphere traps heat, raising Venus’s surface temperature above 460°C."
    },
    {
        "question": "According to Kepler’s first law, planetary orbits are:",
        "choices": ["A. Ellipses with the Sun at one focus", "B. Circles with the Sun at center", "C. Parabolas", "D. Hyperbolas"],
        "answer": "A. Ellipses with the Sun at one focus",
        "explanation": "Kepler’s first law defines the shape of orbital paths."
    },
    {
        "question": "Escape velocity depends on:",
        "choices": ["A. Mass and radius of the planet", "B. Planet’s temperature", "C. Distance from the Sun", "D. Planet’s rotation speed"],
        "answer": "A. Mass and radius of the planet",
        "explanation": "vₑ = √(2GM/R) — it increases with planetary mass and decreases with radius."
    },
    {
        "question": "The term ‘metallicity’ in astrophysics refers to:",
        "choices": ["A. The fraction of mass in elements heavier than helium", "B. The amount of iron only", "C. The density of a planet", "D. The magnetic field strength"],
        "answer": "A. The fraction of mass in elements heavier than helium",
        "explanation": "In astronomy, all elements heavier than helium are called 'metals'."
    },
    {
        "question": "What is the source of the solar wind?",
        "choices": ["A. Hot plasma escaping the corona", "B. Magnetic field lines in the photosphere", "C. Hydrogen burning in the core", "D. Planetary magnetic fields"],
        "answer": "A. Hot plasma escaping the corona",
        "explanation": "The corona’s high temperature allows particles to overcome solar gravity and stream outward."
    },
    {
        "question": "Which planet has a rotation axis tilted almost parallel to its orbital plane?",
        "choices": ["A. Uranus", "B. Saturn", "C. Jupiter", "D. Neptune"],
        "answer": "A. Uranus",
        "explanation": "Uranus is tilted by ~98°, possibly due to a massive collision early in its history."
    },
    {
        "question": "Which two elements make up about 98% of the Sun’s mass?",
        "choices": ["A. Hydrogen and Helium", "B. Oxygen and Iron", "C. Carbon and Silicon", "D. Helium and Nitrogen"],
        "answer": "A. Hydrogen and Helium",
        "explanation": "The Sun is ~74% hydrogen and ~24% helium by mass; all heavier elements (‘metals’) are less than 2%."
    },
    {
        "question": "Which layer of the Sun emits the visible light we see?",
        "choices": ["A. Photosphere", "B. Chromosphere", "C. Corona", "D. Core"],
        "answer": "A. Photosphere",
        "explanation": "The photosphere is the Sun’s visible surface, at ~5800 K."
    },
    {
        "question": "What is the main energy source in the Sun?",
        "choices": ["A. Nuclear fusion of hydrogen into helium", "B. Gravitational contraction", "C. Chemical combustion", "D. Radioactive decay"],
        "answer": "A. Nuclear fusion of hydrogen into helium",
        "explanation": "Fusion in the core releases energy as hydrogen nuclei combine into helium."
    },
    {
        "question": "What is the approximate surface temperature of the Sun?",
        "choices": ["A. 5800 K", "B. 10000 K", "C. 3000 K", "D. 15000 K"],
        "answer": "A. 5800 K",
        "explanation": "The Sun’s photosphere emits radiation corresponding to about 5800 K."
    },
    {
        "question": "The solar corona is much hotter than the photosphere because of:",
        "choices": ["A. Magnetic energy heating", "B. Nuclear fusion", "C. Gravitational pressure", "D. Radioactive decay"],
        "answer": "A. Magnetic energy heating",
        "explanation": "Magnetic reconnection and plasma waves transfer energy to the corona, raising it to millions of K."
    },
    {
        "question": "The solar wind originates from which region of the Sun?",
        "choices": ["A. Corona", "B. Photosphere", "C. Radiative zone", "D. Core"],
        "answer": "A. Corona",
        "explanation": "The hot, low-density corona allows charged particles to escape the Sun’s gravity, forming the solar wind."
    },
    {
        "question": "Sunspots appear dark because they are:",
        "choices": ["A. Cooler than surrounding regions", "B. Holes in the Sun", "C. Absorbing light", "D. Composed of dust"],
        "answer": "A. Cooler than surrounding regions",
        "explanation": "Sunspots are magnetically active areas about 1000–1500 K cooler than the surrounding photosphere."
    },
    {
        "question": "The proton-proton chain converts hydrogen into helium mainly in the:",
        "choices": ["A. Core", "B. Photosphere", "C. Chromosphere", "D. Corona"],
        "answer": "A. Core",
        "explanation": "Temperatures >10 million K in the core allow hydrogen fusion to occur."
    },
    {
        "question": "The neutrinos produced by the Sun originate from:",
        "choices": ["A. Nuclear reactions in the core", "B. Coronal flares", "C. Solar wind", "D. Photospheric radiation"],
        "answer": "A. Nuclear reactions in the core",
        "explanation": "Neutrinos are direct byproducts of the proton-proton chain fusion reactions."
    },

    # --- Planetary Science & Formation ---
    {
        "question": "Why are terrestrial planets rocky while giant planets are gaseous?",
        "choices": ["A. Temperature gradient in the solar nebula", "B. Larger mass of inner planets", "C. Magnetic fields", "D. Chemical reactions with hydrogen"],
        "answer": "A. Temperature gradient in the solar nebula",
        "explanation": "Close to the Sun, only refractory materials condensed; farther out, ices and gases could also accumulate."
    },
    {
        "question": "Which law relates orbital period (P) and semi-major axis (a)?",
        "choices": ["A. Kepler’s Third Law", "B. Newton’s First Law", "C. Stefan–Boltzmann Law", "D. Wien’s Law"],
        "answer": "A. Kepler’s Third Law",
        "explanation": "Kepler’s Third Law: P² ∝ a³ for objects orbiting the same star."
    },
    {
        "question": "According to Kepler’s First Law, planetary orbits are:",
        "choices": ["A. Elliptical with the Sun at one focus", "B. Circular", "C. Parabolic", "D. Hyperbolic"],
        "answer": "A. Elliptical with the Sun at one focus",
        "explanation": "All planets move in ellipses with the Sun at one focal point."
    },
    {
        "question": "Kepler’s Second Law (law of areas) means:",
        "choices": ["A. Planets move faster near the Sun", "B. Planets move slower near the Sun", "C. All orbits are circular", "D. Orbits are constant speed"],
        "answer": "A. Planets move faster near the Sun",
        "explanation": "A line from the Sun to the planet sweeps out equal areas in equal times."
    },
    {
        "question": "What force keeps planets in orbit?",
        "choices": ["A. Gravity", "B. Magnetic force", "C. Centrifugal force", "D. Radiation pressure"],
        "answer": "A. Gravity",
        "explanation": "The Sun’s gravitational attraction provides the centripetal force for orbital motion."
    },
    {
        "question": "The escape velocity from a planet is proportional to:",
        "choices": ["A. sqrt(M/R)", "B. M/R²", "C. R²/M", "D. 1/M"],
        "answer": "A. sqrt(M/R)",
        "explanation": "Escape velocity is vₑ = √(2GM/R), increasing with mass and decreasing with radius."
    },
    {
        "question": "The Roche limit describes:",
        "choices": ["A. Distance where a body is torn apart by tides", "B. Max size of an asteroid", "C. Radius of gravitational capture", "D. Distance for stable orbit"],
        "answer": "A. Distance where a body is torn apart by tides",
        "explanation": "Inside this limit, tidal forces exceed a moon’s self-gravity."
    },
    {
        "question": "Which planet has the largest day-night temperature contrast?",
        "choices": ["A. Mercury", "B. Venus", "C. Earth", "D. Jupiter"],
        "answer": "A. Mercury",
        "explanation": "Without an atmosphere, Mercury heats intensely by day and cools drastically at night."
    },
    {
        "question": "Which planet’s dense CO₂ atmosphere causes extreme greenhouse heating?",
        "choices": ["A. Venus", "B. Mars", "C. Earth", "D. Saturn"],
        "answer": "A. Venus",
        "explanation": "Venus’s thick CO₂ atmosphere traps heat, creating surface temperatures >460°C."
    },
    {
        "question": "Which planet has a rotation axis tilted about 98°?",
        "choices": ["A. Uranus", "B. Neptune", "C. Jupiter", "D. Saturn"],
        "answer": "A. Uranus",
        "explanation": "Uranus rotates on its side, possibly due to a giant impact early in its history."
    },

    # --- Meteorites, Asteroids & Comets ---
    {
        "question": "Which type of meteorite preserves the Solar System’s original solid composition (minus gases)?",
        "choices": ["A. CI carbonaceous chondrites", "B. Iron meteorites", "C. Achondrites", "D. Pallasites"],
        "answer": "A. CI carbonaceous chondrites",
        "explanation": "CI chondrites have element ratios close to the Sun’s non-volatile composition."
    },
    {
        "question": "What are comets primarily made of?",
        "choices": ["A. Ice and dust", "B. Iron and rock", "C. Silicate minerals", "D. Hydrogen gas"],
        "answer": "A. Ice and dust",
        "explanation": "Comets are icy bodies that sublimate when approaching the Sun, forming tails."
    },
    {
        "question": "Where is the asteroid belt located?",
        "choices": ["A. Between Mars and Jupiter", "B. Beyond Neptune", "C. Between Earth and Venus", "D. Around Saturn"],
        "answer": "A. Between Mars and Jupiter",
        "explanation": "The asteroid belt lies between 2–3 AU from the Sun."
    },
    {
        "question": "Which region contains icy objects like Pluto and Eris?",
        "choices": ["A. Kuiper Belt", "B. Oort Cloud", "C. Asteroid Belt", "D. Inner Solar System"],
        "answer": "A. Kuiper Belt",
        "explanation": "The Kuiper Belt extends beyond Neptune and holds icy dwarf planets."
    },
    {
        "question": "The Oort Cloud is thought to be:",
        "choices": ["A. A distant spherical reservoir of comets", "B. A dense asteroid field", "C. The region of solar fusion", "D. The Sun’s corona"],
        "answer": "A. A distant spherical reservoir of comets",
        "explanation": "The Oort Cloud is a vast shell of icy bodies ~50,000 AU from the Sun."
    },

    # --- Physics & Formulas ---
    {
        "question": "Gravitational potential energy between two masses M and m separated by distance r is:",
        "choices": ["A. -GMm/r", "B. GMm/r²", "C. GMm/r³", "D. -GMm²/r"],
        "answer": "A. -GMm/r",
        "explanation": "The potential energy is negative, indicating a bound system."
    },
    {
        "question": "The total energy of a bound orbit is:",
        "choices": ["A. Negative", "B. Zero", "C. Positive", "D. Infinite"],
        "answer": "A. Negative",
        "explanation": "For bound systems, total (kinetic + potential) energy is negative."
    },
    {
        "question": "Which formula gives escape velocity from a planet?",
        "choices": ["A. v = √(2GM/R)", "B. v = GM/R²", "C. v = GM/R", "D. v = R²/GM"],
        "answer": "A. v = √(2GM/R)",
        "explanation": "Escape velocity comes from equating kinetic and gravitational potential energies."
    },
    {
        "question": "Stefan–Boltzmann law relates luminosity and temperature as:",
        "choices": ["A. L ∝ T⁴", "B. L ∝ 1/T", "C. L ∝ T²", "D. L ∝ e^T"],
        "answer": "A. L ∝ T⁴",
        "explanation": "Total emitted flux increases rapidly with temperature to the fourth power."
    },
    {
        "question": "Wien’s law gives the wavelength of maximum emission as:",
        "choices": ["A. λₘₐₓT = constant", "B. λₘₐₓ/T = constant", "C. λₘₐₓ = cT", "D. λₘₐₓ = hT²"],
        "answer": "A. λₘₐₓT = constant",
        "explanation": "Hotter objects peak at shorter wavelengths (bluer colors)."
    },
    {
        "question": "If the luminosity of a star doubles but its temperature stays constant, what happens to its radius?",
        "choices": ["A. Increases by √2", "B. Doubles", "C. Halves", "D. Stays constant"],
        "answer": "A. Increases by √2",
        "explanation": "L ∝ R²T⁴ ⇒ if L doubles and T constant, R increases by √2."
    },

    # --- Space Environment & Measurement ---
    {
        "question": "One astronomical unit (AU) is approximately:",
        "choices": ["A. Average distance Earth–Sun", "B. Radius of the Sun", "C. Distance Earth–Moon", "D. Jupiter’s orbit radius"],
        "answer": "A. Average distance Earth–Sun",
        "explanation": "1 AU ≈ 1.496 × 10¹¹ meters."
    },
    {
        "question": "Which planet has the strongest magnetic field?",
        "choices": ["A. Jupiter", "B. Earth", "C. Saturn", "D. Neptune"],
        "answer": "A. Jupiter",
        "explanation": "Jupiter’s field is 20,000 times stronger than Earth’s due to its metallic hydrogen interior."
    },
    {
        "question": "Which planet rotates fastest?",
        "choices": ["A. Jupiter", "B. Earth", "C. Venus", "D. Neptune"],
        "answer": "A. Jupiter",
        "explanation": "Jupiter’s rotation period is about 10 hours—shortest in the solar system."
    },
    {
        "question": "The term 'albedo' refers to:",
        "choices": ["A. Reflectivity of a surface", "B. Density of a planet", "C. Gravitational acceleration", "D. Orbital eccentricity"],
        "answer": "A. Reflectivity of a surface",
        "explanation": "Albedo measures the fraction of incident light a body reflects."
    },
    {
        "question": "Which planet has the lowest density?",
        "choices": ["A. Saturn", "B. Mercury", "C. Earth", "D. Mars"],
        "answer": "A. Saturn",
        "explanation": "Saturn’s mean density is less than water (~0.7 g/cm³)."
    },
    {
        "question": "The greenhouse effect is strongest on which planet?",
        "choices": ["A. Venus", "B. Earth", "C. Mars", "D. Neptune"],
        "answer": "A. Venus",
        "explanation": "Thick CO₂ atmosphere traps heat efficiently."
    }
]
# -----------------------------
# SESSION STATE INIT
# -----------------------------
if "shuffled_questions" not in st.session_state:
    st.session_state.shuffled_questions = random.sample(questions, len(questions))

if "q_index" not in st.session_state:
    st.session_state.q_index = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "user_answers" not in st.session_state:
    st.session_state.user_answers = [None] * len(st.session_state.shuffled_questions)

# Shuffle choices
if "shuffled_choices" not in st.session_state:
    st.session_state.shuffled_choices = [random.sample(q["choices"], len(q["choices"])) for q in st.session_state.shuffled_questions]

# -----------------------------
# DISPLAY QUESTION
# -----------------------------
q = st.session_state.shuffled_questions[st.session_state.q_index]
choices = st.session_state.shuffled_choices[st.session_state.q_index]

st.subheader(f"Question {st.session_state.q_index + 1}: {q['question']}")

# -----------------------------
# HANDLE ANSWER SELECTION
# -----------------------------
def handle_answer(selected_choice):
    st.session_state.user_answers[st.session_state.q_index] = selected_choice
    # Update score
    if selected_choice == q["answer"]:
        st.session_state.score += 1
        st.session_state.feedback = f"✅ Correct! {q['explanation']}"
    else:
        st.session_state.feedback = f"❌ Incorrect. Correct answer: **{q['answer']}**\n\n{q['explanation']}"
    # Move to next question instantly if not last
    if st.session_state.q_index < len(st.session_state.shuffled_questions) - 1:
        st.session_state.q_index += 1
        st.session_state.feedback_next = st.session_state.feedback  # Save feedback to show after next rerun
    else:
        st.session_state.feedback_next = st.session_state.feedback

# Display choices as big buttons
col_count = 2
for i in range(0, len(choices), col_count):
    cols = st.columns(col_count)
    for j, choice in enumerate(choices[i:i+col_count]):
        if cols[j].button(choice, key=f"{st.session_state.q_index}_{choice}"):
            handle_answer(choice)
            st.experimental_rerun()  # instantly rerun to show next question

# Show feedback for previous question (if any)
if "feedback_next" in st.session_state and st.session_state.feedback_next:
    st.markdown(st.session_state.feedback_next)
    st.session_state.feedback_next = ""  # clear after showing

# -----------------------------
# PROGRESS & SCORE
# -----------------------------
st.progress((st.session_state.q_index + 1) / len(questions))
st.caption(f"Question {st.session_state.q_index + 1} of {len(questions)}")
st.metric("Current Score", f"{st.session_state.score} / {len(questions)}")