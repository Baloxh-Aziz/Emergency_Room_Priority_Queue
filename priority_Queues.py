class Patient:
    def __init__(self, name, severity):
        self.name = name
        self.severity = severity # Lower number = higher priority

    def __str__(self):
        return f"{self.name} (Severity: {self.severity})"
    
class EmergencyRoom:
    # Task 2: Dynamic Capacity
    def __init__(self,capacity = 6):
        self.capacity = capacity
        self.queue = []
        
    def add_patient(self, patient):
        # Task 4: Emergency Override
        if len(self.queue) >= self.capacity and patient.severity == 0:
            print(f"Emergency override! Added critical patient {patient.name}.")
            self.queue.append(patient)
            self.queue.sort(key=lambda p: p.severity)
            return
        
        # Task 1: Capacity Handling
        elif len(self.queue) >= self.capacity:
            print(f"Queue is full! Cannot add {patient.name}.")
            return
        self.queue.append(patient)
        self.queue.sort(key=lambda p: p.severity)

    def treat_patient(self):
        if self.queue:
            patient = self.queue.pop(0)
            print(f"Treating: {patient}")
        else:
            print("No patients to treat.")

    def show_queue(self):
        print("Current Patient Queue:")
        for i, patient in enumerate(self.queue, start=1):
            print(f"{i}. {patient}")
            print()

# Example usage
er = EmergencyRoom()
er.add_patient(Patient("Zara", 2))
er.add_patient(Patient("Ali", 5))
er.add_patient(Patient("Fatima", 3))
er.add_patient(Patient("John", 1))
er.show_queue()
er.treat_patient()
er.show_queue()