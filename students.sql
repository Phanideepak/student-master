create database students;

use students;

create table students.university_degree(
  id int not null auto_increment,
  name varchar(40) not null,
  description varchar(200) not null,
  duration int not null,
  is_single tinyint(1) not null default '1',
  created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  primary key(id)
);

create table students.department(
    id int not null auto_increment,
    name varchar(60) not null,
    description varchar(200) not null,
    hod varchar(40) not null,
    email varchar(40) not null,
    phone varchar(20) not null,
    created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    primary key(id)
);

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


create table students.student(
   id int not null auto_increment,
   student_id varchar(40) not null,
   first_name varchar(40) not null,
   last_name varchar(40) not null,
   email varchar(40) not null,
   degree_id int not null,
   joining_year date not null,
   graduated_date date,
   created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
   updated_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
   primary key (id),
   foreign key (degree_id) references students.university_degree(id)
);
