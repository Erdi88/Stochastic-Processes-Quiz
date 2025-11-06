import streamlit as st
import random

st.set_page_config(page_title="Space Quiz 2025", layout="centered")

# -----------------------------
# QUESTIONS (same as before)
# -----------------------------

# FYS-2019 Sun, Planets and Space - Phone-Friendly Quiz Database

quiz_questions = [
    # Star Formation
    {
        "question": "Stars form in which type of interstellar clouds?",
        "options": ["A: Low-temperature, high-density", "B: High-temperature, low-density", "C: Low-temperature, low-density"],
        "answer": "A",
        "explanation": "Star formation requires clouds that are cold enough to collapse and dense enough for gravity to dominate."
    },
    {
        "question": "The first step in star formation is called:",
        "options": ["A: Jeans instability", "B: Collision of two exoplanets", "C: Encounter of two interstellar clouds"],
        "answer": "A",
        "explanation": "Jeans instability occurs when a gas cloud becomes gravitationally unstable and begins to collapse."
    },
    {
        "question": "Most stars in the Milky Way are main-sequence stars because:",
        "options": ["A: They are all brighter than other stars", "B: They are in the vicinity of the solar system", "C: All stars spend most of their lifetime in the main sequence phase"],
        "answer": "C",
        "explanation": "Stars spend the majority of their life fusing hydrogen in the main sequence stage."
    },
    {
        "question": "The typical temperature in the Sun’s core is roughly:",
        "options": ["A: 10^5–10^6 K", "B: 6000 K", "C: 15×10^6 K"],
        "answer": "C",
        "explanation": "The core temperature of the Sun is around 15 million K, sufficient for nuclear fusion."
    },
    {
        "question": "The main energy source in the Sun’s interior is:",
        "options": ["A: Thermal fusion", "B: Neutron capture", "C: Radioactive decay"],
        "answer": "A",
        "explanation": "Fusion of hydrogen into helium in the Sun’s core is the primary energy source."
    },
    {
        "question": "Which reaction product from the Sun reaches Earth almost immediately?",
        "options": ["A: Neutrinos", "B: Atomic nuclei in the solar wind", "C: Photons from sunlight"],
        "answer": "A",
        "explanation": "Neutrinos escape the Sun’s interior almost immediately due to their weak interaction with matter."
    },
    {
        "question": "The luminosity of a star is determined by which two parameters?",
        "options": ["A: Mass and age", "B: Radius and surface temperature", "C: Distance and apparent brightness"],
        "answer": "B",
        "explanation": "Luminosity L = 4πR^2σT^4 depends on the star’s radius and surface temperature."
    },
    {
        "question": "Which physical concept explains why planets orbit in the same direction?",
        "options": ["A: Conservation of energy", "B: Conservation of angular momentum", "C: Kepler's laws"],
        "answer": "B",
        "explanation": "Angular momentum conservation of the rotating protoplanetary disk results in aligned orbital directions."
    },

    # Planets, Moons, Solar System
    {
        "question": "Which planets are terrestrial and which are gas giants?",
        "options": ["A: Mercury, Venus, Earth, Mars = terrestrial; Jupiter, Saturn, Uranus, Neptune = gas giants",
                    "B: Mercury, Venus, Earth = terrestrial; Mars, Jupiter, Saturn, Uranus, Neptune = gas giants",
                    "C: All planets are gas giants"],
        "answer": "A",
        "explanation": "Terrestrial planets are small, rocky, and dense; gas giants are large and mostly gaseous."
    },
    {
        "question": "Why is Mercury’s atmosphere so thin compared to Venus?",
        "options": ["A: It is too small to hold a thick atmosphere", "B: It is too far from the Sun", "C: Its surface is icy"],
        "answer": "A",
        "explanation": "Mercury’s low gravity and proximity to the Sun cause atmospheric particles to escape easily."
    },
    {
        "question": "What defines a planet’s Hill sphere conceptually?",
        "options": ["A: Region where tidal forces break satellites", "B: Region where the planet dominates satellite attraction", "C: Region where atmosphere can exist"],
        "answer": "B",
        "explanation": "The Hill sphere is the zone where the planet’s gravity dominates over the Sun’s for satellites."
    },
    {
        "question": "How is the Hill radius roughly calculated?",
        "options": ["A: r_Hill = (m/M)^(1/3) * R", "B: r_Hill = sqrt(m*M)/R", "C: r_Hill = m*R^2/M"],
        "answer": "A",
        "explanation": "r_Hill = (m/M)^(1/3) * R where m is planet mass, M is Sun mass, R is planet-Sun distance."
    },
    {
        "question": "What is the Roche limit, and why is it important?",
        "options": ["A: Minimum orbital distance before satellite is tidally disrupted",
                    "B: Maximum orbit where planet retains atmosphere",
                    "C: Distance where satellite escapes to Sun"],
        "answer": "A",
        "explanation": "Inside the Roche limit, tidal forces exceed satellite’s self-gravity, breaking it apart."
    },
    {
        "question": "If a moon is inside the Roche limit, what happens?",
        "options": ["A: It becomes a comet", "B: It disintegrates due to tidal forces", "C: It stays in stable orbit"],
        "answer": "B",
        "explanation": "Tidal forces exceed gravitational cohesion, causing disintegration."
    },
    {
        "question": "Explain the difference between a meteor, meteoroid, and meteorite.",
        "options": ["A: Meteoroid=space, Meteor=atmosphere, Meteorite=ground", "B: Meteor=Moon, Meteoroid=Earth, Meteorite=Sun", "C: All same"],
        "answer": "A",
        "explanation": "Meteoroid travels in space, meteor is the visible streak in atmosphere, meteorite hits ground."
    },
    {
        "question": "Which small solar system object is most massive?",
        "options": ["A: Dwarf planet", "B: Comet", "C: Asteroid"],
        "answer": "A",
        "explanation": "Dwarf planets are generally more massive than comets or asteroids."
    },
    {
        "question": "How are comet orbits classified as short-period or long-period?",
        "options": ["A: By size of comet nucleus", "B: By orbital period", "C: By composition"],
        "answer": "B",
        "explanation": "Short-period comets have orbital periods <200 years, long-period >200 years."
    },
    {
        "question": "Where do long-period comets come from? Where do short-period comets come from?",
        "options": ["A: Long=Oort cloud, Short=Kuiper belt", "B: Long=Kuiper belt, Short=Oort cloud", "C: Both from asteroid belt"],
        "answer": "A",
        "explanation": "Long-period comets originate in distant Oort cloud, short-period in Kuiper belt."
    },

    # Orbits and Space Mechanics
    {
        "question": "Conceptually, what is a Hohmann transfer orbit?",
        "options": ["A: Elliptical orbit connecting two circular orbits", "B: Circular orbit around Sun", "C: Parabolic orbit out of solar system"],
        "answer": "A",
        "explanation": "Hohmann transfer uses an ellipse tangent to both starting and target orbits."
    },
    {
        "question": "How would you calculate the transfer time to Mars in a Hohmann orbit?",
        "options": ["A: Half the orbital period of the transfer ellipse", "B: Equal to Earth orbital period", "C: Twice the orbital period of Mars"],
        "answer": "A",
        "explanation": "Time = 0.5 × period of the elliptical transfer orbit."
    },
    {
        "question": "What does the vis-viva equation describe?",
        "options": ["A: Orbital velocity at distance r", "B: Gravitational potential energy", "C: Tidal forces on planets"],
        "answer": "A",
        "explanation": "v^2 = GM(2/r - 1/a) gives orbital velocity at any point of an orbit."
    },
    {
        "question": "How can you mentally check the vis-viva equation for a circular orbit?",
        "options": ["A: Set r = a, then v = sqrt(GM/r)", "B: Set r = 0", "C: Set v = 0"],
        "answer": "A",
        "explanation": "In circular orbit, radius = semimajor axis, and vis-viva reduces to circular velocity."
    },
    {
        "question": "Conceptually, how would you find perihelion and aphelion speeds using vis-viva?",
        "options": ["A: Use r = perihelion/aphelion distances in vis-viva", "B: Use r = 0", "C: Use average orbital speed only"],
        "answer": "A",
        "explanation": "Plug perihelion/aphelion distances into vis-viva equation to get respective velocities."
    },
    {
        "question": "What is a geostationary satellite, and what determines its orbital altitude?",
        "options": ["A: Satellite fixed above equator; altitude determined by orbital period = Earth rotation", 
                    "B: Satellite moving over poles; altitude random", 
                    "C: Satellite orbiting Moon"],
        "answer": "A",
        "explanation": "Geostationary satellites orbit above equator with period matching Earth's rotation."
    },
    {
        "question": "Explain what the effective potential is in orbital motion.",
        "options": ["A: Total energy including centrifugal term", "B: Gravitational potential only", "C: Kinetic energy only"],
        "answer": "A",
        "explanation": "Effective potential combines gravitational potential and centrifugal potential for radial motion."
    },
    {
        "question": "How does total energy determine orbit type?",
        "options": ["A: E<0 bound, E=0 parabolic, E>0 hyperbolic", "B: E>0 bound, E<0 unbound", "C: Energy irrelevant"],
        "answer": "A",
        "explanation": "Bound orbits occur when total energy is negative; unbound orbits occur when energy is ≥0."
    },

    # Radiation, Temperature, Blackbody
    {
        "question": "Conceptually, how do you calculate a planet’s equilibrium temperature?",
        "options": ["A: Use radiation balance formula: absorbed = emitted", 
                    "B: Measure surface directly", 
                    "C: Use orbital speed only"],
        "answer": "A",
        "explanation": "Planet temperature comes from balancing absorbed solar energy and emitted blackbody radiation."
    },
    {
        "question": "How does albedo affect a planet’s equilibrium temperature?",
        "options": ["A: Higher albedo lowers temperature", "B: Higher albedo increases temperature", "C: Albedo has no effect"],
        "answer": "A",
        "explanation": "Albedo reflects sunlight; more reflection means less absorbed energy."
    },
    {
        "question": "Why does Earth’s average temperature differ from blackbody calculation?",
        "options": ["A: Atmosphere traps heat (greenhouse effect)", "B: Orbit is circular", "C: Sun emits only infrared"],
        "answer": "A",
        "explanation": "Greenhouse gases raise Earth's surface temperature above the simple blackbody estimate."
    },
    {
        "question": "What is a blackbody?",
        "options": ["A: Perfect absorber and emitter of radiation", "B: Reflects all light", "C: Only emits infrared"],
        "answer": "A",
        "explanation": "A blackbody absorbs all incident light and emits spectrum determined by temperature."
    },
    {
        "question": "How do solar radius and surface temperature affect luminosity?",
        "options": ["A: L = 4πR^2σT^4", "B: L = R*T", "C: L = 4πR/T"],
        "answer": "A",
        "explanation": "Luminosity increases with both surface area (R^2) and temperature to the fourth power."
    },
    {
        "question": "Why is Venus hotter than Earth?",
        "options": ["A: Strong greenhouse effect", "B: Closer to Sun only", "C: Larger radius"],
        "answer": "A",
        "explanation": "Venus’ thick CO2 atmosphere traps heat, making it hotter than Earth."
    },
    {
        "question": "Why is Moon’s blackbody temperature similar to Earth’s?",
        "options": ["A: Same distance from Sun", "B: Same atmosphere", "C: Moon reflects all sunlight"],
        "answer": "A",
        "explanation": "Equilibrium temperature mainly depends on solar distance, which is similar for Moon and Earth."
    },

    # Solar Wind and Sunspots
    {
        "question": "How does solar wind interact with planet magnetospheres?",
        "options": ["A: Deflected by magnetic field", "B: Absorbed by atmosphere", "C: Unaffected"],
        "answer": "A",
        "explanation": "Charged particles are deflected by magnetic fields, forming magnetospheres."
    },
    {
        "question": "Why is Earth slightly warmer during solar maximum despite sunspots?",
        "options": ["A: Total solar irradiance slightly higher", "B: Sunspots emit more light", "C: Earth orbit changes"],
        "answer": "A",
        "explanation": "Sunspots reduce radiation locally, but faculae increase total irradiance, warming Earth."
    },
    {
        "question": "How to estimate thermal velocity of solar wind protons?",
        "options": ["A: v_th = sqrt(2kT/m)", "B: v_th = m/k", "C: v_th = T^2"],
        "answer": "A",
        "explanation": "Thermal speed comes from kinetic theory: v_th = sqrt(2kT/m)."
    },
    {
        "question": "Compare thermal speed of solar wind particles to bulk speed; implication?",
        "options": ["A: Thermal < bulk; particles flow mainly with wind", "B: Thermal > bulk; particles escape", "C: Equal"],
        "answer": "A",
        "explanation": "Bulk flow dominates particle motion; thermal motion is smaller but contributes to spread."
    },
    {
        "question": "Which solar activity parameters are commonly measured?",
        "options": ["A: Sunspots, solar flux, neutrinos", "B: Sunspots only", "C: Magnetic field only"],
        "answer": "A",
        "explanation": "Sunspots, solar flux, and neutrinos are monitored to track solar activity cycles."
    },

    # Comets and Missions
    {
        "question": "Describe the structure of a comet.",
        "options": ["A: Nucleus, coma, dust/gas tail", "B: Core only", "C: Rings and moons"],
        "answer": "A",
        "explanation": "Comet has a solid nucleus, a coma of gas/dust, and often a visible tail from solar radiation."
    },
    {
        "question": "How are Kuiper belt objects similar/different to comets?",
        "options": ["A: Both icy; KBOs larger and more distant", "B: Only composition differs", "C: KBOs are stars"],
        "answer": "A",
        "explanation": "Both are icy bodies, but KBOs orbit beyond Neptune and are usually larger."
    },
    {
        "question": "Why are comet nuclei made mostly of ice and dust?",
        "options": ["A: Formed beyond ice line in cold protoplanetary disk", "B: Formed near Sun", "C: Captured asteroids"],
        "answer": "A",
        "explanation": "Low temperatures beyond ice line allow volatile ices to condense into comets."
    },
    {
        "question": "Why might comet orbits differ from predictions?",
        "options": ["A: Perturbations by planets or non-gravitational forces", "B: Shape of comet changes", "C: Sun’s gravity is irregular"],
        "answer": "A",
        "explanation": "Gravitational perturbations and outgassing forces can alter comet trajectories."
    },
    {
        "question": "The Hill sphere radius depends on which parameters?",
        "options": ["A: Planet mass, Sun mass, distance to Sun", "B: Planet size only", "C: Distance only"],
        "answer": "A",
        "explanation": "r_Hill ~ R * (m/M)^(1/3), where m = planet mass, M = Sun mass, R = planet-Sun distance."
    },
    {
        "question": "If a planet is more massive, how does its Hill radius change?",
        "options": ["A: Increases", "B: Decreases", "C: Stays same"],
        "answer": "A",
        "explanation": "r_Hill scales as the cube root of planet mass: bigger mass → larger sphere of influence."
    },
    {
        "question": "The Roche limit depends mainly on:",
        "options": ["A: Planet density, satellite density", "B: Orbital period", "C: Surface temperature"],
        "answer": "A",
        "explanation": "Roche limit ~ R_planet * (2ρ_planet/ρ_satellite)^(1/3)."
    },
    {
        "question": "Inside the Roche limit, satellites are:",
        "options": ["A: Tidally disrupted", "B: Stable", "C: Moving faster than light"],
        "answer": "A",
        "explanation": "Tidal forces overcome self-gravity of the satellite inside Roche limit."
    },

    # Orbits and Energy
    {
        "question": "A satellite in a circular orbit has what total energy?",
        "options": ["A: Negative, half the potential energy", "B: Zero", "C: Positive"],
        "answer": "A",
        "explanation": "Total energy E = K + U = -GMm/(2r) for circular orbit."
    },
    {
        "question": "In vis-viva equation, if r < a (closer to focus), velocity is:",
        "options": ["A: Greater than circular speed", "B: Less than circular speed", "C: Zero"],
        "answer": "A",
        "explanation": "v^2 = GM(2/r - 1/a); smaller r → higher speed at periapsis."
    },
    {
        "question": "Parabolic orbit total energy is:",
        "options": ["A: Zero", "B: Negative", "C: Positive"],
        "answer": "A",
        "explanation": "E = 0 corresponds to escape velocity, parabolic trajectory."
    },
    {
        "question": "Hyperbolic orbit total energy is:",
        "options": ["A: Positive", "B: Negative", "C: Zero"],
        "answer": "A",
        "explanation": "Unbound orbits have E > 0; hyperbolic orbits escape gravitational pull."
    },
    {
        "question": "How to estimate transfer time for Hohmann orbit to another planet?",
        "options": ["A: Half of ellipse period", "B: Full Earth year", "C: Full Mars year"],
        "answer": "A",
        "explanation": "Transfer time = 0.5 × orbital period of the Hohmann ellipse."
    },
    {
        "question": "Earth-Mars Hohmann transfer: at launch, spacecraft moves faster than Earth’s orbit. Why?",
        "options": ["A: Needs higher energy to reach Mars orbit", "B: To avoid gravity", "C: Random"],
        "answer": "A",
        "explanation": "Extra velocity (Δv) increases semi-major axis of transfer ellipse toward Mars."
    },

    # Radiation, Temperature, Blackbody
    {
        "question": "Planet absorbs fraction (1-A) of sunlight. A is:",
        "options": ["A: Albedo", "B: Temperature", "C: Distance"],
        "answer": "A",
        "explanation": "Albedo = fraction reflected; absorbed energy fraction = 1 - A."
    },
    {
        "question": "Equilibrium temperature T_eq formula:",
        "options": ["A: T_eq = [(1-A)L/16πσr^2]^(1/4)", "B: T_eq = L/r", "C: T_eq = σT^4"],
        "answer": "A",
        "explanation": "Balance absorbed and emitted radiation for blackbody planet."
    },
    {
        "question": "If albedo doubles, T_eq:",
        "options": ["A: Decreases", "B: Increases", "C: Unchanged"],
        "answer": "A",
        "explanation": "Higher albedo → less absorption → cooler planet."
    },
    {
        "question": "Thermal velocity of particle:",
        "options": ["A: v_th = sqrt(2kT/m)", "B: v_th = kT", "C: v_th = sqrt(T)"],
        "answer": "A",
        "explanation": "Kinetic theory: v_th ~ sqrt(2kT/m)."
    },
    {
        "question": "Solar wind average speed compared to proton thermal speed:",
        "options": ["A: Bulk flow ~400 km/s, thermal ~40 km/s", "B: Both equal", "C: Bulk < thermal"],
        "answer": "A",
        "explanation": "Bulk speed dominates; thermal speed smaller but adds velocity spread."
    },
    {
        "question": "Blackbody radiation peaks at wavelength λ_max ~",
        "options": ["A: Wien’s law λ_max = b/T", "B: λ_max = T^4", "C: λ_max = T/σ"],
        "answer": "A",
        "explanation": "Wien’s law: hotter bodies emit shorter wavelength light."
    },
    {
        "question": "Sun’s blackbody temperature ~",
        "options": ["A: 5778 K", "B: 6000°C", "C: 300 K"],
        "answer": "A",
        "explanation": "Sun’s surface temperature ~5778 K, determines spectrum."
    },

    # Comets
    {
        "question": "Comet tail points:",
        "options": ["A: Away from Sun", "B: Toward Sun", "C: Orbit direction"],
        "answer": "A",
        "explanation": "Solar radiation and solar wind push ion/dust tail away from Sun."
    },
    {
        "question": "Short-period comets come from:",
        "options": ["A: Kuiper belt", "B: Oort cloud", "C: Asteroid belt"],
        "answer": "A",
        "explanation": "Kuiper belt comets have periods <200 years."
    },
    {
        "question": "Long-period comets come from:",
        "options": ["A: Oort cloud", "B: Kuiper belt", "C: Earth"],
        "answer": "A",
        "explanation": "Oort cloud is distant, isotropic reservoir for long-period comets."
    },
    {
        "question": "Comet nucleus composition:",
        "options": ["A: Ice + dust", "B: Rock only", "C: Gas only"],
        "answer": "A",
        "explanation": "Formed beyond ice line, retaining volatiles and dust."
    },
    {
        "question": "Comet orbit deviations due to:",
        "options": ["A: Planetary perturbations + outgassing", "B: Only Sun", "C: Only collisions"],
        "answer": "A",
        "explanation": "Gravitational and non-gravitational forces alter trajectory."
    },

    # Missions and Observations
    {
        "question": "What is a geostationary orbit altitude roughly?",
        "options": ["A: 36,000 km above equator", "B: 6,000 km", "C: 100,000 km"],
        "answer": "A",
        "explanation": "Altitude gives 24-hour orbital period matching Earth rotation."
    },
    {
        "question": "What is the solar neutrino problem?",
        "options": ["A: Fewer neutrinos detected than predicted", "B: No neutrinos detected", "C: Neutrinos too fast"],
        "answer": "A",
        "explanation": "Observed flux was 1/3 predicted; solved by neutrino oscillations."
    },
    {
        "question": "Sunspots indicate:",
        "options": ["A: Strong magnetic fields, cooler areas", "B: Hotter surface", "C: High radiation"],
        "answer": "A",
        "explanation": "Sunspots are magnetic regions with suppressed convection → cooler."
    },
    {
        "question": "Solar cycle duration ~",
        "options": ["A: 11 years", "B: 22 years", "C: 5 years"],
        "answer": "A",
        "explanation": "Sunspot activity rises and falls with ~11-year cycle."
    },
    {
        "question": "Aurora occurs due to:",
        "options": ["A: Solar wind interacting with magnetosphere", "B: Moon phases", "C: Sunspots only"],
        "answer": "A",
        "explanation": "Charged particles excite atmospheric atoms, producing light."
    },
    {
        "question": "Estimate the equilibrium temperature of a planet at 1 AU from the Sun with albedo 0.3.",
        "options": ["A: ~255 K", "B: ~300 K", "C: ~200 K"],
        "answer": "A",
        "explanation": "T_eq ~ [(1-A)L/(16πσr^2)]^(1/4); for Earth: r=1 AU, A=0.3 → T_eq ~ 255 K."
    },
    {
        "question": "If a planet's albedo doubles, how does T_eq change approximately?",
        "options": ["A: Decreases by ~16%", "B: Increases", "C: Unchanged"],
        "answer": "A",
        "explanation": "T_eq ~ (1-A)^(1/4); doubling A reduces absorbed energy → cooler planet."
    },
    {
        "question": "Circular orbit velocity for Earth at 1 AU (~1.5e11 m) around Sun (M=2e30 kg)?",
        "options": ["A: ~30 km/s", "B: ~10 km/s", "C: ~50 km/s"],
        "answer": "A",
        "explanation": "v_circ = sqrt(GM/r) ~ sqrt(6.67e-11 * 2e30 / 1.5e11) ≈ 29.8 km/s."
    },
    {
        "question": "A spacecraft in a Hohmann transfer from Earth to Mars. What fraction of the orbital period of the transfer ellipse is the travel time?",
        "options": ["A: 1/2", "B: 1", "C: 1/4"],
        "answer": "A",
        "explanation": "Hohmann transfer: travel time = 0.5 × period of elliptical orbit connecting Earth and Mars."
    },
    {
        "question": "Perihelion speed of an elliptical orbit is generally:",
        "options": ["A: Greater than circular orbit at same distance", "B: Less", "C: Equal"],
        "answer": "A",
        "explanation": "Vis-viva: v^2 = GM(2/r - 1/a); smaller r → higher speed."
    },
    {
        "question": "Approximate Hill sphere radius for Earth (m=6e24 kg) around Sun (M=2e30 kg) at 1 AU?",
        "options": ["A: ~1.5 million km", "B: ~150,000 km", "C: ~15 million km"],
        "answer": "A",
        "explanation": "r_Hill = R*(m/3M)^(1/3) ~ 1.5e8 km*(6e24/(6e30))^(1/3) ≈ 1.5e6 km."
    },
    {
        "question": "If Mars has 1/10 Earth mass, how does its Hill radius compare?",
        "options": ["A: Smaller by ~2.15×", "B: Larger", "C: Same"],
        "answer": "A",
        "explanation": "r_Hill ~ m^(1/3); (0.1)^(1/3) ≈ 0.464 → smaller than Earth."
    },
    {
        "question": "Thermal velocity of protons in solar wind at T=1e6 K?",
        "options": ["A: ~40 km/s", "B: ~400 km/s", "C: ~4 km/s"],
        "answer": "A",
        "explanation": "v_th = sqrt(2kT/m_p) ~ sqrt(2*1.38e-23*1e6/1.67e-27) ≈ 40 km/s."
    },
    {
        "question": "Sun’s blackbody temperature ~5778 K. Peak wavelength λ_max?",
        "options": ["A: ~500 nm", "B: ~2000 nm", "C: ~50 nm"],
        "answer": "A",
        "explanation": "Wien’s law: λ_max = 2.898e-3 / T ≈ 2.898e-3 / 5778 ≈ 501 nm (green-yellow)."
    },
    {
        "question": "Roche limit for a satellite with density 1000 kg/m³ orbiting Earth (ρ=5500 kg/m³)?",
        "options": ["A: ~18,000 km", "B: ~6,000 km", "C: ~36,000 km"],
        "answer": "A",
        "explanation": "Roche limit ~ R_planet*(2ρ_planet/ρ_satellite)^(1/3); Earth radius ~6371 km → ~18,000 km."
    },
    {
        "question": "Escape velocity from Moon (R=1.74e6 m, M=7.35e22 kg)?",
        "options": ["A: ~2.38 km/s", "B: ~11 km/s", "C: ~0.5 km/s"],
        "answer": "A",
        "explanation": "v_esc = sqrt(2GM/R) ~ sqrt(2*6.67e-11*7.35e22/1.74e6) ≈ 2.38 km/s."
    },
    {
        "question": "Δv to move from low Earth orbit (r=7000 km) to geostationary orbit (r=42,000 km) approx?",
        "options": ["A: ~3.1 km/s", "B: ~7 km/s", "C: ~1 km/s"],
        "answer": "A",
        "explanation": "Using Hohmann transfer: Δv_total ~ 3.1 km/s."
    },
    {
        "question": "If a comet has semi-major axis a=50 AU, orbital period?",
        "options": ["A: ~350 years", "B: 50 years", "C: 500 years"],
        "answer": "A",
        "explanation": "Kepler’s 3rd law: P^2 = a^3 → P = sqrt(50^3) ≈ 353 years."
    },
    {
        "question": "If solar flux doubles, equilibrium temperature changes by factor ~?",
        "options": ["A: 2^(1/4) ~ 1.19", "B: 2", "C: 4"],
        "answer": "A",
        "explanation": "T_eq ~ L^(1/4); doubling L → T_eq increases by 2^(1/4) ≈ 1.19."
    },
    {
        "question": "A satellite at r = 10,000 km around Earth; gravitational potential energy (U = -GMm/r)?",
        "options": ["A: Negative, magnitude ~6.67e7 * m", "B: Positive", "C: Zero"],
        "answer": "A",
        "explanation": "Gravitational potential is always negative; U ~ -GMm/r."
    }  
]

# Total questions: 50


# -----------------------------
# SESSION STATE INIT
# -----------------------------
if "q_index" not in st.session_state:
    st.session_state.q_index = 0

if "shuffled_questions" not in st.session_state:
    st.session_state.shuffled_questions = random.sample(quiz_questions, len(quiz_questions))  # Shuffle questions

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
