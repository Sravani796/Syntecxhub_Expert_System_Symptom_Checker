rules = [
    (["fever"], "fever detected"),(["cough"], "cough detected"),(["cold"], "common cold detected"),(["headache"], "headache detected"),
    (["chills"], "chills detected"),(["fatigue"], "fatigue detected"),(["weakness"], "weakness detected"),(["dizziness"], "dizziness detected"),
    (["nausea"], "nausea detected"),(["vomiting"], "vomiting detected"),(["diarrhea"], "diarrhea detected"),(["stomach pain"], "stomach pain detected"),

    (["fever", "cough"], "flu"),
    (["fever", "body pain"], "viral infection"),
    (["fever", "chills"], "infection"),
    (["fatigue", "weakness"], "low immunity"),

    (["cough", "sore throat"], "throat infection"),
    (["runny nose", "sneezing"], "common cold"),

    (["cough", "breathlessness"], "respiratory issue"),

    (["headache", "light sensitivity"], "migraine"),
    (["headache", "dizziness"], "low bp"),
    (["nausea", "headache"], "possible migraine"),
    (["headache"], "headache detected"),

    (["stomach pain", "vomiting"], "food poisoning"),
    (["diarrhea", "stomach pain"], "gastric issue"),

    (["breathlessness", "chest pain"], "emergency condition"),

    (["flu", "body pain"], "influenza suspected"),
    (["viral infection"], "rest advised"),
    (["respiratory issue"], "consult doctor"),
    (["emergency condition"], "seek immediate help")
]
print("\nExpert System - Symptom Checker")
print("Enter symptoms separated by comma (e.g., fever, cough, headache)")

facts = set()
for s in input("Your symptoms: ").split(","):
    s = s.strip().lower()
    if s:
        facts.add(s)

log = []
changed = True

while changed:
    changed = False
    for condition, result in rules:
        if all(symptom in facts for symptom in condition) and result not in facts:
            facts.add(result)
            log.append(" + ".join(condition) + " -> " + result)
            changed = True

print("\nInference Steps:")
if log:
    for step in log:
        print(step)
else:
    print("No rules matched directly.")

print("\nFinal Observation:")
if "seek immediate help" in facts:
    print("Serious symptoms detected. Immediate medical attention recommended.")
elif "flu" in facts:
    print("Flu-like infection detected. Rest and hydration advised.")
elif "viral infection" in facts:
    print("Viral infection suspected. Take rest and monitor symptoms.")
elif "respiratory issue" in facts:
    print("Respiratory issue detected. Consult doctor if symptoms persist.")
elif "migraine" in facts or "headache detected" in facts:
    print("Headache-related condition detected. Avoid stress and rest well.")
elif "common cold" in facts:
    print("Common cold detected. Basic care and hydration recommended.")
elif "gastric issue" in facts:
    print("Digestive issue detected. Eat light food and rest.")
elif "low immunity" in facts:
    print("Low immunity detected. Improve diet and sleep cycle.")
else:
    print("No major condition detected. Monitor symptoms if they persist.")