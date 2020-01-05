class VerificationProof:
    
    def __init__(self):
    
        self.ver_flag = False
        self.id_type = ""
        self.id_no = ""
        self.id_path = ""
        self.carely_id = ""
        #under_ver = False ----> Print using function when finding data
    
    def is_verified(cat):

        if not ver_flag:
            print(cat," is not verified")
        #else if not under_ver:
        #    print(cat," is under verification process")
        else:
            print(cat," is Verified")

    #def get_verified(cat, info):
        #show id proof and details of person and check if verified or not

    #def upload_details(cat,image):
        #upload details of id proof, change under_ver to true
