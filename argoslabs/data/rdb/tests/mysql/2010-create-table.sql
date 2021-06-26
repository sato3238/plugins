-- create table

DROP TABLE IF EXISTS foo;

CREATE TABLE foo (
  id BIGINT NOT NULL AUTO_INCREMENT,
  name CHAR(30) NOT NULL,
  age INT NOT NULL,
  PRIMARY KEY (id)
);

ALTER DATABASE mytest CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
ALTER TABLE foo CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
