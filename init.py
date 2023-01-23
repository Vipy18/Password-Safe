import pandas as pd
from cryptography.fernet import Fernet
import os

# Use this to reset or initialize pass file
# A sample or Original Pass file is needed for this, find it in Clear Data Folder
print(r"You need to enter access key, it'll be used to extract you password. Be sure to remember it")
pswd = input('Access Key:\n')
pkey = Fernet.generate_key()
fernet = Fernet(pkey)
pswdencd = fernet.encrypt(pswd.encode())
while True:
    try:
        if os.path.exists("pass"):
            print('Resetting Access Key...')
            B = pd.read_pickle(r'pass')
            break
        else:
            raise ValueError
    except ValueError:
        print('Setting up Access Key...')
        B = pd.read_pickle(r'Clean Data\CleanpPass')
        for user in B.index :
            B = B.drop(user, axis=0)
        break


B.at['MastPass', 'Pass'] = pswdencd
B.at['MastPass', 'Site'] = 'root'
B.at['MastPass', 'Key'] = fernet
print(B)
B.to_pickle('pass')
input("Press Any Key to Finish...")
