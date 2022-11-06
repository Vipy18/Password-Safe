import pandas as pd
from cryptography.fernet import Fernet

# Use this to reset or initialize pass file
# A sample or Original Pass file is needed for this, find it in Clear Data Folder
print(r"You need to enter access key, it'll be used to extract you password. Be sure to remeber it")
pswd = input('Access Key:\n')
pkey = Fernet.generate_key()
fernet = Fernet(pkey)
pswdencd = fernet.encrypt(pswd.encode())
B = pd.read_pickle('pass')
for user in B.index:
    B = B.drop(user, axis=0)

B.at['MastPass', 'Pass'] = pswdencd
B.at['MastPass', 'Site'] = 'root'
B.at['MastPass', 'Key'] = fernet
print(B)
B.to_pickle('pass')
