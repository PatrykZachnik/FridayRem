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
# ==================================
# Removed from list by domain
def by_domain():
    client_file_path = os.path.join(folder_Name, "Domain.txt")
    with open(client_file_path) as f:
            client_list = [line.rstrip() for line in f]
    for x in client_list:
            df.drop(df[df["Domain"]  == x].index,inplace=True)
#===================================
# Removed from list by two statements
name_list = df["Name"].values.tolist()
for i in name_list:
        if i.startswith("V"):
                df.drop(df[df["Client"]  == "Client5"].index & df[df["Name"]  == i].index ,inplace=True)

        else:
                pass


df.drop(df[df["Client"]  == "Client5"].index & df[df["Name"]  == "DOKER"].index ,inplace=True)

    # if i.lower().startswith("v"):
        # df.drop(df[df["Client"]  == "Client5"].index & df[df["Name"]  == i],inplace=True)




print(df)