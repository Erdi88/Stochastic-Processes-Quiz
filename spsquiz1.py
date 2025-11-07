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
