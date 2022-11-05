import pandas as pd
import numpy as np
import eel
from cryptography.fernet import Fernet
from datetime import datetime

Database = pd.read_pickle('pass')
# The data in encrypted form has its own datatype and class, if we save it to CSV, it gets turned into string.
# String cannot be decrypted by library as it is.
# To prevent that, we're using to_pickle().


# to add an id just put Add(user,pswd,site)
def Add(user, pswd, site) :
    pkey = Fernet.generate_key()
    fernet = Fernet(pkey)
    now = datetime.now()
    pswdencd = fernet.encrypt(pswd.encode())
    curtime = now.strftime("%d/%m/%Y %H:%M:%S")
    Database.loc[user, :] = [pswdencd, fernet, site, curtime]
    # We can't store Key as it in Database.
    # The Fernet(pkey) value generated everytime, even for same key is different
    # so we're storing Fernet(pkey) as it is
    Database.to_pickle('pass')


# to get data back use Collect(user)
def Collect(user) :
    pswd = Database.Pass[user]
    pfer = Database.Key[user]
    decoded_pass = pfer.decrypt(pswd).decode()
    return [decoded_pass, Database.Site[user], Database.DnT[user]]
