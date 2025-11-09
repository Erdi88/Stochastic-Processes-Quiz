import streamlit as st
import random

st.set_page_config(page_title="Database Systems Quiz 2025", layout="centered")

# -----------------------------
# QUESTIONS (same as before)
# -----------------------------

questions = [
    {
        "question": "What defines the habitable zone around a star?",
        "choices": ["A. The region where liquid water can exist on a planet's surface",
                    "B. The distance at which planets are tidally locked",
                    "C. The area with the highest asteroid density",
                    "D. The zone where magnetic fields are strongest"],
        "answer": "A. The region where liquid water can exist on a planet's surface",
        "explanation": "The habitable zone is the range of distances from a star where a planet can have liquid water, essential for life as we know it."
    },
    {
        "question": "What is the Drake equation used for?",
        "choices": ["A. Estimating the number of active, communicative extraterrestrial civilizations in the Milky Way",
                    "B. Calculating comet impact probabilities",
                    "C. Measuring the luminosity of a star",
                    "D. Determining the age of planets"],
        "answer": "A. Estimating the number of active, communicative extraterrestrial civilizations in the Milky Way",
        "explanation": "The Drake equation multiplies factors like star formation rate, fraction of stars with planets, and probability of life to estimate extraterrestrial civilizations."
    },
    {
        "question": "The dust rings of Uranus were discovered in 1977. How?",
        "choices": ["A. By observing stellar occultations",
                    "B. Using the Hubble Space Telescope",
                    "C. Through radio emissions",
                    "D. By flyby spacecraft imagery"],
        "answer": "A. By observing stellar occultations",
        "explanation": "Occultations occur when a planet passes in front of a star, allowing detection of rings through dips in starlight."
    },
    {
        "question": "Which two parameters does Kepler’s third law relate?",
        "choices": ["A. Orbital period and average orbital radius",
                    "B. Planet mass and orbital speed",
                    "C. Star mass and luminosity",
                    "D. Planet radius and surface gravity"],
        "answer": "A. Orbital period and average orbital radius",
        "explanation": "Kepler’s third law shows that the square of a planet's orbital period is proportional to the cube of the semi-major axis of its orbit."
    },
    {
        "question": "Mercury has a very thin atmosphere while Saturn has a thick one because Mercury's gravity is too weak to retain gases, and Saturn's stronger gravity retains a thick atmosphere. True or False?",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "Planetary gravity, temperature, and solar radiation affect atmospheric retention. Mercury is small and close to the Sun, losing most gases."
    },
    {
        "question": "How are meteor showers linked to comets?",
        "choices": ["A. Meteor showers occur when Earth passes through debris left by comets",
                    "B. Comets emit meteor showers when they leave the solar system",
                    "C. Meteor showers create new comets in the outer Solar System",
                    "D. They are unrelated phenomena"],
        "answer": "A. Meteor showers occur when Earth passes through debris left by comets",
        "explanation": "Comets leave trails of dust and particles that cause meteors when Earth crosses these orbits."
    },
    {
        "question": "What defines an Astronomical Unit (AU)?",
        "choices": ["A. Average distance from Earth to the Sun",
                    "B. Distance light travels in one year",
                    "C. Diameter of the Sun",
                    "D. Radius of Earth"],
        "answer": "A. Average distance from Earth to the Sun",
        "explanation": "1 AU is approximately 149.6 million kilometers, the average distance between Earth and Sun."
    },
    {
        "question": "How is the Lyapunov characteristic exponent used?",
        "choices": ["A. To distinguish between regular and chaotic trajectories",
                    "B. To measure planetary mass",
                    "C. To calculate orbital speed",
                    "D. To determine star luminosity"],
        "answer": "A. To distinguish between regular and chaotic trajectories",
        "explanation": "Positive Lyapunov exponents indicate chaos, while zero or negative exponents indicate regular motion."
    },
    {
        "question": "What powers the stars?",
        "choices": ["A. Nuclear fusion in their cores",
                    "B. Gravitational collapse",
                    "C. Chemical reactions",
                    "D. Rotational energy"],
        "answer": "A. Nuclear fusion in their cores",
        "explanation": "Stars fuse hydrogen into helium in their cores, releasing energy that powers them."
    },
    {
        "question": "What is runaway growth in planetary formation?",
        "choices": ["A. Rapid accretion of planetesimals forming protoplanets",
                    "B. Sudden collapse of a star",
                    "C. Increase in comet velocity near planets",
                    "D. Explosion of planetary atmospheres"],
        "answer": "A. Rapid accretion of planetesimals forming protoplanets",
        "explanation": "Runaway growth occurs when larger bodies attract more material faster, leading to faster growth than smaller bodies."
    },
    {
        "question": "As a comet approaches the Sun, its velocity can increase up to 11 times its initial velocity at infinity. The impact parameter b is the distance the comet would have passed the Sun without gravitational influence. Which statement is true about calculating b?",
        "choices": ["A. It is derived from energy and angular momentum conservation",
                    "B. It is measured directly from the comet’s tail",
                    "C. It is equal to the comet’s initial distance from the Sun",
                    "D. It depends only on the comet’s mass"],
        "answer": "A. It is derived from energy and angular momentum conservation",
        "explanation": "The impact parameter can be calculated using the conservation of energy and angular momentum for hyperbolic trajectories."
    },
    {
        "question": "When a comet’s tail gets disconnected, which tail is usually affected and why?",
        "choices": ["A. The ion (plasma) tail, because of interactions with the solar magnetic field",
                    "B. The dust tail, because of solar radiation pressure",
                    "C. Both tails, due to tidal forces",
                    "D. Neither tail is affected; it is an optical illusion"],
        "answer": "A. The ion (plasma) tail, because of interactions with the solar magnetic field",
        "explanation": "The ion tail is made of charged particles carried by the solar wind and can get disconnected when encountering magnetic disturbances."
    },
    {
        "question": "The Sun’s magnetic field at 1 AU has roughly equal radial and azimuthal components. What causes this?",
        "choices": ["A. The combination of the Sun’s rotation and solar wind stretching the field lines",
                    "B. Planetary magnetic fields balancing the solar field",
                    "C. Tidal interactions with comets",
                    "D. Sunspots creating temporary magnetic fields"],
        "answer": "A. The combination of the Sun’s rotation and solar wind stretching the field lines",
        "explanation": "The Sun’s rotation causes azimuthal twisting of magnetic field lines, while the solar wind stretches them radially."
    },
    {
        "question": "True or False: Sunspots follow an 11-year cycle, changing in number and position on the Sun’s surface.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "Sunspot numbers increase and decrease in an 11-year cycle, migrating toward the solar equator as the cycle progresses."
    },
    {
        "question": "What is the Virial Theorem and when do we use it?",
        "choices": ["A. It relates kinetic and potential energy in a gravitational system; used to determine stability of clouds",
                    "B. It predicts comet trajectories using angular momentum",
                    "C. It measures the luminosity of stars",
                    "D. It calculates orbital period of planets"],
        "answer": "A. It relates kinetic and potential energy in a gravitational system; used to determine stability of clouds",
        "explanation": "The Virial theorem states that for a stable, self-gravitating system, 2K + U = 0. It is used to determine whether clouds will collapse to form stars."
    },
    {
        "question": "The Jeans criterion determines when a cloud will collapse under gravity. Which inequality expresses it?",
        "choices": ["A. 3 M c k_B T / m < 3/5 G M^2 / R_c",
                    "B. 3 M c k_B T / m > 3/5 G M^2 / R_c",
                    "C. 2 K + U = 0",
                    "D. v_escape > v_orbital"],
        "answer": "A. 3 M c k_B T / m < 3/5 G M^2 / R_c",
        "explanation": "This inequality, derived from the Virial theorem, indicates that when gravitational energy dominates thermal energy, a cloud becomes unstable and collapses."
    },
    {
        "question": "The Jeans mass MJ gives the minimum mass for gravitational collapse. Which expression is correct?",
        "choices": ["A. MJ = (5 k_B T / G m)^(3/2) * (3 / 4πρ)^(1/2)",
                    "B. MJ = (G m / 5 k_B T)^(3/2) * (4πρ / 3)^(1/2)",
                    "C. MJ = 3 M c k_B T / m",
                    "D. MJ = R_c^3 / G M^2"],
        "answer": "A. MJ = (5 k_B T / G m)^(3/2) * (3 / 4πρ)^(1/2)",
        "explanation": "Starting from the Jeans criterion, this formula gives the critical mass at which a cloud becomes gravitationally unstable and collapses to form stars."
    },
    {
        "question": "Which phenomena are related to planetary environments: Hill sphere, Roche limit, and synchronous orbit?",
        "choices": ["A. They define regions of gravitational influence and tidal effects around a planet",
                    "B. They are used to measure a planet’s magnetic field",
                    "C. They define the atmosphere thickness",
                    "D. They describe comet trajectories"],
        "answer": "A. They define regions of gravitational influence and tidal effects around a planet",
        "explanation": "Hill sphere is the region a planet dominates gravitationally; Roche limit defines tidal disruption of moons; synchronous orbit is where orbital period equals rotation period."
    },
    {
        "question": "True or False: The Roche limit for a planet and moon with equal densities is rRoche ≤ √3/2 R.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "Using tidal acceleration and the moon's gravity, the Roche limit shows the closest distance a moon can orbit without being disrupted by planetary tides."
    },
    {
        "question": "The largest impact velocity a meteoroid can have on a planet depends on which factors?",
        "choices": ["A. The planet’s orbital radius R and the mass M of the star it orbits",
                    "B. Only the meteoroid’s composition",
                    "C. Only the planet’s mass",
                    "D. Only the Sun’s magnetic field"],
        "answer": "A. The planet’s orbital radius R and the mass M of the star it orbits",
        "explanation": "The maximum impact velocity is determined by the planet’s orbital speed around the star and the gravitational influence of the star."
    },
     {
        "question": "The formation of stars is possible in:",
        "choices": ["A. Low-temperature, high-density interstellar clouds",
                    "B. High-temperature, low-density interstellar clouds",
                    "C. Low-temperature, low-density interstellar clouds"],
        "answer": "A. Low-temperature, high-density interstellar clouds",
        "explanation": "Star formation occurs in regions with high density and low temperatures, allowing gravitational collapse."
    },
    {
        "question": "Which of the products of reactions in the interior of the Sun reaches the Earth?",
        "choices": ["A. Neutrinos",
                    "B. Atomic nuclei in the solar wind",
                    "C. Photons from the solar light"],
        "answer": "A. Neutrinos",
        "explanation": "Neutrinos escape directly from the Sun's core and reach Earth almost immediately, whereas photons take thousands of years to reach the surface."
    },
    {
        "question": "The Giant planets grew in the protoplanetary disk by:",
        "choices": ["A. Collecting smaller planets",
                    "B. Accumulation of planetesimals, dust, and gas",
                    "C. Gravitational collapse"],
        "answer": "B. Accumulation of planetesimals, dust, and gas",
        "explanation": "Giant planets formed by accreting gas and solid material from the protoplanetary disk, gradually growing larger than terrestrial planets."
    },
    {
        "question": "The rings of Neptune were discovered in 1984:",
        "choices": ["A. With camera observations from the Voyager 2 spacecraft",
                    "B. With stellar occultation observations",
                    "C. With ground-based telescope observations"],
        "answer": "B. With stellar occultation observations",
        "explanation": "Stellar occultations allow detection of faint rings when the planet passes in front of a star, revealing rings by dips in starlight."
    },
    {
        "question": "The first exoplanet around a main sequence star was discovered by:",
        "choices": ["A. Its thermal emission brightness",
                    "B. The Doppler shift in the spectrum of its host star",
                    "C. Its transit reducing the brightness of the host star"],
        "answer": "B. The Doppler shift in the spectrum of its host star",
        "explanation": "The radial velocity method detects the tiny wobble in a star’s motion caused by the gravitational pull of an orbiting planet."
    },
    {
        "question": "What is the main process of heat transfer from the Sun to the planets?",
        "choices": ["A. Diffusion",
                    "B. Convection",
                    "C. Radiation"],
        "answer": "C. Radiation",
        "explanation": "Energy from the Sun is transmitted through space primarily as electromagnetic radiation (light), not by conduction or convection."
    },
    {
        "question": "Several different observations of the Sun are made to monitor the progress of its 11-year cycle. Which of the listed parameters is NOT typically used to monitor the solar cycle?",
        "choices": ["A. Sunspot number",
                    "B. Solar flux at radio wavelength",
                    "C. Solar neutrino flux"],
        "answer": "C. Solar neutrino flux",
        "explanation": "Sunspot numbers and solar flux are used to track the solar cycle, while solar neutrino flux remains roughly constant."
    },
    {
        "question": "In comparison to Earth’s orbit, the intensity of sunlight at the orbit of Jupiter is reduced by approximately:",
        "choices": ["A. 1/5",
                    "B. 1/25",
                    "C. 1/125"],
        "answer": "C. 1/25",
        "explanation": "Solar intensity decreases with the square of the distance from the Sun. Jupiter is ~5 AU from the Sun, so intensity is 1/25 that at Earth."
    },
    {
        "question": "Short-period comets are observed when they approach the inner solar system from the:",
        "choices": ["A. Kuiper belt",
                    "B. Planetary nebula",
                    "C. Molecular cloud"],
        "answer": "A. Kuiper belt",
        "explanation": "Short-period comets originate from the Kuiper belt beyond Neptune and have orbital periods less than 200 years."
    },
    {
        "question": "Which of the following parameters most affected the bulk density of solar system planets at present?",
        "choices": ["A. Element compositions in the protoplanetary disk",
                    "B. Condensation temperatures in the protoplanetary disk",
                    "C. Self-gravity of the planets"],
        "answer": "A. Element compositions in the protoplanetary disk",
        "explanation": "Planetary bulk density primarily depends on the mix of rock, metal, and ices in the material from which planets formed."
    },
    {
        "question": "With few exceptions, the planets and other solar system objects orbit the Sun in the same direction. What concept of classical physics explains this observation?",
        "choices": ["A. Conservation of energy",
                    "B. Conservation of angular momentum",
                    "C. Kepler’s laws"],
        "answer": "B. Conservation of angular momentum",
        "explanation": "The protoplanetary disk’s initial rotation led to most objects conserving angular momentum, orbiting the Sun in the same direction."
    },
    {
        "question": "When comparing solar element abundance and element abundance of a primitive meteorite, what is the main difference?",
        "choices": ["A. The meteorite contains amino acids",
                    "B. The meteorite contains less He because the Sun is enriched in He",
                    "C. The meteorite contains smaller amounts of the volatile elements"],
        "answer": "C. The meteorite contains smaller amounts of the volatile elements",
        "explanation": "Meteorites generally lack volatile elements that escaped from the protoplanetary disk, whereas the Sun retains them."
    },
    {
        "question": "The moons of the solar system planets are typically located:",
        "choices": ["A. Inside the Roche limit of the planet",
                    "B. Inside the Hill sphere of the planet",
                    "C. Inside the Jeans radius"],
        "answer": "B. Inside the Hill sphere of the planet",
        "explanation": "The Hill sphere defines the region around a planet where its gravity dominates over the Sun, allowing moons to orbit stably."
    },
    {
        "question": "Asteroid families describe asteroids with:",
        "choices": ["A. Similar composition",
                    "B. Similar orbital parameters, inclination and semi-major axis",
                    "C. Similar size and bulk density"],
        "answer": "B. Similar orbital parameters, inclination and semi-major axis",
        "explanation": "Asteroid families are groups of asteroids sharing similar orbital elements, indicating a common origin from a parent body."
    },
    {
        "question": "True or False: Despite sunspots being cooler and darker, Earth’s atmosphere can be slightly warmer during solar maximum than solar minimum.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "Increased solar activity during maximum enhances solar irradiance and UV radiation, slightly warming Earth's upper atmosphere despite darker sunspots."
    },
    {
        "question": "The thermal velocity of particles in the solar wind depends primarily on:",
        "choices": ["A. Temperature of the solar wind",
                    "B. Distance from the Sun",
                    "C. Magnetic field strength",
                    "D. Planetary composition"],
        "answer": "A. Temperature of the solar wind",
        "explanation": "Thermal velocity of protons and electrons is determined by the kinetic temperature of the plasma, independent of bulk flow velocity."
    },
    {
        "question": "True or False: The Hill sphere defines the region around a planet where its gravity dominates over the Sun’s.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "Within the Hill sphere, satellites can orbit a planet stably without being pulled away by the Sun."
    },
    {
        "question": "Which assumption is made to derive the hydrostatic equilibrium equation for planetary atmospheres?",
        "choices": ["A. The atmosphere is in steady-state and velocity terms are negligible",
                    "B. The atmosphere is fully convective",
                    "C. The atmosphere rotates as a solid body",
                    "D. The Sun’s magnetic field is constant"],
        "answer": "A. The atmosphere is in steady-state and velocity terms are negligible",
        "explanation": "Hydrostatic equilibrium assumes pressure gradients balance gravity, neglecting large-scale flows or accelerations."
    },
    {
        "question": "The scale height H in a planetary atmosphere is physically interpreted as:",
        "choices": ["A. The height over which pressure drops by a factor of e",
                    "B. The total height of the atmosphere",
                    "C. The distance to the ionosphere",
                    "D. The maximum altitude for clouds"],
        "answer": "A. The height over which pressure drops by a factor of e",
        "explanation": "Scale height H = k_B T / (mg) represents the characteristic height over which atmospheric pressure decreases exponentially."
    },
    {
        "question": "True or False: Comets and Kuiper belt objects share similar compositions, being mostly ices and dust, but comets develop tails when approaching the Sun.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "Kuiper belt objects and comets are both icy bodies, but comets show activity like tails when solar radiation sublimates their ices near the Sun."
    },
    {
        "question": "Which component of a comet is directly influenced by the solar wind?",
        "choices": ["A. Ion (plasma) tail",
                    "B. Dust tail",
                    "C. Nucleus",
                    "D. Coma"],
        "answer": "A. Ion (plasma) tail",
        "explanation": "The ion tail is formed from charged particles carried by the solar wind and always points away from the Sun."
    },
    {
        "question": "True or False: The Sun’s 11-year cycle affects solar wind speed and coronal structure.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "During solar maximum and minimum, sunspot numbers and coronal magnetic structures change, influencing solar wind patterns."
    },
     {
        "question": "Star formation typically begins with:",
        "choices": ["A. Jeans instability in a molecular cloud",
                    "B. Collision of two exoplanets",
                    "C. Encounter of two interstellar clouds"],
        "answer": "A. Jeans instability in a molecular cloud",
        "explanation": "Gravitational collapse due to Jeans instability in dense molecular clouds initiates star formation."
    },
    {
        "question": "Which small object in the solar system is typically the most massive?",
        "choices": ["A. Dwarf planet",
                    "B. Comet nucleus",
                    "C. Asteroid"],
        "answer": "A. Dwarf planet",
        "explanation": "Dwarf planets are generally larger and more massive than comets or typical asteroids."
    },
    {
        "question": "Primary and secondary planetary atmospheres differ mainly in:",
        "choices": ["A. How they are acquired: primary from nebula gas, secondary from outgassing or impacts",
                    "B. Their magnetic field strength",
                    "C. Their orbital period around the Sun",
                    "D. Whether they contain water"],
        "answer": "A. How they are acquired: primary from nebula gas, secondary from outgassing or impacts",
        "explanation": "Primary atmospheres are captured from the protoplanetary disk, while secondary atmospheres are generated by volcanic outgassing or impacts."
    },
    {
        "question": "Hot Jupiters are:",
        "choices": ["A. Gas giant exoplanets very close to their stars with high temperatures",
                    "B. Gas giants in the Kuiper belt",
                    "C. Young stars forming planets",
                    "D. Comets with unusually large masses"],
        "answer": "A. Gas giant exoplanets very close to their stars with high temperatures",
        "explanation": "Hot Jupiters orbit very close to their stars, causing high surface temperatures due to intense stellar irradiation."
    },
    {
        "question": "Most stars observed in the Milky Way are main sequence stars because:",
        "choices": ["A. These are all brighter than other stars in the Milky Way",
                    "B. These are in the vicinity of the solar system",
                    "C. All stars spend a long time as main sequence stars"],
        "answer": "C. All stars spend a long time as main sequence stars",
        "explanation": "Stars spend the majority of their lifetimes fusing hydrogen into helium on the main sequence, making them the most commonly observed stars."
    },
    {
        "question": "Light emitted from the Sun reaches Earth within about 8 minutes. The solar wind emitted at the same time reaches Earth:",
        "choices": ["A. At the same time",
                    "B. Earlier",
                    "C. Later"],
        "answer": "C. Later",
        "explanation": "Solar wind particles travel much slower than light and typically take 2–4 days to reach Earth, depending on their speed."
    },
    {
        "question": "The blackbody temperature of the Earth’s Moon is:",
        "choices": ["A. Significantly higher because the Moon is exposed to the solar wind",
                    "B. Significantly lower because the Moon’s radius is less than 1/3 of the Earth’s radius",
                    "C. The same because both are at the same distance from the Sun"],
        "answer": "C. The same because both are at the same distance from the Sun",
        "explanation": "Blackbody temperature depends primarily on distance from the Sun and albedo, not on the size of the body."
    },
    {
        "question": "The blackbody temperature of Venus is:",
        "choices": ["A. Higher than that of the Earth",
                    "B. Lower than that of the Earth",
                    "C. About the same because both planets have similar size"],
        "answer": "A. Higher than that of the Earth",
        "explanation": "Venus has a strong greenhouse effect due to its thick CO₂ atmosphere, raising its surface temperature above Earth’s."
    },
    {
        "question": "The solar system comets contain dust and ice because:",
        "choices": ["A. They are fragments of the outer icy planets",
                    "B. They formed outside of the ice line in the protoplanetary cloud",
                    "C. They formed in the cold interstellar medium"],
        "answer": "B. They formed outside of the ice line in the protoplanetary cloud",
        "explanation": "Comets formed beyond the ice line where temperatures were low enough for volatile ices to condense along with dust."
    },
    {
        "question": "Most of the solar wind particles that reach Earth are:",
        "choices": ["A. Absorbed in the Earth’s atmosphere",
                    "B. Deflected by the Earth’s magnetic field",
                    "C. Reach the surface of the Earth without interaction"],
        "answer": "B. Deflected by the Earth’s magnetic field",
        "explanation": "Earth’s magnetosphere protects the surface by deflecting most solar wind particles."
    },
    {
        "question": "Which objects are located in the Sun–Earth Lagrange points?",
        "choices": ["A. The Jupiter trojans",
                    "B. ESA’s Solar Heliospheric Observatory (SOHO) spacecraft",
                    "C. The Mars trojans"],
        "answer": "B. ESA’s Solar Heliospheric Observatory (SOHO) spacecraft",
        "explanation": "SOHO is positioned at the Sun–Earth L1 Lagrange point, where gravitational forces allow it to remain in a stable position relative to Earth and the Sun."
    },
     {
        "question": "What is the origin of the name Allende given to the meteorite found in 1969?",
        "choices": ["A. The name was chosen because of the writer with the same name",
                    "B. It was found in northern Mexico, near the village of Pueblito de Allende",
                    "C. It is by convention named after the person who discovered it in Northern Mexico"],
        "answer": "B. It was found in northern Mexico, near the village of Pueblito de Allende",
        "explanation": "Meteorites are commonly named after the location where they were found."
    },
    {
        "question": "Which of these objects is observed in the solar system?",
        "choices": ["A. Exoplanets",
                    "B. Brown dwarfs",
                    "C. Dwarf planets"],
        "answer": "C. Dwarf planets",
        "explanation": "Dwarf planets, such as Pluto, are observed in the solar system, while exoplanets are outside the solar system and brown dwarfs are sub-stellar objects."
    },
    {
        "question": "What is the approximate temperature in the interior of the Sun?",
        "choices": ["A. 10^5 – 10^6 K",
                    "B. 6000 K",
                    "C. 15 × 10^6 K"],
        "answer": "C. 15 × 10^6 K",
        "explanation": "The core of the Sun reaches temperatures of about 15 million Kelvin, where nuclear fusion occurs."
    },
    {
        "question": "Pluto is not classified as a planet anymore because:",
        "choices": ["A. It turned out its shape is not spherical",
                    "B. It turned out it does not have an atmosphere",
                    "C. It does not clear its orbital region from other objects"],
        "answer": "C. It does not clear its orbital region from other objects",
        "explanation": "The IAU redefined planets in 2006; Pluto is classified as a dwarf planet because it shares its orbit with other objects in the Kuiper belt."
    },
    {
        "question": "Several different observations of the Sun are made to monitor the progress of its 11-year cycle; which parameter is NOT typically used?",
        "choices": ["A. Sunspot number",
                    "B. Solar flux at radio wavelength",
                    "C. Solar neutrino flux"],
        "answer": "C. Solar neutrino flux",
        "explanation": "Sunspot numbers and solar radio flux are used to track the solar cycle; solar neutrino flux remains roughly constant."
    },
     {
        "question": "Which step is part of the currently accepted formation of the solar system?",
        "choices": [
            "A. Collapse of a molecular cloud into a rotating disk",
            "B. Instant creation of planets from interstellar dust",
            "C. Planets forming before the Sun",
            "D. Stars forming from planetary collisions"
        ],
        "answer": "A. Collapse of a molecular cloud into a rotating disk",
        "explanation": "The solar system formed from a collapsing molecular cloud that flattened into a rotating protoplanetary disk, where planets eventually accreted."
    },
    {
        "question": "What does it mean for a celestial body to be tidally locked?",
        "choices": [
            "A. Its rotational period equals its orbital period around another body",
            "B. Its orbit is highly eccentric",
            "C. It has no atmosphere",
            "D. It always orbits in the equatorial plane"
        ],
        "answer": "A. Its rotational period equals its orbital period around another body",
        "explanation": "Tidal locking occurs when a body's rotation period matches its orbital period, causing the same face to always point toward its partner (like the Moon and Earth)."
    },
    {
        "question": "Which factor primarily shapes the Earth’s magnetosphere?",
        "choices": [
            "A. Interaction of solar wind with Earth's magnetic field",
            "B. Earth’s orbital speed around the Sun",
            "C. The Moon’s gravitational pull",
            "D. Earth's atmosphere density"
        ],
        "answer": "A. Interaction of solar wind with Earth's magnetic field",
        "explanation": "The solar wind compresses the magnetosphere on the day side and stretches it into a long tail on the night side, producing the characteristic shape."
    },
    {
        "question": "Why does Earth’s average surface temperature differ from its blackbody temperature?",
        "choices": [
            "A. Due to atmospheric greenhouse effects and albedo",
            "B. Because Earth is closer to the Sun than calculated",
            "C. The Moon reflects sunlight onto Earth",
            "D. Solar wind increases surface temperature directly"
        ],
        "answer": "A. Due to atmospheric greenhouse effects and albedo",
        "explanation": "The blackbody calculation ignores greenhouse gases and surface reflectivity, which trap heat and modify the temperature."
    },
    {
        "question": "The Hill radius of a planet defines:",
        "choices": [
            "A. The region where the planet’s gravity dominates over the star’s gravity",
            "B. The maximum radius of the planet",
            "C. The Roche limit of the planet",
            "D. The orbital speed of moons"
        ],
        "answer": "A. The region where the planet’s gravity dominates over the star’s gravity",
        "explanation": "The Hill sphere is the region around a planet within which satellites can orbit without being pulled away by the star."
    },
    {
        "question": "The Roche limit determines:",
        "choices": [
            "A. The closest distance a moon can orbit a planet without being tidally disrupted",
            "B. The farthest stable orbit of a planet",
            "C. The distance at which tides stop affecting a moon",
            "D. The size limit of asteroids"
        ],
        "answer": "A. The closest distance a moon can orbit a planet without being tidally disrupted",
        "explanation": "Within the Roche limit, tidal forces exceed the self-gravity of a satellite, potentially breaking it apart."
    },
    {
        "question": "In a gravitational potential, a particle with total energy E greater than zero will:",
        "choices": [
            "A. Escape to infinity on a hyperbolic trajectory",
            "B. Remain in a stable circular orbit",
            "C. Oscillate between two radii indefinitely",
            "D. Fall directly into the central mass"
        ],
        "answer": "A. Escape to infinity on a hyperbolic trajectory",
        "explanation": "If the total energy is positive, the particle is unbound and follows an open (hyperbolic or parabolic) trajectory away from the central mass."
    },
    {
    "question": "Which of the following statements about meteors, meteorites, and craters is correct?",
    "choices": [
        "A. Earth has meteors, meteorites, and craters",
        "B. Moon has meteors but no meteorites",
        "C. Mars has no craters",
        "D. Meteors occur only on Earth"
    ],
    "answer": "A. Earth has meteors, meteorites, and craters",
    "explanation": "Earth's atmosphere burns up many meteoroids (meteors) but some reach the surface (meteorites). Craters exist on all rocky bodies but are more visible on bodies without erosion."
    },
    {
    "question": "What is a key difference between the b Pictoris debris disk and the solar system's interplanetary dust cloud?",
    "choices": [
        "A. The b Pictoris disk is much more extended",
        "B. The solar system has no dust",
        "C. Both are composed entirely of gas",
        "D. Only b Pictoris contains planets"
    ],
    "answer": "A. The b Pictoris disk is much more extended",
    "explanation": "The b Pictoris debris disk spans ~1500 AU, far larger than the solar system's zodiacal dust cloud, but both contain small dust particles orbiting their central star."
    },
    {
    "question": "What do the b Pictoris debris disk and the solar system's dust cloud have in common?",
    "choices": [
        "A. Both contain dust particles orbiting a star",
        "B. Both are remnants of planetary collisions only",
        "C. Both contain no planets",
        "D. Both are fully gaseous"
    ],
    "answer": "A. Both contain dust particles orbiting a star",
    "explanation": "Despite differences in size and structure, both consist of small dust particles orbiting their respective stars."
    },
    {
    "question": "How was the first exoplanet around a main-sequence star detected?",
    "choices": [
        "A. By direct imaging",
        "B. By the Doppler shift of the star's spectrum",
        "C. By measuring star spots",
        "D. By the planet's thermal radiation"
    ],
    "answer": "B. By the Doppler shift of the star's spectrum",
    "explanation": "The radial velocity (Doppler) method detects a star's motion due to the gravitational pull of orbiting planets; Kepler’s laws alone cannot detect exoplanets."
    },
    {
    "question": "An asteroid has a semi-major axis of 3.1 AU and eccentricity 0.60. Its perihelion distance is closest to:",
    "choices": [
        "A. 1.24 AU",
        "B. 2.0 AU",
        "C. 3.1 AU",
        "D. 4.96 AU"
    ],
    "answer": "A. 1.24 AU",
    "explanation": "Perihelion = a(1-e) = 3.1*(1-0.6) ≈ 1.24 AU. Aphelion = a(1+e) ≈ 4.96 AU."
    }, 
    {
    "question": "Which solar system body has an ionosphere and why?",
    "choices": [
        "A. Earth, because solar radiation ionizes the upper atmosphere",
        "B. Moon, because it has strong volcanic activity",
        "C. Mars, because it has no atmosphere",
        "D. Mercury, because it has a thick atmosphere"
    ],
    "answer": "A. Earth, because solar radiation ionizes the upper atmosphere",
    "explanation": "An ionosphere forms where solar UV and X-rays ionize atmospheric particles. The Moon has no atmosphere, and Mercury and Mars have very thin atmospheres."
    },
    {
        "question": "If asked to derive the blackbody temperature of a planet, which steps would you take?",
        "choices": [
            "A. Use the Stefan-Boltzmann law, set absorbed solar power equal to emitted thermal power",
            "B. Measure the planet with a thermometer",
            "C. Assume the planet has the same temperature as the Sun",
            "D. Use Kepler's third law directly"
        ],
        "answer": "A. Use the Stefan-Boltzmann law, set absorbed solar power equal to emitted thermal power",
        "explanation": "The blackbody temperature comes from energy balance between incoming solar radiation and thermal emission."
    },
    {
        "question": "When calculating the Roche limit for a planet and satellite, what is your general approach?",
        "choices": [
            "A. Compare tidal forces to the satellite's self-gravity",
            "B. Measure the planet’s temperature",
            "C. Calculate orbital period only",
            "D. Determine the planet's escape velocity"
        ],
        "answer": "A. Compare tidal forces to the satellite's self-gravity",
        "explanation": "The Roche limit is derived by balancing tidal forces trying to pull apart a satellite with its internal gravitational cohesion."
    },
    {
        "question": "How would you estimate the Hill radius of a planet?",
        "choices": [
            "A. Use the formula r_Hill = R * (m/(3M))^(1/3) where m is planet mass, M is star mass, R is orbital distance",
            "B. Measure the size of the planet’s rings",
            "C. Measure the planet’s rotation period",
            "D. Estimate from the planet’s density"
        ],
        "answer": "A. Use the formula r_Hill = R * (m/(3M))^(1/3) where m is planet mass, M is star mass, R is orbital distance",
        "explanation": "The Hill radius defines the region where a planet’s gravity dominates over its star, allowing stable satellite orbits."
    },
    {
        "question": "To calculate the perihelion and aphelion of an asteroid orbit, which quantities do you need?",
        "choices": [
            "A. Semi-major axis and eccentricity",
            "B. Planet mass only",
            "C. Radius of the asteroid",
            "D. The asteroid’s albedo"
        ],
        "answer": "A. Semi-major axis and eccentricity",
        "explanation": "Perihelion = a(1-e) and aphelion = a(1+e). These are derived directly from orbital parameters."
    },
    {
        "question": "When asked to estimate the solar wind speed required to compress Mercury’s magnetosphere, which physical principles would you use?",
        "choices": [
            "A. Equate solar wind dynamic pressure to magnetic pressure",
            "B. Use Kepler’s laws",
            "C. Use the planet’s temperature only",
            "D. Measure solar flares visually"
        ],
        "answer": "A. Equate solar wind dynamic pressure to magnetic pressure",
        "explanation": "The solar wind compresses the magnetosphere where dynamic pressure equals magnetic pressure from the planetary field."
    },
    {
        "question": "If you were asked to estimate the temperature of an exoplanet in radiation balance, what steps would you take?",
        "choices": [
            "A. Use the star's luminosity, distance from the planet, albedo, and Stefan-Boltzmann law",
            "B. Assume it has the same temperature as Earth",
            "C. Measure with a telescope directly",
            "D. Estimate from the planet’s mass alone"
        ],
        "answer": "A. Use the star's luminosity, distance from the planet, albedo, and Stefan-Boltzmann law",
        "explanation": "The equilibrium temperature comes from the absorbed stellar radiation balanced by thermal emission of the planet."
    },
    {
        "question": "How would you calculate the Hohmann transfer time from Earth to Mars?",
        "choices": [
            "A. Use orbital mechanics formulas for the semi-major axis of the transfer ellipse and Kepler’s third law",
            "B. Measure the distance with a ruler",
            "C. Estimate based on solar wind",
            "D. Use the planet’s mass only"
        ],
        "answer": "A. Use orbital mechanics formulas for the semi-major axis of the transfer ellipse and Kepler’s third law",
        "explanation": "The Hohmann transfer time is half the orbital period of the elliptical orbit connecting Earth and Mars."
    },
    {
        "question": "To determine whether a meteoroid will reach Mars, what approach would you use?",
        "choices": [
            "A. Analyze the meteoroid’s orbit relative to Mars and its velocity at intersection",
            "B. Measure Mars’ surface temperature",
            "C. Use the Sun’s blackbody radiation",
            "D. Check if Mars has moons"
        ],
        "answer": "A. Analyze the meteoroid’s orbit relative to Mars and its velocity at intersection",
        "explanation": "You need to know the meteoroid's orbit and relative velocity to determine if it will collide with Mars."
    },
    {
        "question": "How would you approach deriving the effective potential for a particle orbiting a mass M?",
        "choices": [
            "A. Combine the gravitational potential energy with the centrifugal potential term from angular momentum",
            "B. Use only the gravitational potential",
            "C. Measure the particle’s velocity with a telescope",
            "D. Use Kepler’s third law alone"
        ],
        "answer": "A. Combine the gravitational potential energy with the centrifugal potential term from angular momentum",
        "explanation": "The effective potential includes the radial gravitational potential plus the angular momentum term L²/(2mr²)."
    },
    {
        "question": "If asked to calculate the temperature difference between Earth’s blackbody temperature and actual average temperature, what would you do?",
        "choices": [
            "A. Consider the greenhouse effect, atmospheric composition, and albedo",
            "B. Assume both are equal",
            "C. Use only the solar constant",
            "D. Use the Moon’s temperature as a reference"
        ],
        "answer": "A. Consider the greenhouse effect, atmospheric composition, and albedo",
        "explanation": "Earth’s actual temperature is higher than its simple blackbody temperature due to greenhouse gases and reflective properties."
    },
    {
        "question": "How would you determine the distance range for stable moons around an exoplanet?",
        "choices": [
            "A. Use the Hill radius and the planet’s mass and orbital distance",
            "B. Measure the planet’s brightness",
            "C. Use Kepler’s first law alone",
            "D. Estimate from the star’s temperature"
        ],
        "answer": "A. Use the Hill radius and the planet’s mass and orbital distance",
        "explanation": "The Hill radius gives the region around a planet where moons can have stable orbits without being pulled away by the star."
    },
    {
        "question": "To estimate the temperature of a planet assuming it is a blackbody, which factors do you need?",
        "choices": [
            "A. Star luminosity, orbital distance, planetary albedo",
            "B. Only the planet’s radius",
            "C. Only the planet’s mass",
            "D. Only the orbital eccentricity"
        ],
        "answer": "A. Star luminosity, orbital distance, planetary albedo",
        "explanation": "The equilibrium temperature comes from balancing absorbed stellar radiation and emitted thermal radiation."
    },
    {
        "question": "How would you estimate the velocity of meteors on Mars from bound orbit meteoroids?",
        "choices": [
            "A. Use energy conservation between orbiting meteoroid and Mars gravitational potential",
            "B. Assume they all have the same velocity as Earth meteors",
            "C. Measure the meteors with a camera directly",
            "D. Use Mars surface temperature"
        ],
        "answer": "A. Use energy conservation between orbiting meteoroid and Mars gravitational potential",
        "explanation": "The velocity is determined by the gravitational potential of Mars and the initial orbital energy of the meteoroid."
    },
    {
        "question": "When tasked with explaining why a body is tidally locked, what reasoning would you use?",
        "choices": [
            "A. Discuss gravitational torque and energy dissipation over time leading to synchronous rotation",
            "B. Assume the body rotates freely",
            "C. Compare it to the Sun’s rotation",
            "D. Use Kepler’s third law only"
        ],
        "answer": "A. Discuss gravitational torque and energy dissipation over time leading to synchronous rotation",
        "explanation": "Tidal forces cause a body to gradually synchronize its rotation period with its orbital period."
    },
    {
        "question": "If asked to sketch the Earth’s magnetosphere and explain its shape, what would your approach be?",
        "choices": [
            "A. Draw a compressed sunward side and elongated tail, and explain with solar wind pressure and Earth's magnetic field",
            "B. Draw a perfect sphere without explanation",
            "C. Use the Moon’s magnetosphere as reference",
            "D. Explain using only gravity"
        ],
        "answer": "A. Draw a compressed sunward side and elongated tail, and explain with solar wind pressure and Earth's magnetic field",
        "explanation": "The shape arises from the balance between the solar wind dynamic pressure and the Earth’s magnetic pressure."
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
