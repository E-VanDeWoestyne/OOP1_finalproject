class Doctor:
    def __init__(self, doctor_id, name, specialization, worktime, qualification, room_number):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.worktime = worktime
        self.qualification = qualification
        self.room_number = room_number

    def get_doctor_id(self):
        print(f"{self.doctor_id}")

    def get_doctor_name(self):
        print(f"{self.name}")

    def get_doctor_specialization(self):
        print(f"{self.get_doctor_specialization}")