science_practices = [
    "Science Practice 1.A: Describe the components of and quantitative information from models and representations that illustrate particulate-level properties only.", "Science Practice 1.B: Describe the components of and quantitative information from models and representations that illustrate macroscopic-level properties only.",
    "Science Practice 2.A: Identify a testable scientific question based on an observation, data, or a model.", "Science Practice 2.B: Formulate a hypothesis or predict the results of an experiment.", "Science Practice 2.C: Identify experimental procedures that are aligned to a scientific question (which may include a sketch of a lab setup).", "Science Practice 2.D: Make observations or collect data from representations of laboratory setups or results, while attending to precision where appropriate.", "Science Practice 2.E: Identify or describe potential sources of experimental error.", "Science Practice 2.F: Explain how modifications to an experimental procedure will alter results.",
    "Science Practice 4.A: Predict and/or explain chemical properties or phenomena (e.g., of atoms or molecules) using given chemical theories, models, and representations.", "Science Practice 4.B: Explain whether a model is consistent with chemical theories.", "Science Practice 4.C: Explain the connection between particulate-level and macroscopic properties of a substance using models and representations.", "Science Practice 4.D: Explain the degree to which a model or representation describes the connection between particulate-level properties and macroscopic properties.",
    "Science Practice 5.A: Identify quantities needed to solve a problem from given information (e.g., text, mathematical expressions, graphs, or tables).", "Science Practice 5.B: Identify an appropriate theory, definition, or mathematical relationship to solve a problem.", "Science Practice 5.C: Explain the relationship between variables within an equation when one variable changes.", "Science Practice 5.D: Identify information presented graphically to solve a problem.", "Science Practice 5.E: Determine a balanced chemical equation for a given chemical phenomenon.", "Science Practice 5.F: Calculate, estimate, or predict an unknown quantity from known quantities by selecting and following a logical computational pathway and attending to precision (e.g., performing dimensional analysis and attending to significant figures).",
    "Science Practice 6.A: Make a scientific claim.", "Science Practice 6.B: Support a claim with evidence from experimental data.", "Science Practice 6.C: Support a claim with evidence from representations or models at the particulate level, such as the structure of atoms and/or molecules.", "Science Practice 6.D: Provide reasoning to justify a claim using chemical principles or laws, or using mathematical justification.", "Science Practice 6.E: Provide reasoning to justify a claim using connections between particulate and macroscopic scales or levels.", "Science Practice 6.F: Explain the connection between experimental results and chemical concepts, processes, or theories.", "Science Practice 6.G: Explain how potential sources of experimental error may affect the experimental results."
]
science_practice_codes = [
    "1.A", "1.B", "2.A", "2.B", "2.C", "2.D", "2.E", "2.F", "4.A", "4.B", "4.C", "4.D", "5.A", "5.B", "5.C", "5.D", "5.E", "5.F", "6.A", "6.B", "6.C", "6.D", "6.E", "6.F", "6.G"
]

class essential_knowledge:
    def __init__(self, topic, learning_objective, essential_knowledge, recommended_practice):
        self.topic = topic
        self.learning_objective = learning_objective
        self.essential_knowledge = essential_knowledge
        self.recommended_practice = recommended_practice

    def __repr__(self):
        return (
            f"essential_knowledge(\n"
            f"    topic={repr(self.topic)},\n"
            f"    recommended_practice={repr(self.recommended_practice)},\n"
            f"    learning_objective={repr(self.learning_objective)},\n"
            f"    essential_knowledge={repr(self.essential_knowledge)}\n"
            f")"
        )

