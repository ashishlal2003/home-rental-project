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