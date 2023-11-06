use ub_skincare;

SELECT * FROM ub_skincare.master_recomm;

SET SQL_SAFE_UPDATES = 0;
UPDATE master_recomm SET skin_type = LOWER(skin_type);
UPDATE master_recomm SET location = LOWER(location);