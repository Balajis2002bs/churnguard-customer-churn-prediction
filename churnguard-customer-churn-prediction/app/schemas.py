from pydantic import BaseModel


class Customer_Data(BaseModel):
    gender:  str
    PhoneService: str
    InternetService: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    
    
    
    
    
    