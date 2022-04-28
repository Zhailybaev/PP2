create database Phonebook;

create role Dia with password 'passw0rd' LOGIN;



grant all privileges on database Phonebook to Phonebook;

-- Creating the table
create table phone
(
    id    int,
    name  varchar(255) not null,
    number   numeric      not null
);


update phone
set name='dfg'
where number=123

update phone
set number=81
where name='wer'

