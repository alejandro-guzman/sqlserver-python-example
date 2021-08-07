-- create database
IF NOT EXISTS(SELECT * FROM sys.databases WHERE name = 'demo1')
BEGIN
    CREATE DATABASE demo1
END
GO

USE demo1
GO

-- create table
IF NOT EXISTS(SELECT * FROM sysobjects WHERE name = 'users' AND xtype = 'U')
BEGIN
    CREATE TABLE users (
        id          INT             NOT NULL IDENTITY(100,100) PRIMARY KEY,
        first_name  VARCHAR(64)     NOT NULL,
        last_name   VARCHAR(64)     NOT NULL,
        created_dt  DATETIME        NOT NULL DEFAULT GETDATE(),
        updated_dt  DATETIME,
        deleted_dt  DATETIME        -- soft deletes
    );
END
GO

-- create trigger for updates
CREATE OR ALTER TRIGGER set_updated_dt ON users FOR UPDATE AS
BEGIN
    UPDATE users
    SET updated_dt = GETDATE()
    FROM users u JOIN inserted i ON u.id = i.id 
END
GO

ALTER TABLE users ENABLE TRIGGER set_updated_dt
GO

-- test data
INSERT INTO users (first_name, last_name) VALUES
('James',       'Lopez'),
('John',        'Reyes'),
('Robert',      'Miller'),
('Barbara',     'Anderson'),
('Elizabeth',   'Taylor'),
('Jennifer',    'Cruz');
GO