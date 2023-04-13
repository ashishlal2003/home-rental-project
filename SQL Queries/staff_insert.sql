use home_rental;



INSERT INTO prop_registration (p_no, type, rooms, rent, address, own_no, name, per_address, tel_no, business_type, cont_no, staff_manage, branch) VALUES
('PG16', 'Flat', 4, 450, '5 Nover Drive, Glasglow, G12 9AX', 'C093', 'Tony Shaw', '12 Park PI, Glasgow G4 OQR', 01412257025, NULL, NULL, 'David Ford', '163 Main St., Glasgow'),
('KH39', 'House', 5, 700, '8 Fairview St., Edinburgh, EH11 4PB', 'D102', 'Mary Lee', '4 Queens Dr., Edinburgh EH6 5AE', 01315523431, 'Grocery Store', 07725124033, 'Karen Black', '57 Princes St., Edinburgh'),
('BD29', 'Flat', 3, 350, '32 Blythswood St., Dundee, DD1 3JX', 'B105', 'Peter Scott', '1 Victoria St., Dundee DD1 2PU', 01382614201, NULL, NULL, 'John Doe', '83 King St., Dundee'),
('LM09', 'Apartment', 2, 500, '11 Lawson St., Aberdeen, AB12 3RT', 'A128', 'Emma Green', '22 Westburn Rd., Aberdeen AB25 2QR', 01224583128, 'Cafe', 07578461329, 'Emily Jones', '23 Union St., Aberdeen'),
('CC13', 'Flat', 1, 300, '23 Cameron St., Inverness, IV1 1HG', 'B137', 'Jack White', '7 Hillhead Rd., Inverness IV2 4RY', 01463232134, NULL, NULL, 'Sarah Smith', '46 High St., Inverness'),
('AC27', 'House', 6, 800, '10 Arthur St., Stirling, FK8 1JW', 'D169', 'Benjamin Taylor', '34 Springkerse Rd., Stirling FK7 7SN', 01786432987, 'Pharmacy', 07743120548, 'George Lee', '3 Dumbarton Rd., Stirling'),
('BT35', 'Apartment', 2, 550, '9 Buchanan St., Paisley, PA1 2QT', 'A091', 'Oliver Clark', '6 Abbey Rd., Paisley PA2 6NB', 01418892220, NULL, NULL, 'Karen Black', '57 Princes St., Edinburgh'),
('SP56', 'Flat', 3, 400, '17 Springfield Rd., Perth, PH1 5RY', 'C123', 'Alex Turner', '20 Dunkeld Rd., Perth PH1 5RW', 01738637251, NULL, NULL, 'John Doe', '83 King St., Dundee'),
('AB45', 'House', 4, 650, '13 Abbey Rd., Ayr, KA7 2SZ', 'D173', 'Sophie Wilson', '11 Craigie Rd., Ayr KA8 0QJ', 01292483528, 'Supermarket', 07578461329, 'Emily Jones', '23 Union St., Aberdeen'),
('GL22', 'House', 4, 600, '23-25 Union St, Glasgow G1 3RB', 'U091', 'Ursula Smith', '27-29 Bath St, Glasgow G2 1HW', 01412861050, 'Marketing', 07385394658, 'Tom Baker', '46 Queen St, Glasgow');

 select * from prop_registration;
 
 INSERT INTO payment_details (monthly_rent, payment_method, deposit_paid, rent_start, rent_finish, duration) VALUES 
(500, 'Cash', 'N', '2022-04-01', '2022-09-30', '6 months'),
(600, 'Credit Card', 'Y', '2022-01-01', '2022-12-31', '1 year'),
(550, 'Cheque', 'Y', '2022-05-01', '2022-10-31', '6 months'),
(700, 'Bank Transfer', 'N', '2022-06-01', '2022-11-30', '6 months'),
(650, 'Cash', 'N', '2022-07-01', '2023-06-30', '1 year'),
(750, 'Credit Card', 'Y', '2022-03-01', '2022-08-31', '6 months'),
(800, 'Cheque', 'Y', '2022-10-01', '2023-09-30', '1 year'),
(850, 'Bank Transfer', 'N', '2022-09-01', '2023-02-28', '6 months'),
(900, 'Cash', 'N', '2022-11-01', '2023-10-31', '1 year'),
(950, 'Credit Card', 'Y', '2022-12-01', '2023-05-31', '6 months');

