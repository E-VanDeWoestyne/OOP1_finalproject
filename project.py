class Doctor:
    # Constructor with attributes
    def __init__(self, doctor_id=None, name=None, specialization=None, worktime=None, qualification=None, room_number=None):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.worktime = worktime
        self.qualification = qualification
        self.room_number = room_number

    # String return for class 
    def __str__(self):
        return f"{self.doctor_id}_{self.name}_{self.specialization}_{self.worktime}_{self.qualification}_{self.room_number}"

    # Getters for each property
    def get_doctor_id(self):
        return(f"{self.doctor_id}")
    def get_doctor_name(self):
        return(f"{self.name}")
    def get_doctor_specialization(self):
        return(f"{self.specialization}")
    def get_doctor_worktime(self):
        return(f"{self.worktime}")
    def get_doctor_qualification(self):
        return(f"{self.qualification}")
    def get_doctor_room_number(self):
        return(f"{self.room_number}")
    # Setters for each property
    def set_doctor_id(self, new_id):
        self.doctor_id = new_id
    def set_doctor_name(self, new_name):
        self.name = new_name
    def set_doctor_specialization(self, new_specialization):
        self.specialization = new_specialization
    def set_doctor_worktime(self, new_worktime):
        self.worktime = new_worktime
    def set_doctor_qualification(self, new_qualification):
        self.qualification = new_qualification
    def set_doctor_room_number(self, new_room_number):
        self.room_number = new_room_number

class DoctorManager:
    # Creates a empty list and uses read_doctors_files to go through doctors.txt and add their info into a list of doctor objects
    def __init__(self):
        self.list_of_doctors = []
        self.read_doctors_file()
    
    # Formats doctor properties for printing to file
    def format_dr_info(self, doctor):
        return f"{doctor.doctor_id}_{doctor.name}_{doctor.specialization}_{doctor.worktime}_{doctor.qualification}_{doctor.room_number}"

    # Creates a new Doctor instance by getting user input
    def enter_dr_info(self):
        doctor_id = input("Enter the doctor's ID: ")
        doctor_name = input("Enter the doctor's name: ")
        doctor_specialty = input("Enter the doctor's specility: ")
        doctor_timing = input("Enter the doctor's timing (e.g., 7am-10pm): ")
        doctor_qualification = input("Enter the doctor's qualification: ")
        doctor_room_number = input("Enter the doctor's room number: ")
        new_doctor = Doctor(doctor_id, doctor_name, doctor_specialty, doctor_timing, doctor_qualification, doctor_room_number)
        return new_doctor

    # Reads doctors.txt, and then instances each one and appends it to the list_of_doctors
    def read_doctors_file(self):
        with open('doctors.txt', 'r') as doctorfile:
            content = doctorfile.read().strip()
            lines = content.splitlines()
            lines.pop(0)
            for line in lines:
                part = line.split('_')
                new_doctor = Doctor(part[0], part[1], part[2], part[3], part[4], part[5])
                self.list_of_doctors.append(new_doctor)

    # Searches doctors by their ID using user input and Doctor getter
    def search_doctor_by_id(self):
        id_search_match = False
        search_id = input("Enter the doctor ID: ")
        for doctor in self.list_of_doctors:
            if doctor.get_doctor_id() == search_id:
                doctor_index = doctor
                id_search_match = True
        if id_search_match == True:
            self.display_doctor_info(doctor_index)
        else:
            print("Can't find the doctor with the same ID on the system")

    # Searches doctors by their name using user input and Doctor getter
    def search_doctor_by_name(self):
        name_search_match = False
        search_name = input("Enter the doctor name: ")
        for doctor in self.list_of_doctors:
            if doctor.get_doctor_name() == search_name:
                doctor_index = doctor
                name_search_match = True
        if name_search_match == True:
            self.display_doctor_info(doctor_index)
        else:
            print("Can't find the doctor with the same name on the system")

    # Display the infor about a specific doctor using the doctor's index in the list_of_doctors
    def display_doctor_info(self, doctor_index):
            print(f"{"Id":<5}{"Name":<23}{"Speciality":<16}{"Timing":<16}{"Qualification":<16}Room Number\n")
            print(f"{doctor_index.get_doctor_id():<5}{doctor_index.get_doctor_name():<23}{doctor_index.get_doctor_specialization():<16}{doctor_index.get_doctor_worktime():<16}{doctor_index.get_doctor_qualification():<16}{doctor_index.get_doctor_room_number()}")

    # Using user input, edits the properties of the specific Doctor instance by getting their ID to search, and then re-writes new info to file
    def edit_dr_info(self):
        id_search_match = False
        search_id = input("Please enter the id of the doctor that you want to edit their information: ")
        for doctor in self.list_of_doctors:
            if doctor.get_doctor_id() == search_id:
                doctor_index = doctor
                id_search_match = True
        if id_search_match == True:
            doctor_index.set_doctor_name(input("Enter new Name: "))
            doctor_index.set_doctor_specialization(input("Enter new Specialty: "))
            doctor_index.set_doctor_worktime(input("Enter new Timing: "))
            doctor_index.set_doctor_qualification(input("Enter new Qualification: "))
            doctor_index.set_doctor_room_number(input("Enter new Room number: "))
            self.write_list_of_doctors_to_file()
            print(f"\nDoctor whose ID is {search_id} has been edited")
        else:
            print("Can't find the doctor with the same ID on the system")

    # Display a list of info for every doctor in the system
    def display_doctors_list(self):
            print(f"{"Id":<5}{"Name":<23}{"Speciality":<16}{"Timing":<16}{"Qualification":<16}Room Number\n")
            for doctor_index in self.list_of_doctors:
                print(f"{(doctor_index.get_doctor_id()):<5}{(doctor_index.get_doctor_name()):<23}{(doctor_index.get_doctor_specialization()):<16}{(doctor_index.get_doctor_worktime()):<16}{(doctor_index.get_doctor_qualification()):<16}{doctor_index.get_doctor_room_number()}")

    # Writes the list_of_doctors to file with proper formatting
    def write_list_of_doctors_to_file(self):
        with open('doctors.txt', 'w') as doctorfile:
            doctorfile.write("id_name_specilist_timing_qualification_roomNb")
            for doctor in self.list_of_doctors:
                doctorfile.write(f"\n{str(doctor)}")

    # Adds a new doctor to file using enter_dr_info()
    def add_dr_to_file(self):
        new_doctor = self.enter_dr_info()
        self.list_of_doctors.append(new_doctor)
        with open('doctors.txt', 'a') as doctorfile:
            doctorfile.write(f"\n{str(new_doctor)}")
        print(f"\nDoctor whose ID is {new_doctor.get_doctor_id()} has been added")

