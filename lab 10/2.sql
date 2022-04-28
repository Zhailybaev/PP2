create database snake;

create role adia with password 'passw0rd' LOGIN;

-- alter role pp2demo_user LOGIN;

grant all privileges on database snake to adia;

-- Creating the table
create table user_score
(
    name  varchar(255) not null,
    level    int,
    score int
);


insert into user_score (name, level, score)
values ('qwe',1,1),
	   ('rty',2,4),
	   ('uiop',2,5),
	   ('asd',3,7),
	   ('dfg',4,10),
	   ('hjk',3,8);