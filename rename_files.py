import os
def rename_files():
    file_list=os.listdir(r"C:\Users\Dell\Documents\Python Programs\prank")
    path=os.getcwd()
    os.chdir(r"C:\Users\Dell\Documents\Python Programs\prank")
    #print file_list
    for file_name in file_list:
        new_name=file_name.translate(None,"1234567890")
        os.rename(file_name,new_name)
    os.chdir(path)
    os.rename("xyz","abc")
rename_files()
