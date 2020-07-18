import database as db

project_name=input("Enter project name : ")

db.make_folder(project_name)

data=db.file_read()


db.get_code(project_name,data)

outputs=db.read_outputs()
file_name=("Name of the file to run(without extension) : :")
data=db.run_code(data,project_name,outputs)

