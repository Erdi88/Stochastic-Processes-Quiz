import streamlit as st
import random

st.set_page_config(page_title="Database Systems Quiz 2025", layout="centered")

# -----------------------------
# QUESTIONS (same as before)
# -----------------------------
questions = [
    # SQL / Relational
    {
        "question": "1️⃣ Find all students with nationality Norway, Sweden, or Denmark.",
        "choices": [
            "A. SELECT name, address FROM Student WHERE nationality IN ('Norway','Sweden','Denmark');",
            "B. SELECT * FROM Student WHERE nationality='Norway' OR nationality='Sweden';",
            "C. SELECT name FROM Student WHERE nationality='Denmark';"
        ],
        "answer": "A. SELECT name, address FROM Student WHERE nationality IN ('Norway','Sweden','Denmark');",
        "explanation": "IN allows checking multiple values at once. We want name and address of all Scandinavian students."
    },
    {
        "question": "2️⃣ Show students who have taken both INF2700 and INF3200.",
        "choices": [
            "A. SELECT ssn, name FROM Exam WHERE courseld='INF2700' AND courseld='INF3200';",
            "B. SELECT ssn, name FROM Student WHERE ssn IN (SELECT student\$sn FROM Exam WHERE courseld='INF2700') AND ssn IN (SELECT student\$sn FROM Exam WHERE courseld='INF3200');",
            "C. SELECT * FROM Student JOIN Exam ON ssn=student\$sn WHERE courseld='INF2700' OR courseld='INF3200';"
        ],
        "answer": "B. SELECT ssn, name FROM Student WHERE ssn IN (SELECT student\$sn FROM Exam WHERE courseld='INF2700') AND ssn IN (SELECT student\$sn FROM Exam WHERE courseld='INF3200');",
        "explanation": "We need students appearing in both subqueries, i.e., they took both courses."
    },
    {
        "question": "3️⃣ What is the main purpose of normalization?",
        "choices": [
            "A. Reduce redundancy and improve data integrity",
            "B. Make queries faster",
            "C. Allow multiple users to access data"
        ],
        "answer": "A. Reduce redundancy and improve data integrity",
        "explanation": "Normalization organizes data to minimize duplication and ensure consistency."
    },
    {
        "question": "4️⃣ Which of the following conditions is required for a relation to be in 3NF?",
        "choices": [
            "A. No transitive dependencies on non-prime attributes",
            "B. Only one primary key",
            "C. All attributes must be numeric"
        ],
        "answer": "A. No transitive dependencies on non-prime attributes",
        "explanation": "3NF requires that all non-key attributes depend only on the primary key and not on other non-key attributes."
    },
    {
        "question": "5️⃣ What is a weak entity in the ER model?",
        "choices": [
            "A. An entity that depends on another entity for existence",
            "B. An entity with few attributes",
            "C. An entity without a primary key"
        ],
        "answer": "A. An entity that depends on another entity for existence",
        "explanation": "Weak entities cannot exist without being linked to a strong entity."
    },
    {
        "question": "6️⃣ Which of the following is a hash-based organization for database files?",
        "choices": [
            "A. Files are stored sequentially by primary key",
            "B. A hash function maps a key value to a specific bucket",
            "C. B-trees are used for indexing"
        ],
        "answer": "B. A hash function maps a key value to a specific bucket",
        "explanation": "Hash-based organization uses a function to directly locate the record."
    },
    {
        "question": "7️⃣ What is the main difference between a hash file and an extensible hash file?",
        "choices": [
            "A. Extensible hash adjusts its directory dynamically, regular hash does not",
            "B. Hash files are faster than extensible hash files in all cases",
            "C. Hash files support only numeric keys"
        ],
        "answer": "A. Extensible hash adjusts its directory dynamically, regular hash does not",
        "explanation": "Extensible hashing allows the hash structure to grow dynamically to avoid collisions."
    },
    {
        "question": "8️⃣ What is an ACID transaction?",
        "choices": [
            "A. A transaction that is Atomic, Consistent, Isolated, and Durable",
            "B. A transaction that is Accelerated, Controlled, Indexed, and Distributed",
            "C. A transaction that only modifies one table"
        ],
        "answer": "A. A transaction that is Atomic, Consistent, Isolated, and Durable",
        "explanation": "ACID ensures database correctness and reliability for transactions."
    },
    {
        "question": "9️⃣ What is write-ahead logging (WAL)?",
        "choices": [
            "A. Logs are written after data is updated",
            "B. Logs are written before data is updated",
            "C. Logs are optional for recovery"
        ],
        "answer": "B. Logs are written before data is updated",
        "explanation": "WAL ensures recovery by writing changes to the log first, before applying to the database."
    },
    {
        "question": "🔟 Which operations are used on a transaction log?",
        "choices": [
            "A. Read, Write, Rollback, Commit",
            "B. Start, End, Delete, Update",
            "C. Add, Remove, Merge, Split"
        ],
        "answer": "A. Read, Write, Rollback, Commit",
        "explanation": "The transaction log records operations to allow recovery and rollback."
    },
    {
        "question": "1️⃣1️⃣ What is a functional dependency X → Y?",
        "choices": [
            "A. Y determines X",
            "B. X determines Y",
            "C. X and Y are independent"
        ],
        "answer": "B. X determines Y",
        "explanation": "A functional dependency X → Y means that if two tuples have the same X value, they must have the same Y value."
    },
    {
        "question": "1️⃣2️⃣ Is the relation R(A,B,C) with F={A→C, B→C} in BCNF?",
        "choices": [
            "A. Yes, because all dependencies have a superkey on the left",
            "B. No, because neither A nor B is a superkey",
            "C. Yes, because C is dependent on A or B"
        ],
        "answer": "B. No, because neither A nor B is a superkey",
        "explanation": "BCNF requires that every determinant is a superkey. Here, A and B are not superkeys."
    },
    {
        "question": "1️⃣3️⃣ Which is a primary performance overhead of a DBMS?",
        "choices": [
            "A. Disk I/O",
            "B. CPU speed",
            "C. RAM size"
        ],
        "answer": "A. Disk I/O",
        "explanation": "Database systems spend most time reading/writing data to disk, which dominates performance."
    },
    {
        "question": "1️⃣4️⃣ Two-phase locking (2PL) is used to:",
        "choices": [
            "A. Prevent deadlocks",
            "B. Ensure serializability",
            "C. Increase disk speed"
        ],
        "answer": "B. Ensure serializability",
        "explanation": "2PL ensures that transactions acquire and release locks in a way that guarantees serializable schedules."
    },
    {
        "question": "1️⃣5️⃣ In strict 2PL, locks are released:",
        "choices": [
            "A. Immediately after use",
            "B. Only after commit",
            "C. Never"
        ],
        "answer": "B. Only after commit",
        "explanation": "Strict 2PL delays releasing locks until transaction commits to prevent cascading aborts."
    },
    {
        "question": "1️⃣6️⃣ What is fuzzy checkpointing?",
        "choices": [
            "A. Checkpoints that pause all transactions",
            "B. Checkpoints allowing transactions to continue during checkpointing",
            "C. Randomly saving data"
        ],
        "answer": "B. Checkpoints allowing transactions to continue during checkpointing",
        "explanation": "Fuzzy checkpoints improve performance by not blocking active transactions."
    },
    {
        "question": "1️⃣7️⃣ Which of the following is a primary key?",
        "choices": [
            "A. Column(s) uniquely identifying a tuple",
            "B. Column storing nulls",
            "C. Any attribute of a table"
        ],
        "answer": "A. Column(s) uniquely identifying a tuple",
        "explanation": "A primary key uniquely identifies each record in a table."
    },
    {
        "question": "1️⃣8️⃣ A foreign key is used to:",
        "choices": [
            "A. Ensure referential integrity between tables",
            "B. Speed up queries",
            "C. Store duplicate data"
        ],
        "answer": "A. Ensure referential integrity between tables",
        "explanation": "Foreign keys link tables and ensure that referenced values exist."
    },
    {
        "question": "1️⃣9️⃣ What does 1NF require?",
        "choices": [
            "A. Atomic values, primary key, no multivalued columns",
            "B. No nulls allowed",
            "C. Sorted table"
        ],
        "answer": "A. Atomic values, primary key, no multivalued columns",
        "explanation": "1NF eliminates repeating groups and enforces atomic attribute values."
    },
    {
        "question": "2️⃣0️⃣ In relational algebra, the selection operator σ is used to:",
        "choices": [
            "A. Choose certain columns",
            "B. Choose certain rows based on a condition",
            "C. Combine two tables"
        ],
        "answer": "B. Choose certain rows based on a condition",
        "explanation": "σ filters rows according to the given predicate."
    },
    # SQL / Relational
    {
        "question": "2️⃣1️⃣ Which SQL clause is used to remove duplicate rows from a query result?",
        "choices": [
            "A. DISTINCT",
            "B. UNIQUE",
            "C. GROUP BY"
        ],
        "answer": "A. DISTINCT",
        "explanation": "DISTINCT removes duplicates in the query result."
    },
    {
        "question": "2️⃣2️⃣ Which SQL query finds all movies from 1990 to 1999?",
        "choices": [
            "A. SELECT title, year FROM Movie WHERE year >= 1990 AND year <= 1999;",
            "B. SELECT title FROM Movie WHERE year IN (1990,1999);",
            "C. SELECT * FROM Movie WHERE year BETWEEN 1989 AND 2000;"
        ],
        "answer": "A. SELECT title, year FROM Movie WHERE year >= 1990 AND year <= 1999;",
        "explanation": "We want all years including 1990 and 1999. BETWEEN could also work if written correctly."
    },
    {
        "question": "2️⃣3️⃣ Which relational algebra operator combines rows from two relations?",
        "choices": [
            "A. Projection (π)",
            "B. Selection (σ)",
            "C. Join (⨝)"
        ],
        "answer": "C. Join (⨝)",
        "explanation": "Join combines tuples from two relations based on a condition."
    },
    {
        "question": "2️⃣4️⃣ What is the difference between primary key and unique key?",
        "choices": [
            "A. Primary key cannot be NULL; unique key can",
            "B. Unique key cannot be NULL; primary key can",
            "C. There is no difference"
        ],
        "answer": "A. Primary key cannot be NULL; unique key can",
        "explanation": "Primary key uniquely identifies rows and cannot contain NULLs; unique key enforces uniqueness but allows one NULL."
    },
    {
        "question": "2️⃣5️⃣ Which operation in relational algebra selects specific columns?",
        "choices": [
            "A. σ (selection)",
            "B. π (projection)",
            "C. ⋈ (join)"
        ],
        "answer": "B. π (projection)",
        "explanation": "Projection selects certain columns from a relation."
    },
    # Normalization & ER
    {
        "question": "2️⃣6️⃣ What is a transitive dependency?",
        "choices": [
            "A. A → B and B → C, then A → C",
            "B. A → B and C → B, then A → C",
            "C. A → B and B → A, then C → A"
        ],
        "answer": "A. A → B and B → C, then A → C",
        "explanation": "Transitive dependency occurs when a non-key attribute depends on another non-key attribute via a chain."
    },
    {
        "question": "2️⃣7️⃣ Which normal form eliminates transitive dependencies?",
        "choices": [
            "A. 1NF",
            "B. 2NF",
            "C. 3NF"
        ],
        "answer": "C. 3NF",
        "explanation": "3NF requires that non-key attributes depend only on primary key, eliminating transitive dependencies."
    },
    {
        "question": "2️⃣8️⃣ What is BCNF?",
        "choices": [
            "A. Boyce-Codd Normal Form ensures every determinant is a superkey",
            "B. A form where every table has a primary key",
            "C. A normalization that only applies to foreign keys"
        ],
        "answer": "A. Boyce-Codd Normal Form ensures every determinant is a superkey",
        "explanation": "BCNF is stricter than 3NF and prevents anomalies caused by functional dependencies."
    },
    {
        "question": "2️⃣9️⃣ What is a derived attribute in ER modeling?",
        "choices": [
            "A. Attribute calculated from other attributes",
            "B. Attribute used as a foreign key",
            "C. Attribute that is a primary key"
        ],
        "answer": "A. Attribute calculated from other attributes",
        "explanation": "Derived attributes are not stored directly but computed from other attributes."
    },
    {
        "question": "3️⃣0️⃣ What is a weak entity’s identifying relationship?",
        "choices": [
            "A. Relationship linking it to a strong entity",
            "B. Relationship between weak entities only",
            "C. Optional relationship"
        ],
        "answer": "A. Relationship linking it to a strong entity",
        "explanation": "Weak entities rely on a strong entity for identification."
    },
    # Indexing & Performance
    {
        "question": "3️⃣1️⃣ What is the difference between a clustered and non-clustered index?",
        "choices": [
            "A. Clustered determines table storage order; non-clustered is separate",
            "B. Non-clustered determines table storage; clustered is separate",
            "C. Both are the same"
        ],
        "answer": "A. Clustered determines table storage order; non-clustered is separate",
        "explanation": "Clustered index arranges table rows physically, non-clustered stores pointers separately."
    },
    {
        "question": "3️⃣2️⃣ Which data structure is commonly used for B+-tree index?",
        "choices": [
            "A. Linked list",
            "B. Balanced tree",
            "C. Hash table"
        ],
        "answer": "B. Balanced tree",
        "explanation": "B+-trees are balanced search trees used to index data efficiently."
    },
    {
        "question": "3️⃣3️⃣ What is the primary performance overhead in DBMS?",
        "choices": [
            "A. Disk I/O",
            "B. CPU computation",
            "C. RAM usage"
        ],
        "answer": "A. Disk I/O",
        "explanation": "Accessing data from disk is slower than computation, dominating performance costs."
    },
    {
        "question": "3️⃣4️⃣ RAID 1 is characterized by:",
        "choices": [
            "A. Mirroring for redundancy",
            "B. Striping without parity",
            "C. Striping with parity"
        ],
        "answer": "A. Mirroring for redundancy",
        "explanation": "RAID 1 duplicates data across disks to prevent data loss."
    },
    {
        "question": "3️⃣5️⃣ Which storage type is typically fastest?",
        "choices": [
            "A. HDD",
            "B. SSD",
            "C. Tape"
        ],
        "answer": "B. SSD",
        "explanation": "Solid-state drives have much faster random access than hard drives or tape."
    },
    # Transactions & Logging
    {
        "question": "3️⃣6️⃣ What are the four ACID properties?",
        "choices": [
            "A. Atomicity, Consistency, Isolation, Durability",
            "B. Accuracy, Consistency, Isolation, Durability",
            "C. Atomicity, Concurrency, Isolation, Data"
        ],
        "answer": "A. Atomicity, Consistency, Isolation, Durability",
        "explanation": "ACID ensures database correctness, even during concurrent or failed transactions."
    },
    {
        "question": "3️⃣7️⃣ What is the purpose of a transaction log?",
        "choices": [
            "A. Allow rollback and recovery",
            "B. Make queries faster",
            "C. Encrypt data"
        ],
        "answer": "A. Allow rollback and recovery",
        "explanation": "Logs record changes to support undo/redo and crash recovery."
    },
    {
        "question": "3️⃣8️⃣ What type of log record is needed to recover from a system crash?",
        "choices": [
            "A. Undo and redo information",
            "B. Only redo",
            "C. Only undo"
        ],
        "answer": "A. Undo and redo information",
        "explanation": "Redo applies committed changes; undo reverses uncommitted changes."
    },
    {
        "question": "3️⃣9️⃣ Checkpoints are used to:",
        "choices": [
            "A. Reduce recovery time",
            "B. Speed up queries",
            "C. Lock the database"
        ],
        "answer": "A. Reduce recovery time",
        "explanation": "Checkpoints record a consistent state so recovery doesn't need to scan entire logs."
    },
    {
        "question": "4️⃣0️⃣ Fuzzy checkpointing allows:",
        "choices": [
            "A. Transactions to continue during checkpointing",
            "B. Pausing all transactions",
            "C. Writing random data to disk"
        ],
        "answer": "A. Transactions to continue during checkpointing",
        "explanation": "Fuzzy checkpoints avoid stopping active transactions, improving performance."
    },
    # More SQL / Queries
    {
        "question": "4️⃣1️⃣ How to count movies that 'Tom Hanks' acted in?",
        "choices": [
            "A. SELECT COUNT(*) FROM Role WHERE aid=(SELECT aid FROM Actor WHERE name='Tom' AND surname='Hanks');",
            "B. SELECT COUNT(*) FROM Actor WHERE name='Tom';",
            "C. SELECT COUNT(mid) FROM Movie;"
        ],
        "answer": "A. SELECT COUNT(*) FROM Role WHERE aid=(SELECT aid FROM Actor WHERE name='Tom' AND surname='Hanks');",
        "explanation": "We count roles played by 'Tom Hanks' using subquery to find his aid."
    },
    {
        "question": "4️⃣2️⃣ How to find all actors in 'Top Gun:Maverick'?",
        "choices": [
            "A. SELECT name, surname FROM Actor WHERE aid IN (SELECT aid FROM Role WHERE mid=(SELECT mid FROM Movie WHERE title='Top Gun:Maverick'));",
            "B. SELECT * FROM Actor;",
            "C. SELECT title FROM Movie WHERE mid=147;"
        ],
        "answer": "A. SELECT name, surname FROM Actor WHERE aid IN (SELECT aid FROM Role WHERE mid=(SELECT mid FROM Movie WHERE title='Top Gun:Maverick'));",
        "explanation": "We join Role and Actor via aid to find all actors in that movie."
    },
    {
        "question": "4️⃣3️⃣ Which SQL construct allows combining results from multiple tables?",
        "choices": [
            "A. JOIN",
            "B. GROUP BY",
            "C. DISTINCT"
        ],
        "answer": "A. JOIN",
        "explanation": "JOIN combines tuples from multiple tables based on related attributes."
    },
    {
        "question": "4️⃣4️⃣ In relational algebra, π_{StudentID, Residence}(σ_{BirthYear<2000}(Students)) means:",
        "choices": [
            "A. Select StudentID and Residence for students born before 2000",
            "B. Select all students",
            "C. Select BirthYear only"
        ],
        "answer": "A. Select StudentID and Residence for students born before 2000",
        "explanation": "σ filters rows; π selects specific columns."
    },
    {
        "question": "4️⃣5️⃣ What is a serializable transaction schedule?",
        "choices": [
            "A. A schedule equivalent to some serial execution",
            "B. Transactions executed randomly",
            "C. Transactions with no logging"
        ],
        "answer": "A. A schedule equivalent to some serial execution",
        "explanation": "Serializable schedules preserve correctness of concurrent transaction execution."
    },
    # True/False style questions
    {
        "question": "4️⃣6️⃣ True or False: In 2PL, transactions can acquire locks after releasing others.",
        "choices": ["True", "False"],
        "answer": "False",
        "explanation": "2PL requires a growing phase (acquire) and shrinking phase (release). No locks after release."
    },
    {
        "question": "4️⃣7️⃣ True or False: Foreign keys can enforce referential integrity.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Foreign keys ensure referenced values exist in another table."
    },
    {
        "question": "4️⃣8️⃣ True or False: Extensible hashing can dynamically grow to avoid collisions.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Extensible hashing uses a directory that grows with the number of buckets."
    },
    {
        "question": "4️⃣9️⃣ True or False: 1NF allows multivalued attributes.",
        "choices": ["True", "False"],
        "answer": "False",
        "explanation": "1NF requires atomic attributes; multivalued columns are not allowed."
    },
    {
        "question": "5️⃣0️⃣ True or False: BCNF always removes all redundancy in a table.",
        "choices": ["True", "False"],
        "answer": "False",
        "explanation": "BCNF removes redundancy caused by functional dependencies, but some redundancy may still exist."
    },
    # More conceptual / performance
    {
        "question": "5️⃣1️⃣ What is the main difference between hash index and B+-tree index?",
        "choices": [
            "A. Hash is fast for equality, B+-tree supports range queries",
            "B. B+-tree is faster for equality, hash supports range queries",
            "C. No difference"
        ],
        "answer": "A. Hash is fast for equality, B+-tree supports range queries",
        "explanation": "B+-trees maintain order for range searches; hash is direct lookup."
    },
    {
        "question": "5️⃣2️⃣ RAID 5 uses:",
        "choices": [
            "A. Striping with parity",
            "B. Mirroring",
            "C. Striping without parity"
        ],
        "answer": "A. Striping with parity",
        "explanation": "RAID 5 stripes data and distributes parity to provide fault tolerance efficiently."
    },
    {
        "question": "5️⃣3️⃣ Which is a disadvantage of BCNF?",
        "choices": [
            "A. May require decomposition leading to more joins",
            "B. Cannot remove redundancy",
            "C. Cannot have primary keys"
        ],
        "answer": "A. May require decomposition leading to more joins",
        "explanation": "Decomposition may increase query complexity even if redundancy is removed."
    },
    {
        "question": "5️⃣4️⃣ In 2PL, rigorous 2PL differs from strict 2PL by:",
        "choices": [
            "A. Releasing read locks only at commit",
            "B. Releasing write locks at commit",
            "C. Acquiring locks faster"
        ],
        "answer": "A. Releasing read locks only at commit",
        "explanation": "Rigorous 2PL holds all locks until commit, ensuring serializability and preventing cascading aborts."
    },
    {
        "question": "5️⃣5️⃣ Why do we need checkpoints in a DBMS?",
        "choices": [
            "A. Reduce recovery time after crashes",
            "B. Reduce disk space",
            "C. Improve query speed"
        ],
        "answer": "A. Reduce recovery time after crashes",
        "explanation": "Checkpoints store consistent states, minimizing log replay during recovery."
    },
    {
        "question": "5️⃣6️⃣ Total price of orders in SQL can be computed using:",
        "choices": [
            "A. SELECT SUM(price*quantity) FROM Order JOIN Product ON Order.pid=Product.pid;",
            "B. SELECT COUNT(*) FROM Order;",
            "C. SELECT AVG(price) FROM Product;"
        ],
        "answer": "A. SELECT SUM(price*quantity) FROM Order JOIN Product ON Order.pid=Product.pid;",
        "explanation": "SUM aggregates total cost per order using JOIN to get product prices."
    },
    {
        "question": "5️⃣7️⃣ In 1NF, how should multi-valued attributes be handled?",
        "choices": [
            "A. Split into separate rows",
            "B. Keep as lists in a column",
            "C. Ignore them"
        ],
        "answer": "A. Split into separate rows",
        "explanation": "1NF requires atomic values, so multi-valued attributes are normalized into separate rows."
    },
    {
        "question": "5️⃣8️⃣ True or False: Serializable schedules allow non-serializable interleaving.",
        "choices": ["True", "False"],
        "answer": "False",
        "explanation": "Serializable schedules behave as if transactions were executed serially."
    },
    {
        "question": "5️⃣9️⃣ In relational algebra, which operator is used to rename attributes?",
        "choices": [
            "A. ρ (rho)",
            "B. σ (sigma)",
            "C. π (pi)"
        ],
        "answer": "A. ρ (rho)",
        "explanation": "ρ allows renaming relations or attributes in relational algebra expressions."
    },
    {
        "question": "6️⃣0️⃣ True or False: Foreign keys can reference composite primary keys.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Foreign keys can reference single or multiple columns forming a composite primary key."
    },
    # Bonus tricky SQL / Relational Algebra
    {
        "question": "6️⃣1️⃣ In relational algebra, how would you express 'all students who took both INF2700 and INF3200'?",
        "choices": [
            "A. π_{ssn,name}(σ_{courseld='INF2700'}(Exam)) ∩ π_{ssn,name}(σ_{courseld='INF3200'}(Exam))",
            "B. π_{ssn,name}(σ_{courseld='INF2700' OR courseld='INF3200'}(Exam))",
            "C. π_{ssn,name}(σ_{courseld='INF2700'}(Exam)) ∪ π_{ssn,name}(σ_{courseld='INF3200'}(Exam))"
        ],
        "answer": "A. π_{ssn,name}(σ_{courseld='INF2700'}(Exam)) ∩ π_{ssn,name}(σ_{courseld='INF3200'}(Exam))",
        "explanation": "Intersection finds students enrolled in both courses."
    },
    {
        "question": "6️⃣2️⃣ Which SQL query lists students who have grade 'A' after 01-01-2021?",
        "choices": [
            "A. SELECT name, address FROM Student JOIN Exam ON ssn=student\$sn WHERE grade='A' AND date>'2021-01-01';",
            "B. SELECT * FROM Exam WHERE grade='A';",
            "C. SELECT ssn FROM Student WHERE grade='A';"
        ],
        "answer": "A. SELECT name, address FROM Student JOIN Exam ON ssn=student\$sn WHERE grade='A' AND date>'2021-01-01';",
        "explanation": "We need to join Student and Exam, then filter by grade and date."
    },
    {
        "question": "6️⃣3️⃣ In relational algebra, how do you get total credits per student?",
        "choices": [
            "A. γ_{ssn, SUM(credits)}(Student ⋈ Exam ⋈ Course)",
            "B. π_{name, credits}(Student ⋈ Exam ⋈ Course)",
            "C. σ_{SUM(credits)>0}(Student ⋈ Exam ⋈ Course)"
        ],
        "answer": "A. γ_{ssn, SUM(credits)}(Student ⋈ Exam ⋈ Course)",
        "explanation": "γ represents aggregation, SUM computes total credits grouped by ssn."
    },
    {
        "question": "6️⃣4️⃣ True or False: A foreign key must always reference a primary key.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Referential integrity requires the foreign key to point to a unique identifier (usually a primary key)."
    },
    {
        "question": "6️⃣5️⃣ What is the difference between HAVING and WHERE in SQL?",
        "choices": [
            "A. WHERE filters before grouping; HAVING filters after grouping",
            "B. HAVING filters rows; WHERE filters columns",
            "C. No difference"
        ],
        "answer": "A. WHERE filters before grouping; HAVING filters after grouping",
        "explanation": "WHERE is used before GROUP BY, HAVING is used to filter aggregates."
    },
    {
        "question": "6️⃣6️⃣ Which type of join includes all rows from left table, even if no match in right table?",
        "choices": [
            "A. LEFT OUTER JOIN",
            "B. INNER JOIN",
            "C. CROSS JOIN"
        ],
        "answer": "A. LEFT OUTER JOIN",
        "explanation": "Left outer join preserves all rows from the left table, filling NULLs for missing matches."
    },
    {
        "question": "6️⃣7️⃣ How does hash indexing handle collisions?",
        "choices": [
            "A. Chaining or open addressing",
            "B. Ignoring duplicates",
            "C. Sorting entries"
        ],
        "answer": "A. Chaining or open addressing",
        "explanation": "Collisions occur when two keys hash to same bucket; handled by chaining or probing."
    },
    {
        "question": "6️⃣8️⃣ True or False: In BCNF, every non-prime attribute must depend on a candidate key.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "BCNF requires all determinants to be superkeys, eliminating dependency anomalies."
    },
    {
        "question": "6️⃣9️⃣ In 2PL, which of the following can prevent cascading aborts?",
        "choices": [
            "A. Strict 2PL",
            "B. Normal 2PL",
            "C. No locking"
        ],
        "answer": "A. Strict 2PL",
        "explanation": "Strict 2PL holds write locks until commit, preventing cascading aborts."
    },
    {
        "question": "7️⃣0️⃣ True or False: Extensible hashing can lead to directory doubling.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "When buckets overflow, the directory may double to accommodate growth dynamically."
    },
    {
        "question": "7️⃣1️⃣ What is the main difference between redo and undo logging?",
        "choices": [
            "A. Redo reapplies committed changes; undo rolls back uncommitted changes",
            "B. Redo rolls back uncommitted changes; undo reapplies committed",
            "C. Both do the same"
        ],
        "answer": "A. Redo reapplies committed changes; undo rolls back uncommitted changes",
        "explanation": "Redo ensures durability; undo ensures atomicity."
    },
    {
        "question": "7️⃣2️⃣ True or False: Functional dependency {A,B} → C means C depends on both A and B.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "C is determined by the combination of A and B."
    },
    {
        "question": "7️⃣3️⃣ Which is NOT part of query processing steps?",
        "choices": [
            "A. Parsing and translation",
            "B. Optimization",
            "C. Index replication"
        ],
        "answer": "C. Index replication",
        "explanation": "Query processing involves parsing, optimization, and execution; index replication is unrelated."
    },
    {
        "question": "7️⃣4️⃣ In RAID, striping improves:",
        "choices": [
            "A. Performance",
            "B. Reliability only",
            "C. Security"
        ],
        "answer": "A. Performance",
        "explanation": "Striping spreads data across disks, allowing parallel access and faster reads/writes."
    },
    {
        "question": "7️⃣5️⃣ What is a weak entity’s primary key composed of?",
        "choices": [
            "A. Its partial key + primary key of owner entity",
            "B. Only its partial key",
            "C. Only a generated number"
        ],
        "answer": "A. Its partial key + primary key of owner entity",
        "explanation": "Weak entities rely on owner entity's primary key combined with their own partial key."
    },
    {
        "question": "7️⃣6️⃣ Which SQL aggregate function ignores NULL values?",
        "choices": [
            "A. SUM, AVG, COUNT(column)",
            "B. SUM, AVG, COUNT(*)",
            "C. COUNT(*) only"
        ],
        "answer": "A. SUM, AVG, COUNT(column)",
        "explanation": "Aggregates skip NULLs except COUNT(*) which counts all rows."
    },
    {
        "question": "7️⃣7️⃣ True or False: In a composite foreign key, all referenced columns must match a candidate key.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Each column in composite foreign key references the corresponding column of a candidate key."
    },
    {
        "question": "7️⃣8️⃣ What is fuzzy checkpointing designed to solve?",
        "choices": [
            "A. Avoid halting active transactions during checkpoint",
            "B. Increase disk speed",
            "C. Reduce memory usage"
        ],
        "answer": "A. Avoid halting active transactions during checkpoint",
        "explanation": "Fuzzy checkpoints allow transactions to continue while checkpointing, improving performance."
    },
    {
        "question": "7️⃣9️⃣ How does write-ahead logging (WAL) ensure recovery?",
        "choices": [
            "A. Log changes before writing to database",
            "B. Write to disk after transaction commit",
            "C. Skip logging for speed"
        ],
        "answer": "A. Log changes before writing to database",
        "explanation": "WAL ensures all updates are recorded in log before modifying the database, ensuring recovery."
    },
    {
        "question": "8️⃣0️⃣ True or False: In relational algebra, union requires the two relations to have the same attributes.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Union combines tuples only if relations are union-compatible (same attributes and types)."
    },
    {
        "question": "8️⃣1️⃣ In relational algebra, which operator corresponds to SQL’s GROUP BY?",
        "choices": [
            "A. γ (gamma)",
            "B. π (pi)",
            "C. σ (sigma)"
        ],
        "answer": "A. γ (gamma)",
        "explanation": "γ is used for aggregation and grouping in relational algebra."
    },
    {
        "question": "8️⃣2️⃣ True or False: A candidate key can contain NULL values.",
        "choices": ["True", "False"],
        "answer": "False",
        "explanation": "Candidate keys must uniquely identify tuples and cannot have NULLs."
    },
    {
        "question": "8️⃣3️⃣ Which step in query processing decides the best execution plan?",
        "choices": [
            "A. Query optimization",
            "B. Parsing",
            "C. Execution"
        ],
        "answer": "A. Query optimization",
        "explanation": "Optimization evaluates alternative plans and chooses the most efficient."
    }
]

