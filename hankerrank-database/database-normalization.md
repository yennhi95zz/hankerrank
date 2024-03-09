# HANKERRANK - DATABASE NORMALIZATION


![Author](https://img.shields.io/badge/Author-Nhi%20Yen-brightgreen)
[![Medium](https://img.shields.io/badge/Medium-Follow%20Me-blue)](https://medium.com/@yennhi95zz/subscribe)
[![GitHub](https://img.shields.io/badge/GitHub-Follow%20Me-lightgrey)](https://github.com/yennhi95zz)
[![Kaggle](https://img.shields.io/badge/Kaggle-Follow%20Me-orange)](https://www.kaggle.com/nhiyen/code)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect%20with%20Me-informational)](https://www.linkedin.com/in/yennhi95zz/)


## I. What is Database Normalization?
Database normalization is a process in database design that aims to organize data in a way that minimizes redundancy and dependency. The primary goal is to create a well-structured database that ensures data integrity, reduces data anomalies, and supports efficient data retrieval and maintenance.

The process of normalization involves breaking down a large table into smaller, related tables and defining relationships between them. This is achieved through a set of rules or normal forms, each addressing specific issues related to data redundancy and dependency. The most commonly used normal forms are the first normal form (1NF), second normal form (2NF), and third normal form (3NF). There are higher normal forms like Boyce-Codd Normal Form (BCNF) and Fourth Normal Form (4NF) that address more complex scenarios.

This [YouTube video](https://www.youtube.com/watch?v=GFQaEYEc8_8) is suggested for a complete explanation.

Here's a brief explanation of the first three normal forms:

### 1. First Normal Form (1NF):

![Alt text](<images/Database normalization-1NF.png>)

- Ensures that each column contains atomic (indivisible) values, and there are no repeating groups or arrays.
- Eliminates duplicate rows by ensuring that each row is uniquely identified.

### 2. Second Normal Form (2NF):

![Alt text](<images/Database normalization-2NF.png>)

- Builds on 1NF by eliminating partial dependencies.
- Requires that all non-key attributes are fully functionally dependent on the entire primary key.
- In simpler terms, every non-key attribute must depend on the entire primary key, not just a part of it.

### 3. Third Normal Form (3NF):

![Alt text](<images/Database normalization-3NF.png>)

- Builds on 2NF by eliminating transitive dependencies.
- Ensures that no transitive dependencies exist in the table, where a non-key attribute is dependent on another non-key attribute.
- Non-key attributes should only depend on the primary key.

Normalization helps in several ways:

- Reduces Redundancy: By breaking down tables and organizing data efficiently, redundancy is minimized, leading to a more compact and manageable database.

- Improves Data Integrity: By eliminating anomalies, such as insertion, update, and deletion anomalies, data integrity is maintained.

- Facilitates Querying: With well-structured tables and relationships, querying the database becomes more straightforward and efficient.

- Simplifies Maintenance: Changes and updates to the database structure are easier to implement and less error-prone.

However, it's important to note that normalization is not a one-size-fits-all solution. Over-normalization can lead to complex queries and reduced performance. Therefore, the level of normalization applied depends on the specific requirements and use cases of the database.

## II. Quiz

### Question 1: 
The following unnormalized table named PRODUCT is transformed to first normal form (1NF) by splitting it into two tables which have X and Y rows (such that X <Y) respectively. Both the tables have Z columns.

```
*Product-ID*    *Colors*    *Price* 
1               Red,Green   15.0
2               Blue        18.0
3               Yellow,Pink 2.5
```

What are the values of X, Y, Z? Enter these integers, each on a new line, in the text-box below. Do not leave any leading or trailing spaces.

**ANSWER:** 3 5 2

**EXPLANATION:**

Table 1: product
```
*Product-ID*    *Price* 
1               15.0
2               18.0
3               2.5
```

Table 2: color
```
*Product-ID*    *Color* 
1               Red
1               Green
2               Blue
3               Yellow
3               Pink
```

### Question 2: 
A particular database is normalized to satisfy a particular level of normalization (either 1NF or 2NF or 3NF). One of the tables contains, among other fields, a column for the **City** and a column for the **Zip Code**. Assuming that there is a **many-to-one** mapping between the set of **Zip Code(s)** and **City**, we may conclude that the database is definitely **NOT** in **NF** form. What is the integer x (1, 2, or 3)? Fill your answer in the text box below.

**ANSWER:** 3

**EXPLANATION:**

The given scenario suggests that there is a many-to-one mapping between the set of Zip Code(s) and City in the table, which implies a functional dependency. To be in the 3rd Normal Form (3NF), the table must already be in 2nd Normal Form (2NF) and should not have any transitive dependencies.

If there is a many-to-one mapping between Zip Code and City, it means that Zip Code functionally determines City. In 2NF, the table would need to have no partial dependencies, and in 3NF, there should be no transitive dependencies. In this case, Zip Code determining City seems like a transitive dependency.

Therefore, the database is not in 3NF. So, the integer x is 3.

**Example:**

Assume we have a table called `Locations`:
```
Zip Code	City	State
12345	Exampleville	StateA
54321	Sampletown	StateB
67890	Anothercity	StateA
```

In this example, Zip Code determines City (many-to-one mapping), and City depends on State. Therefore, there is a transitive dependency: `Zip Code → City → State`.

To bring the table to 3NF, we can decompose it into two tables:

Table `ZipCodes`:
```
Zip Code	City
12345	Exampleville
54321	Sampletown
67890	Anothercity
```
Table `Cities`:
```
City	State
Exampleville	StateA
Sampletown	StateB
Anothercity	StateA
```

Now, there are no transitive dependencies in each table. The `ZipCodes` table is in 2NF as it has a single-column primary key, and both tables are in 3NF.

This example demonstrates how the initial table was not in 3NF due to a transitive dependency, and by decomposing it, we achieve 3NF.

### Question 3: 

A database used by a college’s application stores the relationship between students and the courses they are enrolled in. We have information for each STUDENT (such as name, date of birth, date of enrollment, student-id) and COURSE (course code, instructor, etc.). In real life, a student takes several courses simultaneously while a subject is studied by several students. We need to capture this many-to-many relationship in our database. From the above information, what is the minimum number of tables required to structure this database in accordance with the rules of 2NF normalization?

**ANSWER:** 3

**EXPLANATION:**

STUDENT table:

| student_id | name         | date_of_birth | date_of_enrollment |
|------------|--------------|----------------|--------------------|
| 1          | John Doe      | 1990-05-15     | 2022-01-01         |
| 2          | Jane Smith    | 1992-08-22     | 2022-02-15         |

COURSE table:

| course_code | instructor    | other_course_details |
|-------------|---------------|-----------------------|
| CS101       | Prof. Johnson | Intro to Computer Sci |
| MATH202     | Prof. Smith   | Advanced Mathematics  |

ENROLLMENT table:

| student_id | course_code | enrollment_date |
|------------|-------------|------------------|
| 1          | CS101       | 2022-01-05       |
| 1          | MATH202     | 2022-01-05       |
| 2          | CS101       | 2022-02-20       |

### Question 4: 

A database, normalized as per 2NF rules, has been split into 10 tables. Each of the tables has exactly two columns: one key attribute and one non-key attribute. What is the minimum number of tables required to express this database in 3NF form? Enter the integer in the text box below. Do not leave any leading or trailing spaces.

**ANSWER:** 10

**EXPLANATION:**

To achieve 3NF (Third Normal Form), the database should meet the following criteria:

- It should already be in 2NF.
- No non-prime attribute should be transitively dependent on any superkey.

Given that each table has exactly two columns (one key attribute and one non-key attribute), and the database is already in 2NF, it implies that each non-key attribute is functionally dependent on the whole key.

To transition to 3NF, we need to ensure that there are no transitive dependencies where a non-prime attribute depends on another non-prime attribute via a prime attribute.

Since each table only has one non-key attribute, there can be no transitive dependencies.

Therefore, the minimum number of tables required to express the database in 3NF form is the same as the number of tables in 2NF, which is 10.

### Question 5: 

Consider the following relation and determinants.

R(a, b,c,d)
```
            a,c -> b,d
            a,d -> b
Also, a,b is a primary key for the above relation.
```


The above relation is in x NF form where x may take the following values {1,2,3,3.5} corresponding to {1NF, 2NF, 3NF and BCNF} respectively.
What is the maximum possible value of x such that the above relation satisfies the *x*NF form?
Your answer should only be restricted to one of these numbers:1/2/3/3.5 Do not leave any leading or trailing spaces.

**ANSWER:** 3

**EXPLANATION:**

To determine the highest normal form (NF) satisfied by the relation, we can analyze the functional dependencies.

- **1NF (First Normal Form):** The relation is already in 1NF because it has a well-defined primary key, and each attribute contains atomic values.

- **2NF (Second Normal Form):** To be in 2NF, there should be no partial dependency of any column on the primary key. Looking at the given functional dependencies, it appears that there might be a partial dependency on the primary key a, b. However, since both functional dependencies have a as part of the key, there is no partial dependency. Therefore, the relation is in 2NF.

- **3NF (Third Normal Form):** To be in 3NF, there should be no transitive dependency of non-prime attributes on the primary key. In this case, both functional dependencies are already in a form where there are no transitive dependencies. Therefore, the relation is in 3NF.

- **BCNF (Boyce-Codd Normal Form):** To be in BCNF, there should be no non-trivial functional dependencies where the determinant is not a superkey. In this case, the determinant a, d -> b violates BCNF because {a, d} is not a superkey. Therefore, the relation is not in BCNF.

So, the highest normal form satisfied by the given relation is 3NF. The answer is 3.

**Example:**

Let's create a sample relation instance:

```
a	b	c	d
1	2	3	4
2	3	4	5
3	4	5	6
```
In this instance:

*(a,c)→(b,d)*
- (1,3)→(2,4)
- (2,4)→(3,5)
- (3,5)→(4,6)

*(a,d)→b*
- (1,4)→2
- (2,5)→3
- (3,6)→4

This relation is in 3NF because there are no transitive dependencies of non-prime attributes on the primary key. Both b and d depend directly on the primary key 
`(a,c)` and `(a,d)`, respectively.

However, the relation fails to satisfy BCNF due to the functional dependency `a,d→b`. In the third row, a=3 and d=6, and (3,6)→4. This implies that b is determined by a non-superkey attribute `(a,d)`, violating the BCNF.

Hence, the relation is in 3NF but not in BCNF, as claimed. The maximum possible value of x such that the relation satisfies the *x*NF form is 3.

### Question 6: 

Let us take the example of a simple movie library. Each movie has a description, director, and serial number. Customers have a name, address, and membership number. Assume only one copy of each movie exists in the library. We are given the following relations and determinants. The keys for each relation are CAPITALIZED.
```
Relations (The key is CAPITALIZED):
customer(name,addr,MEMBERNO)
movie(DESCRIPTION,director,serialno)
borrow(memberno,DATE,SERIALNO)

Determinants:
description->director,serialno
serialno->description
serialno->director
name,addr -> memberno
memberno -> name,addr
serialno,date -> memberno
```
The above relation is in x**NF form where x may take the following values {1,2,3,3.5} corresponding to {1NF, 2NF, 3NF and BCNF} respectively.
What is the maximum possible value of **x such that the above relation satisfies the *x*NF form?
Your answer should only be restricted to one of these numbers:1/2/3/3.5 Do not leave any leading or trailing spaces.

**ANSWER:** 2

**EXPLANATION:**

Let's reevaluate the given information:
1. The `movie` relation has attributes (DESCRIPTION, director, serialno).
2. The `borrow` relation has attributes (memberno, DATE, SERIALNO).
3. The `customer` relation has attributes (name, addr, MEMBERNO).

Now, let's look at the determinants:

- `description -> director, serialno`: This indicates a partial dependency of director and serialno on the attribute description.
- `serialno -> description`: This suggests a transitive dependency where the description depends on the serial number.
- `serialno -> director`: Similar to the above, there is a transitive dependency of director on serialno.
- `name, addr -> memberno`: This indicates a composite key for the customer relation.
- `memberno -> name, addr`: This suggests a functional dependency of name and addr on memberno.
- `serialno, date -> memberno`: There is a dependency of memberno on a composite key of serialno and date.

Based on these determinants, it appears that there are transitive dependencies and partial dependencies present in the schema. Therefore, the schema is not in 3NF. However, it can be decomposed into 2NF to eliminate these issues.

The correct answer is 2 (Second Normal Form). 

### Question 7: 

Let us take the example of a simple movie library. Each movie has a description, director, and serial number. Customers have a name, address, and membership number. Assume only one copy of each movie exists in the library. We are given the following relations and determinants:
```
Relations:
movie(DESCRIPTION,serialno)
serial(SERIALNO,director)
customer(name,addr,MEMBERNO)
borrow(memberno,DATE,SERIALNO)

Determinants:
description->director,serialno
serialno->description
serialno->director
name,addr -> memberno
memberno -> name,addr
serialno,date -> memberno

```
The above relation is in x**NF form where x may take the following values {1,2,3,3.5} corresponding to {1NF, 2NF, 3NF and BCNF} respectively.
What is the maximum possible value of **x such that the above relation satisfies the *x*NF form?
Your answer should only be restricted to one of these numbers:1/2/3/3.5 Do not leave any leading or trailing spaces.

**ANSWER:** 3.5 (BCNF)

**EXPLANATION:**

Let's reassess the given relations and determinants:

1. The `movie` relation has attributes (DESCRIPTION, serialno).
2. The `serial` relation has attributes (SERIALNO, director).
3. The `customer` relation has attributes (name, addr, MEMBERNO).
4. The `borrow` relation has attributes (memberno, DATE, SERIALNO).

Now, considering the determinants:

- `description -> director, serialno`: This suggests a dependency of director and serialno on the attribute description.
- `serialno -> description`: There is a dependency of description on serialno.
- `serialno -> director`: There is a dependency of director on serialno.
- `name, addr -> memberno`: This indicates a composite key for the customer relation.
- `memberno -> name, addr`: This suggests a functional dependency of name and addr on memberno.
- `serialno, date -> memberno`: There is a dependency of memberno on a composite key of serialno and date.

The schema appears to be in 3NF as there are no transitive dependencies or partial dependencies. However, it is not in BCNF since the determinant `serialno, date -> memberno` does not satisfy the criteria for BCNF since the candidate key `(serialno, date)` is sufficient to determine `memberno`, and there are no non-trivial dependencies on part of the candidate key.

Therefore, the maximum possible value for xNF is 3.5 (BCNF).


### Question 8: 

Let us take the example of a simple movie library. Each movie has a description, director, and serial number. Customers have a name, address, and membership number. Assume only one copy of each movie exists in the library. We are given the following relations and determinants. The keys for each relation are CAPITALIZED.

```
Relations (The key is CAPITALIZED):
customer(name,addr,MEMBERNO)
movie(DESCRIPTION,director,serialno)
borrow(memberno,DATE,SERIALNO)
```
Which of these determinants is a NON-KEY dependency? In the text box, only enter the index number (1-6) of the dependency which you have identified as non-key.

```
1.  description->director,serialno
2.  serialno->description
3.  serialno->director
4.  name,addr -> memberno
5.  memberno -> name,addr
6.  serialno,date -> memberno
```
Output Format

In the text box, only enter the index number (1-6) of the dependency which you have identified as non-key.

**ANSWER:** 3

**EXPLANATION:**

Let's analyze each determinant:

- `description->director,serialno`: This determinant involves the primary key (serialno) and is a key dependency.

- `serialno->description`: This determinant involves the primary key (serialno) and is a key dependency.

- `serialno->director`: This determinant involves the primary key (serialno), but it is not a superkey since it does not uniquely determine all other attributes in the relation. Therefore, it is a non-key dependency.

- `name,addr -> memberno`: This determinant involves the primary key (memberno) and is a key dependency.

- `memberno -> name,addr`: This determinant involves the primary key (memberno) and is a key dependency.

- `serialno,date -> memberno`: This determinant involves the primary key (memberno) and is a key dependency.

In summary, determinant 3 (serialno->director) is a non-key dependency as it does not form a superkey for the relation.


### Question 9: 

Consider the following relation and determinants. The key(s) are bolded.
R(**a, b** ,c,d,e)

Which of these determinants is a NON-CANDIDATE key? In the text box, only enter the index number (1-3) of the dependency which you have identified as non-key.

```
a,c -> b,d,e
a,d -> b
a,c,e -> b,d
```

**ANSWER:** 2

**EXPLANATION:**

**What are superkey, candidate key, and non-candidate key?**

1. Superkey:

- A superkey is a set of one or more attributes that, taken collectively, can uniquely identify a tuple (row) in a relation (table).
- In other words, a superkey has the property that no two distinct tuples in the relation will have the same combination of values for the attributes in the superkey.
- A superkey may contain more attributes than necessary to uniquely identify a tuple.

Example:

- Consider a relation "`Student`" with attributes `{Student_ID, Name, Email, Phone}`. The set `{Student_ID, Email}` is a superkey because it uniquely identifies each student.

2. Candidate Key:

- A candidate key is a minimal superkey, meaning it is a superkey with no unnecessary attributes. Removing any attribute from a candidate key would cause it to lose its uniqueness property.
- In a relation, there can be multiple candidate keys.

Example:

- In the "`Student`" relation, both `{Student_ID}` and `{Email}` are candidate keys because each uniquely identifies a student, and removing any attribute from them would result in a loss of uniqueness.

3. Non-Candidate Key:

- A non-candidate key is any superkey that is not a candidate key. It may contain extra attributes that are not required for unique identification.

Example:

- If we consider the superkey `{Student_ID, Email, Phone}` for the "`Student`" relation, it is a non-candidate key because it contains more attributes than necessary to uniquely identify a student. `{Student_ID}` and `{Email}` are the candidate keys in this case.

In summary:

- A superkey is any set of attributes that uniquely identifies a tuple.
- A candidate key is a minimal superkey, and a relation can have multiple candidate keys.
- A non-candidate key is any superkey that is not a candidate key because it contains unnecessary attributes.

----------

For the question above, To identify the non-candidate key, let's analyze each determinant:
- `a,c→b,d,e`: This determinant seems to suggest that the combination of attributes `a` and `c` uniquely determines attributes `b, d, and e`. Since `a and c` together can determine all the other attributes, it indicates a candidate key or part of a candidate key.

- `a,d→b`: This determinant suggests that the combination of attributes `a and d` uniquely determines attribute b. Since it's not the full set of attributes, 
`a,d` could potentially be a candidate key. However, since it's not a full superkey (it doesn't determine all the other attributes), it's a non-candidate key.
- `a,c,e→b,d`: This determinant suggests that the combination of attributes `a, c, and e` uniquely determines attributes `b and d`. Like determinant 1, this could be part of a candidate key.

Therefore, the determinant that represents a non-candidate key is index number 2: `a,d→b`. It's not a full superkey and doesn't determine all other attributes, making it a non-candidate key.

### Question 10: 

The following table stores rows of information about pizza deliveries. The three columns correspond to the `Restaurant name, Crust, Delivery Area`. We convert this table into Fourth Normal Form and so we end up creating two tables, each with two columns and N rows. (Both the new tables have an equal number of rows)

```
Restaurant  Crust       Delivery Area
-------------------------------------------
X Pizza     Thick       Whitefield
X Pizza     Thick       Greenville
X Pizza     Thick       Capital
X Pizza     Stuffed     Whitefield
X Pizza     Stuffed     Greenville
X Pizza     Stuffed     Capital
Papa Pizza  Thin        Capital
Papa Pizza  Stuffed     Capital
F1 Pizza    Thick       Whitefield
F1 Pizza    Thick       Greenville
F1 Pizza    Thin        Whitefield
F1 Pizza    Thin        Greenville

```
In the text box below, enter the value of the integer N.


**ANSWER:** 6

**EXPLANATION:**

Table 1:
```
Restaurant  Crust
-----------------
X Pizza     Thick
X Pizza     Stuffed
Papa Pizza  Thin
Papa Pizza  Stuffed
F1 Pizza    Thick
F1 Pizza    Thin
```

Table 2:
```
Crust       Delivery Area
--------------------------
Thick       Whitefield
Thick       Greenville
Thick       Capital
Stuffed     Whitefield
Stuffed     Greenville
Stuffed     Capital
Thin        Capital
```