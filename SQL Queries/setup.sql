Create database home_rental;
Use home_rental;

create table staff(staff_number varchar(100),
full_name varchar(100),
sex char(1),
DOB date,
position varchar(100),
salary decimal(10,2),
branch_number varchar(100),
branch_address varchar(100),
telephone_number varchar(100),
supervisor_name varchar(100),
manager_start_date date,
manager_bonus decimal(10,2));

Alter table staff add primary key(staff_number);



-- CREATE INDEX idx_branch_number ON staff(branch_number);
CREATE INDEX idx_staff_name ON staff(full_name);


create table prop_registration(p_no varchar(100),
type varchar(100),
rooms int,
rent int,
address varchar(100),
own_no varchar(100),
name varchar(100),
per_address varchar(100),
tel_no varchar(15),
business_type varchar(100),
cont_no varchar(15),
staff_manage varchar(100),
branch varchar(100),
city varchar(100));

Alter table prop_registration add primary key (p_no);
Alter table prop_registration add foreign key (staff_manage) references staff(full_name);


create table branch_office(branch_number varchar(4),
branch_address varchar(100),
telephone_number varchar(100),
city varchar(100));

Alter table branch_office add primary key (branch_number);
Alter table staff add foreign key (branch_number) references branch_office(branch_number);


create table client_registration(client_no varchar(100),
name varchar(100),
type varchar(100),
max_rent int,
branch_no varchar(100),
branch varchar(100),
registered_by varchar(100),
date_registered date);

Alter table client_registration add primary key (client_no);

create table comments(client_no varchar(100),
name varchar(100),
date date,
comments varchar(100));

Alter table comments add primary key (client_no);
Alter table comments add foreign key (client_no) references client_registration( client_no);


create table lease_table(client_number varchar(100),
full_name varchar(100),
monthly_rent int,
payment_method varchar(100),
deposit_paid char(1),
property_number varchar(100),
property_address varchar(100),
rent_start date,
rent_finish date,
duration varchar(100)
);

Alter table lease_table add primary key (property_number);
Alter table lease_table add foreign key (client_number) references client_registration(client_no);
Alter table lease_table add foreign key (property_number) references prop_registration(p_no);
