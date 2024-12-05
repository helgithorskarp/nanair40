class ValidationUI:
    @staticmethod
    def validateName(name) -> str | bool:
        """Checks if the name is valid, includes only letters and is not empty, if [b]ack or [q]uit were entered we return the letter"""
        if name.lower() in ('q', 'b'):
            return name


        if not name:
            return False
        
        if not all(c.isalpha() or c == ' ' for c in name):
            return False

        
        return True
    
    @staticmethod
    def validateKennitala(kennitala) -> str | bool:
        """Checks if the kennitals is valid, includes only numbers and has len = 10, if [b]ack or [q]uit were entered we return the letter"""
        if kennitala.lower() in ('q', 'b'):
            return kennitala
        
        if len(kennitala) != 10:
            return False
        if not kennitala.isdigit():
            return False
        
        return True
    
    @staticmethod
    def validatePhone(phone) -> str | bool:
        """Checks if the phone number is valid, includes only numbers and has len = 7, if [b]ack or [q]uit were entered we return the letter"""
        if phone.lower() in ('q', 'b'):
            return phone
        if len(phone) != 7:
            return False
        if not phone.isdigit():
            return False
        
        return True

    @staticmethod
    def validateEmail(email) -> str | bool:
        ''''"""Checks if the email is valid, has a @ sign, if [b]ack or [q]uit were entered we return the letter"""'''
        if email.lower() in ('q', 'b'):
            return email
        
        if '@' in email:
            return True
        else:
            return False 


    @staticmethod
    def validateCondition(condition):
        if condition.lower() in ('q', 'b'):
            return condition
        
        if condition.lower() in ("excellent", "good", "fair", "poor"):
            return True
        return False
        

    @staticmethod
    def validateFacilitiesRequiringMaintenance(facilitiesRequiringMaintenance):
        if facilitiesRequiringMaintenance.lower() in ('q', 'b'):
            return facilitiesRequiringMaintenance
        
        return True
    

    @staticmethod
    def validateText(text):
        if text.lower() in ('q', 'b'):
            return text
        
        return True
    
    @staticmethod
    def validateID(propertyNumber):
        if propertyNumber.lower() in ('q', 'b'):
            return propertyNumber
        
        if not propertyNumber:
            return False
        
        return True
