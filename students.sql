create database students;

use students;

create table students.university_degree(
  id int not null auto_increment,
  name varchar(40) not null unique,
  description varchar(200) not null unique,
  duration int not null,
  is_single tinyint(1) not null default '1',
  created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  primary key(id)
);

alter table students.university_degree modify name varchar(40) not null unique; 
alter table students.university_degree modify description varchar(200) not null unique;

create table students.department(
    id int not null auto_increment,
    name varchar(60) not null unique,
    description varchar(200) not null unique,
    hod varchar(40) not null,
    email varchar(40) not null unique,
    phone varchar(20) not null,
    created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    primary key(id)
);

alter table students.department modify name varchar(60) not null unique;
alter table students.department modify description varchar(200) not null unique;
alter table students.department modify email varchar(40) not null unique;

create table students.dept_degree_mapping(
   id int not null auto_increment,
   dept_id int not null,
   degree_id int not null,
   created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
   updated_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
   is_active tinyint(1) not null default '1',
   primary key(id),
   foreign key (dept_id) references students.department(id),
   foreign key (degree_id) references students.university_degree(id)
);

alter table students.dept_degree_mapping add constraint UC_DEPT_DEGREE unique(dept_id,degree_id); 


create table students.student(
   id int not null auto_increment,
   student_id varchar(40) not null unique,
   first_name varchar(40) not null,
   last_name varchar(40) not null,
   email varchar(40) not null unique,
   degree_id int not null,
   joining_date date not null,
   graduated_date date,
   created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
   updated_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
   primary key (id),
   foreign key (degree_id) references students.university_degree(id)
);

alter table students.student modify column  email varchar(40) not null unique;

alter table students.student modify column student_id varchar(40) not null unique;