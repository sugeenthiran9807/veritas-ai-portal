-- ====================================================================
-- EXNO-6B: Three-Tier Web Application Database Script
-- AI Content Verification System - Student Examination Registry
-- Database Name: AIContentVerification
-- ====================================================================

-- Create Database
CREATE DATABASE AIContentVerification;
GO

USE AIContentVerification;
GO

-- Create Table
CREATE TABLE student_exam (
    regno INT PRIMARY KEY,
    studentname VARCHAR(50) NOT NULL,
    exam VARCHAR(100) NOT NULL,
    score VARCHAR(10) NOT NULL,
    result VARCHAR(20) NOT NULL
);
GO

-- Insert Initial Seed Records from Lab Manual
INSERT INTO student_exam (regno, studentname, exam, score, result) VALUES
(9947, 'M. MOHAMED ZAID', 'AI Content Verification Examination', '5 / 5', 'PASS'),
(9948, 'ROOH', 'AI Content Verification Examination', '5 / 5', 'PASS'),
(9949, 'NOOR', 'AI Content Verification Examination', '4 / 5', 'PASS'),
(9950, 'AIRA', 'AI Content Verification Examination', '3 / 5', 'PASS'),
(9951, 'MEER', 'AI Content Verification Examination', '5 / 5', 'PASS'),
(9952, 'AYAN', 'AI Content Verification Examination', '2 / 5', 'FAIL'),
(9807, 'SUGEENTHIRAN', 'AI Content Verification Examination', '5 / 5', 'PASS');
GO

-- Sample Verification Queries
SELECT * FROM student_exam;
SELECT * FROM student_exam WHERE regno = 9807;
