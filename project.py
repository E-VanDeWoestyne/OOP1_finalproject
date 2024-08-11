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
