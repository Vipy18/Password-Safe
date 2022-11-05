import pandas as pd
import numpy as np
import eel
from cryptography.fernet import Fernet
from datetime import datetime

Database = pd.read_csv('pass.csv')

# to add an id just put Add(user,pswd,site)
def Add(user,pswd,site):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    now = datetime.now()
    Database.at[user,:] = [fernet.encrypt(pswd.encode()),key,site,now.strftime("%d/%m/%Y %H:%M:%S"),]
    Database.to_csv('pass.csv')

# to get data back use Collect(user)
def Collect(user):
    pswd = Database.Pass[user]
    key = Database.Key[user]
    fernet = Fernet(key)
    decoded_pass = fernet.decrypt(pswd).decode()
    return [decoded_pass,Database.Site[user],Database.DnT[user]]





    