json_data = [
    {
        "messages": [
            {"role": "user", "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 1.1, Moles and Molar Mass?"},
            {"role": "assistant", "content": "Learning Objective 1.1A: Calculate quantities of a substance or its relative number of particles using dimensional analysis and the mole concept. > (Essential Knowledge 1.1.A.1: One cannot count particles directly while performing laboratory work. Thus, there must be a connection between the masses of substances reacting and the actual number of particles undergoing chemical changes. Essential Knowledge 1.1.A.2: Avogadro’s number (N = 6.022 × 10^23 mol−1) provides the connection between the number of moles in a pure sample of a substance and the number of constituent particles (or formula units) of that substance. Essential Knowledge 1.1.A.3: Expressing the mass of an individual atom or molecule in atomic mass units (amu) is useful because the average mass in amu of one particle (atom or molecule) or formula unit of a substance will always be numerically equal to the molar mass of that substance in grams. Thus, there is a quantitative connection between the mass of a substance and the number of particles that the substance contains. EQN: n = m/M)"}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 1.2, Mass Spectra of Elements?"},
            {"role": "assistant", "content": "Learning Objective 1.2A: Explain the quantitative relationship between the mass spectrum of an element and the masses of the element’s isotopes. > (Essential Knowledge 1.2.A.1: The mass spectrum of a sample containing a single element can be used to determine the identity of the isotopes of that element and the relative abundance of each isotope in nature. Essential Knowledge 1.2.A.2: The average atomic mass of an element can be estimated from the weighted average of the isotopic masses using the mass of each isotope and its relative abundance. [Exclusion Statement: Interpreting mass spectra of samples containing multiple elements or peaks arising from species other than singly charged monatomic ions will not be assessed on the AP Exam.])"}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 1.3, Elemental Composition of Pure Substances?"},
            {"role": "assistant", "content": "Learning Objective 1.3A: Explain the quantitative relationship between the elemental composition by mass and the empirical formula of a pure substance. > (Essential Knowledge 1.3.A.1: Some pure substances are composed of individual molecules, while others consist of atoms or ions held together in fixed proportions as described by a formula unit. Essential Knowledge 1.3.A.2: According to the law of definite proportions, the ratio of the masses of the constituent elements in any pure sample of that compound is always the same. Essential Knowledge 1.3.A.3: The chemical formula that lists the lowest whole number ratio of atoms of the elements in a compound is called the empirical formula.)"}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 1.4, Composition of Mixtures?"},
            {"role": "assistant", "content": "Learning Objective 1.4A: Explain the quantitative relationship between the elemental composition by mass and the composition of substances in a mixture. > (Essential Knowledge 1.4.A.1: Pure substances contain atoms, molecules, or formula units of a single type. Mixtures contain atoms, molecules, or formula units of two or more types, whose relative proportions can vary. Essential Knowledge 1.4.A.2: Elemental analysis can be used to determine the relative numbers of atoms in a compound.)"}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 1.5, Atomic Structure and Electron Configuration?"},
            {"role": "assistant", "content": "Learning Objective 1.5A: Represent the ground-state electron configuration of an atom of an element or its ions using the Aufbau principle. > (Essential Knowledge 1.5.A.1: The atom is composed of negatively charged electrons and a positively charged nucleus that is made of protons and neutrons. Essential Knowledge 1.5.A.2: Coulomb’s law is used to calculate the force between two charged particles. EQN: Fcoulombic ∝ q1q2/r^2 Essential Knowledge 1.5.A.3: In atoms and ions, the electrons can be thought of as being in “shells (energy levels)” and “subshells (sublevels),” as described by the ground-state electron configuration. Inner electrons are called core electrons, and outer electrons are called valence electrons. The electron configuration is explained by quantum mechanics, as delineated in the Aufbau principle and exemplified in the periodic table of the elements. [Exclusion Statement: The assignment of quantum numbers to electrons in subshells of an atom will not be assessed on the AP Exam.] Essential Knowledge 1.5.A.4: The relative energy required to remove an electron from different subshells of an atom or ion or from the same subshell in different atoms or ions (ionization energy) can be estimated through a qualitative application of Coulomb’s law. This energy is related to the distance from the nucleus and the effective (shield) charge of the nucleus.)"}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 1.6, Photoelectron Spectroscopy?"},
            {"role": "assistant", "content": "Learning Objective 1.6A: Explain the relationship between the photoelectron spectrum of an atom or ion and: i. The ground-state electron configuration of the species. ii. The interactions between the electrons and the nucleus. > (Essential Knowledge 1.6.A.1: The energies of the electrons in a given shell can be measured experimentally with photoelectron spectroscopy (PES). The position of each peak in the PES spectrum is related to the energy required to remove an electron from the corresponding subshell, and the relative height of each peak is (ideally) proportional to the number of electrons in that subshell.)"}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 1.7, Periodic Trends?"},
            {"role": "assistant", "content": "Learning Objective 1.7A: Explain the relationship between trends in atomic properties of elements and electronic structure and periodicity. > (Essential Knowledge 1.7.A.1: The organization of the periodic table is based on patterns of recurring properties of the elements, which are explained by patterns of ground-state electron configurations and the presence of completely or partially filled shells (and subshells) of electrons in atoms. [Exclusion Statement: Writing the electron configuration of elements that are exceptions to the aufbau principle will not be assessed on the AP Exam.] Essential Knowledge 1.7.A.2: Trends in atomic properties within the periodic table (periodicity) can be predicted by the position of the element on the periodic table and qualitatively understood using Coulomb’s law, the shell model, and the concepts of shielding and effective nuclear charge. These properties include: i. Ionization energy ii. Atomic and ionic radii iii. Electron affinity iv. Electronegativity. Essential Knowledge 1.7.A.3: The periodicity (in 1.7.A.2) is useful to predict/estimate values of properties in the absence of data.)"}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 1.8, Valence Electrons and Ionic Compounds?"},
            {"role":"assistant", "content": "Learning Objective 1.8A: Explain the relationship between trends in the reactivity of elements and periodicity. > (Essential Knowledge 1.8.A.1: The likelihood that two elements will form a chemical bond is determined by the interactions between the valence electrons and nuclei of elements. Essential Knowledge 1.8.A.2: Elements in the same column of the periodic table tend to form analogous compounds. Essential Knowledge 1.8.A.3: Typical charges of atoms in ionic compounds are governed by the number of valence electrons and predicted by their location on the periodic table.)"}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 2.1, Types of Chemical Bonds?"},
            {"role": "assistant", "content": "Learning Objective 2.1.A: Explain the relationship between the type of bonding and the properties of the elements participating in the bond. > (Essential Knowledge 2.1.A.1: Electronegativity values for the representative elements increase going from left to right across a period and decrease going down a group. These trends can be understood qualitatively through the electronic structure of the atoms, the shell model, and Coulomb’s law. Essential Knowledge 2.1.A.2: Valence electrons shared between atoms of similar electronegativity constitute a nonpolar covalent bond. For example, bonds between carbon and hydrogen are effectively nonpolar even though carbon is slightly more electronegative than hydrogen. Essential Knowledge 2.1.A.3: Valence electrons shared between atoms of unequal electronegativity constitute a polar covalent bond. i. The atom with a higher electronegativity will develop a partial negative charge relative to the other atom in the bond. ii. In single bonds, greater differences in electronegativity lead to greater bond dipoles. iii. All polar bonds have some ionic character, and the difference between ionic and covalent bonding in not distinct but rather a continuum. Essential Knowledge 2.1.A.4: The difference in electronegativity is not the only factor in determining if a bond should be designated as ionic or covalent. Generally, bonds between a metal and nonmetal are ionic, and bonds between two nonmetals are covalent. Examination of the properties of a compound is the best way to characterize the type of bonding. Essential Knowledge 2.1.A.5: In a metallic solid, the valence electrons from the metal atoms are considered to be delocalized and not associated with any individual atom.)"}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 2.2, Intramolecular Force and Potential Energy?"},
            {"role": "assistant", "content": "Learning Objective 2.2.A: Represent the relationship between potential energy and distance between atoms, based on factors that influence the interaction strength. > (Essential Knowledge 2.2.A.1: A graph of potential energy versus the distance between atoms (internuclear distance) is a useful representation for describing the interactions between atoms. Such graphs illustrate both the equilibrium bond length (the separation between atoms at which the potential energy is lowest) and the bond energy (the energy required to separate the atoms). Essential Knowledge 2.2.A.2: In a covalent bond, the bond length is influenced by both the size of the atom’s core and the bond order (i.e., single, double, triple). Bonds with a higher order are shorter and have larger bond energies. Essential Knowledge 2.2.A.3: Coulomb’s law can be used to understand the strength of interactions between cations and anions. i. Because the interaction strength is proportional to the charge on each ion, larger charges lead to stronger interactions. ii. Because the interaction strength increases as the distance between the centers of the ions (nuclei) decreases, smaller ions lead to stronger interactions.)"}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 2.3, Structure of Ionic Solids?"},
            {"role": "assistant", "content": "Learning Objective 2.3.A: Represent an ionic solid with a particulate model that is consistent with Coulomb’s law and the properties of the constituent ions. > (Essential Knowledge 2.3.A.1: The cations and anions in an ionic crystal are arranged in a systematic, periodic 3-D array that maximizes the attractive forces among cations and anions while minimizing the repulsive forces. [Exclusion Statement: Knowledge of specific crystal structures is not essential to an understanding of the learning objective and will not be assessed on the AP Exam.])"}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 2.4, Structure of Metals and Alloys?"},
            {"role": "assistant", "content": "Learning Objective 2.4.A: Represent a metallic solid and/or alloy using a model to show essential characteristics of the structure and interactions present in the substance. > (Essential Knowledge 2.4.A.1: Metallic bonding can be represented as an array of positive metal ions surrounded by delocalized valence electrons (i.e., a “sea of electrons”). Essential Knowledge 2.4.A.2: Interstitial alloys form between atoms of significantly different radii, where the smaller atoms fill the interstitial spaces between the larger atoms (e.g., with steel in which carbon occupies the interstices in iron). Essential Knowledge 2.4.A.3: Substitutional alloys form between atoms of comparable radius, where one atom substitutes for the other in the lattice. (e.g., in certain brass alloys, other elements, usually zinc, substitute for copper.)"}
            ]
    },
    {
        "messages": [
            {"role": "user", "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 2.5, Lewis Diagrams?"},
            {"role": "assistant", "content": "Learning Objective 2.5.A: Represent a molecule with a Lewis diagram. > (Essential Knowledge 2.5.A.1: Lewis diagrams can be constructed according to an established set of principles.)"}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 2.6, Resonance and Formal Charge?"},
            {"role": "assistant", "content": "Learning Objective 2.6.A: Represent a molecule with a Lewis diagram that accounts for resonance between equivalent structures or that uses formal charge to select between nonequivalent structures. > (Essential Knowledge 2.6.A.1: In cases where more than one equivalent Lewis structure can be constructed, resonance must be included as a refinement to the Lewis structure. In many such cases, this refinement is needed to provide qualitatively accurate predictions of molecular structure and properties. Essential Knowledge 2.6.A.2: The octet rule and formal charge can be used as criteria for determining which of several possible valid Lewis diagrams provides the best model for predicting molecular structure and properties. Essential Knowledge 2.6.A.3: As with any model, there are limitations to the use of the Lewis structure model, particularly in cases with an odd number of valence electrons.)"}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 2.7, VSEPR and Hybridization?"},
            {"role": "assistant", "content": "Learning Objective 2.7.A: Based on the relationship between Lewis diagrams, VSEPR theory, bond orders, and bond polarities: i. Explain structural properties of molecules. ii. Explain electron properties of molecules. > (Essential Knowledge 2.7.A.1: VSEPR theory uses the Coulombic repulsion between electrons as a basis for predicting the arrangement of electron pairs around a central atom. Essential Knowledge 2.7.A.2: Both Lewis diagrams and VSEPR theory must be used for predicting electronic and structural properties of many covalently bonded molecules and polyatomic ions, including the following: i. Molecular geometry (linear, trigonal planar, tetrahedral, trigonal pyramidal, bent, trigonal bipyramidal, seesaw, T-shaped, octahedral, square pyramidal, square planar) ii. Bond angles iii. Relative bond energies based on bond order iv. Relative bond lengths (multiple bonds, effects of atomic radius) v. Presence of a dipole moment vi. Hybridization of valence orbitals for atoms within a molecule or polyatomic ion. Essential Knowledge 2.7.A.3: The terms “hybridization” and “hybrid atomic orbital” are used to describe the arrangement of electrons around a central atom. When the central atom is sp hybridized, its ideal bond angles are 180°; for sp2 hybridized atoms the bond angles are 120°; and for sp3 hybridized atoms the bond angles are 109.5°. Essential Knowledge 2.7.A.4: Bond formation is associated with overlap between atomic orbitals. In multiple bonds, such overlap leads to the formation of both sigma and pi bonds. The overlap is stronger in sigma than pi bonds, which is reflected in sigma bonds having greater bond energy than pi bonds. The presence of a pi bond also prevents the rotation of the bond and leads to geometric isomers.)"}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 3.1, Intermolecular and Interparticle Forces?"},
            {"role": "assistant", "content": "Learning Objective 3.1.A: Explain the relationship between the chemical structures of molecules and the relative strength of their intermolecular forces when: i. The molecules are of the same chemical species. ii. The molecules are of two different chemical species. > (Essential Knowledge 3.1.A.1: London dispersion forces are a result of the Coulombic interactions between temporary, fluctuating dipoles. London dispersion forces are often the strongest net intermolecular force between large molecules. i. Dispersion forces increase with increasing contact area between molecules and with increasing polarizability of the molecules. ii. The polarizability of a molecule increases with an increasing number of electrons in the molecule and the size of the electron cloud. It is enhanced by the presence of pi bonding. iii. The term “London dispersion forces” should be used synonymously with the term “van der Waals forces”. Essential Knowledge 3.1.A.2: The dipole moment of a polar molecule leads to additional interactions with other chemical species. Essential Knowledge 3.1.A.3: Hydrogen bonding is a special type of dipole-dipole interaction that occurs when a hydrogen atom is bonded to a highly electronegative atom (e.g., N, O, F) and is attracted to an unshared pair of electrons on another electronegative atom. Essential Knowledge 3.1.A.4: The strength of hydrogen bonding is greater than that of dipole-dipole interactions and London dispersion forces. Essential Knowledge 3.1.A.5: The strength of intermolecular forces can be used to predict the boiling points of molecular compounds. Essential Knowledge 3.1.A.6: The strength of intermolecular forces can be used to predict the solubility of molecular compounds in various solvents.)"}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 3.2, Properties of Solutions?"},
            {"role": "assistant", "content": "Learning Objective 3.2.A: Explain the relationship between the properties of solutions and the nature of the solute and solvent. > (Essential Knowledge 3.2.A.1: The properties of a solution are determined by the nature of the solute and solvent. Essential Knowledge 3.2.A.2: The concentration of a solution can be expressed in various ways, including molarity, molality, mole fraction, and percent by mass. Essential Knowledge 3.2.A.3: The colligative properties of a solution depend on the number of solute particles in the solution. These properties include: i. Vapor pressure lowering ii. Boiling point elevation iii. Freezing point depression iv. Osmotic pressure. Essential Knowledge 3.2.A.4: The colligative properties of a solution can be used to determine the molar mass of a solute.)"}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 3.3, Properties of Liquids?"},
            {"role": "assistant", "content": "Learning Objective 3.3.A: Represent the differences between solid, liquid, and gas phases using a particulate-level model. > (Essential Knowledge 3.3.A.1: Solids can be crystalline, where the particles are arranged in a regular three-dimensional structure, or they can be amorphous, where the particles do not have a regular, orderly arrangement. In both cases, the motion of the individual particles is limited, and the particles do not undergo overall translation with respect to each other. The structure of the solid is influenced by interparticle interactions and the ability of the particles to pack together. Essential Knowledge 3.3.A.2: The constituent particles in liquids are in close contact with each other, and they are continually moving and colliding. The arrangement and movement of particles are influenced by the nature and strength of the forces (e.g., polarity, hydrogen bonding, and temperature) between the particles. Essential Knowledge 3.3.A.3: The solid and liquid phases for a particular substance typically have similar molar volume because, in both phases, the constituent particles are in close contact at all times. Essential Knowledge 3.3.A.4: In the gas phase, the particles are in constant motion. Their frequencies of collision and the average spacing between them are dependent on temperature, pressure, and volume. Because of this constant motion, and minimal effects of forces between particles, a gas has neither a definite volume nor a definite shape. [Exclusion Statement: Understanding/interpreting phase diagrams will not be assessed on the AP Exam.])"}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 3.4, Ideal Gas Law?"},
            {"role": "assistant", "content": "Learning Objective 3.4.A: Explain the relationship between the macroscopic properties of a sample of gas or mixture of gases using the ideal gas law. > (Essential Knowledge 3.4.A.1: The macroscopic properties of ideal gases are related through the ideal gas law: EQN: PV = nRT. Essential Knowledge 3.4.A.2: In a sample containing a mixture of ideal gases, the pressure exerted by each component (the partial pressure) is independent of the other components. Therefore, the partial pressure of a gas within the mixture is proportional to its mole fraction (X), and the total pressure of the sample is the sum of the partial pressures. EQN: PA = Ptotal × XA, where XA = moles A/total moles; EQN: Ptotal = PA + PB + PC + … Essential Knowledge 3.4.A.3: Graphical representations of the relationships between P, V, T, and n are useful to describe gas behavior.)"}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 3.5, Kinetic Molecular Theory?"},
            {"role": "assistant", "content": "Learning Objective 3.5.A: Explain the relationship between the motion of particles and the macroscopic properties of gases with: i. The kinetic molecular theory (KMT). ii. A particulate model. iii. A graphical representation. > (Essential Knowledge 3.5.A.1: The kinetic molecular theory (KMT) relates the macroscopic properties of gases to motions of the particles in the gas. The Maxwell-Boltzmann distribution describes the distribution of the kinetic energies of particles at a given temperature. Essential Knowledge 3.5.A.2: All the particles in a sample of matter are in continuous, random motion. The average kinetic energy of a particle is related to its average velocity by the equation: EQN: KE = ½ mv^2. Essential Knowledge 3.5.A.3: The Kelvin temperature of a sample of matter is proportional to the average kinetic energy of the particles in the sample. Essential Knowledge 3.5.A.4: The Maxwell-Boltzmann distribution provides a graphical representation of the energies/velocities of particles at a given temperature.)"}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 3.6, Deviations from Ideal Gas Law?"},
            {"role": "assistant", "content": "Learning Objective 3.6.A: Explain the relationship among non-ideal behaviors of gases, interparticle forces, and/or volumes. > (Essential Knowledge 3.6.A.1: The ideal gas law does not explain the actual behavior of real gases. Deviations from the ideal gas law may result from interparticle attractions among gas molecules, particularly at conditions that are close to those resulting in condensation. Deviations may also arise from particle volumes, particularly at extremely high pressures.)"}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 3.7, Solutions and Mixtures?"},
            {"role": "assistant", "content": "Learning Objective 3.7.A: Calculate the number of solute particles, volume, or molarity of solutions. > (Essential Knowledge 3.7.A.1: Solutions, also sometimes called homogeneous mixtures, can be solids, liquids, or gases. In a solution, the macroscopic properties do not vary throughout the sample. In a heterogeneous mixture, the macroscopic properties depend on location in the mixture. Essential Knowledge 3.7.A.2: Solution composition can be expressed in a variety of ways; molarity is the most common method used in the laboratory. EQN: M = nsolute /Lsolution)"}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 3.8, Representations of Solutions?"},
            {"role": "assistant", "content": "Learning Objective 3.8.A: Using particulate models for mixtures: i. Represent interactions between components. ii. Represent concentrations of components. > (Essential Knowledge 3.8.A.1: Particulate representations of solutions communicate the structure and properties of solutions, by illustration of the relative concentrations of the components in the solution and/or drawings that show interactions among the components. Exclusion Statement: Colligative properties will not be assessed on the AP Exam. Exclusion Statement: Calculations of molality, percent by mass, and percent by volume for solutions will not be assessed on the AP Exam.)"}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 3.9, Separation of Solutions and Mixtures?"},
            {"role": "assistant", "content": "Learning Objective 3.9.A: Explain the results of a separation experiment based on intermolecular interactions. > (Essential Knowledge 3.9.A.1: The components of a liquid solution cannot be separated by filtration. They can, however, be separated using processes that take advantage of differences in the intermolecular interactions of the components. i. Chromatography (paper, thin-layer, and column) separates chemical species by taking advantage of the differential strength of intermolecular interactions between and among the components and with the surface components of the stationary phase. The resulting chromatogram can be used to infer the relative polarities of components in a mixture. ii. Distillation separates chemical species by taking advantage of the differential strength of intermolecular interactions between and among the components and the effects these interactions have on the vapor pressures of the components in the mixture.)"}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 3.10, Solubility?"},
            {"role": "assistant", "content": "Learning Objective 3.10.A: Explain the relationship between the solubility of ionic and molecular compounds in aqueous and nonaqueous solvents, and the intermolecular interactions between particles. > (Essential Knowledge 3.10.A.1: Substances with similar intermolecular interactions tend to be miscible or soluble in one another.)"}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 3.11, Spectroscopy and the Electromagnetic Spectrum?"},
            {"role": "assistant", "content": "Learning Objective 3.11.A: Explain the relationship between a region of the electromagnetic spectrum and the types of molecular or electronic transitions associated with that region. > (Essential Knowledge 3.11.A.1: Differences in absorption or emission of photons in different spectral regions are related to the different types of molecular motion or electronic transition: i. Microwave radiation is associated with transitions in molecular rotational levels. ii. Infrared radiation is associated with transitions in molecular vibrational levels. iii. Ultraviolet/visible radiation is associated with transitions in electronic energy levels.)"}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 3.12, Properties of Photons?"},
            {"role": "assistant", "content": "Learning Objective 3.12.A: Explain the properties of an absorbed or emitted photon in relationship to an electronic transition in an atom or molecule. > (Essential Knowledge 3.12.A.1: When a photon is absorbed (or emitted) by an atom or molecule, the energy of the species is increased (or decreased) by an amount equal to the energy of the photon. Essential Knowledge 3.12.A.2: The wavelength of the electromagnetic wave is related to its frequency and the speed of light by the equation: EQN: c = λν. The energy of a photon is related to the frequency of the electromagnetic wave through Planck’s equation: EQN: E = ℎν.)"}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 3.13, Beer-Lambert Law?"},
            {"role": "assistant", "content": "Learning Objective 3.13.A: Explain the amount of light absorbed by a solution of molecules or ions in relationship to the concentration, path length, and molar absorptivity. > (Essential Knowledge 3.13.A.1: The Beer-Lambert law relates the absorption of light by a solution to three variables according to the equation: EQN: A = εbc. The molar absorptivity, ε, describes how intensely a chemical species absorbs light of a specific wavelength. The path length, b, and concentration, c, are proportional to the number of light-absorbing particles in the light path. Essential Knowledge 3.13.A.2: In most experiments the path length and wavelength of light are held constant. In such cases, the absorbance is proportional only to the concentration of absorbing molecules or ions. The spectrophotometer is typically set to the wavelength of maximum absorbance (optimum wavelength) for the species being analyzed to ensure the maximum sensitivity of measurement.)"}
        ]
    },
    {
        "messages": [
            {
                "role": "user",
                "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 4.1, Introduction For Reactions?"
            },
            {
                "role": "assistant",
                "content": "Learning Objective 4.1.A: Identify evidence of chemical and physical changes in matter. > (Essential Knowledge 4.1.A.1: A physical change occurs when a substance undergoes a change in properties but not a change in composition. Changes in the phase of a substance (solid, liquid, gas) or formation/separation of mixtures of substances are common physical changes. Essential Knowledge 4.1.A.2: A chemical change occurs when substances are transformed into new substances, typically with different compositions. Production of heat or light, formation of a gas, formation of a precipitate, and/or color change provide possible evidence that a chemical change has occurred.)"
            }
        ]
    },
    {
        "messages": [
            {
                "role": "user",
                "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 4.2, Net Ionic Equations?"
            },
            {
                "role": "assistant",
                "content": "Learning Objective 4.2.A: Represent changes in matter with a balanced chemical or net ionic equation: i. For physical changes. ii. For given information about the identity of the reactants and/or product. iii. For ions in a given chemical reaction. > (Essential Knowledge 4.2.A.1: All physical and chemical processes can be represented symbolically by balanced equations. Essential Knowledge 4.2.A.2: Chemical equations represent chemical changes. These changes are the result of a rearrangement of atoms into new combinations; thus, any representation of a chemical change must contain equal numbers of atoms of every element before and after the change occurred. Equations thus demonstrate that mass and charge are conserved in chemical reactions. Essential Knowledge 4.2.A.3: Balanced molecular, complete ionic, and net ionic equations are differing symbolic forms used to represent a chemical reaction. The form used to represent the reaction depends on the context in which it is to be used.)"
            }
        ]
    },
    {
        "messages": [
            {
                "role": "user",
                "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 4.3, Representations of Reactions?"
            },
            {
                "role": "assistant",
                "content": "Learning Objective 4.3.A: Represent a given chemical reaction or physical process with a consistent particulate model. > (Essential Knowledge 4.3.A.1: Balanced chemical equations in their various forms can be translated into symbolic particulate representations.)"
            }
        ]
    },
    {
        "messages": [
            {
                "role": "user",
                "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 4.4, Physical and Chemical Changes?"
            },
            {
                "role": "assistant",
                "content": "Learning Objective 4.4.A: Explain the relationship between macroscopic characteristics and bond interactions for: i. Chemical processes. ii. Physical processes. > (Essential Knowledge 4.4.A.1: Processes that involve the breaking and/or formation of chemical bonds are typically classified as chemical processes. Processes that involve only changes in intermolecular interactions, such as phase changes, are typically classified as physical processes. Essential Knowledge 4.4.A.2: Sometimes physical processes involve the breaking of chemical bonds. For example, plausible arguments could be made for the dissolution of a salt in water, as either a physical or chemical process, involves breaking of ionic bonds, and the formation of ion-dipole interactions between ions and solvent.)"
            }
        ]
    },
    {
        "messages": [
            {
                "role": "user",
                "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 4.5, Stoichiometry?"
            },
            {
                "role": "assistant",
                "content": "Learning Objective 4.5.A: Explain changes in the amounts of reactants and products based on the balanced reaction equation for a chemical process. > (Essential Knowledge 4.5.A.1: Because atoms must be conserved during a chemical process, it is possible to calculate product amounts by using known reactant amounts, or to calculate reactant amounts given known product amounts. Essential Knowledge 4.5.A.2: Coefficients of balanced chemical equations contain information regarding the proportionality of the amounts of substances involved in the reaction. These values can be used in chemical calculations involving the mole concept. Essential Knowledge 4.5.A.3: Stoichiometric calculations can be combined with the ideal gas law and calculations involving molarity to quantitatively study gases and solutions.)"
            }
        ]
    },
    {
        "messages": [
            {
                "role": "user",
                "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 4.6, Introduction to Titration?"
            },
            {
                "role": "assistant",
                "content": "Learning Objective 4.6.A: Identify the equivalence point in a titration based on the amounts of the titrant and analyte, assuming the titration reaction goes to completion. > (Essential Knowledge 4.6.A.1: Titrations may be used to determine the amount of an analyte in solution. The titrant has a known concentration of a species that reacts specifically and quantitatively with the analyte. The equivalence point of the titration occurs when the analyte is totally consumed by the reacting species in the titrant. The equivalence point is often indicated by a change in a property (such as color) that occurs when the equivalence point is reached. This observable event is called the endpoint of the titration.)"
            }
        ]
    },
    {
        "messages": [
            {
                "role": "user",
                "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 4.7, Types of Chemical Reactions?"
            },
            {
                "role": "assistant",
                "content": "Learning Objective 4.7.A: Identify a reaction as acid-base, oxidation-reduction, or precipitation. > (Essential Knowledge 4.7.A.1: Acid-base reactions involve transfer of one or more protons (H+ ions) between chemical species. Essential Knowledge 4.7.A.2: Oxidation-reduction (redox) reactions involve transfer of one or more electrons between chemical species, as indicated by changes in oxidation numbers of the involved species. Combustion is an important subclass of oxidation-reduction reactions, in which a species reacts with oxygen gas. In the case of hydrocarbons, carbon dioxide and water are products of complete combustion. Essential Knowledge 4.7.A.3: In a redox reaction, electrons are transferred from the species that is oxidized to the species that is reduced. Essential Knowledge 4.7.A.4: Oxidation numbers may be assigned to each of the atoms in the reactants and products; this is often an effective way to identify the oxidized and reduced species in a redox reaction. Essential Knowledge 4.7.A.5: Precipitation reactions frequently involve mixing ions in aqueous solution to produce an insoluble or sparingly soluble ionic compound. All sodium, potassium, ammonium, and nitrate salts are soluble in water.)"
            }
        ]
    },
    {
        "messages": [
            {
                "role": "user",
                "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 4.8, Introduction to Acid-Base Reactions?"
            },
            {
                "role": "assistant",
                "content": "Learning Objective 4.8.A: Identify species as Brønsted-Lowry acids, bases, and/or conjugate acid-base pairs, based on proton-transfer involving those species. > (Essential Knowledge 4.8.A.1: By definition, a Brønsted-Lowry acid is a proton donor and a Brønsted-Lowry base is a proton acceptor. Essential Knowledge 4.8.A.2: Only in aqueous solutions, water plays an important role in many acid-base reactions, as its molecular structure allows it to accept protons from and donate protons to dissolved species. Essential Knowledge 4.8.A.3: When an acid or base ionizes in water, the conjugate acid-base pairs can be identified and their relative strengths compared.)"
            }
        ]
    },
    {
        "messages": [
            {
                "role": "user",
                "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 4.9, Oxidation-Reduction (Redox) Reactions?"
            },
            {
                "role": "assistant",
                "content": "Learning Objective 4.9.A: Represent a balanced redox reaction equation using half-reactions. > (Essential Knowledge 4.9.A.1: Balanced chemical equations for redox reactions can be constructed from half-reactions.)"
            }
        ]
    },
    {
        "messages":[
            {
                "role": "user",
                "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 5.1, Reaction Rates?"
            },
            {
                "role": "assistant",
                "content": "Learning Objective 5.1.A: Explain the relationship between the rate of a chemical reaction and experimental parameters. > (Essential Knowledge 5.1.A.1: The kinetics of a chemical reaction is defined as the rate at which an amount of reactants is converted to products per unit of time. Essential Knowledge 5.1.A.2: The rates of change of reactant and product concentrations are determined by the stoichiometry in the balanced chemical equation. Essential Knowledge 5.1.A.3: The rate of a reaction is influenced by reactant concentrations, temperature, surface area, catalysts, and other environmental factors.)"
            }
        ]
    },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 5.2, Introduction to Rate Law?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 5.2.A: Represent experimental data with a consistent rate law expression. > (Essential Knowledge 5.2.A.1: Experimental methods can be used to monitor the amounts of reactants and/or products of a reaction over time and to determine the rate of the reaction. Essential Knowledge 5.2.A.2: The rate law expresses the rate of a reaction as proportional to the concentration of each reactant raised to a power. Essential Knowledge 5.2.A.3: The power of each reactant in the rate law is the order of the reaction with respect to that reactant. The sum of the powers of the reactant concentrations in the rate law is the overall order of the reaction. Essential Knowledge 5.2.A.4: The proportionality constant in the rate law is called the rate constant. The value of this constant is temperature dependent and the units reflect the overall reaction order. Essential Knowledge 5.2.A.5: Comparing initial rates of a reaction is a method to determine the order with respect to each reactant.)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 5.3, Concentration Changes Over Time?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 5.3.A: Identify the rate law expression of a chemical reaction using data that show how the concentrations of reaction species change over time. > (Essential Knowledge 5.3.A.1: The order of a reaction can be inferred from a graph of concentration of reactant versus time. Essential Knowledge 5.3.A.2: If a reaction is first order with respect to a reactant being monitored, a plot of the natural log (ln) of the reactant concentration as a function of time will be linear. Essential Knowledge 5.3.A.3: If a reaction is second order with respect to a reactant being monitored, a plot of the reciprocal of the concentration of that reactant versus time will be linear. Essential Knowledge 5.3.A.4: The slopes of the concentration versus time data for zeroth, first, and second order reactions can be used to determine the rate constant for the reaction. Zeroth order: EQN: [A]t − [A]0 = −kt. First order: EQN: ln[A]t − ln[A]0 = −kt. Second order: EQN: 1/[A]t − 1/[A]0 = kt. Essential Knowledge 5.3.A.5: Half-life is a critical parameter for first order reactions because the half-life is constant and related to the rate constant for the reaction by the equation: EQN: t1/2 = 0.693/k. Essential Knowledge 5.3.A.6: Radioactive decay processes provide an important illustration of first order kinetics.)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 5.4, Elementary Reactions?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 5.4.A: Represent an elementary reaction as a rate law expression using stoichiometry. > (Essential Knowledge 5.4.A.1: The rate law of an elementary reaction can be inferred from the stoichiometry of the particles participating in a collision. Essential Knowledge 5.4.A.2: Elementary reactions involving the simultaneous collision of three or more particles are rare.)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 5.5, Collision Model?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 5.5.A: Explain the relationship between the rate of an elementary reaction and the frequency, energy, and orientation of particle collisions. > (Essential Knowledge 5.5.A.1: For an elementary reaction to successfully produce products, reactants must successfully collide to initiate bond-breaking and bond-making events. Essential Knowledge 5.5.A.2: In most reactions, only a small fraction of the collisions leads to a reaction. Successful collisions have both sufficient energy to overcome the activation energy requirements and orientations that allow the bonds to rearrange in the required manner. Essential Knowledge 5.5.A.3: The Maxwell-Boltzmann distribution curve describes the distribution of particle energies; this distribution can be used to gain a qualitative estimate of the fraction of collisions with sufficient energy to lead to a reaction, and also how that fraction depends on temperature.)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 5.6, Reaction Energy Profile?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 5.6.A: Represent the activation energy and overall energy change in an elementary reaction using a reaction energy profile. > (Essential Knowledge 5.6.A.1: Elementary reactions typically involve the breaking of some bonds and the forming of new ones. Essential Knowledge 5.6.A.2: The reaction coordinate is the axis along which the complex set of motions involved in rearranging reactants to form products can be plotted. Essential Knowledge 5.6.A.3: The energy profile gives the energy along the reaction coordinate, which typically proceeds from reactants, through a transition state, to products. The energy difference between the reactants and the transition state is the activation energy for the forward reaction. Essential Knowledge 5.6.A.4: The rate of an elementary reaction is temperature dependent because the proportion of particle collisions that are energetic enough to reach the transition state varies with temperature. The Arrhenius equation relates the temperature dependence of the rate of an elementary reaction to the activation energy needed by molecular collisions to reach the transition state. [Exclusion Statement: Calculations involving the Arrhenius equation will not be assessed on the AP Exam.])"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 5.7, Introduction to Reaction Mechanisms?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 5.7.A: Identify the components of a reaction mechanism. > (Essential Knowledge 5.7.A.1: A reaction mechanism consists of a series of elementary reactions, or steps, that occur in sequence. The components may include reactants, intermediates, products, and catalysts. Essential Knowledge 5.7.A.2: The elementary steps when combined should align with the overall balanced equation of a chemical reaction. Essential Knowledge 5.7.A.3: A reaction intermediate is produced by some elementary steps and consumed by others, such that it is present only while a reaction is occurring. Essential Knowledge 5.7.A.4: Experimental detection of a reaction intermediate is a common way to build evidence in support of one reaction mechanism over an alternative mechanism. [Exclusion Statement: Collection of data pertaining to detection of a reaction intermediate will not be assessed on the AP Exam.])"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 5.8, Reaction Mechanism and Rate Law?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 5.8.A: Identify the rate law for a reaction from a mechanism in which the first step is rate limiting. > (Essential Knowledge 5.8.A.1: For reaction mechanisms in which each elementary step is irreversible, or in which the first step is rate limiting, the rate law of the reaction is set by the molecularity of the slowest elementary step (i.e., the rate-limiting step). [Exclusion Statement: Collection of data pertaining to detection of a reaction intermediate will not be assessed on the AP Exam.])"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 5.9, Pre-Equilibrium Approximation?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 5.9.A: Identify the rate law for a reaction from a mechanism in which the first step is not rate limiting. > (Essential Knowledge 5.9.A.1: If the first elementary reaction is not rate limiting, approximations (such as pre-equilibrium) must be made to determine a rate law expression.)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 5.10, Multistep Reaction Energy Profile?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 5.10.A: Represent the activation energy and overall energy change in a multistep reaction with a reaction energy profile. > (Essential Knowledge 5.10.A.1: Knowledge of the energetics of each elementary reaction in a mechanism allows for the construction of an energy profile for a multistep reaction.)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 5.11, Catalysis?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 5.11.A: Explain the relationship between the effect of a catalyst on a reaction and changes in the reaction mechanism. > (Essential Knowledge 5.11.A.1: In order for a catalyst to increase the rate of a reaction, the addition of the catalyst must increase the number of effective collisions and/or provide a reaction path with a lower activation energy relative to the original reaction coordinate. Essential Knowledge 5.11.A.2: In a reaction mechanism containing a catalyst, the net concentration of the catalyst is constant. However, the catalyst will frequently be consumed in the rate-determining step of the reaction, only to be regenerated in a subsequent step in the mechanism. Essential Knowledge 5.11.A.3: Some catalysts accelerate a reaction by binding to the reactant(s). The reactants are either oriented more favorably or react with lower activation energy. There is often a new reaction intermediate in which the catalyst is bound to the reactant(s). Many enzymes function in this manner. Essential Knowledge 5.11.A.4: Some catalysts involve covalent bonding between the catalyst and the reactant(s). An example is acid-base catalysis, in which a reactant or intermediate either gains or loses a proton. This introduces a new reaction intermediate and new elementary reactions involving that intermediate. Essential Knowledge 5.11.A.5: In surface catalysis, a reactant or intermediate binds to, or forms a covalent bond with, the surface. This introduces elementary reactions involving these new bound reaction intermediate(s).)"
                }
            ]
        },
    {
        "messages":[
            {
                "role": "user",
                "content": "What are the Leanring Objectives and Essential Knowledge Statements for Topic 6.1, Endothermic and Exothermic Processes?"
            },
            {
                "role": "assistant",
                "content": "Learning Objective 6.1.A: Explain the relationship between experimental observations and energy changes associated with a chemical or physical transformation. > (Essential Knowledge 6.1.A.1: Temperature changes in a system indicate energy changes. Essential Knowledge 6.1.A.2: Energy changes in a system can be described as endothermic and exothermic processes such as the heating or cooling of a substance, phase changes, or chemical transformations. Essential Knowledge 6.1.A.3: When a chemical reaction occurs, the energy of the system either decreases (exothermic reaction), increases (endothermic reaction), or remains the same. For exothermic reactions, the energy lost by the reacting species (system) is gained by the surroundings, as heat transfer from or work done by the system. Likewise, for endothermic reactions, the system gains energy from the surroundings by heat transfer to or work done on the system. Essential Knowledge 6.1.A.4: The formation of a solution may be an exothermic or endothermic process, depending on the relative strengths of intermolecular/interparticle interactions before and after the dissolution process.)"
            }
        ]
    },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 6.2, Energy Diagrams?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 6.2.A: Represent a chemical or physical transformation with an energy diagram. > (Essential Knowledge 6.2.A.1: A physical or chemical process can be described with an energy diagram that shows the endothermic or exothermic nature of that process.)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 6.3, Heat Transfer and Thermal Equilibrium?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 6.3.A: Explain the relationship between the transfer of thermal energy and molecular collisions. > (Essential Knowledge 6.3.A.1: The particles in a warmer body have a greater average kinetic energy than those in a cooler body. Essential Knowledge 6.3.A.2: Collisions between particles in thermal contact can result in the transfer of energy. This process is called “heat transfer,” “heat exchange,” or “transfer of energy as heat.” Essential Knowledge 6.3.A.3: Eventually, thermal equilibrium is reached as the particles continue to collide. At thermal equilibrium, the average kinetic energy of both bodies is the same, and hence, their temperatures are the same.)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 6.4, Heat Capacity and Calorimetry?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 6.4.A: Calculate the heat q absorbed or released by a system undergoing heating/cooling based on the amount of the substance, the heat capacity, and the change in temperature. > (Essential Knowledge 6.4.A.1: The heating of a cool body by a warmer body is an important form of energy transfer between two systems. The amount of heat transferred between two bodies may be quantified by the heat transfer equation: EQN: q = mcΔT. Calorimetry experiments are used to measure the transfer of heat. Essential Knowledge 6.4.A.2: The first law of thermodynamics states that energy is conserved in chemical and physical processes. Essential Knowledge 6.4.A.3: The transfer of a given amount of thermal energy will not produce the same temperature change in equal masses of matter with differing specific heat capacities. Essential Knowledge 6.4.A.4: Heating a system increases the energy of the system, while cooling a system decreases the energy of the system. Essential Knowledge 6.4.A.5: The specific heat capacity of a substance and the molar heat capacity are both used in energy calculations. Essential Knowledge 6.4.A.6: Chemical systems change their energy through three main processes: heating/cooling, phase transitions, and chemical reactions. Essential Knowledge 6.4.A.7: In calorimetry experiments involving dissolution, temperature changes of the mixture within the calorimeter can be used to determine the direction of energy flow. If the temperature of the mixture increases, thermal energy is released by the dissolution process (exothermic). If the temperature of the mixture decreases, thermal energy is absorbed by the dissolution process (endothermic).)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 6.5, Energy of Phase Changes?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 6.5.A: Explain changes in the heat q absorbed or released by a system undergoing a phase transition based on the amount of the substance in moles and the molar enthalpy of the phase transition. > (Essential Knowledge 6.5.A.1: Energy must be transferred to a system to cause a substance to melt (or boil). The energy of the system therefore increases as the system undergoes a solid-to-liquid (or liquid-to-gas) phase transition. Likewise, a system releases energy when it freezes (or condenses). The energy of the system decreases as the system undergoes a liquid-to-solid (or gas-to-liquid) phase transition. The temperature of a pure substance remains constant during a phase change. Essential Knowledge 6.5.A.2: The energy absorbed during a phase change is equal to the energy released during a complementary phase change in the opposite direction. For example, the molar enthalpy of condensation of a substance is equal to the negative of its molar enthalpy of vaporization. Similarly, the molar enthalpy of fusion can be used to calculate the energy absorbed when melting a substance and the energy released when freezing a substance.)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 6.6, Introduction to Enthalpy of Reaction?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 6.6.A: Calculate the heat q absorbed or released by a system undergoing a chemical reaction in relationship to the amount of the reacting substance in moles and the molar enthalpy of reaction. > (Essential Knowledge 6.6.A.1: The enthalpy change of a reaction gives the amount of heat energy released (for negative values) or absorbed (for positive values) by a chemical reaction at constant pressure. Essential Knowledge 6.6.A.2: When the products of a reaction are at a different temperature than their surroundings, they exchange energy with the surroundings to reach thermal equilibrium. Thermal energy is transferred to the surroundings as the reactants convert to products in an exothermic reaction. Thermal energy is transferred from the surroundings as the reactants convert to products in an endothermic reaction. Essential Knowledge 6.6.A.3: The chemical potential energy of the products of a reaction is different from that of the reactants because of the breaking and forming of bonds. The energy difference results in a change in the kinetic energy of the particles, which manifests as a temperature change. Exclusion Statement: The technical distinctions between enthalpy and internal energy will not be assessed on the AP Exam. Most reactions studied at the AP level are carried out at constant pressure, where the enthalpy change of the process is equal to the heat (and by extension, the energy) of reaction.)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 6.7, Bond Enthalpies?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 6.7.A: Calculate the enthalpy change of a reaction based on the average bond energies of bonds broken and formed in the reaction. > (Essential Knowledge 6.7.A.1: During a chemical reaction, bonds are broken and/or formed, and these events change the potential energy of the system. Essential Knowledge 6.7.A.2: The average energy required to break all of the bonds in the reactant molecules can be estimated by adding up the average bond energies of all the bonds in the reactant molecules. Likewise, the average energy released in forming the bonds in the product molecules can be estimated. If the energy released is greater than the energy required, the reaction is exothermic. If the energy required is greater than the energy released, the reaction is endothermic.)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 6.8, Enthalpy of Formation?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 6.8.A: Calculate the enthalpy change for a chemical or physical process based on the standard enthalpies of formation. > (Essential Knowledge 6.8.A.1: Tables of standard enthalpies of formation can be used to calculate the standard enthalpies of reactions. EQN: ΔH°reaction = ΣΔHf°products − ΣΔHf°reactants)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 6.9, Hess’s Law?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 6.9.A: Represent a chemical or physical process as a sequence of steps. > (Essential Knowledge 6.9.A.1: Many processes can be broken down into a series of steps. Each step in the series has its own energy change. Learning Objective 6.9.B: Explain the relationship between the enthalpy of a chemical or physical process and the sum of the enthalpies of the individual steps. > (Essential Knowledge 6.9.B.1: Because total energy is conserved (first law of thermodynamics), and each individual reaction in a sequence transfers thermal energy to or from the surroundings, the net thermal energy transferred in the sequence will be equal to the sum of the thermal energy transfers in each of the steps. These thermal energy transfers are the result of potential energy changes among the species in the reaction sequence; thus, at constant pressure, the enthalpy change of the overall process is equal to the sum of the enthalpy changes of the individual steps. Essential Knowledge 6.9.B.2: The following are essential principles of Hess’s law: i. When a reaction is reversed, the enthalpy change stays constant in magnitude but becomes reversed in mathematical sign. ii. When a reaction is multiplied by a factor c, the enthalpy change is multiplied by the same factor c. iii. When two (or more) reactions are added to obtain an overall reaction, the individual enthalpy changes of each reaction are added to obtain the net enthalpy change of the overall reaction. Exclusion Statement: The concept of state functions will not be assessed on the AP Exam.)"
                }
            ]
        },
        {
            "messages":[
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 7.1, Introduction to Equilibrium?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 7.1.A: Explain the relationship between the occurrence of a reversible chemical or physical process, and the establishment of equilibrium, to experimental observations. > (Essential Knowledge 7.1.A.1: Many observable processes are reversible. Examples include evaporation and condensation of water, absorption and desorption of a gas, or dissolution and precipitation of a salt. Some important reversible chemical processes include the transfer of protons in acid-base reactions and the transfer of electrons in redox reactions. Essential Knowledge 7.1.A.2: When equilibrium is reached, no observable changes occur in the system. Reactants and products are simultaneously present, and the concentrations or partial pressures of all species remain constant. Essential Knowledge 7.1.A.3: The equilibrium state is dynamic. The forward and reverse processes continue to occur at equal rates, resulting in no net observable change. Essential Knowledge 7.1.A.4: Graphs of concentration, partial pressure, or rate of reaction versus time for simple chemical reactions can be used to understand the establishment of chemical equilibrium.)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 7.2, Direction of Reversible Reactions?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 7.2.A: Explain the relationship between the direction in which a reversible reaction proceeds and the relative rates of the forward and reverse reactions. > (Essential Knowledge 7.2.A.1: If the rate of the forward reaction is greater than the reverse reaction, then there is a net conversion of reactants to products. If the rate of the reverse reaction is greater than that of the forward reaction, then there is a net conversion of products to reactants. An equilibrium state is reached when these rates are equal.)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 7.3, Reaction Quotient and Equilibrium Constant?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 7.3.A: Represent the reaction quotient Qc or Qp, for a reversible reaction, and the corresponding equilibrium expressions Kc = Qc or Kp = Qp. > (Essential Knowledge 7.3.A.1: The reaction quotient Qc describes the relative concentrations of reaction species at any time. For gas phase reactions, the reaction quotient may instead be written in terms of partial pressures as Qp. The reaction quotient tends toward the equilibrium constant such that at equilibrium Kc = Qc and Kp = Qp. As examples, for the reaction aA + bB ⇌ cC + dD, the law of mass action indicates that the equilibrium expression for (Kc, Qc) is Kc = [C]^c[D]^d / [A]^a[B]^b and that for (Kp, Qp) is Kp = (PC)^c(PD)^d / (PA)^a(PB)^b. Essential Knowledge 7.3.A.2: The reaction quotient does not include substances whose concentrations (or partial pressures) are independent of the amount, such as for solids and pure liquids.)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 7.4, Calculating the Equilibrium Constant?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 7.4.A: Calculate Kc or Kp based on experimental observations of concentrations or pressures at equilibrium. > (Essential Knowledge 7.4.A.1: Equilibrium constants can be determined from experimental measurements of the concentrations or partial pressures of the reactants and products at equilibrium.)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 7.5, Magnitude of the Equilibrium Constant?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 7.5.A: Explain the relationship between very large or very small values of K and the relative concentrations of chemical species at equilibrium. > (Essential Knowledge 7.5.A.1: Some equilibrium reactions have very large K values and proceed essentially to completion. Others have very small K values and barely proceed at all.)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 7.6, Properties of the Equilibrium Constant?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 7.6.A: Represent a multistep process with an overall equilibrium expression, using the constituent K expressions for each individual reaction. > (Essential Knowledge 7.6.A.1: When a reaction is reversed, K is inverted. Essential Knowledge 7.6.A.2: When the stoichiometric coefficients of a reaction are multiplied by a factor c, K is raised to the power c. Essential Knowledge 7.6.A.3: When reactions are added together, the K of the resulting overall reaction is the product of the K’s for the reactions that were summed. Essential Knowledge 7.6.A.4: Since the expressions for K and Q have identical mathematical forms, all valid algebraic manipulations of K also apply to Q.)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 7.7, Calculating Equilibrium Concentrations?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 7.7.A: Identify the concentrations or partial pressures of chemical species at equilibrium based on the initial conditions and the equilibrium constant. > (Essential Knowledge 7.7.A.1: The concentrations or partial pressures of species at equilibrium can be predicted given the balanced reaction, initial concentrations, and the appropriate K. Essential Knowledge 7.7.A.2: When Q < K, the reaction will proceed with a net consumption of reactants and generation of products. When Q > K, the reaction will proceed with a net consumption of products and generation of reactants. When Q = K, the system is at dynamic equilibrium; both forward and reverse reactions proceed at the same rate, and the proportion of reactants and products remains constant.)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 7.8, Representations of Equilibrium?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 7.8.A: Represent a system undergoing a reversible reaction with a particulate model. > (Essential Knowledge 7.8.A.1: Particulate representations can be used to describe the relative numbers of reactant and product particles present prior to and at equilibrium, and the value of the equilibrium constant.)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 7.9, Introduction to Le Châtelier’s Principle?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 7.9.A: Identify the response of a system at equilibrium to an external stress, using Le Châtelier's principle. > (Essential Knowledge 7.9.A.1: Le Châtelier’s principle can be used to predict the response of a system to stresses such as addition or removal of a chemical species, change in temperature, change in volume/pressure of a gas-phase system, or dilution of a reaction system. Essential Knowledge 7.9.A.2: Le Châtelier’s principle can be used to predict the effect that a stress will have on experimentally measurable properties such as pH, temperature, and color of a solution.)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 7.10, Reaction Quotient and Le Châtelier’s Principle?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 7.10.A: Explain the relationships between Q, K, and the direction in which a reversible reaction will proceed to reach equilibrium. > (Essential Knowledge 7.10.A.1: A disturbance to a system at equilibrium causes Q to differ from K, thereby taking the system out of equilibrium. The system responds by bringing Q back into agreement with K, thereby establishing a new equilibrium state. Essential Knowledge 7.10.A.2: Some stresses, such as changes in concentration, cause a change in Q only. A change in temperature causes a change in K. In either case, the concentrations or partial pressures of species redistribute to bring Q and K back into equality.)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 7.11, Introduction to Solubility Equilibria?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 7.11.A: Calculate the solubility of a salt based on the value of Ksp for the salt. > (Essential Knowledge 7.11.A.1: The dissolution of a salt is a reversible process whose extent can be described by Ksp, the solubility-product constant. Essential Knowledge 7.11.A.2: The solubility of a substance can be calculated from the Ksp for the dissolution process. This relationship can also be used to predict the relative solubility of different substances. Essential Knowledge 7.11.A.3: The solubility rules can be quantitatively related to Ksp, in which Ksp values >1 correspond to soluble salts. Essential Knowledge 7.11.A.4: The molar solubility of one or more species in a saturated solution can be used to calculate the Ksp of a substance.)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 7.12, Common-Ion Effect?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 7.12.A: Identify the solubility of a salt, and/or the value of Ksp for the salt, based on the concentration of a common ion already present in solution. > (Essential Knowledge 7.12.A.1: The solubility of a salt is reduced when it is dissolved into a solution that already contains one of the ions present in the salt. The impact of this “common-ion effect” on solubility can be understood qualitatively using Le Châtelier’s principle or calculated from the Ksp for the dissolution process.)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 8.1, Introduction to Acids and Bases?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 8.1.A: Calculate the values of pH and pOH, based on Kw and the concentration of all species present in a neutral solution of water. > (Essential Knowledge 8.1.A.1: The concentrations of hydronium ion and hydroxide ion are often reported as pH and pOH, respectively. EQN: pH = −log[H3O+] EQN: pOH = −log[OH−] The terms “hydrogen ion” and “hydronium ion” and the symbols H+(aq) and H3O+(aq) are often used interchangeably for the aqueous ion of hydrogen. Hydronium ion and H3O+(aq) are preferred, but H+(aq) is also accepted on the AP Exam. Essential Knowledge 8.1.A.2: Water autoionizes with an equilibrium constant Kw. EQN: Kw = [H3O+][OH−] = 1.0 × 10−14 at 25°C Essential Knowledge 8.1.A.3: In pure water, pH = pOH is called a neutral solution. At 25°C, pKw = 14.0 and thus pH = pOH = 7.0. EQN: pKw = 14 = pH + pOH at 25°C Essential Knowledge 8.1.A.4: The value of Kw is temperature dependent, so the pH of pure, neutral water will deviate from 7.0 at temperatures other than 25°C.)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 8.2, pH and pOH of Strong Acids and Bases?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 8.2.A: Calculate pH and pOH based on concentrations of all species in a solution of a strong acid or a strong base. > (Essential Knowledge 8.2.A.1: Molecules of a strong acid (e.g., HCl, HBr, HI, HClO4, H2SO4, and HNO3) will completely ionize in aqueous solution to produce hydronium ions and the conjugate base of the acid. As such, the concentration of H3O+ in a strong acid solution is equal to the initial concentration of the strong acid, and thus the pH of the strong acid solution is easily calculated. Essential Knowledge 8.2.A.2: When dissolved in solution, strong bases (e.g., group I and II hydroxides) completely dissociate to produce hydroxide ions. As such, the concentration of OH− in a strong base solution is equal to the initial concentration of a group I hydroxide and double the initial concentration of a group II hydroxide, and thus the pOH (and pH) of the strong base solution is easily calculated.)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 8.3, Weak Acid and Base Equilibria?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 8.3.A: Explain the relationship among pH, pOH, and concentrations of all species in a solution of a monoprotic weak acid or weak base. > (Essential Knowledge 8.3.A.1: Weak acids react with water to produce hydronium ions. However, only a small percentage of molecules of a weak acid will ionize in this way. Thus, the concentration of H3O+ is much less than the initial concentration of the molecular acid, and the vast majority of the acid molecules remain un-ionized. Essential Knowledge 8.3.A.2: A solution of a weak acid involves equilibrium between an un-ionized acid and its conjugate base. The equilibrium constant for this reaction is Ka, often reported as pKa. The pH of a weak acid solution can be determined from the initial acid concentration and the pKa. EQN: [H3O+][A−] / [HA] = Ka EQN: pKa = −log Ka Essential Knowledge 8.3.A.3: Weak bases react with water to produce hydroxide ions in solution. However, ordinarily just a small percentage of the molecules of a weak base in solution will ionize in this way. Thus, the concentration of OH− in the solution does not equal the initial concentration of the base, and the vast majority of the base molecules remain un-ionized. Essential Knowledge 8.3.A.4: A solution of a weak base involves equilibrium between an un-ionized base and its conjugate acid. The equilibrium constant for this reaction is Kb, often reported as pKb. The pH of a weak base solution can be determined from the initial base concentration and the pKb. EQN: [OH−][HB+] / [B] = Kb EQN: pKb = −log Kb Essential Knowledge 8.3.A.5: The percent ionization of a weak acid (or base) can be calculated from its pKa (pKb) and the initial concentration of the acid (base). The percent ionization can also be calculated from the initial concentration of the acid (base) and the equilibrium concentration of any of the species in the equilibrium expression. Essential Knowledge 8.3.A.6: For any conjugate acid-base pair, the acid ionization constant and base ionization constant are related by Kw: EQN: Kw = Ka × Kb EQN: pKw = pKa + pKb)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 8.4, Acid-Base Reactions and Buffers?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 8.4.A: Explain the relationship among the concentrations of major species in a mixture of weak and strong acids and bases. > (Essential Knowledge 8.4.A.1: When a strong acid and a strong base are mixed, they react quantitatively in a reaction represented by the equation: H+(aq) + OH−(aq) → H2O(l). The pH of the resulting solution may be determined from the concentration of excess reagent. Essential Knowledge 8.4.A.2: When a weak acid and a strong base are mixed, they react quantitatively in a reaction represented by the equation: HA(aq) + OH−(aq) ⇌ A−(aq) + H2O(l). If the weak acid is in excess, then a buffer solution is formed, and the pH can be determined from the Henderson-Hasselbalch (H−H) equation. If the strong base is in excess, then the pH can be determined from the moles of excess hydroxide ion and the total volume of solution. If they are equimolar, then the (slightly basic) pH can be determined from the equilibrium represented by the equation: A−(aq) + H2O(l) ⇌ HA(aq) + OH−(aq). Essential Knowledge 8.4.A.3: When a weak base and a strong acid are mixed, they will react quantitatively in a reaction represented by the equation: B(aq) + H3O+(aq) ⇌ HB+(aq) + H2O(l). If the weak base is in excess, then a buffer solution is formed, and the pH can be determined from the H−H equation. If the strong acid is in excess, then the pH can be determined from the moles of excess hydronium ion and the total volume of solution. If they are equimolar, then the (slightly acidic) pH can be determined from the equilibrium represented by the equation: HB+(aq) + H2O(l) ⇌ B(aq) + H3O+(aq). Essential Knowledge 8.4.A.4: When a weak acid and a weak base are mixed, they will react to an equilibrium state whose reaction may be represented by the equation: HA(aq) + B(aq) ⇌ A−(aq) + HB+(aq).)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 8.5, Acid-Base Titrations?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 8.5.A: Explain results from the titration of a mono- or polyprotic acid or base solution, in relation to the properties of the solution and its components. > (Essential Knowledge 8.5.A.1: An acid-base reaction can be carried out under controlled conditions in a titration. A titration curve, plotting pH against the volume of titrant added, is useful for summarizing results from a titration. Essential Knowledge 8.5.A.2: At the equivalence point for titrations of monoprotic acids or bases, the number of moles of titrant added is equal to the number of moles of analyte originally present. This relationship can be used to obtain the concentration of the analyte. This is the case for titrations of strong acids/bases and weak acids/bases. Essential Knowledge 8.5.A.3: For titrations of weak acids/bases, it is useful to consider the point halfway to the equivalence point, that is, the half-equivalence point. At this point, there are equal concentrations of each species in the conjugate acid-base pair, for example, for a weak acid [HA] = [A−]. Because pH = pKa when the conjugate acid and base have equal concentrations, the pKa can be determined from the pH at the half-equivalence point in a titration. Essential Knowledge 8.5.A.4: At the equivalence point, pH is determined by the major species in solution. Strong acid and strong base titrations result in neutral pH at the equivalence point. However, in titrations of weak acids (weak bases), the conjugate base of the weak acid (conjugate acid of the weak base) is present at the equivalence point and can undergo proton-transfer reactions with the surrounding water, producing basic (acidic) solutions. Essential Knowledge 8.5.A.5: For polyprotic acids, titration curves can be used to determine the number of acidic protons. In doing so, the major species present at any point along the curve can be identified, along with the pKa associated with each proton in a weak polyprotic acid. Exclusion Statement: Computation of the concentration of each species present in the titration curve for polyprotic acids will not be assessed on the AP Exam. Such computations for titration of monoprotic acids are within the scope of the course (see 8.4.A.2 and 8.4.A.3), as is qualitative reasoning regarding what species are present in large versus small concentrations at any point in a titration of a polyprotic acid.)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 8.6, Molecular Structure of Acids and Bases?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 8.6.A: Explain the relationship between the strength of an acid or base and the structure of the molecule or ion. > (Essential Knowledge 8.6.A.1: The protons on a molecule that will participate in acid-base reactions, and the relative strength of these protons, can be inferred from the molecular structure. i. Strong acids (such as HCl, HBr, HI, HClO4, H2SO4, and HNO3) have very weak conjugate bases that are stabilized by electronegativity, inductive effects, resonance, or some combination thereof. ii. Carboxylic acids are one common class of weak acid. iii. Strong bases (such as group I and II hydroxides) have very weak conjugate acids. iv. Common weak bases include nitrogenous bases such as ammonia as well as carboxylate ions. v. Electronegative elements tend to stabilize the conjugate base relative to the conjugate acid, and so increase acid strength.)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 8.7, pH and pKa?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 8.7.A: Explain the relationship between the predominant form of a weak acid or base in solution at a given pH and the pKa of the conjugate acid or the pKb of the conjugate base. > (Essential Knowledge 8.7.A.1: The protonation state of an acid or base (i.e., the relative concentrations of HA and A−) can be predicted by comparing the pH of a solution to the pKa of the acid in that solution. When solution pH < acid pKa, the acid form has a higher concentration than the base form. When solution pH > acid pKa, the base form has a higher concentration than the acid form. Essential Knowledge 8.7.A.2: Acid-base indicators are substances that exhibit different properties (such as color) in their protonated versus deprotonated state, making that property respond to the pH of a solution. Essential Knowledge 8.7.A.3: To ensure accurate results in a titration experiment, acid-base indicators should be selected that have a pKa close to the pH at the equivalence point.)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 8.8, Properties of Buffers?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 8.8.A: Explain the relationship between the ability of a buffer to stabilize pH and the reactions that occur when an acid or a base is added to a buffered solution. > (Essential Knowledge 8.8.A.1: A buffer solution contains a large concentration of both members in a conjugate acid-base pair. The conjugate acid reacts with added base and the conjugate base reacts with added acid. These reactions are responsible for the ability of a buffer to stabilize pH.)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 8.9, Henderson-Hasselbalch Equation?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 8.9.A: Identify the pH of a buffer solution based on the identity and concentrations of the conjugate acid-base pair used to create the buffer. > (Essential Knowledge 8.9.A.1: The pH of the buffer is related to the pKa of the acid and the concentration ratio of the conjugate acid-base pair. This relation is a consequence of the equilibrium expression associated with the dissociation of a weak acid, and is described by the Henderson-Hasselbalch equation. Adding small amounts of acid or base to a buffered solution does not significantly change the ratio of [A−]/[HA] and thus does not significantly change the solution pH. The change in pH on addition of acid or base to a buffered solution is therefore much less than it would have been in the absence of the buffer. EQN: pH = pKa + log([A−] / [HA]) Exclusion Statement: Computation of the change in pH resulting from the addition of an acid or a base to a buffer will not be assessed on the AP Exam. Exclusion Statement: Derivation of the Henderson-Hasselbalch equation will not be assessed on the AP Exam.)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 8.10, Buffer Capacity?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 8.10.A: Explain the relationship between the buffer capacity of a solution and the relative concentrations of the conjugate acid and conjugate base components of the solution. > (Essential Knowledge 8.10.A.1: Increasing the concentration of the buffer components (while keeping the ratio of these concentrations constant) keeps the pH of the buffer the same but increases the capacity of the buffer to neutralize added acid or base. Essential Knowledge 8.10.A.2: When a buffer has more conjugate acid than base, it has a greater buffer capacity for addition of added base than acid. When a buffer has more conjugate base than acid, it has a greater buffer capacity for addition of added acid than base.)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 8.11, pH and Solubility?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 8.11.A: Identify the qualitative effect of changes in pH on the solubility of a salt. > (Essential Knowledge 8.11.A.1: The solubility of a salt is pH sensitive when one of the constituent ions is a weak acid, a weak base, or the hydroxide ion. These effects can be understood qualitatively using Le Châtelier’s principle. Exclusion Statement: Computations of solubility as a function of pH will not be assessed on the AP Exam.)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 9.1, Introduction to Entropy?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 9.1.A: Identify the sign and relative magnitude of the entropy change associated with chemical or physical processes. > (Essential Knowledge 9.1.A.1: Entropy increases when matter becomes more dispersed. For example, the phase change from solid to liquid or from liquid to gas results in a dispersal of matter as the individual particles become freer to move and generally occupy a larger volume. Similarly, for a gas, the entropy increases when there is an increase in volume (at constant temperature), and the gas molecules are able to move within a larger space. For reactions involving gas-phase reactants or products, the entropy generally increases when the total number of moles of gas-phase products is greater than the total number of moles of gas-phase reactants. Essential Knowledge 9.1.A.2: Entropy increases when energy is dispersed. According to kinetic molecular theory (KMT), the distribution of kinetic energy among the particles of a gas broadens as the temperature increases. As a result, the entropy of the system increases with an increase in temperature.)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 9.2, Absolute Entropy and Entropy Change?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 9.2.A: Calculate the standard entropy change for a chemical or physical process based on the absolute entropies (standard molar entropies) of the species involved in the process. > (Essential Knowledge 9.2.A.1: The entropy change for a process can be calculated from the absolute entropies of the species involved before and after the process occurs. EQN: ΔS°reaction = ΣS°products − ΣS°reactants)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 9.3, Gibbs Free Energy and Thermodynamic Favorability?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 9.3.A: Explain whether a physical or chemical process is thermodynamically favored based on an evaluation of ΔG°. > (Essential Knowledge 9.3.A.1: The Gibbs free energy change for a chemical process in which all the reactants and products are present in a standard state (as pure substances, as solutions of 1.0 M concentration, or as gases at a pressure of 1.0 atm (or 1.0 bar)) is given the symbol ΔG°. Essential Knowledge 9.3.A.2: The standard Gibbs free energy change for a chemical or physical process is a measure of thermodynamic favorability. Historically, the term “spontaneous” has been used to describe processes for which ΔG° < 0. The phrase “thermodynamically favored” is preferred instead so that common misunderstandings (equating “spontaneous” with “suddenly” or “without cause”) can be avoided. When ΔG° < 0 for the process, it is said to be thermodynamically favored. Essential Knowledge 9.3.A.3: The standard Gibbs free energy change for a physical or chemical process may also be determined from the standard Gibbs free energy of formation of the reactants and products. EQN: ΔG°reaction = ΣΔG°f products − ΣΔG°f reactants. Essential Knowledge 9.3.A.4: In some cases, it is necessary to consider both enthalpy and entropy to determine if a process will be thermodynamically favored. The freezing of water and the dissolution of sodium nitrate are examples of such phenomena. Essential Knowledge 9.3.A.5: Knowing the values of ΔH° and ΔS° for a process at a given temperature allows ΔG° to be calculated directly. EQN: ΔG° = ΔH° − TΔS°. Essential Knowledge 9.3.A.6: In general, the temperature conditions for a process to be thermodynamically favored (ΔG° < 0) can be predicted from the signs of ΔH° and ΔS° as shown in the table below: ΔH° ΔS° Symbols ΔG° < 0, favored at: < 0 > 0 < > all T > 0 < 0 > < no T > 0 > 0 > > high T < 0 < 0 < < low T. In cases where ΔH° < 0 and ΔS° > 0, no calculation of ΔG° is necessary to determine that the process is thermodynamically favored (ΔG° < 0). In cases where ΔH° > 0 and ΔS° < 0, no calculation of ΔG° is necessary to determine that the process is thermodynamically unfavored (ΔG° > 0).)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 9.4, Thermodynamic and Kinetic Control?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 9.4.A: Explain, in terms of kinetics, why a thermodynamically favored reaction might not occur at a measurable rate. > (Essential Knowledge 9.4.A.1: Many processes that are thermodynamically favored do not occur to any measurable extent, or they occur at extremely slow rates. Essential Knowledge 9.4.A.2: Processes that are thermodynamically favored, but do not proceed at a measurable rate, are under “kinetic control.” High activation energy is a common reason for a process to be under kinetic control. The fact that a process does not proceed at a noticeable rate does not mean that the chemical system is at equilibrium. If a process is known to be thermodynamically favored, and yet does not occur at a measurable rate, it is reasonable to conclude that the process is under kinetic control.)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 9.5, Free Energy and Equilibrium?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 9.5.A: Explain whether a process is thermodynamically favored using the relationships between K, ΔG°, and T. > (Essential Knowledge 9.5.A.1: The phrase “thermodynamically favored” (ΔG° < 0) means that the products are favored at equilibrium (K > 1) under standard conditions. Essential Knowledge 9.5.A.2: The equilibrium constant is related to free energy by the equations EQN: K = e−ΔG°/RT and EQN: ΔG° = −RT ln K. Essential Knowledge 9.5.A.3: Connections between K and ΔG° can be made qualitatively through estimation. When ΔG° is near zero, the equilibrium constant will be close to 1. When ΔG° is much larger or much smaller than RT, the value of K deviates strongly from 1. Essential Knowledge 9.5.A.4: Processes with ΔG° < 0 favor products (i.e., K > 1) and those with ΔG° > 0 favor reactants (i.e., K < 1).)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 9.6, Free Energy of Dissolution?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 9.6.A: Explain the relationship between the solubility of a salt and changes in the enthalpy and entropy that occur in the dissolution process. > (Essential Knowledge 9.6.A.1: The free energy change (ΔG°) for dissolution of a substance reflects a number of factors: the breaking of the intermolecular interactions that hold the solid together, the reorganization of the solvent around the dissolved species, and the interaction of the dissolved species with the solvent. It is possible to estimate the sign and relative magnitude of the enthalpic and entropic contributions to each of these factors. However, making predictions for the total change in free energy of dissolution can be challenging due to the cancellations among the free energies associated with the three factors cited.)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 9.7, Coupled Reactions?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 9.7.A: Explain the relationship between external sources of energy or coupled reactions and their ability to drive thermodynamically unfavorable processes. > (Essential Knowledge 9.7.A.1: An external source of energy can be used to make a thermodynamically unfavorable process occur. Examples include: i. Electrical energy to drive an electrolytic cell or charge a battery. ii. Light to drive the overall conversion of carbon dioxide to glucose in photosynthesis. Essential Knowledge 9.7.A.2: A desired product can be formed by coupling a thermodynamically unfavorable reaction that produces that product to a favorable reaction (e.g., the conversion of ATP to ADP in biological systems). In the coupled system, the individual reactions share one or more common intermediates. The sum of the individual reactions produces an overall reaction that achieves the desired outcome and has ΔG° < 0.)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 9.8, Galvanic (Voltaic) and Electrolytic Cells?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 9.8.A: Explain the relationship between the physical components of an electrochemical cell and the overall operational principles of the cell. > (Essential Knowledge 9.8.A.1: Each component of an electrochemical cell (electrodes, solutions in the half-cells, salt bridge, voltage/current measuring device) plays a specific role in the overall functioning of the cell. The operational characteristics of the cell (galvanic vs. electrolytic, direction of electron flow, reactions occurring in each half-cell, change in electrode mass, evolution of a gas at an electrode, ion flow through the salt bridge) can be described at both the macroscopic and particulate levels. Essential Knowledge 9.8.A.2: Galvanic, sometimes called voltaic, cells involve a thermodynamically favored reaction, whereas electrolytic cells involve a thermodynamically unfavored reaction. Visual representations of galvanic and electrolytic cells are tools of analysis to identify where half-reactions occur and in what direction current flows. Essential Knowledge 9.8.A.3: For all electrochemical cells, oxidation occurs at the anode and reduction occurs at the cathode. Exclusion Statement: Labeling an electrode as positive or negative will not be assessed on the AP Exam.)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 9.9, Cell Potential and Free Energy?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 9.9.A: Explain whether an electrochemical cell is thermodynamically favored, based on its standard cell potential and the constituent half-reactions. > (Essential Knowledge 9.9.A.1: Electrochemistry encompasses the study of redox reactions that occur within electrochemical cells. The reactions are either thermodynamically favored (resulting in a positive voltage) or thermodynamically unfavored (resulting in a negative voltage and requiring an externally applied potential for the reaction to proceed). Essential Knowledge 9.9.A.2: The standard cell potential of electrochemical cells can be calculated by identifying the oxidation and reduction half-reactions and their respective standard reduction potentials. Essential Knowledge 9.9.A.3: ΔG° (standard Gibbs free energy change) is proportional to the negative of the cell potential for the redox reaction from which it is constructed. Thus, a cell with a positive E° involves a thermodynamically favored reaction, and a cell with a negative E° involves a thermodynamically unfavored reaction. EQN: ΔG° = −nFE°)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 9.10, Cell Potential Under Nonstandard Conditions?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 9.10.A: Explain the relationship between deviations from standard cell conditions and changes in the cell potential. > (Essential Knowledge 9.10.A.1: In a real system under nonstandard conditions, the cell potential will vary depending on the concentrations of the active species. The cell potential is a driving force toward equilibrium; the farther the reaction is from equilibrium, the greater the magnitude of the cell potential. Essential Knowledge 9.10.A.2: Equilibrium arguments such as Le Châtelier’s principle do not apply to electrochemical systems, because the systems are not in equilibrium. Essential Knowledge 9.10.A.3: The standard cell potential E° corresponds to the standard conditions of Q = 1. As the system approaches equilibrium, the magnitude (i.e., absolute value) of the cell potential decreases, reaching zero at equilibrium (when Q = K). Deviations from standard conditions that take the cell further from equilibrium than Q = 1 will increase the magnitude of the cell potential relative to E°. Deviations from standard conditions that take the cell closer to equilibrium than Q = 1 will decrease the magnitude of the cell potential relative to E°. In concentration cells, the direction of spontaneous electron flow can be determined by considering the direction needed to reach equilibrium. Essential Knowledge 9.10.A.4: Algorithmic calculations using the Nernst equation are insufficient to demonstrate an understanding of electrochemical cells under nonstandard conditions. However, students should qualitatively understand the effects of concentration on cell potential and use conceptual reasoning, including the qualitative use of the Nernst equation: EQN: E = E° − (RT/nF) ln Q to solve problems.)"
                }
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the Learning Objectives and Essential Knowledge Statements for Topic 9.11, Electrolysis and Faraday’s Law?"
                },
                {
                    "role": "assistant",
                    "content": "Learning Objective 9.11.A: Calculate the amount of charge flow based on changes in the amounts of reactants and products in an electrochemical cell. > (Essential Knowledge 9.11.A.1: Faraday’s laws can be used to determine the stoichiometry of the redox reaction occurring in an electrochemical cell with respect to the following: i. Number of electrons transferred ii. Mass of material deposited on or removed from an electrode (as in electroplating) iii. Current iv. Time elapsed v. Charge of ionic species EQN: I = q/t)"
                }
            ]
        }
   ]
