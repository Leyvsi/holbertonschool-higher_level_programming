# SQL - Introduction

This project is an introduction to **SQL (Structured Query Language)** and **MySQL 8.0**. The goal is to understand how to manage relational databases, create tables, and manipulate data using DDL (Data Definition Language) and DML (Data Manipulation Language).

## Learning Objectives

By the end of this project, I will be able to explain:
* What a relational database is.
* What SQL stands for and its basic syntax.
* How to create, modify, and delete databases and tables.
* How to perform CRUD operations (Create, Read, Update, Delete).
* The difference between DDL and DML.

## Requirements

* **Environment:** Ubuntu 22.04 LTS
* **Database Version:** MySQL 8.0 (8.0.25)
* **Style:** * All SQL keywords are in **UPPERCASE**.
    * Every script starts with a comment describing the task.
    * Every query is preceded by a short comment.
    * Files end with a new line.

## Tasks

| File | Description |
| --- | --- |
| `0-list_databases.sql` | Lists all databases of the MySQL server. |

## Usage

To execute the scripts, use the following command structure:

```bash
cat <file_name>.sql | mysql -hlocalhost -uroot -p
