from ... import adminDB
from datetime import datetime

class Student(adminDB.Model):
        __bind_key__ = 'students_mysql'
        __tablename__ = 'student'       
        id = adminDB.Column(adminDB.Integer, primary_key = True)
        student_id = adminDB.Column(adminDB.String(40), nullable = False)
        first_name  = adminDB.Column(adminDB.String(40), nullable = False)
        last_name = adminDB.Column(adminDB.String(40), nullable = False)
        email = adminDB.Column(adminDB.String(40), nullable = False)
        degree_id = adminDB.Column(adminDB.Integer,adminDB.ForeignKey('university_degree.id'), nullable = False)
        joining_year = adminDB.Column(adminDB.Date(), nullable = False)
        graduated_date = adminDB.Column(adminDB.Date())
        created_at = adminDB.Column(adminDB.DateTime(), default = datetime.utcnow)
        updated_at = adminDB.Column(adminDB.DateTime(), onupdate = datetime.utcnow)
 
class UniversityDegree(adminDB.Model):
      __bind_key__ = 'students_mysql'
      __tablename__ = 'university_degree'
      id = adminDB.Column(adminDB.Integer, primary_key = True)
      name  = adminDB.Column(adminDB.String(40), nullable = False)
      description = adminDB.Column(adminDB.String(200), nullable = False)
      duration = adminDB.Column(adminDB.Integer, nullable = False)
      is_single = adminDB.Column(adminDB.Boolean(), default = True)
      created_at = adminDB.Column(adminDB.DateTime(), default = datetime.utcnow)
      updated_at = adminDB.Column(adminDB.DateTime(), onupdate = datetime.utcnow)
      
      students = adminDB.relationship('Student',backref = 'degree_id',lazy = True)
      dept_degree_mappings = adminDB.relationship('DepartmentDegreeMapping',backref = 'degree_id', lazy = True)   
           

class  Department(adminDB.Model):
          __bind_key__ = 'students_mysql'
          __tablename__ = 'department'
          id = adminDB.Column(adminDB.Integer, primary_key = True)
          name  = adminDB.Column(adminDB.String(60), nullable = False)
          description = adminDB.Column(adminDB.String(200), nullable = False)
          hod = adminDB.Column(adminDB.String(40), nullable = False)
          email = adminDB.Column(adminDB.String(40), nullable = False)
          phone = adminDB.Column(adminDB.String(200), nullable = False)
          created_at = adminDB.Column(adminDB.DateTime(), default = datetime.utcnow)
          updated_at = adminDB.Column(adminDB.DateTime(), onupdate = datetime.utcnow)
          
          dept_degree_mappings = adminDB.relationship('DepartmentDegreeMapping',backref = 'dept_id', lazy = True)   

class DepartmentDegreeMapping(adminDB.Model):
          __bind_key__ = 'students_mysql'
          __tablename__ = 'dept_degree_mapping'
          id = adminDB.Column(adminDB.Integer, primary_key = True)
          dept_id = adminDB.Column(adminDB.Integer,adminDB.ForeignKey('department.id'), nullable = False)
          degree_id = adminDB.Column(adminDB.Integer,adminDB.ForeignKey('university_degree.id'), nullable = False)
          created_at = adminDB.Column(adminDB.DateTime(), default = datetime.utcnow)
          updated_at = adminDB.Column(adminDB.DateTime(), onupdate = datetime.utcnow)
          is_active =  adminDB.Column(adminDB.Boolean(), default = True)
          