recommended_practices = ["5.B", "5.D", "2.A", "5.A", "1.A", "4.B", "4.A", "4.C", "6.A", "5.D", "4.C", "4.C", "1.A", "6.C", "6.C", "4.D", "4.C", "4.C", "5.C", "4.A", "6.E", "5.F", "4.C", "2.C", "4.D", "4.A", "5.F", "2.E", "2.B", "5.E", "1.A", "6.B", "5.C", "5.D", "1.B", "1.B", "5.E", "6.E", "5.C", "5.B", "5.E", "6.E", "1.A", "1.B", "5.B", "5.B", "1.A", "6.E", "6.D", "5.D", "6.E", "2.D", "1.B", "5.F", "5.F", "5.F", "5.A", "6.D", "4.D", "5.D", "5.C", "6.D", "5.A", "5.D", "4.C", "6.F", "5.F", "5.B", "2.F", "5.B", "5.B", "5.C", "5.C", "5.D", "6.C", "2.D", "6.D", "5.F", "6.G", "2.D", "6.C", "5.F", "6.E", "6.E", "6.D", "4.D", "4.D", "2.F", "5.F", "6.D", "5.B"]
def parse_json_to_data(json_data):
    data = []
    for entry in json_data:
        user_message = entry["messages"][0]["content"]
        assistant_message = entry["messages"][1]["content"]

        topic_start = user_message.find("Topic ")
        topic_end = user_message.find(", ", topic_start)
        topic_number = user_message[topic_start + 6 : topic_end].strip()
        topic_name = user_message[topic_end + 2 : len(user_message)-1].strip()

        learning_objective_end = assistant_message.find(" > ")
        learning_objective = assistant_message[:learning_objective_end].strip()
        essential_knowledge_parts = assistant_message[learning_objective_end + 4 :]
        essential_knowledge_list = [
            ek.strip() for ek in essential_knowledge_parts.split("Essential Knowledge") if ek.strip()
        ]
        for ek in essential_knowledge_list:
            if ":" in ek:
                ek_key, ek_content = ek.split(":", 1)
                ek_text = f"Essential Knowledge {ek_key.strip()}:{ek_content.strip()}"
                data.append(
                    essential_knowledge(
                    topic=f"{topic_number}, {topic_name}",
                    learning_objective=learning_objective,
                    essential_knowledge=ek_text,
                    recommended_practice=""
            )
        )
    past_topic = ""
    count = 1
    loops = 0
    real_loops = 0
    for i in data:
        current_topic = i.topic
        if current_topic == past_topic:
            count += 1
            loops += real_loops-count
        else:
            count = 1
            real_loops = 0
        i.recommended_practice = recommended_practices[loops]
        past_topic = current_topic
        loops += 1
        real_loops += 1
        for j in range(len(science_practice_codes)):
            if i.recommended_practice == science_practice_codes[j]:
                i.recommended_practice = science_practices[j]
    return data
