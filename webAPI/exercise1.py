import subprocess
import json

def check_employee(id):
    result = subprocess.Popen(f'curl https://dummy.restapiexample.com/api/v1/employee/{id} -X GET', shell=True, stdout=subprocess.PIPE)
    result.wait()
    data, err = result.communicate()
    result = json.loads(str(data.decode('utf-8')))
    print(result)

def create_employee():
    data = '{"name": "test", "salary": 123, "age": 23}'
    
    result = subprocess.Popen(f'curl https://dummy.restapiexample.com/api/v1/create -H "Content-Type: application/json" -d {data} -X POST' , shell=True, stdout=subprocess.PIPE)
    result.wait()
    data, err = result.communicate()
    result = json.loads(str(data.decode('utf-8')))
    print(result)
    if result["status"] == "success":
        id = result["data"]
        print(id["id"])
        return id["id"]
    else:
        print("Not created")

def delete_employee(id):
    result = subprocess.Popen(f'curl https://dummy.restapiexample.com/api/v1/delete/{id} -X DELETE', shell=True, stdout=subprocess.PIPE)
    result.wait()
    data, err = result.communicate()
    result = json.loads(str(data.decode('utf-8')))
    print("deleted with ",{result["status"]})

id_created = create_employee()
check_employee(id_created)
#delete_employee(id_created)