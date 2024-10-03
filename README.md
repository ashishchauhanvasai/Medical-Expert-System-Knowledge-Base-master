Medical Expert System

Project Description
This Python-based medical expert system is designed to diagnose diseases based on user-provided symptoms. The system utilizes an expert system framework (experta) and a knowledge base of diseases, their symptoms, descriptions, and treatments. By answering a series of symptom-related questions, the system attempts to match the symptoms with a known disease and provides the user with a probable diagnosis, description, and recommended treatments.


Features
Accepts user input for various symptoms.
Matches input symptoms with the predefined set of diseases.
Provides a brief description and treatment plan for the diagnosed disease.
If symptoms do not match a disease exactly, it suggests the closest possible match.

Installation
Prerequisites
Python 3.x
Required Libraries: experta

Setup Instructions
1) Clone the repository or download the code:

bash
Copy code :- 
git clone <repository-url>

2) Install the necessary Python packages:
bash
Copy code :- 
pip install experta

#Running the System :-
To run the medical expert system, execute the following command:

bash
Copy code:-
python expert_system.py


Upon execution, the system will greet the user and ask for input about various symptoms. After collecting the data, it will provide a diagnosis or the closest possible match, along with a description and suggested treatments.

Example Usage:- Hi! I am Ashish R. Chauhan, I am here to help you make your health better.
For that you'll have to answer a few questions about your conditions
Do you feel any of the following symptoms:
headache (yes/no): yes
back pain (yes/no): no
chest pain (yes/no): yes
cough (yes/no): yes

The most probable disease that you have is Influenza.
A short description of the disease is given below:
Influenza, commonly known as 'the flu', is a viral infection that attacks your respiratory system.

The common medications and procedures suggested by other real doctors are:
- Antiviral drugs
- Rest and hydration


#Directory Structure
Medical-Expert-System-Knowledge-Base/
│
├── expert_system.py                 # Main Python script
├── diseases.txt                     # List of diseases
├── Disease symptoms/                # Folder containing symptoms files for each disease
│   ├── Disease1.txt
│   ├── Disease2.txt
│   └── ...
├── Disease descriptions/            # Folder containing descriptions for each disease
│   ├── Disease1.txt
│   ├── Disease2.txt
│   └── ...
└── Disease treatments/              # Folder containing treatments for each disease
    ├── Disease1.txt
    ├── Disease2.txt
    └── ...


    
#Contributing
Feel free to contribute by submitting pull requests or reporting issues. Please make sure that all contributions align with the existing project structure.
