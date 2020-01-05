create database carelydb;
use carelydb;
create table Caretaker(
    id varchar(50) NOT NULL,
    fname varchar(30) NOT NULL,
    lname varchar(30) NOT NULL,
    mname varchar(30) DEFAULT NULL,
    mobno varchar(20) NOT NULL,
    dob varchar(16) NOT NULL,
    address varchar(100) NOT NULL,
    bg varchar(5) NOT NULL,
    picpath varchar(20) DEFAULT NULL,
    reviewed boolean DEFAULT False,
    flagged boolean DEFAULT False,
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
    reviewed boolean DEFAULT False,
    flagged boolean DEFAULT False,
    health_condition varchar(100) NOT NULL,
    strikes integer DEFAULT 0,
    no_of_caretaker integer DEFAULT 0,
    specail_remarks varchar(100) DEFAULT "",
    delayflag boolean DEFAULT True,
    PRIMARY KEY(id)
);

create table BookingRecord(
    ct_id varchar(50) NOT NULL,
    el_id varchar(50) NOT NULL,
    reg_datetime varchar(25),
    no_of_hours integer DEFAULT 1
);

create table PendingBooking(
    per_id varchar(50) NOT NULL,
    req_id varchar(50) NOT NULL,
    reg_datetime varchar(25),
    no_of_hours integer DEFAULT 1
);

create table VerificationProof(
    ver_flag boolean DEFAULT False,
    id_type varchar(20) DEFAULT "",
    id_no varchar(20) DEFAULT "",
    id_path varchar(20) DEFAULT "",
    carely_id varchar(50) NOT NULL
);

create table ReviewInfo(
    id varchar(20) NOT NULL,
    review varchar(40) DEFAULT "",
    rating integer DEFAULT 0
);