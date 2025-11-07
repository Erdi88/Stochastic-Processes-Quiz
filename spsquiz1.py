import streamlit as st
import random

st.set_page_config(page_title="Database Systems Quiz 2025", layout="centered")

# -----------------------------
# QUESTIONS (same as before)
# -----------------------------

questions = [
    {
        "question": "What is the main source of the Sun’s energy?",
        "options": ["A: Gravitational contraction", "B: Nuclear fusion of hydrogen", "C: Radioactive decay", "D: Chemical reactions"],
        "answer": "B",
        "explanation": "The Sun’s energy comes from hydrogen nuclei fusing into helium in its core, releasing energy via E=mc²."
    },
    {
        "question": "Which particles from the Sun reach Earth almost instantly after being produced in the core?",
        "options": ["A: Photons", "B: Neutrinos", "C: Protons", "D: Solar wind ions"],
        "answer": "B",
        "explanation": "Neutrinos pass through the Sun and space almost without interaction, arriving at Earth in about 8 minutes."
    },
    {
        "question": "The approximate temperature of the Sun’s core is about:",
        "options": ["A: 6,000 K", "B: 15 million K", "C: 1 million K", "D: 100,000 K"],
        "answer": "B",
        "explanation": "The Sun’s core temperature is around 1.5 × 10⁷ K, sufficient for hydrogen fusion."
    },
    {
        "question": "True or False: The Sun transfers energy to the planets mainly through convection.",
        "options": ["True", "False"],
        "answer": "False",
        "explanation": "Energy transfer from the Sun to planets occurs via radiation (light), not convection."
    },
    {
        "question": "Which physical law explains why all planets orbit the Sun in roughly the same direction?",
        "options": ["A: Newton’s Third Law", "B: Conservation of Angular Momentum", "C: Kepler’s Second Law", "D: Universal Gravitation"],
        "answer": "B",
        "explanation": "Conservation of angular momentum in the rotating solar nebula caused planets to form in the same orbital direction."
    },
    {
        "question": "A Hohmann transfer orbit is primarily used to:",
        "options": ["A: Land on a moon", "B: Change orbital inclination", "C: Transfer between two circular orbits", "D: Maintain geostationary position"],
        "answer": "C",
        "explanation": "It’s the most fuel-efficient two-burn transfer between circular orbits in the same plane."
    },
    {
        "question": "True or False: A planet’s Hill sphere depends only on its mass.",
        "options": ["True", "False"],
        "answer": "False",
        "explanation": "It also depends on the planet’s distance from the Sun — farther planets have larger Hill spheres."
    },
    {
        "question": "What is the Roche limit?",
        "options": ["A: Minimum distance where a moon can orbit without breaking apart", "B: Distance where escape velocity equals orbital velocity", "C: Region of gravitational equilibrium", "D: Maximum stable orbital radius"],
        "answer": "A",
        "explanation": "Inside the Roche limit, tidal forces overcome a moon’s self-gravity, possibly forming rings."
    },
    {
        "question": "In planetary formation, what is 'runaway growth'?",
        "options": ["A: Rapid accumulation of mass by the largest planetesimals", "B: Evaporation of small dust particles", "C: Expansion of a protoplanet’s orbit", "D: Loss of gas by photoevaporation"],
        "answer": "A",
        "explanation": "Larger planetesimals attract material faster, growing disproportionately — a positive feedback process."
    },
    {
        "question": "Kepler’s third law connects which two parameters of a planet’s orbit?",
        "options": ["A: Period and mass", "B: Eccentricity and inclination", "C: Period and semi-major axis", "D: Velocity and radius"],
        "answer": "C",
        "explanation": "Kepler’s third law: P² ∝ a³ — orbital period squared is proportional to the cube of the semi-major axis."
    },
    {
        "question": "True or False: Mercury has a thin atmosphere because of its strong gravity.",
        "options": ["True", "False"],
        "answer": "False",
        "explanation": "Mercury’s gravity is weak and its temperature is high, so gas escapes easily, leaving only a thin exosphere."
    },
    {
        "question": "A primary atmosphere is composed mainly of:",
        "options": ["A: Outgassed CO₂ and N₂", "B: Captured hydrogen and helium", "C: Oxygen and ozone", "D: Volcanic dust and ice"],
        "answer": "B",
        "explanation": "Primary atmospheres are captured directly from the solar nebula (H and He), while secondary atmospheres come from outgassing or impacts."
    },
    {
        "question": "Which property most influences a planet’s bulk density?",
        "options": ["A: Distance from the Sun", "B: Composition", "C: Rotation rate", "D: Number of moons"],
        "answer": "B",
        "explanation": "Planets with rocky composition are denser; those with ice and gas are less dense."
    },
    {
        "question": "A surface-bound exosphere refers to:",
        "options": ["A: A dense layer of air near the ground", "B: Gas particles escaping freely without collisions", "C: A subsurface ocean", "D: A magnetic boundary layer"],
        "answer": "B",
        "explanation": "In an exosphere, gas particles rarely collide and follow ballistic trajectories — typical for Mercury or the Moon."
    },
    {
        "question": "True or False: Atmospheric composition generally stays constant with altitude.",
        "options": ["True", "False"],
        "answer": "False",
        "explanation": "Heavier gases settle lower; lighter gases dominate at higher altitudes."
    },
    {
        "question": "Where do short-period comets originate?",
        "options": ["A: Oort Cloud", "B: Kuiper Belt", "C: Asteroid Belt", "D: Solar corona"],
        "answer": "B",
        "explanation": "Short-period comets come from the Kuiper Belt and have orbits lasting under 200 years."
    },
    {
        "question": "Where do long-period comets originate?",
        "options": ["A: Asteroid Belt", "B: Kuiper Belt", "C: Oort Cloud", "D: Main Belt"],
        "answer": "C",
        "explanation": "Long-period comets come from the distant, spherical Oort Cloud extending thousands of AU from the Sun."
    },
    {
        "question": "True or False: Meteor showers are linked to debris left behind by comets.",
        "options": ["True", "False"],
        "answer": "True",
        "explanation": "Earth passes through trails of cometary dust, producing meteor showers when particles burn in the atmosphere."
    },
    {
        "question": "Which is most massive among these small Solar System objects?",
        "options": ["A: Dwarf planet", "B: Asteroid", "C: Comet nucleus", "D: Meteoroid"],
        "answer": "A",
        "explanation": "Dwarf planets like Pluto or Eris are the most massive class of small bodies."
    },
    {
        "question": "True or False: Crater counts give the same meteoroid flux estimate on Mars and its moons.",
        "options": ["True", "False"],
        "answer": "False",
        "explanation": "Different gravity, surface age, and atmosphere cause different apparent crater densities and flux estimates."
    },
    {
        "question": "How was the first exoplanet around a main-sequence star discovered?",
        "options": ["A: Direct imaging", "B: Transit method", "C: Radial velocity (Doppler wobble)", "D: Gravitational microlensing"],
        "answer": "C",
        "explanation": "The first exoplanet around a Sun-like star (51 Pegasi b) was found by detecting the star’s Doppler shifts due to the planet’s gravity."
    },
    {
        "question": "A 'hot Jupiter' refers to:",
        "options": ["A: A massive planet far from its star", "B: A gas giant close to its star", "C: A small rocky planet with lava surface", "D: A young planet still contracting"],
        "answer": "B",
        "explanation": "Hot Jupiters are gas giants orbiting very close to their stars, resulting in high temperatures and short orbital periods."
    },
    {
        "question": "Which parameter primarily determines an exoplanet’s equilibrium temperature?",
        "options": ["A: Planet’s mass", "B: Distance from its star", "C: Rotation speed", "D: Magnetic field strength"],
        "answer": "B",
        "explanation": "The farther a planet is from its star, the less radiation it receives, leading to a lower equilibrium temperature."
    },
    {
        "question": "The habitable zone around a star is defined as:",
        "options": ["A: The region where liquid water can exist", "B: The zone with maximum stellar flux", "C: The orbit where comets form", "D: The magnetic boundary of the star"],
        "answer": "A",
        "explanation": "It’s the distance range where conditions allow liquid water to be stable on a planet’s surface."
    },
    {
        "question": "The Drake equation is used to estimate:",
        "options": ["A: The age of the universe", "B: The number of intelligent civilizations", "C: The lifetime of stars", "D: The speed of galactic rotation"],
        "answer": "B",
        "explanation": "The Drake equation multiplies several factors to estimate the number of detectable extraterrestrial civilizations."
    },
    {
        "question": "True or False: The Sun’s magnetic activity cycle lasts about 11 years.",
        "options": ["True", "False"],
        "answer": "True",
        "explanation": "The number of sunspots rises and falls in an ~11-year cycle, marking the solar activity period."
    },
    {
        "question": "Why is Earth slightly warmer during solar maximum, despite sunspots being cooler?",
        "options": ["A: Increased solar luminosity from faculae", "B: Greenhouse gas buildup", "C: Tidal effects from the Moon", "D: Decreased albedo"],
        "answer": "A",
        "explanation": "Bright magnetic regions (faculae) increase total solar output, offsetting the cooling effect of sunspots."
    },
    {
        "question": "What is observed in the solar wind at 1 AU?",
        "options": ["A: Plasma of protons and electrons", "B: Neutral hydrogen gas", "C: Only magnetic fields", "D: Cosmic dust grains"],
        "answer": "A",
        "explanation": "The solar wind is a stream of charged particles—mostly protons and electrons—flowing outward from the Sun."
    },
    {
        "question": "True or False: The Sun’s magnetic field at 1 AU is purely radial.",
        "options": ["True", "False"],
        "answer": "False",
        "explanation": "Due to the Sun’s rotation, the field has a spiral (azimuthal) component—forming the Parker spiral."
    },
    {
        "question": "A Sun-synchronous orbit is useful because:",
        "options": ["A: It keeps constant sunlight conditions for imaging", "B: It avoids eclipses", "C: It moves with the solar wind", "D: It remains fixed over the equator"],
        "answer": "A",
        "explanation": "Sun-synchronous orbits precess so that each pass occurs at the same local solar time, ideal for consistent lighting in observations."
    },
    {
        "question": "True or False: Energy from the Sun reaches Earth mainly by conduction.",
        "options": ["True", "False"],
        "answer": "False",
        "explanation": "There’s no medium for conduction in space—energy is transferred by electromagnetic radiation."
    },
    {
        "question": "Which two factors determine a star’s luminosity?",
        "options": ["A: Radius and surface temperature", "B: Mass and density", "C: Age and composition", "D: Magnetic field and rotation rate"],
        "answer": "A",
        "explanation": "Luminosity follows L = 4πR²σT⁴, depending on the star’s size and surface temperature."
    },
    {
        "question": "True or False: Most stars in the Milky Way are main-sequence stars.",
        "options": ["True", "False"],
        "answer": "True",
        "explanation": "The main sequence phase lasts the majority of a star’s lifetime, so most observed stars are in this stage."
    },
    {
        "question": "What determines whether a planet retains an atmosphere over time?",
        "options": ["A: Temperature and escape velocity", "B: Distance from Earth", "C: Rotation rate", "D: Number of moons"],
        "answer": "A",
        "explanation": "Gas retention depends on how fast molecules move (temperature) versus how fast the planet can hold them (escape velocity)."
    },
    {
        "question": "If a spacecraft moves from Earth’s orbit to Mars’ orbit via a Hohmann transfer, the transfer ellipse’s semi-major axis is:",
        "options": ["A: (r_Earth + r_Mars)/2", "B: (r_Earth × r_Mars)/2", "C: (r_Mars − r_Earth)", "D: (r_Mars + r_Earth)²"],
        "answer": "A",
        "explanation": "The Hohmann transfer orbit’s semi-major axis is the average of the two circular orbital radii."
    },
    {
        "question": "True or False: Increasing a planet’s mass increases the size of its Hill sphere.",
        "options": ["True", "False"],
        "answer": "True",
        "explanation": "A more massive planet has stronger gravity relative to the Sun, allowing a larger region of stable satellite orbits."
    },
    {
        "question": "What happens if a moon orbits inside the Roche limit?",
        "options": ["A: It becomes tidally locked", "B: It may be torn apart by tidal forces", "C: It speeds up its orbit", "D: It escapes into space"],
        "answer": "B",
        "explanation": "Tidal stresses exceed the moon’s self-gravity, causing fragmentation—forming rings or debris."
    },
    {
        "question": "True or False: The habitable zone moves outward as a star evolves into a red giant.",
        "options": ["True", "False"],
        "answer": "True",
        "explanation": "As luminosity increases, the region where water can exist moves farther from the star."
    },
    {
        "question": "Which formula would you use to compare energy output between a sunspot and the normal solar surface?",
        "options": ["A: L ∝ T⁴", "B: L ∝ 1/T", "C: L ∝ T²", "D: L ∝ √T"],
        "answer": "A",
        "explanation": "Blackbody radiation follows the Stefan–Boltzmann law: energy ∝ T⁴, so cooler regions emit much less energy."
    },
    {
        "question": "True or False: Venus is hotter than Earth because it’s closer to the Sun.",
        "options": ["True", "False"],
        "answer": "False",
        "explanation": "Venus’s extreme heat is due to its dense CO₂ atmosphere and strong greenhouse effect, not just its distance."
    },
    {
        "question": "How does the solar wind interact with Earth’s magnetic field?",
        "options": ["A: It passes straight through", "B: It’s deflected, creating a magnetosphere", "C: It heats the atmosphere directly", "D: It increases Earth’s rotation speed"],
        "answer": "B",
        "explanation": "The solar wind is deflected by Earth’s magnetic field, forming the magnetosphere and sometimes causing auroras."
    },
    {
        "question": "True or False: The Sun’s 11-year cycle is tracked by counting sunspots.",
        "options": ["True", "False"],
        "answer": "True",
        "explanation": "Sunspots increase and decrease in a predictable ~11-year cycle, used to monitor solar activity."
    },
    {
        "question": "The solar wind mainly consists of which particles?",
        "options": ["A: Protons and electrons", "B: Neutrons", "C: Neutral hydrogen atoms", "D: Cosmic rays"],
        "answer": "A",
        "explanation": "It’s a plasma made mostly of protons and electrons, continuously streaming from the Sun’s corona."
    },
    {
        "question": "True or False: The thermal velocity of solar wind protons is usually higher than their bulk flow speed.",
        "options": ["True", "False"],
        "answer": "False",
        "explanation": "The bulk flow (hundreds of km/s) is faster than the random thermal motion of the protons."
    },
    {
        "question": "Why does the Sun’s magnetic field have both radial and azimuthal components at 1 AU?",
        "options": ["A: Magnetic field reversals", "B: Solar differential rotation and wind outflow", "C: Interaction with planets", "D: Cosmic ray pressure"],
        "answer": "B",
        "explanation": "The combination of solar rotation and the outward-moving solar wind winds the field into a spiral pattern (Parker spiral)."
    },
    {
        "question": "What is the typical bulk velocity of the solar wind near Earth?",
        "options": ["A: 100 km/s", "B: 400 km/s", "C: 1500 km/s", "D: 20 km/s"],
        "answer": "B",
        "explanation": "At 1 AU, the solar wind flows at ~400 km/s on average, with faster streams during high solar activity."
    },
    {
        "question": "True or False: A Sun-synchronous satellite passes over each location on Earth at different local times each day.",
        "options": ["True", "False"],
        "answer": "False",
        "explanation": "Sun-synchronous orbits maintain a constant local solar time for imaging consistency."
    },
    {
        "question": "Which orbit allows a satellite to appear fixed above one point on Earth?",
        "options": ["A: Polar", "B: Geostationary", "C: Sun-synchronous", "D: Elliptical"],
        "answer": "B",
        "explanation": "A geostationary satellite orbits at ~35,786 km, matching Earth’s rotation period and appearing stationary over the equator."
    },
    {
        "question": "True or False: A planet’s orbital energy determines whether its path is bound or unbound.",
        "options": ["True", "False"],
        "answer": "True",
        "explanation": "If total energy is negative, the orbit is bound; if positive, the object escapes to infinity."
    },
    {
        "question": "What does the vis-viva equation describe?",
        "options": ["A: The relation between orbital speed, position, and semi-major axis", "B: The escape speed from a planet", "C: The surface gravity of a star", "D: The expansion of the universe"],
        "answer": "A",
        "explanation": "The vis-viva equation v² = GM(2/r − 1/a) links orbital velocity, distance, and the semi-major axis."
    },
    {
        "question": "True or False: A circular orbit has the same speed everywhere because r = a.",
        "options": ["True", "False"],
        "answer": "True",
        "explanation": "For circular orbits, distance from the focus is constant, so the orbital velocity doesn’t vary."
    },
    {
        "question": "Conceptually, how would you find perihelion and aphelion speeds of an orbit?",
        "options": ["A: Use the vis-viva equation with r = r_min or r_max", "B: Multiply the semi-major axis by eccentricity", "C: Divide orbital period by mass", "D: Assume constant velocity"],
        "answer": "A",
        "explanation": "By applying v² = GM(2/r − 1/a) at the closest and farthest orbital points (r_min, r_max)."
    },
    {
        "question": "What determines the equilibrium temperature of a planet?",
        "options": ["A: Distance from its star and albedo", "B: Planet’s density", "C: Its moons’ orbits", "D: Its magnetic field strength"],
        "answer": "A",
        "explanation": "A planet’s temperature depends mainly on how much sunlight it receives and how much it reflects (albedo)."
    },
    {
        "question": "True or False: A perfect blackbody absorbs all incident radiation.",
        "options": ["True", "False"],
        "answer": "True",
        "explanation": "By definition, a blackbody absorbs all incoming radiation and re-emits according to its temperature."
    },
    {
        "question": "Why is the Moon’s blackbody temperature similar to Earth’s?",
        "options": ["A: It has an atmosphere", "B: It receives similar solar flux", "C: It rotates quickly", "D: It has volcanic heating"],
        "answer": "B",
        "explanation": "Both Earth and Moon are at roughly the same distance from the Sun and thus receive similar solar energy per area."
    },
    {
        "question": "True or False: The solar constant increases if the Sun expands into a red giant.",
        "options": ["True", "False"],
        "answer": "True",
        "explanation": "A larger, more luminous Sun would greatly increase the solar energy reaching a given distance."
    },
    {
        "question": "What is the approximate blackbody temperature of Earth (ignoring greenhouse effects)?",
        "options": ["A: 255 K", "B: 300 K", "C: 100 K", "D: 500 K"],
        "answer": "A",
        "explanation": "Using solar flux and albedo, Earth’s equilibrium temperature is about 255 K (~−18°C)."
    },
    {
        "question": "Describe the structure of a comet’s nucleus and surrounding regions.",
        "options": ["A: Rocky core only", "B: Icy nucleus with coma and tails", "C: Metallic center with rings", "D: Gas-only sphere"],
        "answer": "B",
        "explanation": "A comet has an icy nucleus surrounded by a coma of gas and dust, with tails pointing away from the Sun."
    },
    {
        "question": "True or False: Comet tails always point opposite to the comet’s motion.",
        "options": ["True", "False"],
        "answer": "False",
        "explanation": "Tails always point away from the Sun due to solar radiation and the solar wind, not necessarily opposite to motion."
    },
    {
        "question": "What was the main goal of the Rosetta mission?",
        "options": ["A: Study the Sun’s corona", "B: Orbit and land on a comet nucleus", "C: Measure dark matter", "D: Explore the Kuiper Belt"],
        "answer": "B",
        "explanation": "ESA’s Rosetta mission orbited comet 67P/Churyumov–Gerasimenko and deployed the Philae lander to its surface."
    },
    {
        "question": "Stars form in which type of interstellar clouds?",
        "options": ["A: Diffuse atomic clouds", "B: Molecular clouds", "C: Ionized H II regions", "D: Planetary nebulae"],
        "answer": "B",
        "explanation": "Stars form in cold, dense molecular clouds where gravity can overcome gas pressure to start collapse."
    },
    {
        "question": "The first step in star formation is called:",
        "options": ["A: Protostar ignition", "B: Gravitational collapse", "C: Main sequence burning", "D: Nuclear condensation"],
        "answer": "B",
        "explanation": "Star formation begins when a region of a molecular cloud collapses under its own gravity, forming a protostar."
    },
    {
        "question": "True or False: Most stars spend the majority of their lives on the main sequence.",
        "options": ["True", "False"],
        "answer": "True",
        "explanation": "The main sequence phase, where hydrogen fusion occurs in the core, is the longest stage in a star’s life."
    },
    {
        "question": "Which two parameters determine a star’s luminosity?",
        "options": ["A: Temperature and radius", "B: Age and distance", "C: Density and metallicity", "D: Rotation and mass loss"],
        "answer": "A",
        "explanation": "Luminosity is proportional to R²T⁴ — both size and surface temperature control how bright a star is."
    },
    {
        "question": "True or False: Planets generally orbit the Sun in random directions.",
        "options": ["True", "False"],
        "answer": "False",
        "explanation": "Conservation of angular momentum in the rotating solar nebula caused most planets to orbit in the same direction."
    },
    {
        "question": "Which planets are terrestrial?",
        "options": ["A: Mercury, Venus, Earth, Mars", "B: Jupiter, Saturn, Uranus, Neptune", "C: Pluto and Eris", "D: Only Earth"],
        "answer": "A",
        "explanation": "The inner four planets are rocky and dense — classified as terrestrial planets."
    },
    {
        "question": "Why is Mercury’s atmosphere so thin compared to Venus?",
        "options": ["A: It’s closer to the Sun and has low gravity", "B: It’s farther from the Sun", "C: It has many moons", "D: It rotates faster"],
        "answer": "A",
        "explanation": "High temperature and weak gravity allow gases to escape from Mercury’s surface easily."
    },
    {
        "question": "True or False: A planet’s Hill sphere defines the region where it can hold moons in stable orbits.",
        "options": ["True", "False"],
        "answer": "True",
        "explanation": "Inside the Hill sphere, a planet’s gravity dominates over the Sun’s, allowing stable satellite orbits."
    },
    {
        "question": "Conceptually, how is the Hill radius calculated?",
        "options": ["A: It depends on planet mass and distance from the Sun", "B: Only on orbital speed", "C: Only on the Sun’s luminosity", "D: On the planet’s temperature"],
        "answer": "A",
        "explanation": "r_H ≈ a × (m_planet / (3M_sun))^(1/3); it grows with planet mass and distance from the Sun."
    },
    {
        "question": "What happens if a moon orbits within the Roche limit of its planet?",
        "options": ["A: It becomes more spherical", "B: It can be torn apart by tidal forces", "C: It gains mass from the planet", "D: It moves to a higher orbit"],
        "answer": "B",
        "explanation": "Tidal forces exceed the moon’s gravity, causing it to disintegrate — forming rings or debris."
    },
    {
        "question": "Why are most moons found within a planet’s Hill sphere?",
        "options": ["A: The planet’s gravity dominates there", "B: It’s the coldest region", "C: It’s protected from solar radiation", "D: It has strong magnetic fields"],
        "answer": "A",
        "explanation": "Outside the Hill sphere, solar gravity overcomes the planet’s pull, making orbits unstable."
    },
    {
        "question": "Explain the difference between a meteor, meteoroid, and meteorite.",
        "options": ["A: They are all the same", "B: Meteoroid = in space, Meteor = in atmosphere, Meteorite = on ground", "C: Meteorite = in space, Meteor = on ground", "D: Meteor = star"],
        "answer": "B",
        "explanation": "A meteoroid travels in space, a meteor is the streak in the sky, and a meteorite is what reaches the surface."
    },
    {
        "question": "True or False: Dwarf planets are typically more massive than comets or asteroids.",
        "options": ["True", "False"],
        "answer": "True",
        "explanation": "Dwarf planets like Pluto and Eris are the largest class of small Solar System bodies."
    },
    {
        "question": "How are comet orbits classified?",
        "options": ["A: By their brightness", "B: By orbital period (short or long)", "C: By their composition", "D: By their distance from Jupiter"],
        "answer": "B",
        "explanation": "Comets with periods under 200 years are short-period; longer ones come from the distant Oort Cloud."
    },
    {
        "question": "Where do long-period comets originate?",
        "options": ["A: The Oort Cloud", "B: The Asteroid Belt", "C: The Kuiper Belt", "D: The Scattered Disk"],
        "answer": "A",
        "explanation": "Long-period comets come from the spherical Oort Cloud, far beyond Pluto."
    },
    {
        "question": "Where do short-period comets come from?",
        "options": ["A: Oort Cloud", "B: Kuiper Belt", "C: Asteroid Belt", "D: Interstellar space"],
        "answer": "B",
        "explanation": "Short-period comets typically originate in the Kuiper Belt, beyond Neptune."
    },
    {
        "question": "True or False: The vis-viva equation can be used to find a spacecraft’s speed at any orbital point.",
        "options": ["True", "False"],
        "answer": "True",
        "explanation": "v² = GM(2/r − 1/a) gives the orbital velocity based on position and semi-major axis."
    },
    {
        "question": "Conceptually, how can you estimate the time for a Hohmann transfer between two planets?",
        "options": ["A: Half the orbital period of the transfer ellipse", "B: Twice the orbital period", "C: Equal to the inner planet’s period", "D: Equal to one full orbit of the outer planet"],
        "answer": "A",
        "explanation": "A Hohmann transfer covers half of an elliptical orbit between the two circular orbits."
    },
    {
        "question": "What does 'effective potential' in orbital motion represent?",
        "options": ["A: Gravitational + rotational energy per mass", "B: Magnetic field strength", "C: Electric charge balance", "D: Kinetic energy only"],
        "answer": "A",
        "explanation": "Effective potential combines gravitational potential with the centrifugal term, useful for analyzing orbital stability."
    },
    {
        "question": "True or False: Total mechanical energy of a bound orbit is negative.",
        "options": ["True", "False"],
        "answer": "True",
        "explanation": "A negative total energy indicates a closed, bound orbit—object cannot escape the central body."
    },
    {
        "question": "Conceptually, what is a blackbody in astronomy?",
        "options": ["A: A perfectly reflecting object", "B: An ideal emitter that absorbs all radiation", "C: A black hole", "D: A starless planet"],
        "answer": "B",
        "explanation": "A blackbody absorbs all incident energy and emits radiation only based on its temperature."
    },
    {
        "question": "How do solar radius and surface temperature affect luminosity?",
        "options": ["A: Luminosity ∝ R²T⁴", "B: Luminosity ∝ 1/(R²T)", "C: Luminosity ∝ R/T²", "D: Luminosity ∝ T"],
        "answer": "A",
        "explanation": "Luminosity grows rapidly with both radius and temperature, following the Stefan–Boltzmann law."
    },
    {
        "question": "True or False: Earth’s actual temperature is higher than its blackbody temperature because of the greenhouse effect.",
        "options": ["True", "False"],
        "answer": "True",
        "explanation": "Atmospheric gases trap infrared radiation, keeping Earth’s surface warmer than the 255 K blackbody estimate."
    },
    {
        "question": "How can an electrostatic + magnetic analyzer measure ion mass on a spacecraft?",
        "options": ["A: By measuring light emission", "B: By combining deflection by electric and magnetic fields", "C: By weighing particles directly", "D: By counting photons"],
        "answer": "B",
        "explanation": "Ion analyzers determine particle mass-to-charge ratios from their deflection in electric and magnetic fields."
    },
    {
        "question": "True or False: Comet orbits can change due to outgassing effects.",
        "options": ["True", "False"],
        "answer": "True",
        "explanation": "Jets of gas from sublimating ice can slightly alter a comet’s path, making its orbit deviate from predictions."
    },
    {
        "question": "Why do planets orbit roughly in the same plane?",
        "options": [
            "A: Due to random collisions during planet formation",
            "B: Because the Sun’s gravity flattens their orbits",
            "C: Result of angular momentum conservation in the protoplanetary disk",
            "D: Because of tidal forces from nearby stars"
        ],
        "answer": "C",
        "explanation": "The protoplanetary disk was rotating, and conservation of angular momentum caused most planets to orbit roughly in the same plane."
    },
    {
        "question": "What differentiates terrestrial and giant planets?",
        "options": [
            "A: Terrestrial planets are gas-rich; giant planets are rocky",
            "B: Terrestrial planets are small, dense, rocky; giants are large, gas-dominated",
            "C: Terrestrial planets are further from the Sun; giants are closer",
            "D: Terrestrial planets have rings; giants do not"
        ],
        "answer": "B",
        "explanation": "Terrestrial planets formed in the hot inner disk and are rocky, whereas giant planets accreted gas and ice in the cooler outer disk."
    },
    {
        "question": "What is the ice line in a protoplanetary disk?",
        "options": [
            "A: The distance where water ice can exist in solid form",
            "B: The boundary between rocky planets and gas giants",
            "C: The limit of the Sun’s magnetic field",
            "D: The distance beyond which planets cannot form"
        ],
        "answer": "A",
        "explanation": "The ice line marks where temperatures are low enough for volatile compounds like water to freeze, aiding formation of giant planet cores."
    },
    {
        "question": "Why does the Moon always show the same face to Earth?",
        "options": [
            "A: Because of tidal locking",
            "B: Because the Moon does not rotate",
            "C: Because Earth’s gravity slows its orbit",
            "D: Because of solar radiation pressure"
        ],
        "answer": "A",
        "explanation": "The Moon is tidally locked to Earth, meaning its rotation period equals its orbital period around Earth."
    },
    {
        "question": "Which of the following is an example of another tidally locked body?",
        "options": [
            "A: Mercury around the Sun",
            "B: Jupiter around the Sun",
            "C: Venus around Earth",
            "D: Mars around the Sun"
        ],
        "answer": "A",
        "explanation": "Mercury rotates three times on its axis for every two orbits around the Sun, a form of tidal resonance (effectively locked in long-term)."
    },
    {
        "question": "Why does Earth have a magnetic field but Venus does not?",
        "options": [
            "A: Earth is larger than Venus",
            "B: Earth has a liquid iron core generating a dynamo; Venus rotates too slowly",
            "C: Venus lacks water",
            "D: Venus is too far from the Sun"
        ],
        "answer": "B",
        "explanation": "Earth’s liquid outer core and rotation drive a magnetic dynamo. Venus rotates very slowly, preventing a similar dynamo."
    },
    {
        "question": "How does a planet’s magnetic field protect its atmosphere?",
        "options": [
            "A: By reflecting sunlight",
            "B: By deflecting solar wind particles",
            "C: By heating the atmosphere",
            "D: By creating auroras"
        ],
        "answer": "B",
        "explanation": "The magnetic field deflects charged particles from the solar wind, preventing significant atmospheric erosion."
    },
    {
        "question": "How are comets classified?",
        "options": [
            "A: By their brightness",
            "B: By orbital period (short or long)",
            "C: By composition",
            "D: By distance from Jupiter"
        ],
        "answer": "B",
        "explanation": "Comets with periods under 200 years are short-period; longer ones typically come from the distant Oort Cloud."
    },
    {
        "question": "What is the main source of energy in the Sun’s interior?",
        "options": [
            "A: Thermal fusion",
            "B: Neutron capture",
            "C: Radioactive decay",
            "D: Gravitational contraction"
        ],
        "answer": "A",
        "explanation": "Hydrogen nuclei fuse into helium in the Sun’s core, releasing energy as radiation."
    },
    {
        "question": "Which formula gives the Hill radius of a planet?",
        "options": [
            "A: r_Hill = (m / M)^(1/3) * R",
            "B: r_Roche = 2.4 * (rho_planet / rho_satellite)^(1/3) * R_planet",
            "C: v_orb = sqrt(G * M / R)",
            "D: T_eq = ((1 - A_B) * L / (16 * pi * r^2 * sigma))^(1/4)"
        ],
        "answer": "A",
        "explanation": "The Hill radius marks the region where a planet dominates the gravitational attraction of nearby satellites."
    },
    {
        "question": "Which formula gives the blackbody temperature of a planet in radiation balance?",
        "options": [
            "A: T = ((1 - A_B) * L / (16 * pi * r^2 * sigma))^(1/4)",
            "B: v = sqrt(G * M / r)",
            "C: P = n * k_B * T",
            "D: r_Hill = (m / M)^(1/3) * R"
        ],
        "answer": "A",
        "explanation": "A planet absorbs energy on the Sun-facing side and radiates over its surface; this formula computes its equilibrium blackbody temperature."
    },
    {
        "question": "Which formula is used to calculate the solar constant at Earth after the Sun changes size and temperature?",
        "options": [
            "A: S = L / (4 * pi * r^2), with L = 4 * pi * R^2 * sigma * T^4",
            "B: v = sqrt(G * M / r)",
            "C: r_Roche = 2.4 * (rho_planet / rho_satellite)^(1/3) * R_planet",
            "D: T_eq = ((1 - A_B) * L / (16 * pi * r^2 * sigma))^(1/4)"
        ],
        "answer": "A",
        "explanation": "The solar constant depends on the Sun’s luminosity and distance; luminosity is computed from radius and surface temperature via the Stefan-Boltzmann law."
    },
    {
        "question": "Which formula is relevant to calculate the transfer time in a Hohmann orbit from Earth to Mars?",
        "options": [
            "A: t_transfer = pi * sqrt(a^3 / (G * M))",
            "B: v = sqrt(G * M * (2 / r - 1 / a))",
            "C: r_Roche = 2.4 * (rho_planet / rho_satellite)^(1/3) * R_planet",
            "D: T_eq = ((1 - A_B) * L / (16 * pi * r^2 * sigma))^(1/4)"
        ],
        "answer": "A",
        "explanation": "The transfer time is half the period of the elliptical Hohmann orbit, which can be derived from Kepler’s third law."
    },
    {
        "question": "The dust rings of Uranus were discovered in 1977. How?",
        "options": [
            "A: With camera observations from Voyager 1 spacecraft",
            "B: With stellar occultation observations",
            "C: With a solar occultation observation"
        ],
        "answer": "B",
        "explanation": "The dust rings of Uranus were first detected using the method of stellar occultation, where the dimming of a background star as it passed behind Uranus' rings revealed their presence."
    },
    {
        "question": "What defines an Astronomical Unit (AU)?",
        "options": [
            "A: The distance from the Sun to Neptune",
            "B: The mean distance from the Earth to the Sun",
            "C: The distance light travels in one hour",
            "D: The radius of Earth's orbit at perihelion"
        ],
        "answer": "B",
        "explanation": "An Astronomical Unit is defined as the average distance between the Earth and the Sun, approximately 149.6 million kilometers."
    },
    {
        "question": "How is the Lyapunov characteristic exponent used to distinguish between regular and chaotic trajectories?",
        "options": [
            "A: It measures the energy of the orbit",
            "B: It quantifies the rate at which nearby trajectories diverge",
            "C: It calculates orbital period",
            "D: It gives the average orbital radius"
        ],
        "answer": "B",
        "explanation": "The Lyapunov exponent indicates how quickly nearby trajectories in phase space diverge. Positive exponents indicate chaotic motion, while zero or negative exponents indicate regular, stable motion."
    },
    {
        "question": "As a comet passes the Sun we observe that its tail at one point gets disconnected. Which of the comet’s tails were broken, and why did it happen?",
        "options": [
            "A: The dust tail, because of solar radiation pressure",
            "B: The ion tail, due to interactions with the solar wind and magnetic field",
            "C: Both tails, due to gravitational perturbations",
            "D: None, tails never break"
        ],
        "answer": "B",
        "explanation": "The ion tail is made of charged particles that interact strongly with the solar wind and the Sun’s magnetic field. Changes in the magnetic field can cause disconnection events in the ion tail."
    },
    {
        "question": "The magnetic field of the Sun typically has radial and azimuthal components that are roughly equal at a distance of 1 AU. What causes this?",
        "options": [
            "A: Solar rotation and the Parker spiral",
            "B: Sunspot activity",
            "C: Convection in the solar core",
            "D: Tidal effects from planets"
        ],
        "answer": "A",
        "explanation": "The Sun’s rotation twists the magnetic field lines into a spiral shape known as the Parker spiral. At 1 AU, the radial and azimuthal components are roughly comparable."
    },
    {
        "question": "The Sun follows an 11-year-long cycle. Discuss the changes that happen to sunspots during these cycles.",
        "options": [
            "A: Sunspots disappear completely at solar minimum and reach maximum at solar maximum",
            "B: Sunspots change color",
            "C: Sunspots migrate from Earth-facing side to far side",
            "D: Sunspots increase only in size but not in number"
        ],
        "answer": "A",
        "explanation": "During the 11-year solar cycle, the number of sunspots varies from a minimum (few or none) to a maximum, reflecting the magnetic activity of the Sun."
    },
    {
        "question": "What is Jeans instability and why is it important?",
        "options": [
            "A: Gravitational collapse of a cloud when internal pressure cannot support it, leading to star formation",
            "B: Instability in planetary orbits",
            "C: Turbulent mixing in the Sun's convection zone",
            "D: Oscillations in comet tails"
        ],
        "answer": "A",
        "explanation": "Jeans instability occurs when a region in a gas cloud exceeds a critical mass or size (the Jeans mass) so that gravity overcomes pressure, leading to collapse and eventually star formation."
    },
    {
        "question": "What is described with the Jeans mass?",
        "options": [
            "A: The mass at which a gas cloud becomes unstable to gravitational collapse",
            "B: The total mass of a star cluster",
            "C: The mass of the Sun",
            "D: The mass needed for a planet to retain an atmosphere"
        ],
        "answer": "A",
        "explanation": "The Jeans mass is the critical mass for which a gas cloud will collapse under its own gravity, initiating star formation."
    },
    {
        "question": "What is the virial theorem and when do we use it?",
        "options": [
            "A: Relates the kinetic and potential energy in a bound system; used to estimate stability of stars and clusters",
            "B: Predicts the luminosity of stars",
            "C: Determines escape velocity from planets",
            "D: Describes the expansion of the universe"
        ],
        "answer": "A",
        "explanation": "The virial theorem states that for a stable, bound gravitational system, twice the kinetic energy plus the potential energy is zero. It's used to analyze systems like star clusters or galaxies."
    },
    {
        "question": "The dust rings of Neptune were discovered in 1984. How?",
        "options": [
            "A: With camera observations from Voyager 1 spacecraft",
            "B: With stellar occultation observations",
            "C: With a solar occultation observation"
        ],
        "answer": "B",
        "explanation": "Neptune's rings were first detected by observing the dimming of a star as it passed behind them (stellar occultation), before Voyager 2 confirmed their structure."
    },
    {
        "question": "What is the main process of heat transfer from Sun to planets?",
        "options": [
            "A: Diffusion / Conduction",
            "B: Convection",
            "C: Radiation"
        ],
        "answer": "C",
        "explanation": "Heat from the Sun reaches planets primarily by radiation, as energy is transmitted through electromagnetic waves across space."
    },
    {
        "question": "What is the main difference when solar element abundance and element abundance of a primitive meteorite are compared?",
        "options": [
            "A: The meteorite contains smaller amounts of the volatile elements",
            "B: The meteorite contains amino acids",
            "C: The meteorite contains less He because Sun is enriched in He"
        ],
        "answer": "A",
        "explanation": "Primitive meteorites lack volatile elements that can easily evaporate, whereas the Sun retains these elements in its composition."
    },
    {
        "question": "With few exceptions, the planets and other solar system objects orbit the Sun in the same direction. What concept of classical physics explains this observation?",
        "options": [
            "A: Conservation of energy",
            "B: Conservation of angular momentum",
            "C: Kepler’s law"
        ],
        "answer": "B",
        "explanation": "The protoplanetary disk's rotation led to most objects conserving angular momentum, causing them to orbit in the same direction."
    },
    {
        "question": "Which of the following parameters most affected the bulk density of solar system planets at present?",
        "options": [
            "A: Element compositions in the protoplanetary disk",
            "B: Condensation temperatures in the protoplanetary disk",
            "C: Self-gravity of the planets"
        ],
        "answer": "A",
        "explanation": "The initial elemental composition of the protoplanetary disk determined the rocky or gaseous nature of planets, strongly influencing their bulk density."
    },
    {
        "question": "In comparison to Earth's orbit, the intensity of sunlight at the orbit of Jupiter is reduced by:",
        "options": [
            "A: 1 / 5",
            "B: 1 / 5^2",
            "C: 1 / 5^3"
        ],
        "answer": "B",
        "explanation": "The intensity of sunlight decreases with the square of distance from the Sun. Jupiter is about 5 AU from the Sun, so intensity is 1/25 of that at Earth."
    },
    {
        "question": "Discuss how the Hill sphere changes when the planet mass m increases.",
        "options": [
            "A: The Hill sphere radius increases with m^(1/3)",
            "B: The Hill sphere radius decreases with m^(1/3)",
            "C: The Hill sphere radius is independent of m",
            "D: The Hill sphere radius increases linearly with m"
        ],
        "answer": "A",
        "explanation": "The Hill sphere radius r_Hill is proportional to (m/3M)^(1/3) R, so increasing the planet’s mass increases the radius of the region where it can dominate satellite orbits."
    },
    {
        "question": "Discuss how the Hill sphere changes when the distance R between planet and star increases.",
        "options": [
            "A: The Hill sphere radius increases linearly with R",
            "B: The Hill sphere radius decreases linearly with R",
            "C: The Hill sphere radius is independent of R",
            "D: The Hill sphere radius increases with R^(1/3)"
        ],
        "answer": "A",
        "explanation": "The Hill sphere radius is directly proportional to the planet-star distance R, so moving farther from the star expands the gravitational sphere of influence."
    },
    {
        "question": "Give an example of a primary planetary atmosphere.",
        "options": [
            "A: Jupiter’s hydrogen-helium atmosphere",
            "B: Earth's nitrogen-oxygen atmosphere",
            "C: Mars' thin carbon dioxide atmosphere",
            "D: Pluto’s nitrogen-methane atmosphere"
        ],
        "answer": "A",
        "explanation": "Primary atmospheres are captured from the solar nebula, like Jupiter’s hydrogen-helium envelope. Secondary atmospheres form later through outgassing or impacts."
    },
    {
        "question": "Give an example of a secondary planetary atmosphere.",
        "options": [
            "A: Jupiter’s hydrogen-helium atmosphere",
            "B: Earth’s nitrogen-oxygen atmosphere",
            "C: Neptune’s hydrogen-helium atmosphere",
            "D: Saturn’s hydrogen-helium atmosphere"
        ],
        "answer": "B",
        "explanation": "Secondary atmospheres form after the planet's formation, often via outgassing or biological activity, like Earth's atmosphere."
    },
    {
        "question": "What does 'hydrostatic equilibrium' describe in an atmosphere?",
        "options": [
            "A: Balance between gravitational force and pressure gradient",
            "B: Balance between centrifugal and gravitational forces",
            "C: The thermal balance between radiation and conduction",
            "D: The balance between atmospheric convection and rotation"
        ],
        "answer": "A",
        "explanation": "Hydrostatic equilibrium occurs when the downward gravitational force is balanced by the upward pressure gradient in a planetary atmosphere."
    },
    {
        "question": "The Sun follows an 11-year-long solar cycle. How do sunspots change during this cycle?",
        "options": [
            "A: Their number increases and decreases periodically",
            "B: Their size increases but number stays constant",
            "C: They move from poles to equator only",
            "D: They disappear entirely at maximum"
        ],
        "answer": "A",
        "explanation": "Sunspots vary in number with the solar cycle, peaking at solar maximum and decreasing at solar minimum."
    },
     {
        "question": "What is the origin of the name Allende given to the meteorite found in 1969?",
        "options": [
            "A: The name was chosen because of the writer with the same name",
            "B: It was found in northern Mexico, near the village of Pueblito de Allende",
            "C: It is by convention named after the person who discovered it in Northern Mexico"
        ],
        "answer": "B",
        "explanation": "The Allende meteorite was named after the village of Pueblito de Allende in northern Mexico where it was found in 1969."
    },
    {
        "question": "Which of the products of the reactions in the interior of the Sun reaches the Earth?",
        "options": [
            "A: Atomic nuclei in the solar wind",
            "B: Photons from the solar light",
            "C: Neutrinos"
        ],
        "answer": "C",
        "explanation": "Neutrinos produced in the Sun’s core escape directly and reach Earth almost immediately, unlike photons which take thousands of years to emerge."
    },
    {
        "question": "Which of these objects is observed in the solar system?",
        "options": [
            "A: Exoplanets",
            "B: Brown dwarfs",
            "C: Dwarf planets"
        ],
        "answer": "C",
        "explanation": "Dwarf planets like Pluto and Ceres are small solar system objects, whereas exoplanets and brown dwarfs exist outside the solar system."
    },
    {
        "question": "What is the approximate temperature in the interior of the Sun?",
        "options": [
            "A: 10^5 – 10^6 K",
            "B: 6000 K",
            "C: 15 × 10^6 K"
        ],
        "answer": "C",
        "explanation": "The core temperature of the Sun is around 15 million Kelvin, which is required for nuclear fusion to occur."
    },
    {
        "question": "With few exceptions, the planets and other solar system objects orbit the Sun in the same direction. What concept of classical physics explains this?",
        "options": [
            "A: Conservation of energy",
            "B: Conservation of angular momentum",
            "C: Kepler’s law"
        ],
        "answer": "B",
        "explanation": "The initial rotation of the protoplanetary disk is conserved as angular momentum, causing most bodies to orbit in the same direction."
    },
    {
        "question": "Asteroid families describe asteroids with:",
        "options": [
            "A: Similar composition",
            "B: Similar orbital parameters, inclination and semi-major axis",
            "C: Similar size and bulk density"
        ],
        "answer": "B",
        "explanation": "Asteroid families are groups of asteroids sharing similar orbits, likely formed from the breakup of a parent body."
    },
    {
        "question": "Pluto is not classified as a planet anymore because:",
        "options": [
            "A: It turned out its shape is not spherical",
            "B: It turned out it does not have an atmosphere",
            "C: It does not clear its orbital region from other objects"
        ],
        "answer": "C",
        "explanation": "Pluto does not dominate its orbit, which is one of the criteria for full planet classification under IAU rules."
    },
    {
        "question": "How was the first extra-solar planet around a main-sequence star discovered?",
        "options": [
            "A: By transit observation",
            "B: By Doppler shift observation",
            "C: By thermal emission observation"
        ],
        "answer": "B",
        "explanation": "The first exoplanet around a main-sequence star was detected using the Doppler shift in the host star's spectrum caused by the planet’s gravitational pull."
    },
    {
        "question": "Which of the following parameters most affected the bulk density of solar system planets at present?",
        "options": [
            "A: Element compositions in the protoplanetary disk",
            "B: Condensation temperatures in the protoplanetary disk",
            "C: Self-gravity of the planets"
        ],
        "answer": "A",
        "explanation": "The initial elemental composition of the protoplanetary disk determines whether a planet becomes rocky, icy, or gaseous, which strongly affects its density."
    },
    {
        "question": "Several different observations of the Sun are made to monitor the progress of its 11-year cycle; which of the listed parameters is NOT typically used to monitor the solar cycle?",
        "options": [
            "A: Sunspot number",
            "B: Solar flux at radio wavelength",
            "C: Solar neutrino flux"
        ],
        "answer": "C",
        "explanation": "Solar neutrino flux is not typically used to monitor the solar cycle because neutrino production in the Sun's core remains relatively constant; sunspots and radio flux vary with the cycle."
    },
    {
        "question": "The Sun follows a periodic change of activity of approximately 11 years. Which of the following parameters is commonly used to measure this cycle?",
        "options": [
            "A: Sunspot number",
            "B: Solar neutrino flux",
            "C: Orbital eccentricity of planets"
        ],
        "answer": "A",
        "explanation": "The number of sunspots is the primary observable used to track the Sun's 11-year cycle, as it directly reflects solar magnetic activity."
    },
    {
        "question": "Despite the observation of dark sunspots during solar maximum, why is the Earth's atmosphere found to be slightly warmer during solar maximum than during solar minimum?",
        "options": [
            "A: Increased solar radiation in other wavelengths",
            "B: Increased reflection from sunspots",
            "C: Decrease in solar wind velocity"
        ],
        "answer": "A",
        "explanation": "Sunspots themselves are cooler, but the overall solar output increases due to bright regions called faculae, which increases the total solar energy reaching Earth."
    },
    {
        "question": "Which object is used to estimate the flux of interplanetary meteoroids at Mars?",
        "options": [
            "A: Crater counts on Mars and its moons",
            "B: Orbital period of Mars",
            "C: Solar rotation period"
        ],
        "answer": "A",
        "explanation": "Meteor flux estimates are derived from crater counts on Mars, Phobos, and Deimos, as well as direct meteor observations."
    },
    {
        "question": "Which of the following best describes a Sun-synchronous orbit?",
        "options": [
            "A: An orbit where the spacecraft always passes over the same solar longitude at the same local solar time",
            "B: An orbit where the spacecraft remains stationary relative to the Sun",
            "C: An orbit where the spacecraft stays at a fixed distance from the Earth"
        ],
        "answer": "A",
        "explanation": "A Sun-synchronous orbit precesses so that the spacecraft passes over any given point on the Sun (or Earth) at the same local solar time, useful for continuous observations."
    },
    {
        "question": "A spacecraft travels from Earth to Mars using a Hohmann transfer orbit. Which of the following statements is correct?",
        "options": [
            "A: It follows an elliptical path tangent to Earth's and Mars' orbits",
            "B: It follows a circular path at constant speed",
            "C: It requires instantaneous acceleration at the midpoint of the orbit"
        ],
        "answer": "A",
        "explanation": "A Hohmann transfer orbit is an elliptical trajectory tangent to the departure and arrival orbits, optimized for minimum energy transfer."
    },
{
        "question": "When estimating the flux of interplanetary objects from crater counts on Mars, Phobos, and Deimos, why could the crater counts lead to different estimates?",
        "options": [
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
        "options": [
            "A: Neutrinos",
            "B: Atomic nuclei in the solar wind",
            "C: Photons from the solar light"
        ],
        "answer": "A",
        "explanation": "Neutrinos interact very weakly with matter and can escape the Sun’s core almost immediately, reaching Earth directly. Photons from the core take thousands of years to reach the surface, and atomic nuclei in the solar wind originate from the Sun’s outer layers, not its core fusion reactions."
    },
    {
        "question": "The first exoplanet around a main-sequence star was discovered by:",
        "options": [
            "A: Its thermal emission brightness",
            "B: The Doppler shift in the spectrum of its host star",
            "C: Its transit reducing the brightness of the host star"
        ],
        "answer": "B",
        "explanation": "The first exoplanet around a main-sequence star was detected using Doppler spectroscopy, observing the wobble of the star caused by the planet's gravitational pull."
    },
    {
        "question": "Which of the following parameters most affected the bulk density of solar system planets at present?",
        "options": [
            "A: Element compositions in the protoplanetary disk",
            "B: Condensation temperatures in the protoplanetary disk",
            "C: Self-gravity of the planets"
        ],
        "answer": "A",
        "explanation": "The bulk density of planets is primarily determined by their elemental composition, which depends on the materials present in the protoplanetary disk during formation."
    },
    {
        "question": "With few exceptions the planets and other solar system objects orbit the Sun in the same direction. What concept of classical physics explains this observation?",
        "options": [
            "A: Conservation of energy",
            "B: Conservation of angular momentum",
            "C: Kepler’s laws"
        ],
        "answer": "B",
        "explanation": "The conservation of angular momentum from the rotating protoplanetary disk causes most objects to orbit in the same direction around the Sun."
    },
    {
        "question": "What is the main difference when solar element abundance and element abundance of a primitive meteorite are compared?",
        "options": [
            "A: The meteorite contains aminoacids",
            "B: The meteorite contains less He because the Sun is enriched in He",
            "C: The meteorite contains smaller amounts of the volatile elements"
        ],
        "answer": "C",
        "explanation": "Meteorites typically have fewer volatile elements compared to the Sun, which loses some of these elements during formation and evolution."
    },
    {
        "question": "The moons of the solar system planets are typically located:",
        "options": [
            "A: Inside the Roche limit of the planet",
            "B: Inside the Hill sphere of the planet",
            "C: Inside the Jeans radius"
        ],
        "answer": "B",
        "explanation": "Moons orbit within the Hill sphere, which defines the region where a planet’s gravity dominates over the Sun’s, allowing stable satellite orbits."
    },
    {
        "question": "Asteroid families describe asteroids with:",
        "options": [
            "A: Similar composition",
            "B: Similar orbital parameters, inclination and semimajor axis",
            "C: Similar size and bulk density"
        ],
        "answer": "B",
        "explanation": "Asteroid families are identified based on clustering in orbital parameters, such as semimajor axis, eccentricity, and inclination, often indicating a common origin from a parent body."
    },
    {
        "question": "Explain what the differential equation of hydrostatic equilibrium (∇P = -gρ) means for a planetary atmosphere.",
        "options": [
            "A: It describes the balance between pressure gradient and gravitational force in the atmosphere",
            "B: It calculates the temperature profile of the atmosphere",
            "C: It describes the chemical composition of the atmosphere"
        ],
        "answer": "A",
        "explanation": "Hydrostatic equilibrium states that the upward pressure gradient force balances the downward gravitational force, maintaining atmospheric stability."
    },
    {
        "question": "Which assumptions were made to derive the hydrostatic equilibrium equation from the full momentum equation?",
        "options": [
            "A: Neglecting viscosity and acceleration, assuming steady-state conditions",
            "B: Assuming the atmosphere is incompressible",
            "C: Ignoring gravitational effects"
        ],
        "answer": "A",
        "explanation": "Deriving hydrostatic equilibrium assumes a steady-state, negligible viscosity, and small vertical accelerations compared to gravity."
    },
    {
    "question": "The Giant planets grew in the protoplanetary disk by:",
    "options": [
        "A: collecting smaller planets",
        "B: accumulation of planetesimals, dust, and gas",
        "C: gravitational collapse"
    ],
    "answer": "B",
    "explanation": "Giant planets formed by gradually accumulating solids and gas from the protoplanetary disk, not by collecting other planets or direct collapse."
    },
    {
        "question": "Light emitted from the Sun reaches Earth within about 8 minutes. The solar wind emitted at the same time reaches Earth:",
        "options": [
            "A: at the same time",
            "B: earlier",
            "C: later"
        ],
        "answer": "C",
        "explanation": "Solar wind particles travel much slower than light, so they reach Earth later than photons from sunlight."
    },
    {
        "question": "The blackbody temperature of the Earth's moon is:",
        "options": [
            "A: significantly higher because the moon is exposed to the solar wind and Earth is not",
            "B: significantly lower because the moon's radius is less than 1/3 of Earth's radius",
            "C: the same because both are at the same distance from the Sun"
        ],
        "answer": "C",
        "explanation": "The Moon and Earth are at nearly the same distance from the Sun, so their equilibrium blackbody temperatures are approximately the same."
    },
    {
        "question": "The blackbody temperature of Venus is:",
        "options": [
            "A: higher than that of the Earth",
            "B: lower than that of the Earth",
            "C: about the same, because both planets have about the same size"
        ],
        "answer": "A",
        "explanation": "Venus is hotter than Earth due to its thick CO2 atmosphere, which traps heat via the greenhouse effect."
    },
    {
        "question": "The solar system comets contain dust and ice because:",
        "options": [
            "A: they are fragments of the outer icy planets",
            "B: they formed outside of the ice line in the protoplanetary cloud",
            "C: they formed in the cold interstellar medium"
        ],
        "answer": "B",
        "explanation": "Comets formed beyond the ice line in the protoplanetary disk where temperatures were low enough for ices to condense, along with dust."
    },
    {
        "question": "Most of the solar wind particles that reach the Earth are:",
        "options": [
            "A: absorbed in the Earth's atmosphere",
            "B: deflected by the Earth's magnetic field",
            "C: reach the surface of the Earth without interaction"
        ],
        "answer": "B",
        "explanation": "Earth's magnetic field deflects most solar wind particles, protecting the surface from direct impact."
    },
    {
        "question": "The term 'habitable zone' is used in astronomy to describe the:",
        "options": [
            "A: region in the solar system that is within the ice line",
            "B: region around a star where Earth-like planets can have liquid water on the surface",
            "C: region in the Milky Way where main sequence stars exist"
        ],
        "answer": "B",
        "explanation": "The habitable zone is defined as the orbital region around a star where temperatures allow liquid water to exist on a planet's surface."
    },
    {
        "question": "The ring systems of planets were discovered in the 20th century. There is one exception:",
        "options": [
            "A: Saturn’s rings are so massive that they are visible even with small telescopes",
            "B: Uranus’ rings were known by astronomers for centuries because they occult stars",
            "C: Jupiter’s rings are easily observed because Jupiter is the giant planet closest to Earth"
        ],
        "answer": "A",
        "explanation": "Saturn's rings are visible even with small telescopes, unlike the faint rings of other planets which required modern observations."
    },
    {
        "question": "Which of these objects is/are located in Lagrange points of the Sun–Earth system:",
        "options": [
            "A: the Jupiter trojans",
            "B: ESA’s Solar Heliospheric Observatory spacecraft: SOHO",
            "C: the Mars trojans"
        ],
        "answer": "B",
        "explanation": "SOHO is located near the Sun–Earth L1 Lagrange point to continuously monitor the Sun."
    },
    {
        "question": "What is the main process of heat transfer from Sun to planets:",
        "options": [
            "A: diffusion",
            "B: convection",
            "C: radiation"
        ],
        "answer": "C",
        "explanation": "Energy from the Sun reaches planets primarily via radiation, not conduction or convection."
    },
    {
        "question": "Long-period comets are observed when they approach the vicinity of the Sun from:",
        "options": [
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
        random.sample(q["options"], len(q["options"])) for q in st.session_state.shuffled_questions
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
