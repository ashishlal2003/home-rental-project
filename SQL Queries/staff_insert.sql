use home_rental;

INSERT INTO staff VALUES
('SG1', 'John Doe', 'M', '1985-01-01', 'Manager', 50000.00, 'B001', '123 Main St, London', 1234567890, NULL, '2022-01-01', 2500.00),
('SG2', 'Jane Smith', 'F', '1990-05-12', 'Supervisor', 35000.00, 'B001', '123 Main St, London', 1234567890, 'John Doe', '2022-01-01', 1500.00),
('SG3', 'Mark Johnson', 'M', '1988-11-15', 'Assistant', 25000.00, 'B001', '123 Main St, London', 1234567890, 'Jane Smith', NULL, NULL),
('SG4', 'Emily Brown', 'F', '1995-04-21', 'Assistant', 25000.00, 'B001', '123 Main St, London', 1234567890, 'Jane Smith', NULL, NULL),
('SG5', 'Susan Brand', 'F', '1940-06-03', 'Manager', 24000.00, 'B003', '163 Main St, Glasgow', 1413392178, NULL, '1990-06-01', 2350.00),
('SG6', 'David Lee', 'M', '1991-09-27', 'Supervisor', 30000.00, 'B003', '163 Main St, Glasgow', 1413392178, 'Susan Brand', '2022-01-01', 1000.00),
('SG7', 'Karen Taylor', 'F', '1994-12-30', 'Assistant', 20000.00, 'B003', '163 Main St, Glasgow', 1413392178, 'David Lee', NULL, NULL),
('SG8', 'Peter Davis', 'M', '1996-07-14', 'Assistant', 20000.00, 'B003', '163 Main St, Glasgow', 1413392178, 'David Lee', NULL, NULL),
('SG9', 'William Adams', 'M', '1993-03-08', 'Supervisor', 32000.00, 'B002', '456 High St, Manchester', 1612345678, 'Michael Brown', '2022-01-01', 1200.00),
('SG10', 'Sarah Miller', 'F', '1997-02-18', 'Assistant', 21000.00, 'B002', '456 High St, Manchester', 1612345678, 'William Adams', NULL, NULL);

select * from staff;

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
('EL21', 'Flat', 2, 350, '7 Elm St., Elgin, IV30 1NY', 'B129', 'Adam Brown', '

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

 
INSERT INTO branch_office (branch_number, branch_address, telephone_number) VALUES
('B003', '163 Main St, Glasgow', 01412257025),
('B005', '10 Princes St, Edinburgh', 01314788585),
('B012', '21 Union St, Aberdeen', 01224632683),
('B019', '12 High St, Inverness', 01463235477),
('B025', '22 Castle St, Stirling', 01786476546),
('B034', '5 King St, Perth', 01738476835),
('B041', '8 Regent St, Dundee', 01382678934),
('B048', '29 Hope St, Glasgow', 01412054065),
('B055', '16 Hanover St, Edinburgh', 01316687692),
('B063', '7 Albyn Pl, Aberdeen', 01224367587);

