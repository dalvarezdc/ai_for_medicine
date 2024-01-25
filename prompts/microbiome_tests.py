# List of medical tests for measuring bacteria in the microbiome
medical_tests = [
    "Stool Microbiome Analysis",
    "Blood Microbiome Analysis",
    "Breath Tests",
    "Gut Permeability Tests",
    "Fecal Calprotectin Test",
    "Lactose Tolerance Test",
    "Hydrogen Breath Test",
    "Stool PCR Analysis",
    "Molecular Microbial Profiling (MMP)"
]

# General queries about microbiome testing
queries = [
    # What is microbiome testing?
    "Define and explain the concept of microbiome testing",
    # History of microbiome testing
    "Outline the historical development and current status of microbiome testing",
    # Stakeholders in microbiome testing
    "Identify the key stakeholders involved in microbiome testing, including researchers, clinicians, and healthcare providers",
    # Advantages and disadvantages of microbiome testing
    "Describe the advantages and disadvantages of each type of microbiome test",
    # Applications of microbiome testing
    "Discuss the various applications of microbiome testing in clinical settings, including diagnosis and management of gastrointestinal disorders, identification of potential gut microbiome imbalances associated with chronic diseases, personalized dietary and lifestyle recommendations based on microbiome composition",
    # Potential role of microbiome testing in research and drug discovery
    "Explore the potential role of microbiome testing in research and drug discovery",
    # Current challenges and limitations of microbiome testing
    "Identify the current challenges and limitations of microbiome testing, including interpreting complex microbiome data, standardizing microbiome test protocols and reporting, defining microbiome-related health outcomes",
    # Emerging technologies for microbiome testing
    "Discuss emerging technologies and research directions that hold promise for improving microbiome testing, including next-generation sequencing (NGS) technologies, machine learning algorithms for microbiome analysis, development of biomarkers for microbiome-related health conditions",
    # Ethical considerations for microbiome testing
    "Address the ethical considerations associated with microbiome testing, including privacy and data protection of microbiome data, informed consent and patient autonomy, potential for stigmatization based on microbiome results",
    # Guidelines and recommendations for responsible and ethical use of microbiome testing
    "Propose guidelines and recommendations for responsible and ethical use of microbiome testing in clinical practice and research"
]

# Specific queries about each medical test
for test in medical_tests:
    # Detailed description of each test
    queries.append(f"Provide a detailed description of the {test} test")

    # Comparison of test advantages and disadvantages
    queries.append(f"Compare and contrast the advantages and disadvantages of the {test} test")

    # Applications of the test
    queries.append(f"Discuss the specific applications of the {test} test in clinical settings and research")