class Patient:
    # Constructor with attributes
    def __init__(self, pid=None, name=None, disease=None, gender=None, age=None):
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age
    
    # String return for class 
    def __str__(self):
        return f"{self.pid}_{self.name}_{self.disease}_{self.gender}_{self.age}"

    # Getters for each property
    def get_pid(self):
        return (f"{self.pid}")
    def get_name(self):
        return (f"{self.name}")
    def get_disease(self):
        return (f"{self.disease}")
    def get_gender(self):
        return (f"{self.gender}")
    def get_age(self):
        return (f"{self.age}")
    # Setters for each property
    def set_pid(self, new_pid):
        self.pid = new_pid
    def set_name(self, new_name):
        self.name = new_name
    def set_disease(self, new_disease):
        self.disease = new_disease
    def set_gender(self, new_gender):
        self.gender = new_gender
    def set_age(self, new_age):
        self.age = new_age


class PatientManager:
    # Creates a empty list and uses read_patients_files to go through patients.txt and add their info into a list of patients objects
    def __init__(self):
        self.list_of_patients = []
        self.read_patients_file()

    # Reads patient file
    def read_patients_file(self):
        with open('patients.txt', 'r') as patientfile:
            content = patientfile.read().strip()
            lines = content.splitlines()
            lines.pop(0)
            for line in lines:
                part = line.split('_')
                new_patient = Patient(part[0], part[1], part[2], part[3], part[4])
                self.list_of_patients.append(new_patient)

    # Formats patient info for writing to file
    def format_patient_Info_for_file(self, patient_index):
        return f"{patient_index.pid}_{patient_index.name}_{patient_index.disease}_{patient_index.gender}_{patient_index.age}"

    # Instantates and returns a patient object
    def enter_patient_info(self):
        pid = input("Enter id: ")
        name = input("Enter name: ")
        disease = input("Enter disease: ")
        gender = input("Enter gender: ")
        age = input("Enter age: ")
        patient_object = Patient(pid, name, disease, gender, age)
        return patient_object
    
    # Searches for patient matching id and displays their info
    def search_patient_by_id(self):
        pid_search_match = False
        search_pid = input("Enter the patient ID: ")
        for patient in self.list_of_patients:
            if patient.get_pid() == search_pid:
                patient_index = patient
                pid_search_match = True
        if pid_search_match == True:
            self.display_patient_info(patient_index)
        else:
            print("Can't find the Patient with the same ID on the system")

    # Displays a specific patient's info
    def display_patient_info(self, patient_index):
            print(f"{"Id":<5}{"Name":<23}{"Disease":<16}{"Gender":<16}{"Age"}\n")
            print(f"{(patient_index.get_pid()):<5}{(patient_index.get_name()):<23}{(patient_index.get_disease()):<16}{(patient_index.get_gender()):<16}{(patient_index.get_age())}")

    # Edits patient info by pid and updates .txt file 
    def edit_patient_info_by_id(self):
        pid_search_match = False
        search_pid = input("Enter the patient ID you wish to edit: ")
        for patient in self.list_of_patients:
            if patient.get_pid() == search_pid:
                patient_index = patient
                pid_search_match = True
        if pid_search_match == True:
            new_name = input("Enter new name: ")
            patient_index.set_name(new_name)
            new_disease = input("Enter new disease: ")
            patient_index.set_disease(new_disease) 
            new_gender = input("Enter new gender: ")
            patient_index.set_gender(new_gender)
            new_age = input("Enter new age: ")
            patient_index.set_age(new_age) 
            self.write_list_of_patients_to_file()
            print(f"Patient whose ID is {search_pid} has been edited.")
        else:
            print("Cannot find the patient ….")

    # Prints out the entire list of patients
    def display_patients_list(self):
            print(f"{"Id":<5}{"Name":<23}{"Disease":<16}{"Gender":<16}{"age"}\n")
            for patient in self.list_of_patients:
                print(f"{(patient.get_pid()):<5}{(patient.get_name()):<23}{(patient.get_disease()):<16}{(patient.get_gender()):<16}{(patient.get_age())}")

    # Overwrites the patient .txt and writes a formated version of list_of_patients
    def write_list_of_patients_to_file(self):
            with open('patients.txt', 'w') as patientfile:
                patientfile.write("id_Name_Disease_Gender_Age")
                for patient in self.list_of_patients:
                    patientfile.write(f"\n{self.format_patient_Info_for_file(patient)}")    

    # Prompts the user to create a patient object and appends it to the list and .txt
    def add_patient_to_file(self):
        patient = self.enter_patient_info()
        self.list_of_patients.append(patient)
        with open('patients.txt', 'a') as patientfile:
            patientfile.write(f"\n{self.format_patient_Info_for_file(patient)}")
        print(f"Patient whose ID is {patient.get_pid()} has been added.")

