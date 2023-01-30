
def emptyMessage(field):
        return (f"{field} cannot be blank or empty")
    
class ValidationUtils():
    def isEmpty(value : str, field: str):
        value = value.strip()
        if not value:
            raise Exception(emptyMessage(field))        
