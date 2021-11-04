INSERT INTO `dojos_and_ninjas_schema`.`DOJOS` (`id`, `first_name`, `last_name`) VALUES ('3', 'Jeremy', 'Wong');
DELETE FROM `dojos_and_ninjas_schema`.`DOJOS` WHERE id in ('1','2','3');
SELECT * FROM DOJOS;
INSERT INTO `dojos_and_ninjas_schema`.`NINJAS` (`id`, `first_name`, `last_name`, `age`, `dojo_id`) VALUES ('9', 'Pablo', 'Pagillin', '24', '3');
SELECT * FROM NINJAS;

SELECT 
	NINJAS.first_name, 
    NINJAS.last_name, 
    NINJAS.age 
FROM NINJAS
JOIN DOJOS ON NINJAS.dojo_id = DOJOS.id
WHERE DOJOS.id = 1;

SELECT 
	NINJAS.first_name, 
    NINJAS.last_name, 
    NINJAS.age 
FROM NINJAS
JOIN DOJOS ON NINJAS.dojo_id = DOJOS.id
WHERE DOJOS.id = 3;

SELECT 
	DOJOs.first_name, 
	DOJOS.last_name 
FROM DOJOS
JOIN NINJAS ON DOJOS.id = NINJAS.dojo_id
WHERE NINJAS.id = 6;

SELECT 
	DOJOs.first_name, 
	DOJOS.last_name 
FROM NINJAS
JOIN DOJOS ON NINJAS.dojo_id = DOJOS.id
WHERE DOJOS.id = 3;
