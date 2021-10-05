from ntpath import join
import pandas as pd
import os


user_input = "Mu2.xlsx"
user_input = os.path.join(os.path.dirname(os.path.abspath(__file__)), user_input)
xls = pd.ExcelFile(user_input)
df = pd.read_excel(xls,index_col=False,na_values=["NA"], engine="openpyxl")

folder_Name = os.path.dirname(os.path.abspath(__file__))
# Removed from list by client 
def by_client():
    client_file_path = os.path.join(folder_Name, "Clients.txt")
    with open(client_file_path) as f:
            client_list = [line.rstrip() for line in f]
    for x in client_list:
            df.drop(df[df["Client"]  == x].index,inplace=True)
# ===================================
# Removed from list by domain
def by_domain():
    Domain_file_path = os.path.join(folder_Name, "Domain.txt")
    with open(Domain_file_path) as f:
            Domain_list = [line.rstrip() for line in f]
    for x in Domain_list:
            df.drop(df[df["Domain"]  == x].index,inplace=True)
# ===================================
# Removed from list by two statements
def by_twostatements():
        name_list = df["Name"].values.tolist()
        for i in name_list:
                if i.startswith("V"):

                        df.drop(df[df["Client"]  == "Client5"].index & df[df["Name"]  == i].index ,inplace=True)

                else:

                        continue


        df.drop(df[df["Client"]  == "Client5"].index & df[df["Name"]  == "DOKER"].index ,inplace=True)
# ===================================
# Removed from list because it's France
def by_france():
        name_list = df["Name"].values.tolist()
        for i in name_list:
                if i.startswith("IFR") | i.startswith("PFR"): #Removed from list because it's France

                                df.drop(df[df["Name"]  == i].index ,inplace=True) #Removed from list because it's France
                else:
                        
                        continue

        df.drop(df[df["IP"]  == "125.22.33"].index, inplace=True)

# ===================================
# Removed from list because Afee
def by_Afee():  
     Affe_file_path = os.path.join(folder_Name, "Afee.txt")
     with open(Affe_file_path) as f:
            Affe_list = [line.rstrip() for line in f]
     for x in Affe_list:
         df.drop(df[df["Name"]  == x].index ,inplace=True)
# ===================================
# Removed from list 
# by_client()
# by_domain()
# # by_twostatements()
by_Afee()

print(df)