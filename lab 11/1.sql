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

--1.Function that returns all records based on a pattern (example of pattern: part of name, surname, phone number)
CREATE OR REPLACE FUNCTION filter(nam  varchar(255) )
  RETURNS TABLE(name  varchar(255), number   numeric) AS $$
BEGIN
 RETURN QUERY
 SELECT PHONE.NAME, PHONE.NUMBER FROM phone where phone.name LIKE 'st%';
END;
$$ LANGUAGE plpgsql;

--2.Create procedure to insert new user by name and phone, update phone if user already exists
CREATE OR REPLACE PROCEDURE insert_user(
	id int,
  name varchar(255),
	number numeric
) 
AS $$
--DECLARE
--	name varchar(255);
--	number numeric;
BEGIN
  
IF EXISTS(SELECT id FROM phone WHERE phone.name = $2) THEN
  update phone
    set number = $3
    where phone.name = $2;
ELSE
  INSERT INTO phone(id,name,number) 
    VALUES($1,$2,$3);
     
END IF;


END
$$
LANGUAGE PLPGSQL;


--5.Implement procedure to deleting data from tables by username or phone
CREATE OR REPLACE PROCEDURE delete_user(
  name varchar(255),
) 
AS $$

BEGIN

  delete
  from phone
  where phone.name = $1;


END
$$
LANGUAGE PLPGSQL;


--4.Create function to querying data from the tables with pagination (by limit and offset)
CREATE OR REPLACE FUNCTION qwe( )
  RETURNS TABLE(id int,  name  varchar(255), number   numeric) AS $$
BEGIN
 RETURN QUERY
 SELECT * FROM phone
  ORDER BY phone.id
  LIMIT 4 OFFSET 4;
END;
$$ LANGUAGE plpgsql;



--3.Create procedure to insert many new users by list of name and phone. Use loop and if statement in stored procedure. Check correctness of phone in procedure and return all incorrect data.
CREATE OR REPLACE FUNCTION list() RETURNS SETOF exbook AS 
$$
DECLARE
  r exbook%rowtype;
BEGIN
FOR r IN
  SELECT * FROM exbook
LOOP
  IF not((r.name LIKE 'f%') or (r.name LIKE 'w%')) THEN
    RETURN NEXT r;
    DELETE FROM exbook where (r.name=exbook.name) and (r.number=exbook.name);

  ELSE
    INSERT INTO phone(id,name,number) 
  	VALUES (r.id,r.name,r.number);
  END IF;
END LOOP;

END
$$ 
LANGUAGE plpgsql;