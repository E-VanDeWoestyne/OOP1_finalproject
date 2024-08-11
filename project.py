class Doctor:
    def __init__(self, doctor_id, name, specialization, worktime, qualification, room_number):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.worktime = worktime
        self.qualification = qualification
        self.room_number = room_number

    def __str__(self):
        return f"{self.doctor_id}_{self.name}_{self.specialization}_{self.worktime}_{self.qualification}_{self.room_number}"

    def get_doctor_id(self):
        print(f"{self.doctor_id}")

    def get_doctor_name(self):
        print(f"{self.name}")

    def get_doctor_specialization(self):
        print(f"{self.get_doctor_specialization}")

    def get_doctor_worktime(self):
        print(f"{self.get_doctor_worktime}")

    def get_doctor_qualification(self):
        print(f"{self.get_doctor_qualification}")

    def get_doctor_room_number(self):
        print(f"{self.get_doctor_room_number}")

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
    def __init__(self):
        self.list_of_doctors = []
        self.read_doctors_file()
    
    def format_dr_info(self, doctor):
        return f"{doctor.doctor_id}_{doctor.name}_{doctor.specialization}_{doctor.worktime}_{doctor.qualification}_{doctor.room_number}"

    def enter_dr_info(self, new_doctor):
        doctor_id = input("Enter the doctor's ID: ")
        doctor_name = input("Enter the doctor's name: ")
        doctor_specialty = input("Enter the doctor's specility: ")
        doctor_timing = input("Enter the doctor's timing (e.g., 7am-10pm): ")
        doctor_qualification = input("Enter the doctor's qualification: ")
        doctor_room_number = input("Enter the doctor's room number: ")
        new_doctor = Doctor(doctor_id, doctor_name, doctor_specialty, doctor_timing, doctor_qualification, doctor_room_number)
        return new_doctor

    def read_doctors_file(self):
        with open('doctors.txt', 'r') as doctorfile:
            content = doctorfile.read().strip()
        lines = content.splitlines()
        lines.pop(0)
        for line in lines:
            part = line.split('_')
            new_doctor = Doctor(part[0], part[1], part[2], part[3], part[4], part[5])
            self.list_of_doctors.append(part)

    def search_doctor_by_id(self):
        id_search_match = False
        search_id = input("Enter the doctor ID: ")
        for doctor in self.list_of_doctors:
            if doctor[0] == search_id:
                doctor_index = doctor
                id_search_match = True
        if id_search_match == True:
            print(f"{"Id":<5}{"Name":<23}{"Speciality":<16}{"Timing":<16}{"Qualification":<16}Room Number\n")
            print(f"{doctor_index[0]:<5}{doctor_index[1]:<23}{doctor_index[2]:<16}{doctor_index[3]:<16}{doctor_index[4]:<16}{doctor_index[5]}")
        else:
            print("Can't find the doctor with the same ID on the system")

    def search_doctor_by_name(self):
        name_search_match = False
        search_name = input("Enter the doctor name: ")
        for doctor in self.list_of_doctors:
            if doctor[0] == search_name:
                doctor_index = doctor
                name_search_match = True
        if name_search_match == True:
            print(f"{"Id":<5}{"Name":<23}{"Speciality":<16}{"Timing":<16}{"Qualification":<16}Room Number\n")
            print(f"{doctor_index[0]:<5}{doctor_index[1]:<23}{doctor_index[2]:<16}{doctor_index[3]:<16}{doctor_index[4]:<16}{doctor_index[5]}")
        else:
            print("Can't find the doctor with the same name on the system")