# -----------------------------
# SESSION STATE INIT
# -----------------------------
if "q_index" not in st.session_state:
    st.session_state.q_index = 0

if "shuffled_questions" not in st.session_state:
    st.session_state.shuffled_questions = random.sample(questions, len(questions))  # Shuffle questions

if "user_answers" not in st.session_state:
    st.session_state.user_answers = [None] * len(st.session_state.shuffled_questions)

if "score" not in st.session_state:
    st.session_state.score = 0

if "feedback" not in st.session_state:
    st.session_state.feedback = ""

# -----------------------------
# SHUFFLE CHOICES PER QUESTION
# -----------------------------
if "shuffled_choices" not in st.session_state:
    st.session_state.shuffled_choices = [
        random.sample(q["choices"], len(q["choices"])) for q in st.session_state.shuffled_questions
    ]

# -----------------------------
# DISPLAY CURRENT QUESTION
# -----------------------------
q = st.session_state.shuffled_questions[st.session_state.q_index]
choices = st.session_state.shuffled_choices[st.session_state.q_index]

st.markdown(f"<h3 style='text-align:center'>{q['question']}</h3>", unsafe_allow_html=True)

# -----------------------------
# CSS FOR LARGE BUTTONS AND NAVIGATION
# -----------------------------
st.markdown("""
<style>
.choice-button {
    width: 90%;
    max-width: 500px;
    min-height: 60px;
    font-size: 18px;
    padding: 15px;
    margin: 10px auto;
    display: block;
    text-align: left;
    border-radius: 10px;
    background-color: #f0f0f0;
    border: 2px solid #ccc;
}
.choice-button:hover {
    background-color: #e0e0e0;
}
.nav-container {
    width: 90%;
    max-width: 500px;
    margin: 20px auto 10px auto;
    display: flex;
    justify-content: space-between;
}
.nav-button {
    width: 120px;
    height: 45px;
    font-size: 16px;
}
.feedback {
    text-align:center;
    font-size:16px;
    margin-top:10px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# DISPLAY CHOICES AS LARGE RECTANGULAR BUTTONS
# -----------------------------
for choice in choices:
    if st.button(choice, key=f"{st.session_state.q_index}_{choice}", help="Click to answer"):
        st.session_state.user_answers[st.session_state.q_index] = choice
        if choice == q["answer"]:
            st.session_state.feedback = f"✅ Correct! {q['explanation']}"
            st.session_state.score += 1
        else:
            st.session_state.feedback = f"❌ Incorrect. Correct: {q['answer']}.\n{q['explanation']}"

if st.session_state.feedback:
    st.markdown(f"<div class='feedback'>{st.session_state.feedback}</div>", unsafe_allow_html=True)

# -----------------------------
# NAVIGATION BUTTONS
# -----------------------------
prev_disabled = st.session_state.q_index == 0
next_disabled = st.session_state.q_index == len(st.session_state.shuffled_questions) - 1

st.markdown("<div class='nav-container'>", unsafe_allow_html=True)
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("⬅️ Previous", key="prev", disabled=prev_disabled):
        if st.session_state.q_index > 0:
            st.session_state.q_index -= 1
            st.session_state.feedback = ""
with col2:
    if st.button("Next ➡️", key="next", disabled=next_disabled):
        if st.session_state.q_index < len(st.session_state.shuffled_questions) - 1:
            st.session_state.q_index += 1
            st.session_state.feedback = ""
st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# PROGRESS AND SCORE
# -----------------------------
st.progress((st.session_state.q_index + 1) / len(st.session_state.shuffled_questions))
st.caption(f"Question {st.session_state.q_index + 1} of {len(st.session_state.shuffled_questions)}")
st.metric("Score", f"{st.session_state.score} / {len(st.session_state.shuffled_questions)}")
