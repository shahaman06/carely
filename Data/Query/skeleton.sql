create database carelydb;
use carelydb;
create table Caretaker(
    id varchar(50) NOT NULL,
    fname varchar(30) NOT NULL,
    lname varchar(30) NOT NULL,
    mname varchar(30) DEFAULT "",
    mobno varchar(20) NOT NULL,
    dob varchar(16) NOT NULL,
    address varchar(100) NOT NULL,
    bg varchar(5) NOT NULL,
    picpath varchar(20) DEFAULT NULL,
    reviewed varchar(5) DEFAULT "False",
    flagged varchar(5) DEFAULT "False",
    verified varchar(5) DEFAULT "False",
    strikes integer DEFAULT 0,
    speciality varchar(50),
    PRIMARY KEY(id)
);

create table Elderly(
    id varchar(50) NOT NULL,
    fname varchar(30) NOT NULL,
    lname varchar(30) NOT NULL,
    mname varchar(30) DEFAULT "",
    mobno varchar(20) NOT NULL,
    dob varchar(16) NOT NULL,
    address varchar(100) NOT NULL,
    bg varchar(5) NOT NULL,
    picpath varchar(20) DEFAULT NULL,
    reviewed varchar(5) DEFAULT "False",
    flagged varchar(5) DEFAULT "False",
    verified varchar(5) DEFAULT "False",
    health_condition varchar(100) NOT NULL,
    strikes integer DEFAULT 0,
    no_of_caretaker integer DEFAULT 0,
    specail_remarks varchar(100) DEFAULT "",
    delayflag varchar(5) DEFAULT "True",
    PRIMARY KEY(id)
);

create table BookingRecord(
    ct_id varchar(50) NOT NULL,
    el_id varchar(50) NOT NULL,
    book_date varchar(16),
    book_time varchar(10),
    no_of_hours integer DEFAULT 0
);

create table PendingBooking(
    per_id varchar(50) NOT NULL,
    req_id varchar(50) NOT NULL,
    book_date varchar(16),
    book_time varchar(10),
    no_of_hours integer DEFAULT 0,
    confirmation varchar(10) DEFAULT "Pending"
);

create table VerificationProof(
    carely_id varchar(50) NOT NULL,
    ver_flag varchar(5) DEFAULT "False",
    under_ver varchar(5) DEFAULT "False",
    id_type varchar(20) DEFAULT "",
    id_no varchar(20) DEFAULT "",
    id_path varchar(20) DEFAULT "",
    PRIMARY KEY(carely_id)
);

create table ReviewInfo(
    id varchar(20) NOT NULL,
    review varchar(40) DEFAULT "",
    rating integer DEFAULT 0
);