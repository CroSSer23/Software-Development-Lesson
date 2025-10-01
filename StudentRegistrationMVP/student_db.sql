-- ============================================================
-- Student Registration System - Database Backup
-- Generated: 2025-10-01 12:50:32
-- ============================================================

-- Create database
CREATE DATABASE IF NOT EXISTS student_db;
USE student_db;

-- Table structure for users
DROP TABLE IF EXISTS users;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(64) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Data for table users
INSERT INTO users (id, username, password) VALUES
(1, 'testuser1', 'ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f');
