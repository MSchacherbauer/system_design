CREATE TABLE user
(
    id       INT          not null AUTO_INCREMENT PRIMARY KEY,
    email    VARCHAR(255) NOT NULL,
    password VARCHAR(255) not null
);

insert into user (email, password)
values ('maxi.schacherbauer@gmail.com', 'Admin123');