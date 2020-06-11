CREATE DATABASE CRAWLER;
CREATE TABLE zl
(
  id           INT AUTO_INCREMENT
    PRIMARY KEY,
  j_name       VARCHAR(100) NULL,
  c_name       VARCHAR(100) NULL,
  c_nature     VARCHAR(30)  NULL,
  c_scale      VARCHAR(30)  NULL,
  description  TEXT         NULL,
  w_place      VARCHAR(100) NULL,
  w_field      VARCHAR(100) NULL,
  w_experience VARCHAR(30)  NULL,
  education    VARCHAR(30)  NULL,
  s_min        VARCHAR(30)  NULL,
  s_max        VARCHAR(30)  NULL,
  t_publish    VARCHAR(100) NULL,
  vacancies    VARCHAR(30)  NULL,
  welfare      TEXT         NULL,
  url          VARCHAR(100) NULL
)
  ENGINE = InnoDB
  CHARSET = utf8;