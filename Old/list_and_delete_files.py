# import OS module
import os
import re

def Rename(name):
    renamed=""
    flag=True
    for chr in name:
        if ord(chr)<128:
            renamed+=chr
            flag=True
        else:
            if flag:
                renamed+="_"
            flag=False
    return renamed

def Rename1(name):
    renamed=""
    for chr in name:
        if ord(chr)<128:
            renamed+=chr
        else:
            renamed+="_"
    return renamed

def rename_dirs(root,dirs):

    for dir in dirs:
        r_dir=Rename(root+"\\"+dir)
        if r_dir!=root+"\\"+dir:
            try:
                os.rename(root+"\\"+dir,r_dir)
                print(root+"\\"+dir+"\n"+r_dir)
            except:
                r_dir=Rename1(root+"\\"+dir)
                print(root+"\\"+dir+"\n"+r_dir)
                os.rename(root+"\\"+dir,r_dir)

def check_and_rename(path):
    pass
    
def list_pattern_files(path,pattern):
    for (root, dirs, files) in os.walk(path):
        # print(root,dirs,files)
        rename_dirs(root,dirs)
        if os.path.exists(root):
            for file in files:
                r_file=Rename(root+"\\"+file)
                
                if r_file!=root+"\\"+file:
                    # print(root+"\\"+file+"\n"+r_file)                
                    try:
                        os.rename(root+"\\"+file,r_file)
                        print(root+"\\"+file+"\n"+r_file)
                    except Exception as e:
                        
                        if "file already exists" in str(e):
                            print("Failed with error ",str(e))
                            r_file=Rename1(root+"\\"+file)
                            r_file='.'.join(r_file.split(".")[:-1])+"_."+r_file.split(".")[-1]
                            print(root+"\\"+file+"\n"+r_file)
                            os.rename(root+"\\"+file,r_file)
                        else:
                            print("Failed with error ",str(e))
                # if re.match(r"[0-9]*", root+"\\"+file):
                #     print("Match "+root+"\\"+file)
                # if file.endswith(pattern):
                #     print(root+"\\"+file)
                #     os.remove(root+"\\"+file)
    
# Get the list of all files and directories
path = "D:\\Mega - Copy"
dir_list = os.listdir(path)

list_pattern_files(path,".mega")

# check_and_rename(path)

# print("Files and directories in '", path, "' :")

# # prints all files
# print(dir_list)
# print(*os.walk(path),sep='\n')


# for f in glob.glob():
#     # os.remove(f)
#     print(f)
