-- this script create tables require for pynard

CREATE TABLE productor(
	productor_id serial primary key
	,productor_name VARCHAR(50)
	,productor_adress VARCHAR(140)
);
CREATE TABLE bottle(
	bottle_id serial primary key
	,bottle_label VARCHAR(140)
	,bottle_creation_year VARCHAR(4)
	,bottle_consomation_limit_date DATE
	,bottle_quantity INTEGER
	,fk_productor_id INT REFERENCES productor(productor_id)

);