data = parse_json_to_data(json_data)

class prompt:
    def __init__(self, prompt, topic, learning_objective, essential_knowledge, science_practice):
        self.prompt = prompt
        self.topic = topic
        self.learning_objective = learning_objective
        self.essential_knowledge = essential_knowledge
        self.science_practice = science_practice

    def __repr__(self):
        return f"Prompt: {self.prompt}\nTopic: {self.topic}\n{self.learning_objective}\n{self.essential_knowledge}\n{self.science_practice}"

class question:
    def __init__(self, question, topic, learning_objective, essential_knowledge, science_practice):
        self.question = question
        self.topic = topic
        self.learning_objective = learning_objective
        self.essential_knowledge = essential_knowledge
        self.science_practice = science_practice

    def __repr__(self):
        return f"Question: {self.question}\nTopic: {self.topic}\n{self.learning_objective}\n{self.essential_knowledge}\n{self.science_practice}"

def generate_questions_unit_num(unit, number_of_questions):
    essential_knowledge_list = []
    questions = []
    for i in data:
        if i.topic.startswith(unit):
            essential_knowledge_list.append(i)
    if len(essential_knowledge_list) == 0:
        return "Please enter a valid unit"
    print(len(essential_knowledge_list))
    if number_of_questions < len(essential_knowledge_list):
        return "Please enter a larger number"
    if number_of_questions == len(essential_knowledge_list):
        for ek in essential_knowledge_list:
            questions.append(f"Create a multiple choice question for subunit {ek.topic}, {(ek.essential_knowledge)[0:27]}, and {ek.recommended_practice[0:20]}. The learning objective is {ek.learning_objective} The essential knowledge is {ek.essential_knowledge} The science practice is {ek.recommended_practice} When crafting the multiple choice question consider the learning objective, essential knowledge, and science practice. The question should have 4 options and an answer. Provide an explanation for the answer. Your explanation should not involve the essential knowledge, learning objective, or science practice, it should be more of an explanation of why the correct answer is correct. If the question needs some kind of diagram, you may add 'context'. Context is not always needed. It would be like a diagram, graph, or particle diagram that was needed for the problem. Things like explanations of situations do not belong in context, those can go in the question itself unless they are excessively long. Context should usually just be descriptions of diagrams, tables, or graphs. If the diagrams are makable with text, then the context can just be the diagrams. If there is some kind of image, graph, or table that is in context, use the shorthand ElementDesc[], filling in the square brackets with the description, to denote the element. Do not confuse context with the question itself, like I said, sometimes context isn't even needed. Also, context should not include some kind of prerequisite knowledge about chemistry.")
    if number_of_questions > len(essential_knowledge_list):
        multiple = number_of_questions / len(essential_knowledge_list)
        print(multiple)
        if multiple.is_integer():
            for ek in essential_knowledge_list:
                questions.append(f"Create {int(multiple)} multiple choice questions for subunit {ek.topic}, {(ek.essential_knowledge)[0:27]}, and {ek.recommended_practice[0:20]}. The learning objective is {ek.learning_objective} The essential knowledge is {ek.essential_knowledge} The science practice is {ek.recommended_practice} When crafting the {int(multiple)} multiple choice questions consider the learning objective, essential knowledge, and science practice. Each question should have 4 options and an answer. For each of them, provide an explanation for the answer. Your explanation should not involve the essential knowledge, learning objective, or science practice, it should be more of an explanation of why the correct answer is correct. If the question needs some kind of diagram, you may add 'context'. Context is not always needed. It would be like a diagram, graph, or particle diagram that was needed for the problem. Things like explanations of situations do not belong in context, those can go in the question itself unless they are excessively long. Context should usually just be descriptions of diagrams, tables, or graphs. If the diagrams are makable with text, then the context can just be the diagrams. Also, context should not include some kind of prerequisite knowledge about chemistry. If there is some kind of image, graph, or table that is in context, use the shorthand ElementDesc[], filling in the square brackets with the description, to denote the element. Do not confuse context with the question itself, like I said, sometimes context isn't even needed. Create all {int(multiple)} questions, don't stop in the middle. All of the questions need to be generated.")
        else:
            multiple = int(multiple) + 1
            print(multiple)
            for ek in essential_knowledge_list:
                questions.append(f"Create {multiple} multiple choice questions for subunit {ek.topic}, {(ek.essential_knowledge)[0:27]}, and {ek.recommended_practice[0:20]}. The learning objective is {ek.learning_objective} The essential knowledge is {ek.essential_knowledge} The science practice is {ek.recommended_practice} When crafting the {multiple} multiple choice questions consider the learning objective, essential knowledge, and science practice. Each question should have 4 options and an answer. For each of them, provide an explanation for the answer. Your explanation should not involve the essential knowledge, learning objective, or science practice, it should be more of an explanation of why the correct answer is correct. If the question needs some kind of diagram, you may add 'context'. Context is not always needed. It would be like a diagram, graph, or particle diagram that was needed for the problem. Things like explanations of situations do not belong in context, those can go in the question itself unless they are excessively long. Context should usually just be descriptions of diagrams, tables, or graphs. If the diagrams are makable with text, then the context can just be the diagrams. Also, context should not include some kind of prerequisite knowledge about chemistry. If there is some kind of image, graph, or table that is in context, use the shorthand ElementDesc[], filling in the square brackets with the description, to denote the element. Do not confuse context with the question itself, like I said, sometimes context isn't even needed. Create all {multiple} questions, don't stop in the middle. All of the questions need to be generated.")
    print(len(questions)*multiple)
    return questions

