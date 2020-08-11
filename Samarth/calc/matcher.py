import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

class Ret_Name:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def return_name(self):
        return (f'Names Entered: {self.name}')
    
    def return_gender(self):
        return( f'Gender is: {self.age}' )