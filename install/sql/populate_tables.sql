-- *************************************************************************
--
-- Author : Pierre BOURGAIN
-- Purpose : first poplation of the database
--
-- *************************************************************************

-- clean table 
DELETE FROM ref_bottle_type;
DELETE FROM ref_meta_type;

-- first populate of bottle type // french ref
INSERT INTO ref_bottle_type(type_name, type_creation_date) VALUES('Ruhm',TODAY());
INSERT INTO ref_bottle_type(type_name, type_creation_date) VALUES('Vin',,TODAY());
INSERT INTO ref_bottle_type(type_name, type_creation_date) VALUES('Whisky',TODAY());
INSERT INTO ref_bottle_type(type_name, type_creation_date) VALUES('Gin',TODAY());
INSERT INTO ref_bottle_type(type_name, type_creation_date) VALUES('Biére',TODAY());
INSERT INTO ref_bottle_type(type_name, type_creation_date) VALUES('Cocktail',TODAY());
INSERT INTO ref_bottle_type(type_name, type_creation_date) VALUES('Soft',TODAY());
INSERT INTO ref_bottle_type(type_name, type_creation_date) VALUES('Troussepinette',TODAY());
INSERT INTO ref_bottle_type(type_name, type_creation_date) VALUES('Calva',TODAY());
INSERT INTO ref_bottle_type(type_name, type_creation_date) VALUES('Génépi',TODAY());
INSERT INTO ref_bottle_type(type_name, type_creation_date) VALUES('Chartreuse',TODAY());
INSERT INTO ref_bottle_type(type_name, type_creation_date) VALUES('Vodka',TODAY());
INSERT INTO ref_bottle_type(type_name, type_creation_date) VALUES('Anisette',TODAY());
INSERT INTO ref_bottle_type(type_name, type_creation_date) VALUES('Get',TODAY());
INSERT INTO ref_bottle_type(type_name, type_creation_date) VALUES('Amer',TODAY());
INSERT INTO ref_bottle_type(type_name, type_creation_date) VALUES('Liqueur',TODAY());

-- First populate meta type // french
INSERT INTO ref_meta_type(familly, composition, ref_type_id, meta_type_creation_date) VALUES('Blanc', 'Canne à sucre',(SELECT type_id FROM ref_bottle_type WHERE type_name = 'Ruhm'),TODAY());
INSERT INTO ref_meta_type(familly, composition, ref_type_id, meta_type_creation_date) VALUES('Ambré', 'Canne à sucre',(SELECT type_id FROM ref_bottle_type WHERE type_name = 'Ruhm'),TODAY());
INSERT INTO ref_meta_type(familly, composition, ref_type_id, meta_type_creation_date) VALUES('Beaujolais', 'Gamay',(SELECT type_id FROM ref_bottle_type WHERE type_name = 'Vin'),TODAY());
INSERT INTO ref_meta_type(familly, composition, ref_type_id, meta_type_creation_date) VALUES('Bourgogne', 'Pinot noir',(SELECT type_id FROM ref_bottle_type WHERE type_name = 'Vin'),TODAY());
INSERT INTO ref_meta_type(familly, composition, ref_type_id, meta_type_creation_date) VALUES('Mâconnais', 'Chardonnay',(SELECT type_id FROM ref_bottle_type WHERE type_name = 'Vin'),TODAY());
INSERT INTO ref_meta_type(familly, composition, ref_type_id, meta_type_creation_date) VALUES('Bordeaux', 'Merlot',(SELECT type_id FROM ref_bottle_type WHERE type_name = 'Vin'),TODAY());
INSERT INTO ref_meta_type(familly, composition, ref_type_id, meta_type_creation_date) VALUES('Bordeaux', 'Cabernet Franc',(SELECT type_id FROM ref_bottle_type WHERE type_name = 'Vin'),TODAY());
