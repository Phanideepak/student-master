from ... import adminDB
from datetime import datetime

class Student(adminDB.Model):
        __bind_key__ = 'students_mysql'
        __tablename__ = 'student'       
        id = adminDB.Column(adminDB.Integer, primary_key = True)
        student_id = adminDB.Column(adminDB.String(40), nullable = False, unique=True)
        first_name  = adminDB.Column(adminDB.String(40), nullable = False)
        last_name = adminDB.Column(adminDB.String(40), nullable = False)
        email = adminDB.Column(adminDB.String(40), nullable = False, unique=True)
        degree_id = adminDB.Column(adminDB.Integer,adminDB.ForeignKey('university_degree.id'), nullable = False)
        joining_year = adminDB.Column(adminDB.Date(), nullable = False)
        graduated_date = adminDB.Column(adminDB.Date())
        created_at = adminDB.Column(adminDB.DateTime(), default = datetime.utcnow)
        updated_at = adminDB.Column(adminDB.DateTime(), onupdate = datetime.utcnow,default = datetime.utcnow)
        
                  
        def save(self):
              adminDB.session.add(self)
              adminDB.session.commit()  
 
class UniversityDegree(adminDB.Model):
      __bind_key__ = 'students_mysql'
      __tablename__ = 'university_degree'
      id = adminDB.Column(adminDB.Integer, primary_key = True)
      name  = adminDB.Column(adminDB.String(40), nullable = False, unique=True)
      description = adminDB.Column(adminDB.String(200), nullable = False, unique=True)
      duration = adminDB.Column(adminDB.Integer, nullable = False)
      is_single = adminDB.Column(adminDB.Boolean(), default = True)
      created_at = adminDB.Column(adminDB.DateTime(), default = datetime.utcnow)
      updated_at = adminDB.Column(adminDB.DateTime(), onupdate = datetime.utcnow, default = datetime.utcnow)
      
      students = adminDB.relationship('Student', backref = 'university_degree',lazy = True)
      dept_degree_mappings = adminDB.relationship('DepartmentDegreeMapping',backref = 'university_degree', lazy = True)
      
      def save(self):
          adminDB.session.add(self)
          adminDB.session.commit()    
           

class  Department(adminDB.Model):
          __bind_key__ = 'students_mysql'
          __tablename__ = 'department'
          id = adminDB.Column(adminDB.Integer, primary_key = True)
          name  = adminDB.Column(adminDB.String(60), nullable = False, unique=True)
          description = adminDB.Column(adminDB.String(200), nullable = False, unique=True)
          hod = adminDB.Column(adminDB.String(40), nullable = False)
          email = adminDB.Column(adminDB.String(40), nullable = False, unique=True)
          phone = adminDB.Column(adminDB.String(200), nullable = False)
          created_at = adminDB.Column(adminDB.DateTime(), default = datetime.utcnow)
          updated_at = adminDB.Column(adminDB.DateTime(), onupdate = datetime.utcnow, default = datetime.utcnow)
          
          dept_degree_mappings = adminDB.relationship('DepartmentDegreeMapping',backref = 'department', lazy = True)
          
          def save(self):
              adminDB.session.add(self)
              adminDB.session.commit()    

class DepartmentDegreeMapping(adminDB.Model):
          __bind_key__ = 'students_mysql'
          __tablename__ = 'dept_degree_mapping'
          id = adminDB.Column(adminDB.Integer, primary_key = True)
          dept_id = adminDB.Column(adminDB.Integer,adminDB.ForeignKey('department.id'), nullable = False)
          degree_id = adminDB.Column(adminDB.Integer,adminDB.ForeignKey('university_degree.id'), nullable = False)
          created_at = adminDB.Column(adminDB.DateTime(), default = datetime.utcnow)
          updated_at = adminDB.Column(adminDB.DateTime(), onupdate = datetime.utcnow, default = datetime.utcnow)
          is_active =  adminDB.Column(adminDB.Boolean(), default = True)
          
          
          def save(self):
              adminDB.session.add(self)
              adminDB.session.commit()  