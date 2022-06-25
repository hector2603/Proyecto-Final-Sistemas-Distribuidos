import json
from InitDB import InitDB
from Repository import Repository
from flask import Flask , request

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Service up'

@app.route('/teacher', methods=['POST'])
def add_teacher():
  repository = Repository()
  json_data = request.get_json(force=True)
  _code = json_data['code']
  _name = json_data['name']
  _lastName = json_data['lastName']
  sql = "INSERT INTO teacher (teacher_code, teacher_name, teacher_last_name)VALUES(%s, %s, %s)"
  data = (_code, _name, _lastName,)
  repository.executeQuery(sql,data) 
  return "teacher created successfully"
  
@app.route('/teacher/<id>', methods=['PUT'])
def update_teacher(id):
  repository = Repository()
  json_data = request.get_json(force=True)
  _name = json_data['name']
  _lastName = json_data['lastName']
  sql = "UPDATE teacher SET teacher_name = %s , teacher_last_name = %s WHERE teacher_code = %s"
  data = (_name, _lastName, id)
  repository.executeQuery(sql,data) 
  return "teacher updated successfully"

@app.route('/teacher', methods=['GET'])
def get_teacher():
  repository = Repository()
  results, row_headers= repository.executeSelectQuery("SELECT * FROM teacher") 
  print(results)
  json_data= []
  for result in results:
    print(result)
    json_data.append(dict(zip(row_headers,result)))
  return json.dumps(json_data)

@app.route('/teacher/<id>', methods=['GET'])
def find_teacher(id):
  repository = Repository()
  results, row_headers= repository.executeSelectQuery("SELECT * FROM teacher WHERE teacher_code={}".format(id)) 
  print(results)
  json_data= []
  for result in results:
    print(result)
    json_data.append(dict(zip(row_headers,result)))
  return json.dumps(json_data)

### Student APIs
@app.route('/student', methods=['POST'])
def add_student():
  repository = Repository()
  json_data = request.get_json(force=True)
  _code = json_data['code']
  _name = json_data['name']
  _lastName = json_data['lastName']
  sql = "INSERT INTO student (student_code, student_name, lstudent_ast_name)VALUES(%s, %s, %s)"
  data = (_code, _name, _lastName,)
  repository.executeQuery(sql,data) 
  return "student created successfully"
  
@app.route('/student/<id>', methods=['PUT'])
def update_student(id):
  repository = Repository()
  json_data = request.get_json(force=True)
  _name = json_data['name']
  _lastName = json_data['lastName']
  sql = "UPDATE student SET student_name = %s , lstudent_ast_name = %s WHERE student_code = %s"
  data = (_name, _lastName, id)
  repository.executeQuery(sql,data) 
  return "student updated successfully"

@app.route('/student', methods=['GET'])
def get_student():
  repository = Repository()
  results, row_headers= repository.executeSelectQuery("SELECT * FROM student") 
  print(results)
  json_data= []
  for result in results:
    print(result)
    json_data.append(dict(zip(row_headers,result)))
  return json.dumps(json_data)

@app.route('/student/<id>', methods=['GET'])
def find_student(id):
  repository = Repository()
  results, row_headers= repository.executeSelectQuery("SELECT * FROM student WHERE student_code={}".format(id)) 
  print(results)
  json_data= []
  for result in results:
    print(result)
    json_data.append(dict(zip(row_headers,result)))
  return json.dumps(json_data)

### Course APIs
@app.route('/course', methods=['POST'])
def add_course():
  repository = Repository()
  json_data = request.get_json(force=True)
  _code = json_data['code']
  _name = json_data['name']
  sql = "INSERT INTO course (course_code, course_name)VALUES(%s, %s)"
  data = (_code, _name)
  repository.executeQuery(sql,data) 
  return "course created successfully"
  
@app.route('/course/<id>', methods=['PUT'])
def update_course(id):
  repository = Repository()
  json_data = request.get_json(force=True)
  _name = json_data['name']
  sql = "UPDATE course SET course_name = %s WHERE course_code = %s"
  data = (_name, id)
  repository.executeQuery(sql,data) 
  return "course updated successfully"

@app.route('/course', methods=['GET'])
def get_course():
  repository = Repository()
  results, row_headers= repository.executeSelectQuery("SELECT * FROM course") 
  print(results)
  json_data= []
  for result in results:
    print(result)
    json_data.append(dict(zip(row_headers,result)))
  return json.dumps(json_data)

@app.route('/course/<id>', methods=['GET'])
def find_course(id):
  repository = Repository()
  results, row_headers= repository.executeSelectQuery("SELECT * FROM course WHERE course_code={}".format(id)) 
  print(results)
  json_data= []
  for result in results:
    print(result)
    json_data.append(dict(zip(row_headers,result)))
  return json.dumps(json_data)


