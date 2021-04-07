"""Module """
from secure_all import AccessRequest
from secure_all.access_management_exception import AccessManagementException

class AccessManager:
    """Class for providing the methods for managing the access to a building"""
    def __init__(self):
        pass

    @staticmethod
    def validate_dni(dni):
        """RETURN TRUE IF THE DNI IS RIGHT, OR FALSE IN OTHER CASE"""

        if dni.isdigit():
            raise AccessManagementException("Invalid DNI. No letter found")
        #else:
            #raise AccessManagementException("Invalid DNI. No letter found")

        if dni.isalpha():
            raise AccessManagementException("Invalid DNI. Only string inserted")

        for i in dni:
            if i == ".":
                raise AccessManagementException("Invalid DNI. Float numbers inserted")


        if len(dni) ==9:
            dni_letter = ('T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X',
                          'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K',
                          'E')

            id_card = ""
            letter = ""

            for i in dni:
                for j in dni_letter:
                    if i == j:
                        letter += i

            for i in dni:
                if i != letter:
                    id_card += i

            i = int(id_card) % 23
            letter = dni_letter[i]

            if letter != (dni[-1]):
                raise AccessManagementException("Invalid DNI letter")

            if letter == (dni[-1]):
                return True

        if len(dni)==8:
            raise AccessManagementException("Invalid DNI. Less than 9 characters found")

        if len(dni)==10:
            raise AccessManagementException("Invalid DNI. More characters than needed")


    def request_access_code(self, id_document, access_type, full_name, email_address, validity):
        """This function allows us to correct the invalid of the test access request"""
        if self.validate_dni(id_document) is False:
            raise AccessManagementException("DNI Invalid")

        if (access_type) not in "GUEST" and (access_type) not in"RESIDENT":
            raise AccessManagementException("Invalid DNI access type")

        if len(full_name) < 3:
            raise AccessManagementException("Invalid name. Less than 3 characters")

        if email_address != "jesusgil2001@gmail.com":
            raise AccessManagementException("Invalid email address")

        if access_type == "GUEST":
            if validity < 2 or validity > 15:
                raise AccessManagementException("Invalid validity for GUEST")

        if access_type == "RESIDENT":
            if validity != 0:
                raise AccessManagementException("Invalid validity for RESIDENT")

        if not " " in full_name:
            raise AccessManagementException("Invalid name. Blank space not found")

        else:
            a_l = AccessRequest (id_document, full_name, access_type, email_address, validity)
            #save the accessrequest in the JSON file
            return a_l.access_code