select * from payment_details;

 
INSERT INTO branch_office (branch_number, branch_address, telephone_number) VALUES 
('B001', '55 Princes St, Edinburgh EH2 2HL', '01312265876/01312267489'),
('B002', '34 Union St, Aberdeen AB11 5BN', '01224565543/01224561278'),
('B003', '163 Main St, Glasgow G11 9QX', '01413392178/01413394439'),
('B004', '23 High St, Inverness IV1 1JY', '01463278451/01463273691'),
('B005', '83 King St, Dundee DD1 2ER', '01382637246/01382638945'),
('B006', '5 Bridge St, Perth PH1 5LA', '01738674328/01738678901'),
('B007', '12 George St, Stirling FK8 2BJ', '01786431245/01786436589'),
('B008', '4 Queen St, Ayr KA7 1EH', '01292456897/01292451236'),
('B009', '15 Chapel St, Paisley PA1 1ER', '01418876123/01418871234'),
('B010', '27 Castle St, Elgin IV30 1BN', '01343567890/01343564321');


select * from branch_office;

INSERT INTO staff VALUES ('SG1', 'John Smith', 'M', '1985-05-20', 'Manager', 75000.00, 'B001', '123 Main St', '555-1234', 'Jane Doe', '2020-01-01', 5000.00);
INSERT INTO staff VALUES ('SG2', 'Jane Doe', 'F', '1990-08-15', 'Supervisor', 60000.00, 'B002', '456 Maple Ave', '555-5678', 'Jim Johnson', '2021-02-01', 3000.00);
INSERT INTO staff VALUES ('SG3', 'Robert Garcia', 'M', '1982-12-10', 'Assistant', 45000.00, 'B003', '789 Oak St', '555-9012', 'John Smith', '2022-01-01', NULL);
INSERT INTO staff VALUES ('SG4', 'Karen Lee', 'F', '1988-02-18', 'Manager', 80000.00, 'B004', '111 Elm St', '555-3456', 'Robert Garcia', '2020-07-01', 7000.00);
INSERT INTO staff VALUES ('SG5', 'David Kim', 'M', '1995-11-02', 'Supervisor', 55000.00, 'B005', '222 Pine St', '555-7890', 'Karen Lee', '2021-06-01', 2500.00);
INSERT INTO staff VALUES ('SG6', 'Samantha Brown', 'F', '1992-04-25', 'Assistant', 40000.00, 'B006', '333 Cedar Ave', '555-1234', 'David Kim', '2022-03-01', NULL);
INSERT INTO staff VALUES ('SG7', 'Andrew Lee', 'M', '1986-09-12', 'Manager', 85000.00, 'B007', '444 Birch St', '555-5678', 'Samantha Brown', '2020-01-01', 8000.00);
INSERT INTO staff VALUES ('SG8', 'Lisa Chen', 'F', '1993-06-22', 'Supervisor', 62000.00, 'B008', '555 Oak St', '555-9012', 'Andrew Lee', '2021-04-01', 3500.00);
INSERT INTO staff VALUES ('SG9', 'Michael Davis', 'M', '1989-03-07', 'Assistant', 47000.00, 'B009', '666 Maple Ave', '555-3456', 'Lisa Chen', '2022-01-01', NULL);
INSERT INTO staff VALUES ('SG10', 'Jessica Nguyen', 'F', '1996-12-31', 'Manager', 90000.00, 'B010', '777 Elm St', '555-7890', 'Michael Davis', '2020-10-01', 10000.00);

select * from staff;

