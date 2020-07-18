import os
def make_folder(folder_name):
    os.mkdir("..\\data\\solutions\\"+folder_name)
def file_read():
    with open("..\\data\\student_data.csv") as file:
        data=file.read()
        data=data.splitlines()
        final_list=[]
        for i in data:
            final_list.append(i.split(","))
        return final_list


def get_code(project_name,data):
    url="git clone https://github.com/"
    os.chdir("..\\data\\solutions\\"+project_name)

    for i in data:
        os.mkdir(i[2])
        os.chdir(i[2])
        os.system("git clone " + url+i[2]+"/"+project_name)
        os.chdir("..")
    os.chdir("..\\..\\..\\code")

def read_outputs():
    number_outputs=os.listdir("..\\test_cases\\output")
    outputs=[]
    os.chdir("..\\test_cases\\output")
    for i in range(1,number_outputs+1):
        file_name=str(i)+".txt"

        with open(file_name) as file:
            outputs.append(file.read().rstrip())
    os.chdir("..\\..\\code")
    return outputs

def run_code(data,project_name,file_name,outputs):
    number_inputs=len(os.listdir("..\\test_caes\\imput"))
    os.chdir("..\\Data\\solutions\\"+project_name)

    score=[]
    for i in range(len(data)):
        os.chdir(data[i][2])

        for inp in range(1,number_inputs+1):
            os.system("python" +file_name +".py"+"<..\\..\\..\\..\\test_cases\\"+str(inp)+".txt"+">"+str(inp)+" .output")
            with open (str(inp)+".ouput") as file:
                if(outputs[inp-1]==file.read()):
                    score.append(True)
                else:
                    score.append(False)
        data[i].append(score)
        #potential error
        score.clear()

        os.chdir("..")
    os.chdir("..\\..\\..\\code")
    return data
    

