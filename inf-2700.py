import streamlit as st
import random

st.set_page_config(page_title="Database Systems Quiz 2025", layout="centered")

# -----------------------------
# QUESTIONS (same as before)
# -----------------------------
questions = [
    # SQL / Relational
    {
        "question": "Which database object stores multiple rows with the same schema?",
        "choices": ["A. Table", "B. View", "C. Index", "D. Sequence"],
        "answer": "A. Table",
        "explanation": "Tables store tuples with the same attributes in relational databases."
    },
    {
        "question": "True or False: A primary key can have NULL values.",
        "choices": ["A. True", "B. False"],
        "answer": "B. False",
        "explanation": "Primary keys must uniquely identify each row and cannot be NULL."
    },
    {
        "question": "Which SQL clause is used to filter rows after a GROUP BY?",
        "choices": ["A. WHERE", "B. HAVING", "C. ORDER BY", "D. SELECT"],
        "answer": "B. HAVING",
        "explanation": "HAVING filters groups, while WHERE filters individual rows."
    },
    {
        "question": "What is a foreign key used for?",
        "choices": ["A. Storing duplicate data", "B. Referencing primary keys in another table", "C. Creating indexes", "D. Ensuring unique values"],
        "answer": "B. Referencing primary keys in another table",
        "explanation": "Foreign keys maintain referential integrity between tables."
    },
    {
        "question": "True or False: SQL JOINs combine rows from two or more tables based on a related column.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "JOINs merge rows where the join condition is met."
    },
    {
        "question": "Which SQL statement is used to remove all records from a table but keep its structure?",
        "choices": ["A. DELETE", "B. DROP", "C. TRUNCATE", "D. REMOVE"],
        "answer": "C. TRUNCATE",
        "explanation": "TRUNCATE removes all rows efficiently but preserves the table."
    },
    {
        "question": "Which normal form requires that every non-key attribute is fully functionally dependent on the primary key?",
        "choices": ["A. 1NF", "B. 2NF", "C. 3NF", "D. BCNF"],
        "answer": "B. 2NF",
        "explanation": "2NF eliminates partial dependencies on a composite primary key."
    },
    {
        "question": "True or False: A B+-tree leaf node contains pointers to actual data records.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "Leaf nodes in B+-trees store data or pointers to data for efficient search."
    },
    
    {
        "question": "Which of the following is a condition for a relation to be in BCNF?",
        "choices": ["A. All attributes are numeric", "B. Every determinant is a candidate key", "C. No duplicate rows", "D. Only one primary key exists"],
        "answer": "B. Every determinant is a candidate key",
        "explanation": "BCNF requires that all functional dependencies have a candidate key as determinant."
    },
    {
        "question": "True or False: A view can store data physically in the database.",
        "choices": ["A. True", "B. False"],
        "answer": "B. False",
        "explanation": "Views are virtual tables; they do not store data but display data from underlying tables."
    },
    {
        "question": "Which SQL aggregate function counts the number of rows?",
        "choices": ["A. SUM", "B. AVG", "C. COUNT", "D. TOTAL"],
        "answer": "C. COUNT",
        "explanation": "COUNT returns the number of rows satisfying the query conditions."
    },
    {
        "question": "Which type of lock allows multiple transactions to read a data item but not write?",
        "choices": ["A. Exclusive lock", "B. Shared lock", "C. Deadlock lock", "D. Optimistic lock"],
        "answer": "B. Shared lock",
        "explanation": "Shared locks allow concurrent reads but prevent writes until released."
    },
    {
        "question": "True or False: WAL (Write-Ahead Logging) ensures updates are logged before they are applied to the database.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "WAL helps recovery by recording changes before actual database updates."
    },
    {
        "question": "Which relational algebra operation combines rows from two tables with a common attribute?",
        "choices": ["A. Union", "B. Difference", "C. Cartesian product", "D. Join"],
        "answer": "D. Join",
        "explanation": "Join merges tuples from tables based on matching attribute values."
    },
    {
        "question": "Which SQL clause sorts the result set?",
        "choices": ["A. WHERE", "B. GROUP BY", "C. ORDER BY", "D. HAVING"],
        "answer": "C. ORDER BY",
        "explanation": "ORDER BY arranges rows in ascending or descending order."
    },
    {
        "question": "True or False: A database transaction must be atomic, consistent, isolated, and durable.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "These are the ACID properties ensuring transaction reliability."
    },
    {
        "question": "Which SQL command changes existing records in a table?",
        "choices": ["A. INSERT", "B. UPDATE", "C. DELETE", "D. ALTER"],
        "answer": "B. UPDATE",
        "explanation": "UPDATE modifies data in existing rows based on conditions."
    },
    {
        "question": "What is the difference between a primary index and a secondary index?",
        "choices": [
            "A. Primary indexes are unique, secondary are not",
            "B. Primary indexes are on sorted files, secondary on unsorted",
            "C. Primary index is on the primary key, secondary can be on other attributes",
            "D. There is no difference"
        ],
        "answer": "C. Primary index is on the primary key, secondary can be on other attributes",
        "explanation": "Primary indexes enforce uniqueness on primary keys; secondary indexes speed up other queries."
    },
    {
        "question": "True or False: In a functional dependency A → B, knowing A determines B uniquely.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "Functional dependency means attribute B is uniquely determined by A."
    },
    {
        "question": "Which SQL statement is used to add a new row to a table?",
        "choices": ["A. INSERT", "B. UPDATE", "C. DELETE", "D. ALTER"],
        "answer": "A. INSERT",
        "explanation": "INSERT adds new tuples into a table."
    },
    {
        "question": "True or False: The Cartesian product of two tables always increases the number of rows.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "Each row of the first table is combined with every row of the second table."
    },
    {
        "question": "Which SQL keyword eliminates duplicate rows in a query result?",
        "choices": ["A. UNIQUE", "B. DISTINCT", "C. FILTER", "D. REMOVE"],
        "answer": "B. DISTINCT",
        "explanation": "DISTINCT ensures each row in the output appears only once."
    },
    {
        "question": "Which operation in relational algebra corresponds to SQL's SELECT ... FROM ... WHERE?",
        "choices": ["A. Projection", "B. Selection", "C. Join", "D. Union"],
        "answer": "B. Selection",
        "explanation": "Selection (σ) filters rows based on a condition."
    },
    {
        "question": "True or False: Deleting a primary key that is referenced by a foreign key without CASCADE will result in an error.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "Referential integrity prevents deletion unless CASCADE is specified."
    },
    {
        "question": "Which SQL clause groups rows with the same values into summary rows?",
        "choices": ["A. GROUP BY", "B. ORDER BY", "C. HAVING", "D. WHERE"],
        "answer": "A. GROUP BY",
        "explanation": "GROUP BY collects rows sharing attribute values for aggregation."
    },
    {
        "question": "What type of join returns all rows from the left table and matched rows from the right table?",
        "choices": ["A. Inner Join", "B. Left Outer Join", "C. Right Outer Join", "D. Full Outer Join"],
        "answer": "B. Left Outer Join",
        "explanation": "Left Outer Join keeps all rows from the left table regardless of matches."
    },
    {
        "question": "True or False: A schema in 3NF can have transitive dependencies.",
        "choices": ["A. True", "B. False"],
        "answer": "B. False",
        "explanation": "3NF removes transitive dependencies on non-key attributes."
    },
    {
        "question": "Which SQL aggregate function calculates the average value of a column?",
        "choices": ["A. SUM", "B. AVG", "C. COUNT", "D. MAX"],
        "answer": "B. AVG",
        "explanation": "AVG returns the arithmetic mean of the selected column."
    },
    {
        "question": "True or False: An index can improve read performance but may slow down write operations.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "Indexes speed up searches but add overhead when inserting/updating data."
    },
    {
        "question": "Which of the following ensures that multiple transactions execute without interfering with each other?",
        "choices": ["A. Normalization", "B. Concurrency control", "C. Indexing", "D. Logging"],
        "answer": "B. Concurrency control",
        "explanation": "Concurrency control mechanisms maintain isolation and prevent anomalies."
    },
    {
        "question": "True or False: A B*-tree can store more keys per node than a B-tree.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "B*-trees split nodes differently, allowing higher space utilization."
    },
    {
        "question": "What is the difference between TRUNCATE and DELETE in SQL?",
        "choices": [
            "A. TRUNCATE is slower than DELETE",
            "B. DELETE can be rolled back, TRUNCATE cannot",
            "C. TRUNCATE removes all rows quickly without logging individual deletions, DELETE removes rows one by one",
            "D. There is no difference"
        ],
        "answer": "C. TRUNCATE removes all rows quickly without logging individual deletions, DELETE removes rows one by one",
        "explanation": "TRUNCATE is faster but less flexible; DELETE can use WHERE and can be rolled back."
    },
    {
        "question": "True or False: Lossless decomposition guarantees that no information is lost during normalization.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "Lossless decomposition ensures the original relation can be reconstructed from decomposed relations."
    },
    {
        "question": "Which SQL keyword is used to enforce uniqueness in a column?",
        "choices": ["A. UNIQUE", "B. PRIMARY", "C. DISTINCT", "D. FOREIGN"],
        "answer": "A. UNIQUE",
        "explanation": "UNIQUE ensures that all values in the column are distinct."
    },
    {
        "question": "Which of the following describes a strict schedule in transaction processing?",
        "choices": [
            "A. Transactions do not lock data",
            "B. Transactions hold exclusive locks until commit or abort",
            "C. Transactions read dirty data",
            "D. Transactions can be partially applied"
        ],
        "answer": "B. Transactions hold exclusive locks until commit or abort",
        "explanation": "Strict schedules prevent cascading aborts by holding locks until completion."
    },
    {
        "question": "True or False: A foreign key must reference a primary key in another table.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "Foreign keys maintain referential integrity by referencing primary keys."
    },
    {
        "question": "Which SQL statement is used to remove an entire table from the database?",
        "choices": ["A. DELETE", "B. DROP", "C. TRUNCATE", "D. REMOVE"],
        "answer": "B. DROP",
        "explanation": "DROP completely removes the table and its data from the database."
    },
    {
        "question": "True or False: In functional dependency A → B, B is dependent on A.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "A functional dependency means knowing A allows you to uniquely determine B."
    },
    {
        "question": "Which transaction property ensures that once a transaction commits, its changes are permanent?",
        "choices": ["A. Atomicity", "B. Consistency", "C. Isolation", "D. Durability"],
        "answer": "D. Durability",
        "explanation": "Durability guarantees that committed changes persist even in case of system failure."
    },
    {
        "question": "True or False: Shared locks allow other transactions to read the same data simultaneously.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "Shared locks permit concurrent reads but block writes."
    },
    {
        "question": "Which relational algebra operation returns rows present in the first table but not in the second?",
        "choices": ["A. Union", "B. Intersection", "C. Difference", "D. Cartesian product"],
        "answer": "C. Difference",
        "explanation": "Difference (−) returns tuples in the first relation not found in the second."
    },
    {
        "question": "Which SQL statement is used to modify the structure of a table?",
        "choices": ["A. ALTER", "B. UPDATE", "C. MODIFY", "D. CHANGE"],
        "answer": "A. ALTER",
        "explanation": "ALTER can add, drop, or modify columns and constraints in a table."
    },
    {
        "question": "True or False: Query optimization improves the performance of database queries.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "Optimized queries run faster and use fewer resources."
    },
    {
        "question": "Which B+-tree node type contains pointers to other nodes and guides searches?",
        "choices": ["A. Root node", "B. Internal node", "C. Leaf node", "D. Index node"],
        "answer": "B. Internal node",
        "explanation": "Internal nodes store keys and child pointers for traversal."
    },
    {
        "question": "True or False: A composite primary key consists of more than one attribute.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "Composite keys use multiple columns to uniquely identify a row."
    },
    {
        "question": "True or False: A view can be used to simplify complex queries for users.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "Views provide a virtual table abstraction over complex queries."
    },
    {
        "question": "Which type of join returns only rows that satisfy the join condition in both tables?",
        "choices": ["A. Inner Join", "B. Left Outer Join", "C. Right Outer Join", "D. Full Outer Join"],
        "answer": "A. Inner Join",
        "explanation": "Inner joins return rows that match the join condition in both tables."
    },
    {
        "question": "Which of the following is NOT a property of ACID transactions?",
        "choices": ["A. Atomicity", "B. Consistency", "C. Isolation", "D. Indexing"],
        "answer": "D. Indexing",
        "explanation": "Indexing is unrelated to transaction properties."
    },
    {
        "question": "True or False: Checkpoints in transaction logs help speed up recovery after a crash.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "Checkpoints reduce the amount of log replay required during recovery."
    },
    {
        "question": "Which type of index stores keys in a sorted order to facilitate range queries?",
        "choices": ["A. Hash index", "B. B+-tree index", "C. Bitmap index", "D. Clustered index"],
        "answer": "B. B+-tree index",
        "explanation": "B+-trees maintain sorted keys for efficient search and range queries."
    },
    {
        "question": "Which relational algebra operation corresponds to SQL's JOIN?",
        "choices": ["A. Union", "B. Cartesian Product", "C. Join", "D. Selection"],
        "answer": "C. Join",
        "explanation": "Join combines tuples from two relations based on a condition."
    },
    {
        "question": "True or False: A B*-tree always has more than one root node.",
        "choices": ["A. True", "B. False"],
        "answer": "B. False",
        "explanation": "B*-trees have a single root node like regular B-trees."
    },
    {
        "question": "Which SQL statement retrieves the top N records ordered by salary?",
        "choices": ["A. SELECT TOP N ...", "B. SELECT ... LIMIT N", "C. SELECT ... ORDER BY salary DESC LIMIT N", "D. SELECT ... ORDER BY salary ASC LIMIT N"],
        "answer": "C. SELECT ... ORDER BY salary DESC LIMIT N",
        "explanation": "LIMIT N after ORDER BY DESC returns top N salaries."
    },
    {
        "question": "True or False: Functional dependency X → Y means that two rows with the same X value must have the same Y value.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "This is the definition of a functional dependency."
    },
    {
        "question": "Which type of join returns all rows from both tables, filling NULL when no match exists?",
        "choices": ["A. Inner Join", "B. Left Outer Join", "C. Right Outer Join", "D. Full Outer Join"],
        "answer": "D. Full Outer Join",
        "explanation": "Full outer joins include unmatched rows from both tables."
    },
    {
        "question": "Which SQL clause filters groups after aggregation?",
        "choices": ["A. WHERE", "B. GROUP BY", "C. HAVING", "D. ORDER BY"],
        "answer": "C. HAVING",
        "explanation": "HAVING filters aggregated results, while WHERE filters individual rows."
    },
    {
        "question": "True or False: In BCNF, every non-trivial functional dependency has a superkey on the left side.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "BCNF ensures all dependencies are on superkeys to eliminate anomalies."
    },
    {
        "question": "Which SQL statement updates existing rows in a table?",
        "choices": ["A. INSERT", "B. UPDATE", "C. ALTER", "D. MODIFY"],
        "answer": "B. UPDATE",
        "explanation": "UPDATE changes data in existing rows according to a condition."
    },
    {
        "question": "True or False: A transaction is atomic if all its operations succeed or none are applied.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "Atomicity ensures no partial changes occur in a transaction."
    },
    {
        "question": "Which index type is best suited for equality searches but poor for range queries?",
        "choices": ["A. Hash index", "B. B+-tree", "C. Bitmap index", "D. Clustered index"],
        "answer": "A. Hash index",
        "explanation": "Hash indexes map values directly to buckets, making equality fast but range searches inefficient."
    },
    {
        "question": "True or False: An SQL VIEW can update underlying tables if it references only one table and no aggregation.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "Simple views without joins or aggregations can allow updates."
    },
    {
        "question": "Which concurrency control technique uses timestamps to order transactions?",
        "choices": ["A. Two-phase locking", "B. Optimistic concurrency control", "C. Timestamp ordering", "D. Deadlock detection"],
        "answer": "C. Timestamp ordering",
        "explanation": "Transactions are executed in timestamp order to ensure serializability."
    },
    {
        "question": "True or False: In a redo phase, only committed transactions are applied to recover a crash.",
        "choices": ["A. True", "B. False"],
        "answer": "B. False",
        "explanation": "Redo applies updates from all transactions to ensure database consistency."
    },
    {
        "question": "Which normal form removes partial dependencies on a composite primary key?",
        "choices": ["A. 1NF", "B. 2NF", "C. 3NF", "D. BCNF"],
        "answer": "B. 2NF",
        "explanation": "2NF eliminates dependencies on part of a composite key."
    },
    {
        "question": "True or False: Dirty reads occur when a transaction reads uncommitted data from another transaction.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "Reading uncommitted changes can lead to inconsistent results."
    },
    {
        "question": "Which SQL keyword enforces that a column cannot contain NULL values?",
        "choices": ["A. PRIMARY KEY", "B. NOT NULL", "C. UNIQUE", "D. FOREIGN KEY"],
        "answer": "B. NOT NULL",
        "explanation": "NOT NULL ensures every row must have a value for the column."
    },
    {
        "question": "True or False: A clustered index determines the physical order of rows in a table.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "Clustered indexes physically order table data according to the key."
    },
    {
        "question": "True or False: Normalization always improves query performance.",
        "choices": ["A. True", "B. False"],
        "answer": "B. False",
        "explanation": "Normalization reduces redundancy but can require joins, which may reduce performance."
    },
    {
        "question": "Which schedule allows transactions to execute concurrently without violating isolation?",
        "choices": ["A. Serializable schedule", "B. Non-serializable schedule", "C. Recoverable schedule", "D. Strict schedule"],
        "answer": "A. Serializable schedule",
        "explanation": "Serializable schedules produce the same result as some serial execution."
    },
    {
        "question": "True or False: In two-phase locking, a transaction must acquire all locks before releasing any.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "Two-phase locking ensures serializability with growing and shrinking phases."
    },
    {
        "question": "True or False: A fuzzy checkpoint allows updates during checkpoint creation to reduce system downtime.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "Fuzzy checkpoints don’t require the database to halt updates, improving performance."
    },
    {
        "question": "Which SQL constraint ensures uniqueness across multiple columns?",
        "choices": ["A. UNIQUE(column1)", "B. UNIQUE(column1, column2)", "C. PRIMARY KEY", "D. FOREIGN KEY"],
        "answer": "B. UNIQUE(column1, column2)",
        "explanation": "Composite UNIQUE constraints ensure no two rows share the same combination of values."
    },
    {
        "question": "True or False: Undo phase in recovery rolls back uncommitted transactions.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "Undo restores database to a consistent state by reversing incomplete transactions."
    },
    {
        "question": "Which SQL statement removes specific rows from a table based on a condition?",
        "choices": ["A. DELETE", "B. TRUNCATE", "C. DROP", "D. REMOVE"],
        "answer": "A. DELETE",
        "explanation": "DELETE removes rows matching the WHERE condition."
    },
    {
        "question": "Which SQL query lists students who have taken both course INF-1101 and INF-2700?",
        "choices": ["A. Using INTERSECT on two SELECTs", "B. Using UNION on two SELECTs", "C. Using JOIN", "D. Using WHERE IN for one course"],
        "answer": "A. Using INTERSECT on two SELECTs",
        "explanation": "INTERSECT returns only students present in both course queries."
    },
    {
        "question": "True or False: In relational algebra, the projection operation can remove duplicate tuples.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "Projection eliminates duplicate rows, returning a set of distinct tuples."
    },
    {
        "question": "Which type of index is ideal for range queries like BETWEEN or >, < comparisons?",
        "choices": ["A. Hash index", "B. B+-tree", "C. Bitmap index", "D. Clustered index"],
        "answer": "B. B+-tree",
        "explanation": "B+-trees allow efficient range searches by traversing leaf nodes sequentially."
    },
    {
        "question": "True or False: In 3NF, every non-prime attribute is non-transitively dependent on every key.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "3NF removes transitive dependencies to reduce redundancy."
    },
    {
        "question": "Which transaction anomaly occurs when two transactions update the same data simultaneously without isolation?",
        "choices": ["A. Dirty Read", "B. Lost Update", "C. Unrepeatable Read", "D. Phantom Read"],
        "answer": "B. Lost Update",
        "explanation": "A lost update happens when one transaction overwrites another transaction’s changes."
    },
    {
        "question": "True or False: A checkpoint allows the database to recover faster after a crash.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "Checkpoints reduce the amount of work during recovery by marking consistent states."
    },
    {
        "question": "Which SQL clause is used to group rows before applying aggregate functions?",
        "choices": ["A. WHERE", "B. HAVING", "C. GROUP BY", "D. ORDER BY"],
        "answer": "C. GROUP BY",
        "explanation": "GROUP BY groups rows for aggregation like COUNT, SUM, AVG."
    },
    {
        "question": "True or False: A foreign key must reference a primary key or a unique key in another table.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "Foreign keys enforce referential integrity by pointing to a unique row in another table."
    },
    {
        "question": "Which type of join would you use to include all students, even if they have not taken any courses?",
        "choices": ["A. Inner Join", "B. Left Outer Join", "C. Right Outer Join", "D. Cross Join"],
        "answer": "B. Left Outer Join",
        "explanation": "Left Outer Join includes all rows from the left table and matches from the right table if they exist."
    },
    {
        "question": "True or False: Undo phase in recovery must be performed before redo phase.",
        "choices": ["A. True", "B. False"],
        "answer": "B. False",
        "explanation": "Redo phase is applied first to ensure committed updates, then undo reverses uncommitted changes."
    },
    {
        "question": "Which normal form eliminates repeating groups?",
        "choices": ["A. 1NF", "B. 2NF", "C. 3NF", "D. BCNF"],
        "answer": "A. 1NF",
        "explanation": "1NF requires each attribute to hold atomic values, removing repeating groups."
    },
    {
        "question": "True or False: In a B+-tree, all records are stored at the leaf nodes.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "B+-tree leaves store all data records; internal nodes only store keys for navigation."
    },
    {
        "question": "Which SQL query finds the highest salary in each department?",
        "choices": ["A. SELECT MAX(salary) FROM Instructor", "B. SELECT dept, MAX(salary) FROM Instructor GROUP BY dept", "C. SELECT dept, salary FROM Instructor WHERE salary = MAX(salary)", "D. SELECT dept, salary FROM Instructor ORDER BY salary DESC"],
        "answer": "B. SELECT dept, MAX(salary) FROM Instructor GROUP BY dept",
        "explanation": "GROUP BY allows aggregation per department."
    },
    {
        "question": "True or False: A schedule is strict if a transaction can read or write uncommitted data from another transaction.",
        "choices": ["A. True", "B. False"],
        "answer": "B. False",
        "explanation": "Strict schedules prevent reading or writing uncommitted data."
    },
    {
        "question": "Which operation in relational algebra selects rows based on a condition?",
        "choices": ["A. Projection", "B. Selection", "C. Join", "D. Union"],
        "answer": "B. Selection",
        "explanation": "Selection (σ) filters tuples satisfying a given predicate."
    },
    {
        "question": "True or False: A dependency-preserving decomposition allows all functional dependencies to be enforced without joins.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "Dependency preservation ensures constraints can be checked on decomposed tables individually."
    },
    {
        "question": "True or False: Hash file organization is better for sequential range queries than B+-tree file organization.",
        "choices": ["A. True", "B. False"],
        "answer": "B. False",
        "explanation": "Hash organization is efficient for equality searches but poor for range queries."
    },
    {
        "question": "Which SQL construct retrieves rows from one table based on matching values in another table?",
        "choices": ["A. Subquery", "B. Join", "C. Index", "D. Aggregate function"],
        "answer": "B. Join",
        "explanation": "Joins combine tables based on a condition to retrieve related rows."
    },
    {
        "question": "True or False: Phantom reads occur when a transaction reads a different set of rows in repeated queries due to another transaction inserting or deleting rows.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "Phantom reads are caused by concurrent inserts or deletes affecting query results."
    },
    {
        "question": "Which SQL clause is used to filter rows before aggregation?",
        "choices": ["A. WHERE", "B. HAVING", "C. GROUP BY", "D. ORDER BY"],
        "answer": "A. WHERE",
        "explanation": "WHERE filters individual rows before aggregation, while HAVING filters groups after aggregation."
    },
    {
        "question": "True or False: In a B*-tree, nodes are more densely packed than in a B-tree, improving storage utilization.",
        "choices": ["A. True", "B. False"],
        "answer": "A. True",
        "explanation": "B*-trees split nodes differently to maintain 2/3 occupancy for better disk space usage."
    },
    {
        "question": "Which type of transaction schedule ensures serializability and strictness simultaneously?",
        "choices": ["A. Recoverable schedule", "B. Strict Two-phase Locking schedule", "C. Fuzzy checkpoint schedule", "D. Timestamp schedule"],
        "answer": "B. Strict Two-phase Locking schedule",
        "explanation": "Strict 2PL enforces serializability and prevents reading uncommitted data."
    },
    {
        "question": "What is the primary performance overhead of database systems in general?",
        "choices": [
            "A. Disk I/O operations",
            "B. CPU processing",
            "C. Network latency",
            "D. Memory allocation"
        ],
        "answer": "A. Disk I/O operations",
        "explanation": "The main performance bottleneck in databases is often the slow speed of disk I/O compared to memory and CPU."
    },
    {
        "question": "If the Product table is organized with a hash on pid, how is its data accessed?",
        "choices": [
            "A. Using sequential scan by pid order",
            "B. By computing a hash function on pid to locate data blocks",
            "C. By binary search on pid values",
            "D. By index range scan"
        ],
        "answer": "B. By computing a hash function on pid to locate data blocks",
        "explanation": "A hash organization stores records in buckets determined by a hash of the key, allowing fast equality lookups."
    },
    {
        "question": "What is the difference between a hash-organized file and a hash index?",
        "choices": [
            "A. A hash file stores data using hashing, while a hash index stores pointers to data",
            "B. A hash file is slower than a hash index",
            "C. Both store the same data structure",
            "D. A hash index requires a sorted file"
        ],
        "answer": "A. A hash file stores data using hashing, while a hash index stores pointers to data",
        "explanation": "A hash-organized file determines physical data placement; a hash index maps hash values to record locations."
    },
    {
        "question": "If the Order table is organized with a hash on cid and a hash index on pid, how is the pid index organized?",
        "choices": [
            "A. As a B+-tree index on pid",
            "B. As a hash structure using pid as key",
            "C. As a bitmap index",
            "D. As a sequential index"
        ],
        "answer": "B. As a hash structure using pid as key",
        "explanation": "A hash index on pid uses a hash function on pid to quickly locate matching records."
    },
    {
        "question": "What is a functional dependency X → Y in a relation?",
        "choices": [
            "A. X uniquely determines Y",
            "B. Y uniquely determines X",
            "C. X and Y are independent",
            "D. X and Y must have the same domain"
        ],
        "answer": "A. X uniquely determines Y",
        "explanation": "A functional dependency X → Y means that for each value of X, there is exactly one value of Y in the relation."
    },
    {
        "question": "What is Boyce-Codd Normal Form (BCNF)?",
        "choices": [
            "A. A relation where every determinant is a candidate key",
            "B. A relation without any foreign keys",
            "C. A relation with no NULL values",
            "D. A relation in 1NF and 2NF only"
        ],
        "answer": "A. A relation where every determinant is a candidate key",
        "explanation": "BCNF eliminates redundancy by ensuring that every determinant in a functional dependency is a candidate key."
    },
    {
        "question": "Given the relation R(A, B, C) with F = {A → C, B → C}, is R in BCNF?",
        "choices": [
            "A. Yes, because every attribute is functionally dependent on a key",
            "B. No, because neither A nor B is a candidate key but both determine C",
            "C. Yes, because it satisfies 3NF",
            "D. No, because it violates atomicity"
        ],
        "answer": "B. No, because neither A nor B is a candidate key but both determine C",
        "explanation": "BCNF requires all determinants to be candidate keys; here, A and B are not, so R violates BCNF."
    },
    {
        "question": "Why do we need BCNF?",
        "choices": [
            "A. To eliminate anomalies caused by partial and transitive dependencies",
            "B. To store more redundant data",
            "C. To increase query time",
            "D. To allow multi-valued attributes"
        ],
        "answer": "A. To eliminate anomalies caused by partial and transitive dependencies",
        "explanation": "BCNF removes redundancy and update anomalies that appear when non-key attributes determine other attributes."
    },
    {
        "question": "What problem may BCNF have?",
        "choices": [
            "A. It can sometimes lose dependency information during decomposition",
            "B. It allows redundancy",
            "C. It violates 1NF",
            "D. It prevents joins"
        ],
        "answer": "A. It can sometimes lose dependency information during decomposition",
        "explanation": "BCNF decomposition is not always dependency-preserving, meaning some constraints may be harder to enforce."
    },
    {
        "question": "What are ACID properties in transaction management?",
        "choices": [
            "A. Atomicity, Consistency, Isolation, Durability",
            "B. Access, Control, Integrity, Delay",
            "C. Action, Communication, Indexing, Durability",
            "D. None of the above"
        ],
        "answer": "A. Atomicity, Consistency, Isolation, Durability",
        "explanation": "ACID ensures reliable transaction processing through these four key properties."
    },
    {
        "question": "What is a log used for in transaction processing?",
        "choices": [
            "A. To record all changes made by transactions for recovery purposes",
            "B. To store query plans",
            "C. To manage indexes",
            "D. To handle concurrency control"
        ],
        "answer": "A. To record all changes made by transactions for recovery purposes",
        "explanation": "Logs maintain a history of updates to enable rollback or recovery after failures."
    },
    {
        "question": "What is the primary purpose of write-ahead logging (WAL)?",
        "choices": [
            "A. To write log records before database pages are updated",
            "B. To perform logging after writing data",
            "C. To optimize query performance",
            "D. To avoid using logs altogether"
        ],
        "answer": "A. To write log records before database pages are updated",
        "explanation": "WAL ensures durability and recoverability by logging changes before applying them to disk."
    },
    {
        "question": "Which types of log records are required to roll back a transaction while the database is running?",
        "choices": [
            "A. Before-image records",
            "B. After-image records",
            "C. Checkpoint records",
            "D. Commit records"
        ],
        "answer": "A. Before-image records",
        "explanation": "Before-images allow restoring data to its previous state when rolling back a transaction."
    },
    {
        "question": "What is the main performance cost of logging operations?",
        "choices": [
            "A. Disk I/O for writing log records",
            "B. CPU computation for generating log entries",
            "C. Memory allocation",
            "D. Lock contention"
        ],
        "answer": "A. Disk I/O for writing log records",
        "explanation": "Logging requires writing data to disk frequently to maintain durability, increasing I/O overhead."
    },
    {
        "question": "Which are the two main types of physical storage media, and what characterizes these?",
        "choices": [],
        "answer": "Magnetic (e.g., HDDs) and Solid-state (e.g., SSDs). Magnetic uses spinning disks, slower; SSD uses flash memory, faster.",
        "explanation": "Magnetic disks rely on moving parts; SSDs are electronic with no moving parts, making them faster."
    },
    {
        "question": "Mention at least four storage types, and organize them from slow to fast.",
        "choices": [],
        "answer": "Tape < HDD < SSD < RAM",
        "explanation": "Tape is the slowest archival medium, HDD slower than SSD, RAM is fastest volatile storage."
    },
    {
        "question": "Explain what is a RAID (Redundant Arrays of Independent Disk), and what are some characteristics of RAID?",
        "choices": [],
        "answer": "RAID combines multiple physical disks into one logical unit for redundancy or performance. Characteristics depend on RAID level (e.g., mirroring, striping, parity).",
        "explanation": "RAID provides fault tolerance and/or performance improvements depending on level (RAID 0,1,5, etc.)."
    },
    {
        "question": "Explain the ACID properties of a database transaction, illustrating their importance in maintaining data integrity.",
        "choices": [],
        "answer": "ACID = Atomicity, Consistency, Isolation, Durability. They ensure transactions are completed correctly, maintain consistent state, isolated from other operations, and survive crashes.",
        "explanation": "ACID prevents partial updates, ensures correct data, avoids interference between transactions, and guarantees persistence."
    },
    {
        "question": "Explain what a serializable transaction schedule is.",
        "choices": [],
        "answer": "A serializable schedule is one where the outcome is equivalent to some serial execution of the transactions.",
        "explanation": "Ensures no concurrency anomalies; transactions appear to execute one after another, even if interleaved."
    },
    # Task 3
    {
        "question": "What are the four basic steps of query processing? Name and explain each step.",
        "choices": [],
        "answer": "1. Parsing & Translation, 2. Optimization, 3. Execution Plan Generation, 4. Query Execution.",
        "explanation": "Parsing checks syntax, optimization finds efficient execution plan, execution plan generated, then query is executed to produce results."
    },
    {
        "question": "Given the relational schema Students(StudentID, Name, Residence, BirthYear, StudyProgram), find an equivalent expression of σBirthYear<2000(∏StudentID, Residence, StudyProgram, BirthYear (Students)).",
        "choices": [],
        "answer": "Select StudentID, Residence, StudyProgram, BirthYear from Students where BirthYear < 2000",
        "explanation": "Projection selects only some attributes, selection filters rows with BirthYear < 2000."
    },
    {
        "question": "Translate the relational algebra expression you found from question 3.2 into a SQL query.",
        "choices": [],
        "answer": "SELECT StudentID, Residence, StudyProgram, BirthYear FROM Students WHERE BirthYear < 2000;",
        "explanation": "Direct translation from relational algebra projection and selection to SQL SELECT and WHERE."
    },
    # Task 4
    {
        "question": "We are creating a database for a multiplayer video game. Add sensible attributes and determine primary keys for each entity: Players, Accounts, Characters, Items, Regions, Dungeons. Mark any derived attributes.",
        "choices": [],
        "answer": "Example: Players(PlayerID PK, Name), Accounts(AccountID PK, PlayerID FK), Characters(CharID PK, AccountID FK), Items(ItemID PK, CharID FK), Regions(RegionID PK), Dungeons(DungeonID PK, RegionID FK).",
        "explanation": "Primary keys uniquely identify entities; foreign keys represent ownership/relationships; derived attributes like 'Level' of character could be computed."
    },
    {
        "question": "Create a diagram connecting each of the entities with relationships (using correct verbs and cardinalities).",
        "choices": [],
        "answer": "Players 'has' Accounts (1-to-1), Accounts 'has' Characters (1-to-many), Characters 'carry' Items (1-to-many), Regions 'contain' Characters (1-to-many), Regions 'have' Dungeons (1-to-many).",
        "explanation": "This shows entity relationships with cardinality constraints."
    },
    {
        "question": "Convert the given inventory table to 1NF.",
        "choices": [],
        "answer": "Ensure each column contains atomic values, no multivalued attributes, add primary key, table unordered, datatypes consistent.",
        "explanation": "1NF requires atomicity and a unique primary key, no repeating groups."
    },
    # Task 5
    {
        "question": "Briefly describe two-phase locking (2PL). Difference between strict and rigorous 2PL and what these solve?",
        "choices": [],
        "answer": "2PL: growing phase (acquire locks), shrinking phase (release locks). Strict 2PL releases all locks at commit, rigorous 2PL at end of transaction. They prevent non-serializable schedules and cascading aborts.",
        "explanation": "Ensures serializability and avoids cascading rollbacks by controlling lock release timing."
    },
    {
        "question": "Suppose T participates in a deadlock and must be rolled back. Outline the procedure for log-based rollback.",
        "choices": [],
        "answer": "Undo all operations of T using transaction logs, restore database to previous consistent state, release locks held by T.",
        "explanation": "Logs allow recovery to maintain ACID properties after abort."
    },
    {
        "question": "In the ER (entity-relationship) model, what do we mean by weak entity types and existence dependence?",
        "choices": [],
        "answer": "A weak entity type cannot be uniquely identified by its own attributes alone and depends on a strong entity; existence dependence means it cannot exist without the strong entity.",
        "explanation": "Weak entities rely on a related strong entity for their identity, typically identified via a partial key combined with a foreign key from the strong entity."
    },
    {
        "question": "What is the purpose of normalization?",
        "choices": [],
        "answer": "To reduce redundancy and avoid anomalies in a database by organizing data into relations based on functional dependencies.",
        "explanation": "Normalization ensures data integrity, reduces duplicate data, and makes updates, inserts, and deletions less error-prone."
    },
    {
        "question": "What are the conditions for a relation to be in 3NF and BCNF?",
        "choices": [],
        "answer": "3NF: Every non-prime attribute is non-transitively dependent on every key. BCNF: Every determinant is a candidate key.",
        "explanation": "3NF removes transitive dependencies; BCNF further removes anomalies where non-candidate keys determine other attributes."
    },
    {
        "question": "Given the relation Flight(routeId, date, departureTime, arrivalTime, destination, seats, aircraftType, passengerCount) with FDs {routeId → departureTime, routeId → arrivalTime, routeId → destination, aircraftType → seats}, what normal form is it in and normalize if necessary?",
        "choices": [],
        "answer": "Not in BCNF because routeId → departureTime/arrivalTime/destination and aircraftType → seats, while routeId or aircraftType alone may not be candidate keys for the entire relation. Decompose into BCNF relations: Flight1(routeId, date, departureTime, arrivalTime, destination), Flight2(aircraftType, seats).",
        "explanation": "BCNF requires all determinants to be candidate keys. Decomposition removes anomalies caused by functional dependencies that violate BCNF."
    },
    {
        "question": "Describe how we organize a file for a database table with extensible hashing.",
        "choices": [],
        "answer": "Extensible hashing uses a directory of pointers to buckets that grow dynamically. The directory doubles when buckets overflow, minimizing collisions and redistributing records.",
        "explanation": "Extensible hashing allows dynamic expansion without reorganizing the entire file, supporting efficient insertions and lookups."
    },
    {
        "question": "Compare extensible hash with basic hash for the organization of a database table file.",
        "choices": [],
        "answer": "Basic hash uses fixed-size buckets, leading to overflow chains when collisions occur. Extensible hash dynamically adjusts directory and bucket sizes to avoid overflows.",
        "explanation": "Extensible hashing improves space utilization and performance compared to static hashing, especially for growing datasets."
    },
    {
        "question": "Sketch how People data are organized on disk with a hash file and provide a brief description.",
        "choices": [],
        "answer": "Data is organized into buckets based on a hash function applied to Pid. Each bucket contains records with the same hash value, and secondary hash indexes on Name point to the corresponding bucket entries.",
        "explanation": "Hash organization allows constant-time lookup by the primary attribute and efficient secondary index access."
    },
    {
        "question": "Sketch an execution plan for Query 6 (list of Ole's todo tasks) and describe the performance overhead.",
        "choices": [],
        "answer": "Execution plan: use secondary index on People.Name to find Ole's Pid, then use DoTask hash on Pid to fetch corresponding Task IDs, finally fetch tasks from Tasks table via Tid. Performance overhead includes multiple index lookups and hash table accesses, potentially requiring random I/O for each step.",
        "explanation": "Hash-based organization speeds up exact-match lookups but may require multiple disk accesses when combining tables."
    },
    {
        "question": "For the relation instance:\nA B C\nx 1 t\nx 2 t\ny 3 u\nz 4 u\nCheck if the following functional dependencies are satisfied: A → B, A → C, AB → C, AC → B.",
        "choices": [],
        "answer": "A → B: No, x maps to both 1 and 2. A → C: Yes, x maps to t consistently. AB → C: Yes, each AB pair uniquely determines C. AC → B: Yes, each AC pair uniquely determines B.",
        "explanation": "A functional dependency X → Y holds if every X value maps to exactly one Y value. Check each FD against all tuples."
    },
    {
        "question": "What is a decomposition of a relation schema?",
        "choices": [],
        "answer": "A decomposition is the process of splitting a relation schema into two or more schemas to remove redundancy or anomalies while preserving information.",
        "explanation": "Decomposition helps achieve normalization forms like 3NF or BCNF and reduces data anomalies."
    },
    {
        "question": "What is a lossless decomposition of a relation schema?",
        "choices": [],
        "answer": "A decomposition is lossless if the original relation can be perfectly reconstructed by joining the decomposed relations.",
        "explanation": "Lossless join ensures no data is lost when splitting tables."
    },
    {
        "question": "What is a dependency-preserving decomposition of a relation schema?",
        "choices": [],
        "answer": "A decomposition is dependency-preserving if all functional dependencies can be enforced on the decomposed schemas without computing joins.",
        "explanation": "This ensures constraints can be checked locally in each table."
    },
    {
        "question": "Describe a duplication elimination algorithm based on sorting for large tables.",
        "choices": [],
        "answer": "Sort the table on all columns, then scan sequentially and remove consecutive duplicate rows. If table is larger than memory, use external sorting (merge sort with disk-based runs).",
        "explanation": "Sorting brings duplicates together, allowing sequential removal; external sort handles memory constraints."
    },
    {
        "question": "Describe a duplication elimination algorithm based on hashing for large tables.",
        "choices": [],
        "answer": "Partition the table using a hash function into buckets that fit in memory, then remove duplicates within each bucket. Merge buckets if necessary.",
        "explanation": "Hashing distributes duplicates into the same bucket, allowing efficient in-memory deduplication without full sort."
    },
    {
        "question": "Compare the performance of sort-based and hash-based duplicate elimination.",
        "choices": [],
        "answer": "Sort-based: O(n log n) plus sequential scan, good if table can be sorted efficiently. Hash-based: O(n), good for large tables if enough buckets and memory exist. Sorting may require multiple disk passes for huge data, hashing depends on bucket distribution.",
        "explanation": "Hashing avoids global sorting but may suffer from bucket overflow; sorting ensures deterministic ordering but may be more I/O heavy."
    },
    {
        "question": "Describe the concept of a foreign key.",
        "choices": [],
        "answer": "A foreign key is an attribute in one table that refers to the primary key in another table, enforcing referential integrity.",
        "explanation": "Foreign keys ensure that relationships between tables are valid and prevent orphaned records."
    },
    {
        "question": "Explain how a transaction precedence graph is built and used to determine serializability.",
        "choices": [],
        "answer": "Nodes represent transactions; edges represent conflicts where one transaction must precede another due to read/write conflicts. If the graph has no cycles, the schedule is conflict-serializable.",
        "explanation": "The graph formalizes dependencies between transactions to check if the schedule can be rearranged into a serial order without violating conflicts."
    },
    {
        "question": "Describe the main fields of an update log record.",
        "choices": [],
        "answer": "Typical fields: Transaction ID, Data item, Old value, New value, Operation type (insert/update/delete), Timestamp.",
        "explanation": "Log records track all changes for recovery and rollback in case of transaction failure."
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


