-- ********************************************************
--
-- Author : Pierre BOURGAIN
-- Purpose : create tables into pynard postgres database
--
-- ********************************************************

-- Clean dabase
DROP TABLE IF EXISTS stock CASCADE;
DROP TABLE IF EXISTS bottle CASCADE;
DROP TABLE IF EXISTS ref_meta_type;
DROP TABLE IF EXISTS ref_bottle_type CASCADE;
DROP TABLE IF EXISTS productor CASCADE;
DROP TABLE IF EXISTS cave CASCADE;
DROP TABLE IF EXISTS ref_location CASCADE;

-- Productor table : one productor per raw
CREATE TABLE productor(
	productor_id SERIAL PRIMARY KEY
	,productor_name VARCHAR(50)
	,productor_address VARCHAR(50)
	,productor_phone VARCHAR(16)
	,productor_mail VARCHAR(50)
	,productor_picture_path VARCHAR(140)
	,productor_creation_date DATE
	,productor_delete_date DATE

);

-- bottle type : ref the type of bottle like wine, whisky etc....
CREATE TABLE ref_bottle_type(
	type_id SERIAL PRIMARY KEY
	,type_name VARCHAR(20)
	,language VARCHAR(3)
	,type_creation_date DATE
);

-- meta type : add details on a type
CREATE TABLE ref_meta_type(
	meta_type_id SERIAL PRIMARY KEY
	,ref_type_id INT REFERENCES ref_bottle_type(type_id)
	,familly VARCHAR(40) -- Beaujolais, Bordeaux, Irlandais, Ecossais ...
	,composition VARCHAR(50) -- grape chardonnais, single malte etc ...
	,meta_type_creation_date DATE
);

-- This table contain a reference for one type of bottle
CREATE TABLE bottle(
	bottle_id SERIAL PRIMARY KEY
	,fk_bottle_type INT REFERENCES ref_bottle_type(type_id)
	,fk_bottle_meta_type INT REFERENCES ref_meta_type(meta_type_id)
	,bottle_name VARCHAR(140)
	,bottle_size DECIMAL(10,6)
	,bottle_production_year VARCHAR(4)
	,bottle_expiration_date VARCHAR(4)
	,bottle_picture_path VARCHAR(140)
	,bottle_creation_date DATE
);

-- cave ref for a user
CREATE TABLE cave(
	cave_id SERIAL PRIMARY KEY
	,cave_name VARCHAR(30)
	,cave_picture_path VARCHAR(140)
	,cave_creation_date DATE
	,cave_last_update DATE
	,cave_delete_date DATE
	
);

CREATE TABLE ref_location(
	location_id SERIAL PRIMARY KEY
	,location_name VARCHAR(50)
);

CREATE TABLE stock(
	fk_cave_id INT REFERENCES cave(cave_id)
	,fk_bottle_id INT REFERENCES bottle(bottle_id)
	,stock_location INT REFERENCES ref_location(location_id)
	,quantity INT
);
