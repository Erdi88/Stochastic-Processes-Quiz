import streamlit as st
import random

st.set_page_config(page_title="Database Systems Quiz 2025", layout="centered")

# -----------------------------
# QUESTIONS (same as before)
# -----------------------------
questions = [
    # SQL / Relational
    {
        "question": "Which SQL keyword is used to remove duplicate rows from a result?",
        "choices": ["A. DISTINCT", "B. UNIQUE", "C. CLEAN", "D. DEDUP"],
        "answer": "A. DISTINCT",
        "explanation": "DISTINCT removes duplicate rows from a query result."
    },
    {
        "question": "Which relational algebra operator combines rows from two relations?",
        "choices": ["A. Projection (π)", "B. Selection (σ)", "C. Join (⨝)"],
        "answer": "C. Join (⨝)",
        "explanation": "Join combines tuples from two relations based on a condition."
    },
    {
        "question": "In SQL, which clause specifies filtering conditions?",
        "choices": ["A. SELECT", "B. WHERE", "C. FROM", "D. GROUP BY"],
        "answer": "B. WHERE",
        "explanation": "The WHERE clause filters rows based on conditions."
    },
    {
        "question": "Which of the following is a candidate key?",
        "choices": [
            "A. A column that uniquely identifies a tuple",
            "B. A column with repeated values",
            "C. Any non-null column",
            "D. A derived column"
        ],
        "answer": "A. A column that uniquely identifies a tuple",
        "explanation": "Candidate keys uniquely identify each row and can become primary keys."
    },
    {
        "question": "True or False: A foreign key can contain NULL values.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Foreign keys can be NULL if the relationship is optional."
    },
    {
        "question": "Which SQL command removes a table completely?",
        "choices": ["A. DELETE", "B. REMOVE", "C. DROP", "D. CLEAR"],
        "answer": "C. DROP",
        "explanation": "DROP TABLE deletes the table structure and its data."
    },
    {
        "question": "Which relational algebra operator corresponds to SQL's SELECT clause?",
        "choices": ["A. Projection (π)", "B. Selection (σ)", "C. Join (⨝)"],
        "answer": "A. Projection (π)",
        "explanation": "Projection selects specific columns, similar to SQL's SELECT."
    },
    {
        "question": "In SQL, which function counts total rows?",
        "choices": ["A. SUM()", "B. COUNT()", "C. TOTAL()", "D. LENGTH()"],
        "answer": "B. COUNT()",
        "explanation": "COUNT() returns the number of rows matching the query."
    },
    {
        "question": "Which SQL clause groups rows with the same value?",
        "choices": ["A. HAVING", "B. GROUP BY", "C. ORDER BY", "D. UNION"],
        "answer": "B. GROUP BY",
        "explanation": "GROUP BY groups rows that share a common column value."
    },
    {
        "question": "True or False: The HAVING clause filters results after aggregation.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "WHERE filters before aggregation; HAVING filters after."
    },
    {
        "question": "What does normalization primarily prevent?",
        "choices": ["A. Data duplication", "B. Data loss", "C. Query optimization", "D. Index creation"],
        "answer": "A. Data duplication",
        "explanation": "Normalization reduces redundancy and improves consistency."
    },
    {
        "question": "Which normal form removes transitive dependencies?",
        "choices": ["A. 1NF", "B. 2NF", "C. 3NF", "D. BCNF"],
        "answer": "C. 3NF",
        "explanation": "Third Normal Form eliminates transitive dependencies."
    },
    {
        "question": "In BCNF, every determinant must be:",
        "choices": ["A. A foreign key", "B. A superkey", "C. A candidate key", "D. A composite key"],
        "answer": "B. A superkey",
        "explanation": "BCNF requires that every determinant is a superkey."
    },
    {
        "question": "True or False: BCNF is always stronger than 3NF.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "BCNF is a stricter version of 3NF."
    },
    {
        "question": "Which of these is a violation of 1NF?",
        "choices": [
            "A. Duplicate rows",
            "B. Multi-valued columns",
            "C. Missing primary key",
            "D. Unsorted table"
        ],
        "answer": "B. Multi-valued columns",
        "explanation": "1NF disallows multi-valued attributes."
    },
    {
        "question": "Which of the following defines a weak entity?",
        "choices": [
            "A. An entity that depends on another for identification",
            "B. An entity with a natural key",
            "C. An entity that has many attributes",
            "D. An independent entity"
        ],
        "answer": "A. An entity that depends on another for identification",
        "explanation": "Weak entities rely on a strong entity’s key for identification."
    },
    {
        "question": "Which key uniquely identifies rows in a table?",
        "choices": ["A. Primary key", "B. Foreign key", "C. Secondary key", "D. Super key only"],
        "answer": "A. Primary key",
        "explanation": "Primary keys uniquely identify each row."
    },
    {
        "question": "True or False: Every relation in 2NF is also in 1NF.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Higher normal forms include the lower ones by definition."
    },
    {
        "question": "Which operation in SQL merges results from two queries without duplicates?",
        "choices": ["A. UNION", "B. INTERSECT", "C. JOIN", "D. MERGE"],
        "answer": "A. UNION",
        "explanation": "UNION merges two query results and removes duplicates."
    },
    {
        "question": "Which indexing structure maintains sorted order of keys?",
        "choices": ["A. Hash index", "B. B+ tree", "C. Bitmap index", "D. Linear hashing"],
        "answer": "B. B+ tree",
        "explanation": "B+ trees keep keys sorted for efficient range queries."
    },
    {
        "question": "True or False: A hash index is ideal for range queries.",
        "choices": ["True", "False"],
        "answer": "False",
        "explanation": "Hash indexes excel at equality lookups, not ranges."
    },
    {
        "question": "What is the primary purpose of a database log?",
        "choices": ["A. Record of transactions", "B. Record of queries", "C. Backup file", "D. Index"],
        "answer": "A. Record of transactions",
        "explanation": "Logs record all changes for recovery and rollback."
    },
    {
        "question": "Which of the following is NOT an ACID property?",
        "choices": ["A. Atomicity", "B. Consistency", "C. Isolation", "D. Dependency"],
        "answer": "D. Dependency",
        "explanation": "Dependency is not part of the ACID properties."
    },
    {
        "question": "True or False: The 'A' in ACID stands for Atomicity.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Atomicity ensures transactions execute all-or-nothing."
    },
    {
        "question": "Which ACID property ensures the database remains valid after a crash?",
        "choices": ["A. Atomicity", "B. Consistency", "C. Durability", "D. Isolation"],
        "answer": "C. Durability",
        "explanation": "Durability guarantees committed transactions survive failures."
    },
    {
        "question": "True or False: Checkpoints in logs speed up recovery.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Checkpoints reduce the amount of log replay needed after crashes."
    },
    {
        "question": "What does 'write-ahead logging' ensure?",
        "choices": [
            "A. Logs are written after data pages",
            "B. Data is written before logs",
            "C. Log records are written before database changes",
            "D. Logs are skipped for fast transactions"
        ],
        "answer": "C. Log records are written before database changes",
        "explanation": "WAL guarantees recoverability by logging changes first."
    },
    {
        "question": "True or False: Two-phase locking can lead to deadlocks.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "2PL ensures serializability but may cause deadlocks."
    },
    {
        "question": "What distinguishes strict 2PL from basic 2PL?",
        "choices": [
            "A. Locks released after commit",
            "B. Locks released before commit",
            "C. No shared locks used",
            "D. No exclusive locks used"
        ],
        "answer": "A. Locks released after commit",
        "explanation": "Strict 2PL holds all locks until the transaction commits."
    },
    {
        "question": "In concurrency control, what is a deadlock?",
        "choices": [
            "A. Infinite waiting between transactions",
            "B. Data inconsistency",
            "C. Transaction commit error",
            "D. Lost update"
        ],
        "answer": "A. Infinite waiting between transactions",
        "explanation": "Deadlock occurs when transactions wait on each other’s locks indefinitely."
    },
    {
        "question": "True or False: A serializable schedule ensures the same result as some serial execution.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Serializable schedules maintain correctness equivalent to serial order."
    },
    {
        "question": "What is a RAID used for in databases?",
        "choices": [
            "A. Redundant disk storage for reliability and speed",
            "B. Backup scheduling",
            "C. Network optimization",
            "D. Query execution"
        ],
        "answer": "A. Redundant disk storage for reliability and speed",
        "explanation": "RAID combines disks to improve performance and fault tolerance."
    },
    {
        "question": "Which type of hash grows dynamically as data increases?",
        "choices": ["A. Static hash", "B. Extensible hash", "C. B+ tree", "D. Bitmap index"],
        "answer": "B. Extensible hash",
        "explanation": "Extensible hashing expands directories dynamically as data grows."
    },
    {
        "question": "True or False: A checkpoint clears all log entries.",
        "choices": ["True", "False"],
        "answer": "False",
        "explanation": "Checkpoints mark a recovery point but do not delete logs."
    },
    {
        "question": "Which SQL clause removes rows from a table?",
        "choices": ["A. DROP", "B. DELETE", "C. REMOVE", "D. ERASE"],
        "answer": "B. DELETE",
        "explanation": "DELETE removes specific rows while preserving the table structure."
    },
    {
        "question": "In relational algebra, what does σ (sigma) represent?",
        "choices": ["A. Selection", "B. Projection", "C. Join", "D. Union"],
        "answer": "A. Selection",
        "explanation": "σ filters rows satisfying a given condition."
    },
    {
        "question": "Which of these ensures transaction isolation?",
        "choices": [
            "A. Locking mechanisms",
            "B. Backup scheduling",
            "C. Replication",
            "D. Indexing"
        ],
        "answer": "A. Locking mechanisms",
        "explanation": "Locks prevent conflicting concurrent operations."
    },
    {
        "question": "True or False: Functional dependency X→Y means each X value determines exactly one Y value.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Functional dependency defines deterministic relationships between attributes."
    },
    {
        "question": "Which SQL command changes values in existing rows?",
        "choices": ["A. INSERT", "B. UPDATE", "C. MODIFY", "D. REPLACE"],
        "answer": "B. UPDATE",
        "explanation": "UPDATE modifies existing data within a table."
    },
    {
        "question": "Which relational operation removes duplicates between two relations?",
        "choices": ["A. UNION", "B. INTERSECT", "C. DIFFERENCE", "D. JOIN"],
        "answer": "C. DIFFERENCE",
        "explanation": "Set difference returns tuples in one relation but not in another."
    },
    {
        "question": "True or False: Primary keys can contain NULL values.",
        "choices": ["True", "False"],
        "answer": "False",
        "explanation": "Primary keys must be unique and non-NULL."
    },
    {
        "question": "Which SQL keyword sorts query results?",
        "choices": ["A. ORDER BY", "B. SORT", "C. GROUP BY", "D. ARRANGE"],
        "answer": "A. ORDER BY",
        "explanation": "ORDER BY sorts results in ascending or descending order."
    },
    {
        "question": "In 3NF, which dependencies are allowed?",
        "choices": [
            "A. Only full key dependencies",
            "B. Partial key dependencies",
            "C. Transitive dependencies",
            "D. Multi-valued dependencies"
        ],
        "answer": "A. Only full key dependencies",
        "explanation": "3NF allows dependencies on a key, not on non-key attributes."
    },
    {
        "question": "Which term describes storing redundant data to improve read speed?",
        "choices": ["A. Denormalization", "B. Normalization", "C. Replication", "D. Indexing"],
        "answer": "A. Denormalization",
        "explanation": "Denormalization introduces redundancy to speed up reads."
    },
    {
        "question": "True or False: Each relation in BCNF is also in 3NF.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "BCNF is stricter, so all BCNF tables satisfy 3NF."
    },
    {
        "question": "Which type of database entity depends on another entity for its existence?",
        "choices": ["A. Weak entity", "B. Strong entity", "C. Composite entity", "D. Independent entity"],
        "answer": "A. Weak entity",
        "explanation": "A weak entity cannot be uniquely identified without a related strong entity."
    },
    {
        "question": "True or False: Every table must have exactly one primary key.",
        "choices": ["True", "False"],
        "answer": "False",
        "explanation": "A table can have multiple candidate keys but only one primary key."
    },
    {
        "question": "Which SQL clause specifies which tables to retrieve data from?",
        "choices": ["A. SELECT", "B. FROM", "C. WHERE", "D. GROUP BY"],
        "answer": "B. FROM",
        "explanation": "FROM identifies the source tables for the query."
    },
    {
        "question": "Which SQL function calculates the average of a numeric column?",
        "choices": ["A. SUM()", "B. AVG()", "C. COUNT()", "D. MEAN()"],
        "answer": "B. AVG()",
        "explanation": "AVG() computes the mean value of a column."
    },
    {
        "question": "True or False: An index speeds up SELECT queries but slows down INSERT operations.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Indexes improve read performance but require updates on writes."
    },
    {
        "question": "Which SQL keyword limits the number of rows returned?",
        "choices": ["A. LIMIT", "B. TOP", "C. FETCH", "D. All of the above"],
        "answer": "D. All of the above",
        "explanation": "Different SQL dialects use LIMIT, TOP, or FETCH to restrict row counts."
    },
    {
        "question": "Which type of lock allows multiple transactions to read but not write?",
        "choices": ["A. Shared lock", "B. Exclusive lock", "C. Deadlock", "D. Optimistic lock"],
        "answer": "A. Shared lock",
        "explanation": "Shared locks permit concurrent reads but block writes."
    },
    {
        "question": "True or False: Extensible hashing allows the directory to grow dynamically.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Extensible hashing expands the directory to handle more data efficiently."
    },
    {
        "question": "Which database design principle reduces redundancy and improves integrity?",
        "choices": ["A. Normalization", "B. Denormalization", "C. Indexing", "D. Partitioning"],
        "answer": "A. Normalization",
        "explanation": "Normalization organizes data to reduce redundancy and maintain integrity."
    },
    {
        "question": "What is the main advantage of using a B+ tree index over a hash index?",
        "choices": [
            "A. Better for equality lookups",
            "B. Supports range queries efficiently",
            "C. Uses less memory",
            "D. Easier to implement"
        ],
        "answer": "B. Supports range queries efficiently",
        "explanation": "B+ trees maintain sorted order, enabling fast range searches."
    },
    {
        "question": "Which SQL statement inserts a new row into a table?",
        "choices": ["A. INSERT", "B. UPDATE", "C. DELETE", "D. MERGE"],
        "answer": "A. INSERT",
        "explanation": "INSERT adds new data into a table."
    },
    {
        "question": "True or False: A transaction must be atomic to satisfy ACID properties.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Atomicity ensures the transaction executes fully or not at all."
    },
    {
        "question": "Which SQL clause filters aggregated results?",
        "choices": ["A. WHERE", "B. HAVING", "C. GROUP BY", "D. SELECT"],
        "answer": "B. HAVING",
        "explanation": "HAVING filters groups after aggregation, unlike WHERE."
    },
    {
        "question": "True or False: A table in 2NF may still contain transitive dependencies.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "2NF removes partial dependencies but not transitive ones; 3NF addresses that."
    },
    {
        "question": "Which database concept ensures transactions appear isolated to each other?",
        "choices": ["A. Atomicity", "B. Consistency", "C. Isolation", "D. Durability"],
        "answer": "C. Isolation",
        "explanation": "Isolation prevents concurrent transactions from interfering with each other."
    },
    {
        "question": "Which SQL keyword combines results from two queries including duplicates?",
        "choices": ["A. UNION ALL", "B. UNION", "C. INTERSECT", "D. JOIN"],
        "answer": "A. UNION ALL",
        "explanation": "UNION ALL merges query results without removing duplicates."
    },
    {
        "question": "True or False: Denormalization can improve query performance by adding redundancy.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Denormalization introduces redundancy to reduce complex joins and speed reads."
    },
    {
        "question": "Which ACID property ensures that transactions do not leave the database in an invalid state?",
        "choices": ["A. Atomicity", "B. Consistency", "C. Isolation", "D. Durability"],
        "answer": "B. Consistency",
        "explanation": "Consistency ensures all rules and constraints are preserved after a transaction."
    },
    {
        "question": "True or False: A foreign key can reference a column that is not unique.",
        "choices": ["True", "False"],
        "answer": "False",
        "explanation": "Foreign keys must reference unique or primary key columns."
    },
    {
        "question": "Which SQL operation modifies existing data in a table?",
        "choices": ["A. INSERT", "B. UPDATE", "C. DELETE", "D. MERGE"],
        "answer": "B. UPDATE",
        "explanation": "UPDATE changes values of existing rows."
    },
    {
        "question": "Which relational algebra operator removes rows that satisfy a condition?",
        "choices": ["A. Selection (σ)", "B. Projection (π)", "C. Difference (-)", "D. Join (⨝)"],
        "answer": "A. Selection (σ)",
        "explanation": "Selection filters tuples based on a condition."
    },
    {
        "question": "True or False: Composite keys consist of multiple attributes combined to form a unique key.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Composite keys use multiple columns to uniquely identify a row."
    },
    {
        "question": "Which SQL clause specifies the order of rows in a query result?",
        "choices": ["A. ORDER BY", "B. GROUP BY", "C. WHERE", "D. SORT"],
        "answer": "A. ORDER BY",
        "explanation": "ORDER BY sorts results by one or more columns."
    },
    {
        "question": "True or False: Checkpoints in logging allow partial recovery without replaying the entire log.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Checkpoints reduce recovery time by marking a stable state."
    },
    {
        "question": "Which SQL clause is used to combine two tables based on a common column?",
        "choices": ["A. JOIN", "B. UNION", "C. INTERSECT", "D. MERGE"],
        "answer": "A. JOIN",
        "explanation": "JOIN combines rows from two tables based on a matching column."
    },
    {
        "question": "True or False: Primary keys can be composite, consisting of more than one column.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Composite primary keys use multiple attributes to ensure uniqueness."
    },
    {
        "question": "Which operation in hashing ensures direct lookup by key?",
        "choices": ["A. Linear search", "B. Hash function", "C. Binary search", "D. B+ tree traversal"],
        "answer": "B. Hash function",
        "explanation": "Hash functions compute the storage location for direct access."
    },
    {
        "question": "Which SQL statement removes specific rows but keeps the table structure?",
        "choices": ["A. DELETE", "B. DROP", "C. TRUNCATE", "D. REMOVE"],
        "answer": "A. DELETE",
        "explanation": "DELETE deletes rows while leaving the table intact."
    },
    {
        "question": "True or False: Every functional dependency X→Y means each X maps to exactly one Y in a relation instance.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Functional dependency defines a deterministic mapping from X to Y."
    },
    {
        "question": "Which SQL clause filters rows before aggregation?",
        "choices": ["A. WHERE", "B. HAVING", "C. GROUP BY", "D. ORDER BY"],
        "answer": "A. WHERE",
        "explanation": "WHERE filters rows before applying aggregate functions."
    },
    {
        "question": "Which ER relationship describes a one-to-many connection?",
        "choices": ["A. One-to-One", "B. One-to-Many", "C. Many-to-Many", "D. Weak-to-Strong"],
        "answer": "B. One-to-Many",
        "explanation": "One-to-many relationships allow one entity to relate to multiple entities in another set."
    },
    {
        "question": "True or False: An entity with no unique identifier is always a weak entity.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Weak entities cannot be uniquely identified without a strong entity key."
    },
    {
        "question": "Which SQL operator selects rows that satisfy multiple conditions?",
        "choices": ["A. AND", "B. OR", "C. NOT", "D. XOR"],
        "answer": "A. AND",
        "explanation": "AND combines conditions and returns only rows where all are true."
    },
    {
        "question": "Which SQL operator selects rows that satisfy at least one condition?",
        "choices": ["A. AND", "B. OR", "C. NOT", "D. XOR"],
        "answer": "B. OR",
        "explanation": "OR returns rows where at least one of the conditions is true."
    },
    {
        "question": "True or False: UNION removes duplicate rows by default.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "UNION merges two queries and eliminates duplicates automatically."
    },
    {
        "question": "Which relational algebra operator is used to combine all attributes from two relations, including all rows?",
        "choices": ["A. Join", "B. Cartesian product (×)", "C. Intersection (∩)", "D. Difference (-)"],
        "answer": "B. Cartesian product (×)",
        "explanation": "Cartesian product returns all possible combinations of tuples from two relations."
    },
    {
        "question": "True or False: Selection (σ) in relational algebra reduces the number of rows.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Selection filters tuples based on a condition, reducing row count."
    },
    {
        "question": "True or False: Projection (π) can reduce the number of columns in a relation.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Projection selects specific columns, removing others."
    },
    {
        "question": "Which SQL keyword returns only rows that match values in another table?",
        "choices": ["A. JOIN", "B. INTERSECT", "C. IN", "D. EXISTS"],
        "answer": "C. IN",
        "explanation": "IN checks if a column value exists in a set of values from another table."
    },
    {
        "question": "Which SQL clause checks conditions after grouping?",
        "choices": ["A. WHERE", "B. HAVING", "C. GROUP BY", "D. ORDER BY"],
        "answer": "B. HAVING",
        "explanation": "HAVING filters grouped results, unlike WHERE which filters before aggregation."
    },
    {
        "question": "True or False: In 1NF, multivalued attributes are allowed.",
        "choices": ["True", "False"],
        "answer": "False",
        "explanation": "1NF disallows multivalued attributes to ensure atomicity of columns."
    },
    {
        "question": "Which type of key can uniquely identify a row but is not the primary key?",
        "choices": ["A. Candidate key", "B. Foreign key", "C. Composite key", "D. Secondary key"],
        "answer": "A. Candidate key",
        "explanation": "Candidate keys are potential primary keys and uniquely identify tuples."
    },
    {
        "question": "True or False: Every foreign key must reference a primary or unique key in another table.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Foreign keys ensure referential integrity by referencing unique columns."
    },
    {
        "question": "Which type of RAID improves fault tolerance by storing parity information?",
        "choices": ["A. RAID 0", "B. RAID 1", "C. RAID 5", "D. RAID 10"],
        "answer": "C. RAID 5",
        "explanation": "RAID 5 uses distributed parity for fault tolerance and allows recovery from a single disk failure."
    },
    {
        "question": "Which file organization method uses a hash function for direct record access?",
        "choices": ["A. Sequential", "B. Heap", "C. Hash", "D. Indexed sequential"],
        "answer": "C. Hash",
        "explanation": "Hashing maps a key directly to a storage location for quick access."
    },
    {
        "question": "True or False: B+ tree indexes are more efficient than hash indexes for range queries.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "B+ trees maintain order, supporting efficient range searches."
    },
    {
        "question": "Which transaction property ensures all-or-nothing execution?",
        "choices": ["A. Atomicity", "B. Consistency", "C. Isolation", "D. Durability"],
        "answer": "A. Atomicity",
        "explanation": "Atomicity guarantees that either all operations of a transaction are executed or none are."
    },
    {
        "question": "Which transaction property ensures that concurrent transactions do not interfere?",
        "choices": ["A. Atomicity", "B. Consistency", "C. Isolation", "D. Durability"],
        "answer": "C. Isolation",
        "explanation": "Isolation ensures transactions behave as if executed serially."
    },
    {
        "question": "True or False: Durability guarantees that committed transactions survive system crashes.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Durability ensures permanent storage of committed changes."
    },
    {
        "question": "Which log technique writes the log before writing the data to the database?",
        "choices": ["A. Post-write logging", "B. Write-ahead logging (WAL)", "C. Lazy logging", "D. Delayed logging"],
        "answer": "B. Write-ahead logging (WAL)",
        "explanation": "WAL ensures changes can be recovered after a crash by logging first."
    },
    {
        "question": "Which database operation is used to undo changes of a transaction?",
        "choices": ["A. Rollback", "B. Commit", "C. Checkpoint", "D. Flush"],
        "answer": "A. Rollback",
        "explanation": "Rollback restores the database to the state before the transaction."
    },
    {
        "question": "True or False: Two-phase locking can prevent lost updates but may cause deadlocks.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "2PL ensures serializability but can lead to deadlock if not managed carefully."
    },
    {
        "question": "Which type of lock allows multiple readers but no writers?",
        "choices": ["A. Exclusive lock", "B. Shared lock", "C. Update lock", "D. Deadlock lock"],
        "answer": "B. Shared lock",
        "explanation": "Shared locks allow concurrent reads but block writes."
    },
    {
        "question": "Which SQL clause is used to combine tables based on matching column values?",
        "choices": ["A. JOIN", "B. UNION", "C. INTERSECT", "D. MERGE"],
        "answer": "A. JOIN",
        "explanation": "JOIN combines rows from two tables when column values match."
    },
    {
        "question": "True or False: Extensible hashing automatically adjusts the directory as more buckets are needed.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Extensible hashing grows dynamically to handle more data without collisions."
    },
    {
        "question": "Which normalization step eliminates partial dependencies?",
        "choices": ["A. 1NF", "B. 2NF", "C. 3NF", "D. BCNF"],
        "answer": "B. 2NF",
        "explanation": "2NF removes partial dependencies on a portion of the primary key."
    },
    {
        "question": "Which normalization step removes transitive dependencies?",
        "choices": ["A. 1NF", "B. 2NF", "C. 3NF", "D. BCNF"],
        "answer": "C. 3NF",
        "explanation": "3NF eliminates dependencies where non-key attributes depend on other non-key attributes."
    },
    {
        "question": "True or False: BCNF requires that every determinant is a superkey.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "BCNF eliminates all anomalies caused by functional dependencies not based on superkeys."
    },
    {
        "question": "Which SQL statement creates a new table?",
        "choices": ["A. CREATE TABLE", "B. INSERT", "C. UPDATE", "D. ALTER TABLE"],
        "answer": "A. CREATE TABLE",
        "explanation": "CREATE TABLE defines a new table structure in the database."
    },
    {
        "question": "True or False: An index always speeds up all types of queries.",
        "choices": ["True", "False"],
        "answer": "False",
        "explanation": "Indexes improve reads but can slow down inserts, updates, and deletes."
    },
    {
        "question": "Which database object stores multiple rows with the same schema?",
        "choices": ["A. Table", "B. View", "C. Index", "D. Sequence"],
        "answer": "A. Table",
        "explanation": "Tables store tuples with the same attributes in relational databases."
    },
    {
        "question": "Which SQL function returns the largest value in a column?",
        "choices": ["A. MIN()", "B. MAX()", "C. COUNT()", "D. SUM()"],
        "answer": "B. MAX()",
        "explanation": "MAX() returns the highest value in a column."
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
