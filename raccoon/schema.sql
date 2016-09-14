CREATE TABLE IF NOT EXISTS students (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name STRING,
  last_name STRING,
  phone_number STRING,
  email STRING
);
    
CREATE TABLE IF NOT EXISTS instructors (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name STRING,
  last_name STRING,
  email STRING,
  rank STRING,
  admin BOOLEAN
);
    
CREATE TABLE IF NOT EXISTS dean (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  full_name STRING,
  contact_information STRING
);
    