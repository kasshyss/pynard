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
INSERT INTO ref_bottle_type(type_name, type_creation_date) VALUES('Rhum',TODAY());
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
INSERT INTO ref_meta_type(familly, composition, ref_type_id, meta_type_creation_date) VALUES('Blanc', 'Canne à sucre',(SELECT type_id FROM ref_bottle_type WHERE type_name = 'Rhum'),TODAY());
INSERT INTO ref_meta_type(familly, composition, ref_type_id, meta_type_creation_date) VALUES('Ambré', 'Canne à sucre',(SELECT type_id FROM ref_bottle_type WHERE type_name = 'Rhum'),TODAY());
INSERT INTO ref_meta_type(familly, composition, ref_type_id, meta_type_creation_date) VALUES('Beaujolais', 'Gamay',(SELECT type_id FROM ref_bottle_type WHERE type_name = 'Vin'),TODAY());
INSERT INTO ref_meta_type(familly, composition, ref_type_id, meta_type_creation_date) VALUES('Bourgogne', 'Pinot noir',(SELECT type_id FROM ref_bottle_type WHERE type_name = 'Vin'),TODAY());
INSERT INTO ref_meta_type(familly, composition, ref_type_id, meta_type_creation_date) VALUES('Mâconnais', 'Chardonnay',(SELECT type_id FROM ref_bottle_type WHERE type_name = 'Vin'),TODAY());
INSERT INTO ref_meta_type(familly, composition, ref_type_id, meta_type_creation_date) VALUES('Bordeaux', 'Merlot',(SELECT type_id FROM ref_bottle_type WHERE type_name = 'Vin'),TODAY());
INSERT INTO ref_meta_type(familly, composition, ref_type_id, meta_type_creation_date) VALUES('Bordeaux', 'Cabernet Franc',(SELECT type_id FROM ref_bottle_type WHERE type_name = 'Vin'),TODAY());

-- populate cave
INSERT INTO cave(cave_name,creation_date,last_update) VALUES('Meriadoc''s cave', TODAY(), TODAY());
INSERT INTO cave(cave_name,creation_date,last_update, delete_date) VALUES('Old Meriadoc''s cave', TODAY(),TODAY(), TODAY());

-- Populate ref location
INSERT INTO ref_location(loacation_name) VALUES('Metzert');
INSERT INTO ref_location(loacation_name) VALUES('Saint-Etienne sur reyssouze');

-- Productor
INSERT INTO productor(productor_name, productor_address, productor_phone, productor_mail,productor_creation_date) VALUES('Cave de la Vigne Blanche', 'Route de la Vigne Blanche, 71260 Clessé, France', '+33385369388', 'No', TODAY());
INSERT INTO productor(productor_name, productor_address, productor_phone, productor_mail,productor_creation_date) VALUES('Comte Senard', '3 rue des Chaumes, 21420 Aloxe Corton, France', '+33380264073', 'office@domainesenard.com', TODAY());
INSERT INTO productor(productor_name, productor_creation_date) VALUES('Destilerias Unitas S.A.', TODAY());

-- Bottle
INSERT INTO bottle(bottle_name, bottle_size, creation_date,fk_bottle_type, fk_bottle_meta_type) VALUES('Diplomatico', 1.0, TODAY(), (SELECT type_id FROM ref_bottle_type WHERE type_name = 'Rhum'), (SELECT meta_type_id FROM ref_meta_type WHERE familly = 'Ambré'));
INSERT INTO bottle(bottle_name, bottle_size, creation_date,fk_bottle_type, fk_bottle_meta_type) VALUES('Aloxe Corton', 0.75, TODAY(), (SELECT type_id FROM ref_bottle_type WHERE type_name = 'Vin'), (SELECT meta_type_id FROM ref_meta_type WHERE familly = 'Bourgogne'));

-- Stock
INSERT INTO stock(quantity, unit_price, fk_cave_id, fk_bottle_id, fk_stock_location) VALUES (2, 40.32, (SELECT cave_id FROM cave WHERE cave_name = 'Meriadoc''s cave'), (SELECT bottle_id FROM bottle WHERE bottle_name = 'Aloxe Corton'), (SELECT location_id FROM ref_location WHERE location_name = 'Metzert'));