def generate_questions(multiple):
    questions = []
    for i in data:
        questions.append(
            prompt(
            prompt=f"Create {multiple} multiple choice questions for subunit {i.topic}, {(i.essential_knowledge)[0:27]}, and {i.recommended_practice[0:20]}. The learning objective is {i.learning_objective} The essential knowledge is {i.essential_knowledge} The science practice is {i.recommended_practice} When crafting the {multiple} multiple choice questions consider the learning objective, essential knowledge, and science practice. Each question should have 4 options and an answer. For each of them, provide an explanation for the answer. Your explanation should not involve the essential knowledge, learning objective, or science practice, it should be more of an explanation of why the correct answer is correct. If the question needs some kind of diagram, you may add 'context'. Context is not always needed. It would be like a diagram, graph, or particle diagram that was needed for the problem. Things like explanations of situations do not belong in context, those can go in the question itself unless they are excessively long. Context should usually just be descriptions of diagrams, tables, or graphs. If the diagrams are makable with text, then the context can just be the diagrams. Also, context should not include some kind of prerequisite knowledge about chemistry. If there is some kind of image, graph, or table that is in context, use the shorthand ElementDesc[], filling in the square brackets with the description, to denote the element. Do not confuse context with the question itself, like I said, sometimes context isn't even needed. Create all {multiple} questions, don't stop in the middle. All of the questions need to be generated.",
            topic=i.topic,
            learning_objective=i.learning_objective,
            essential_knowledge=i.essential_knowledge,
            science_practice=i.recommended_practice
        )
    )  
    print(f"Generated {len(questions)*multiple} questions")
    return questions

