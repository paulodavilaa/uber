-- CREATE TABLE empleado (id INTEGER NOT NULL PRIMARY KEY, nombre TEXT NOT NULL, correo NOT NULL);
-- INSERT INTO empleado VALUES(1, "Juan", "correo1@miempresa.com");
INSERT INTO empleado VALUES(2, "Pedro", "correo2@miempresa.com");
-- INSERT INTO empleado VALUES(3, "Rosa", "correo3@miempresa.com");

-- SELECT * FROM empleado

-- DELETE FROM empleado WHERE id=2;
SELECT * FROM empleado
-- UPDATE empleado SET nombre='Francisco' WHERE id=1;