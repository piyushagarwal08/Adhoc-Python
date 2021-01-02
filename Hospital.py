import sys
class Hospital:
    def __init__(self,Id,FirstName,LastName):
        print()
        self.Id = Id.lower()
        self.FirstName = FirstName.lower()
        self.LastName = LastName.lower()

    def PatientData(self):
        file = open("Patient.txt","r")
        content = file.read().strip().split("\n")
        PatientData = []
        for data in content:
            PatientData.append(data.split(","))
            
        return PatientData

    def DoctorData(self):
        file = open("Doctors.txt","r")
        content = file.read().strip().split("\n")
        DoctorData = []
        for data in content:
            DoctorData.append(data.split(","))
            
        return DoctorData

    def DataFormatting(self,Result):
        for i in range(0,len(Result)-1):
            Result[i] = Result[i]+","
        Result[-1] = Result[-1] +"\n"
        return Result

        
        
    def addVisit(self):
        flag=False
        self.DoctorId = input("Enter the doctor Id: ").strip().lower()
        DoctorData = self.DoctorData()
        
        PatientData = self.PatientData()

        try:
            docDetails = [i for i in DoctorData if i[0].lower() == self.DoctorId][0]
        except:
            print("There is no such doctor in hospital")
            sys.exit()
            
        if len(docDetails) > 0 and int(docDetails[-1])<40:
            try:
                patientDetails = [i for i in PatientData if i[0].lower() == self.Id][0]
            except:
                patientDetails = []
                
            if len(patientDetails)==0:
                PatientVisit = '0'
                PatientConsultationHours = int(input("Enter no of hours of consultation required: "))
                Result = [self.Id,self.DoctorId,self.FirstName,self.LastName,PatientVisit,str(PatientConsultationHours)]
                docDetails[-1] = str(int(docDetails[-1])+PatientConsultationHours)
                flag=True
            else:
                PatientConsultationHours = int(input("Enter no of hours of consultation required: "))
                Result = [self.Id,self.DoctorId,self.FirstName,self.LastName,str(int(patientDetails[4])+1),str(int(patientDetails[-1])+PatientConsultationHours)]
                docDetails[-1] = str(int(docDetails[-1])+PatientConsultationHours)
                
            with open("Patient.txt","w") as file:
                self.PatientPayData= (int(Result[4]),PatientConsultationHours)
                if flag:
                    PatientData.append(Result)
                else:
                    for data in PatientData:
                        if data[0].lower() == self.Id:
                            PatientData[PatientData.index(data)] = Result
                            break
                for data in PatientData:
                    file.writelines(self.DataFormatting(data))
                    

            with open("Doctors.txt","w") as file:
                for data in DoctorData:
                    if data[0].lower() == self.DoctorId:
                        DoctorData[DoctorData.index(data)] = docDetails
                        break
                            
                for data in DoctorData:
                    file.writelines(self.DataFormatting(data))
        else:
            print("Doctor cannot have more visits this week")
            sys.exit()
        return

    def calculatePay(self,PatientPayData):
        print()
        DoctorData = self.DoctorData()
        try:
            doctorDetails = [i for i in DoctorData if i[0].lower() == self.DoctorId][0]
        except:
            print("No such doctor in hospital")
            return
        if PatientPayData[0]<3:
            print("Pay: AED ",PatientPayData[1]*150)
        else:
            print("Pay: AED ",PatientPayData[1]*50)
        
        return

    def calculateBill(self,PatientPayData):
        print()
        DoctorData = self.DoctorData()
        PatientData = self.PatientData()
        for data in DoctorData:
            if data[0] == self.DoctorId:
                print("Doctor Details")
                print("  ".join(data))
                HourlyPay = float(data[-2])
                break
        for data in PatientData:
            if data[0] == self.Id:
                print("Patient Details")
                print("  ".join(data))
                Pay = PatientPayData[1]*HourlyPay
                break
        TotalPay = 0.05*Pay + Pay
        print("Pay(including VAT) AED:",TotalPay)
        return
    
obj1 = Hospital("17BCON173","Name","LastName")
obj1.addVisit()
obj1.calculatePay(obj1.PatientPayData)
obj1.calculateBill(obj1.PatientPayData)

obj2 = Hospital("17BCO23198","ABC","JAIN")
obj2.addVisit()
obj2.calculatePay(obj1.PatientPayData)
obj2.calculateBill(obj1.PatientPayData)

obj3 = Hospital("17BCON173","Marie","Agarwal")
obj3.addVisit()
obj3.calculatePay(obj1.PatientPayData)
obj3.calculateBill(obj1.PatientPayData)