prompts = generate_questions(5)

from openai import OpenAI
client = OpenAI()
questions = []
count = 0
for prompt in prompts:
    response = client.chat.completions.create(
    model="chatgpt-4o-latest",
    messages=[
        {
        "role": "system",
        "content": [
            {
            "type": "text",
            "text": "You are an assistant that creates multiple-choice questions for AP Chemistry. In AP Chemistry there are 9 units, and each has some subunits. Each subunit has 1 or 2 learning objectives and each learning objective has 1-6 essential knowledge statements. A learning objective is denoted like 1.1.A, 1.1. A is the only learning objective for subunit 1.1. An essential knowledge statement is denoted as 1.1.A.1 or 1.1.A.2, both of which are essential knowledges for learning objective 1.1.A. There is also something called Science practices, and there are 5 sections each with a few subsections for MCQs, 1, 2, 4, 5 and 6. A science practice is denoted as 1.A or 1.B, or 5.E or 5.F. Each MCQ should have an essential knowledge statement and science practice tied to it. All of this info and the questions above are from the AP Chemistry Course and Exam Description (CED), at the link https://apcentral.collegeboard.org/media/pdf/ap-chemistry-course-and-exam-description.pdf. An example of the format you should answer in is: \"Context: 1s2 2s2 2p6 3s2 3p6, Question: Which of the following species has the electron configuration shown above? Options:(A) O, (B) Ne, (C) K+, (D) Cl+, Answer: (C), Essential Knowledge: 1.5.A.3, Question SP: 1.A\". Context would be something that would be shown above the question like a graph, table or just a string of text like shown above, or any combination of these. Another example of a question (this one with multiple objects of context) is: \"Context: HCl(aq) + CaCO3(s) → CaCl2(aq) + CO2(g) + H2O(l), The reaction between HCl(aq) and CaCO3(s) is represented by the equation above. Two separate trials were carried out using CaCO3(s) samples of the same mass, but one sample was a single piece of CaCO3(s), and one sample was composed of small pieces of CaCO3(s). The loss of mass of CaCO3(s) as a function of time for both trials is shown in the graph below. ElementDesc[Type: Graph, Specifications: Graph with the y-axis labeled 'Loss of Mass of CaCO₃(s) (g)' and the x-axis labeled 'Time (s)'. It shows two curves, labeled X and Y. Curve Y rises steeply at first, then levels off. Curve X rises more gradually and also levels off, but at a lower point than Curve Y.], Question: Which of the curves, X or Y, represents the reaction with small pieces of CaCO3(s), and why?, Options: (A), (B) Curve X, because it takes a shorter time for the reaction to go to completion due to the larger surface area of CaCO3(s), (C) Curve Y, because it shows that the reaction proceeded at a nonuniform rate, (D) Curve Y, because it takes a shorter time for the reaction to go to completion due to the larger surface area of CaCO3(s), Answer:(D), Essential Knowledge: 5.1.A.3, Question SP: 6.F\". You don't need to provide context if the question does not require it. You will be given a learning objective, essential knowledge statement, and science practice and you will be asked to generate questions."
            }
        ]
        },
        {
            "role": "user",
            "content": prompt.prompt
        }
    ],
    temperature=1.02,
    max_tokens=16383,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    questions_starting_value = len(questions)
    current_questions = response.choices[0].message.content
    last_question = False
    while(not last_question):
        start_index = current_questions.find("**Context:**")
        end_index = current_questions.find("---")
        if end_index == -1:
            last_question = True
            end_index = len(current_questions)
        questions.append(
            question(
                question=current_questions[start_index:end_index],
                topic=prompt.topic,
                learning_objective=prompt.learning_objective,
                essential_knowledge=prompt.essential_knowledge,
                science_practice=prompt.science_practice
            )
        )
        current_questions = current_questions[end_index+3:]
    count += 1
    print(count)
    if count > 1:
        break
print(questions[4])