from experta import KnowledgeEngine, Fact, Rule, DefFacts, NOT, W, MATCH

diseases_list = []
diseases_symptoms = []
symptom_map = {}
d_desc_map = {}
d_treatment_map = {}

def preprocess():
    global diseases_list, diseases_symptoms, symptom_map, d_desc_map, d_treatment_map
    diseases = open(r"C:\Users\hriti\OneDrive\Desktop\PYTHON\Medical-Expert-System-Knowledge-Base-master\diseases.txt")
    diseases_t = diseases.read()
    diseases_list = diseases_t.split("\n")
    diseases.close()
    
    for disease in diseases_list:
        # Open and process Disease symptoms file
        disease_s_file = open(r"C:\Users\hriti\OneDrive\Desktop\PYTHON\Medical-Expert-System-Knowledge-Base-master\Disease symptoms\\" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        s_list = disease_s_data.split("\n")
        s_list = tuple([symptom.lower().strip() for symptom in s_list])  # Normalize and store as tuple
        diseases_symptoms.append(s_list)
        symptom_map[s_list] = disease
        disease_s_file.close()
        
        # Open and process Disease descriptions file
        disease_s_file = open(r"C:\Users\hriti\OneDrive\Desktop\PYTHON\Medical-Expert-System-Knowledge-Base-master\Disease descriptions\\" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        d_desc_map[disease] = disease_s_data
        disease_s_file.close()
        
        # Open and process Disease treatments file
        disease_s_file = open(r"C:\Users\hriti\OneDrive\Desktop\PYTHON\Medical-Expert-System-Knowledge-Base-master\Disease treatments\\" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        d_treatment_map[disease] = disease_s_data
        disease_s_file.close()

def get_details(disease):
    return d_desc_map.get(disease, "No description available")

def get_treatments(disease):
    return d_treatment_map.get(disease, "No treatment available")

def if_not_matched(disease):
    if disease:  # Ensure there's a disease to show details for
        print(f"\nThe most probable disease that you have is {disease}\n")
        print("A short description of the disease is given below:\n")
        print(get_details(disease) + "\n")
        print("The common medications and procedures suggested by other real doctors are:\n")
        print(get_treatments(disease) + "\n")
    else:
        print("\nDid not find any disease that matches your exact symptoms.\n")

class Greetings(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        print("\nHi! I am Ashish R. Chauhan, I am here to help you make your health better.")
        print("For that you'll have to answer a few questions about your conditions")
        print("Do you feel any of the following symptoms:")
        yield Fact(action="find_disease")

    @Rule(Fact(action='find_disease'), NOT(Fact(headache=W())), salience=1)
    def symptom_0(self):
        self.declare(Fact(headache=input("headache (yes/no): ").strip().lower()))

    @Rule(Fact(action='find_disease'), NOT(Fact(back_pain=W())), salience=1)
    def symptom_1(self):
        self.declare(Fact(back_pain=input("back pain (yes/no): ").strip().lower()))

    @Rule(Fact(action='find_disease'), NOT(Fact(chest_pain=W())), salience=1)
    def symptom_2(self):
        self.declare(Fact(chest_pain=input("chest pain (yes/no): ").strip().lower()))

    @Rule(Fact(action='find_disease'), NOT(Fact(cough=W())), salience=1)
    def symptom_3(self):
        self.declare(Fact(cough=input("cough (yes/no): ").strip().lower()))

    # Add additional symptoms here...

    @Rule(Fact(action='find_disease'), Fact(disease=MATCH.disease), salience=-998)
    def disease(self, disease):
        if_not_matched(disease)

    @Rule(Fact(action='find_disease'),
          Fact(headache=MATCH.headache),
          Fact(back_pain=MATCH.back_pain),
          Fact(chest_pain=MATCH.chest_pain),
          Fact(cough=MATCH.cough),
          # Add all symptoms here...
          NOT(Fact(disease=MATCH.disease)), salience=-999)
    def not_matched(self, headache, back_pain, chest_pain, cough):
        print("\nDid not find any disease that matches your exact symptoms")
        lis = [headache, back_pain, chest_pain, cough]
        lis = [symptom if symptom == "yes" else "no" for symptom in lis]  # Normalize input for matching
        max_count = 0
        max_disease = ""
        
        for key, val in symptom_map.items():
            count = 0
            for j in range(len(lis)):
                if key[j] == "yes" and lis[j] == "yes":
                    count += 1
            if count > max_count:
                max_count = count
                max_disease = val
        if_not_matched(max_disease)

if __name__ == "__main__":
    preprocess()
    engine = Greetings()
    while True:
        engine.reset()  # Prepare the engine for the execution.
        engine.run()    # Run it!
        print("Would you like to diagnose some other symptoms? (yes/no)")
        if input().lower() == "no":
            print("You are Healthy , No need treatment")
            break  # Use break instead of exit() to allow for cleanup