### Class APIs
@app.route('/class', methods=['POST'])
def add_class():
  repository = Repository()
  json_data = request.get_json(force=True)
  _code = json_data['code']
  _course = json_data['course']
  _teacher = json_data['teacher']
  _year = json_data['year']
  _period = json_data['period']
  sql = "INSERT class (class_code, class_course_code, class_teacher_code, year, period)VALUES(%s, %s, %s, %s, %s)"
  data = (_code, _course, _teacher, _year, _period)
  repository.executeQuery(sql,data) 
  return "class created successfully"
  
@app.route('/class/<id>', methods=['PUT'])
def update_class(id):
  repository = Repository()
  json_data = request.get_json(force=True)
  _course = json_data['course']
  _teacher = json_data['teacher']
  _year = json_data['year']
  _period = json_data['period']
  sql = "UPDATE class SET class_course_code = %s, class_teacher_code = %s, year = %s, period = %s WHERE class_code = %s"
  data = (_course, _teacher, _year, _period, id)
  repository.executeQuery(sql,data) 
  return "class updated successfully"

@app.route('/class', methods=['GET'])
def get_class():
  repository = Repository()
  results, row_headers= repository.executeSelectQuery("SELECT * FROM class") 
  print(results)
  json_data= []
  for result in results:
    print(result)
    json_data.append(dict(zip(row_headers,result)))
  return json.dumps(json_data)

@app.route('/class/<id>', methods=['GET'])
def find_class(id):
  repository = Repository()
  results, row_headers= repository.executeSelectQuery("SELECT * FROM class WHERE class_code={}".format(id)) 
  print(results)
  json_data= []
  for result in results:
    print(result)
    json_data.append(dict(zip(row_headers,result)))
  return json.dumps(json_data)


### grades APIs
@app.route('/grades', methods=['POST'])
def add_grades():
  repository = Repository()
  json_data = request.get_json(force=True)
  _class = json_data['class']
  _student = json_data['student']
  _note = json_data['note']
  sql = "INSERT class_stundent_note (class_code, student_code, note)VALUES(%s, %s, %s)"
  data = (_class, _student, _note)
  repository.executeQuery(sql,data) 
  return "grade created successfully"
  
@app.route('/grades/', methods=['PUT'])
def update_grades():
  repository = Repository()
  _class = request.args.get('class')
  _student = request.args.get('student') 
  json_data = request.get_json(force=True)
  _note = json_data['note']
  sql = "UPDATE class_stundent_note SET note = %s WHERE class_code = %s AND student_code = %s"
  data = (_note, _class, _student)
  repository.executeQuery(sql,data) 
  return "grade updated successfully"

@app.route('/grades/all', methods=['GET'])
def get_grades():
  repository = Repository()
  results, row_headers= repository.executeSelectQuery("SELECT * FROM class_stundent_note") 
  print(results)
  json_data= []
  for result in results:
    print(result)
    json_data.append(dict(zip(row_headers,result)))
  return json.dumps(json_data)

@app.route('/grades/class_student', methods=['GET'])
def find_class_student_grades():
  repository = Repository()
  _class = request.args.get('class')
  _student = request.args.get('student')   
  results, row_headers= repository.executeSelectQuery("SELECT * FROM class_stundent_note WHERE class_code = {} AND student_code = {}".format(_class,_student)) 
  print(results)
  json_data= []
  for result in results:
    print(result)
    json_data.append(dict(zip(row_headers,result)))
  return json.dumps(json_data)

@app.route('/grades/class', methods=['GET'])
def find_class_grades():
  repository = Repository()
  _class = request.args.get('class')
  results, row_headers= repository.executeSelectQuery("SELECT * FROM class_stundent_note WHERE class_code = {} ".format(_class)) 
  print(results)
  json_data= []
  for result in results:
    print(result)
    json_data.append(dict(zip(row_headers,result)))
  return json.dumps(json_data)  

@app.route('/grades/student', methods=['GET'])
def find_student_grades():
  repository = Repository()
  _student = request.args.get('student')
  results, row_headers= repository.executeSelectQuery("SELECT * FROM class_stundent_note WHERE student_code = {} ".format(_student)) 
  print(results)
  json_data= []
  for result in results:
    print(result)
    json_data.append(dict(zip(row_headers,result)))
  return json.dumps(json_data)  

@app.route('/synchronize', methods=['GET'])
def synchronizeDB():
  repository = Repository()
  repository.synchronizeDB()
  return "Database synchronized successfully"

@app.route('/initdb')
def db_init():
  DB_Inited = InitDB()
  DB_Inited.initDB1()
  DB_Inited.initDB2()

  return 'init database'

if __name__ == "__main__":
  app.run(host ='0.0.0.0')