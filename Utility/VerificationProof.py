class VerificationProof:
    def __init__(self):

        self.ver_flag = False
        self.id_type = ""
        self.id_no = ""
        self.id_path = ""
        self.carely_id = ""
        self.under_ver = "False"

    # def get_verified(cat, info):
    # show id proof and details of person and check if verified or not

    def update_details(self):  # (,image):
        print("\nVerification ID Details :- \n")
        self.id_type = input("Enter ID Type: ")
        self.id_no = input("Enter ID Number: ")
        self.id_path = input("Enter ID file path(images/vp/): ")
        self.under_ver = "True"
        return (self.ver_flag, self.under_ver, self.id_type, self.id_no, self.id_path)
