show databases;
use projectdb;
show tables;

CREATE TABLE PersonalInfo(
    Sname varchar(25),
    DOB varchar(20),
	ID varchar(15),
    Email varchar(40),
    Phone varchar(10),
    BG char(5),
    Height int,
    Weight int,
    District varchar(25)
);
CREATE TABLE Parent_Details(
	FatherName varchar(30),
    FatherPhn_No varchar(15),
    MotherName varchar(15),
    MotherPhn_No varchar(30),
    District varchar(40)
    );
CREATE TABLE Educational_Details(
	Id varchar(30),
	CollegeName varchar(50),
    CollegeCode int,
    Degree varchar(10),
    Department varchar(10),
    Year varchar(5),
    RegisterNo int,
    RollNo int,
    Year_Of_Passing int,
    Batch varchar(20),
    Admission_Type varchar(30),
    Counsling_No varchar(20)
    );
CREATE TABLE Address_Details(
	Id varchar(30),
	Cur_DoorNo varchar(10),
    Cur_Street varchar(50),
    cur_District varchar(30),
    Cur_Post varchar(25),
    Cur_Pin_Code varchar(10),
    Cur_State varchar(30),
    Per_DoorNo varchar(10),
    Per_Street varchar(50),
    per_District varchar(30),
    Per_Post varchar(25),
    Per_Pin_Code varchar(10),
    Per_State varchar(30),
    Contact_No varchar(10)
);

DELETE FROM PersonalInfo;
DELETE FROM Parent_Details;
DELETE FROM Educational_Details;
DELETE FROM Address_Details;

select * from PersonalInfo;
select * from Parent_Details;
select * from Educational_Details;   
select * from Address_Details;

drop table PersonalInfo;
drop table Parent_Details;
drop table Educational_details;
drop table Address_Details;