class Manager:
    @staticmethod
    def display_menu():
        main_flag = True
        while main_flag == True:
            print("Welcome to Alberta Hospital (AH) Managment system\nSelect from the following options, or select 3 to stop:\n1 - 	Doctors\n2 - 	Patients\n3 -	Exit Program")
            main_input = input(">>> ")

            # If the user chooses doctor menu, a DoctorManager instance is generated and it does tasks from user inputs by using methods of DoctorManager
            if main_input == "1":
                doctor_flag = True
                while doctor_flag == True:
                    doc_manager_instance = DoctorManager()
                    print("Doctors Menu:\n1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu")
                    doctor_input = input(">>> ")
                    if doctor_input == "1":
                        doc_manager_instance.display_doctors_list()
                    elif doctor_input == "2":
                        doc_manager_instance.search_doctor_by_id()
                    elif doctor_input == "3":
                        doc_manager_instance.search_doctor_by_name()
                    elif doctor_input == "4":
                        doc_manager_instance.add_dr_to_file()
                    elif doctor_input == "5":
                        doc_manager_instance.edit_dr_info()
                    elif doctor_input == "6":
                        doctor_flag = False

            # If the user chooses patient menu, a PatientManager instance is generated and it does tasks from user inputs by using methods of PatientManager
            elif main_input == "2":
                patient_flag = True
                while patient_flag == True:
                    patient_manager_instance = PatientManager()
                    print("Patients Menu:\n1 - Display patients list\n2 - Search for patient by ID\n3 - Add patient\n4 - Edit patient info\n5 - Back to the Main Menu")
                    patient_input = input(">>> ")
                    if patient_input == "1":
                        patient_manager_instance.display_patients_list()
                    elif patient_input == "2":
                        patient_manager_instance.search_patient_by_id()
                    elif patient_input == "3":
                        patient_manager_instance.add_patient_to_file()
                    elif patient_input == "4":
                        patient_manager_instance.edit_patient_info_by_id()
                    elif patient_input == "5":
                        patient_flag = False

            # Exit out of the program and say good bye
            elif main_input == "3":
                main_flag = False
                print("Thanks for using the program. Bye!")

Manager.display_menu()