# HANKERRANK - INDEX


![Author](https://img.shields.io/badge/Author-Nhi%20Yen-brightgreen)
[![Medium](https://img.shields.io/badge/Medium-Follow%20Me-blue)](https://medium.com/@yennhi95zz/subscribe)
[![GitHub](https://img.shields.io/badge/GitHub-Follow%20Me-lightgrey)](https://github.com/yennhi95zz)
[![Kaggle](https://img.shields.io/badge/Kaggle-Follow%20Me-orange)](https://www.kaggle.com/nhiyen/code)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect%20with%20Me-informational)](https://www.linkedin.com/in/yennhi95zz/)


## Question 1: How many index architecture type classifications are there in MS SQL Server?

**ANSWER:**

Microsoft SQL Server primarily uses **02 main types** of index architectures: `clustered` and `non-clustered indexes`. These indexes help optimize query performance by providing a quick lookup mechanism for the data stored in tables.

**Clustered Index:**
- Determines the physical order of data rows in a table.
- The table can have only one clustered index.
- Data rows are sorted based on the clustered index key.
- The leaf nodes of the clustered index contain the actual data rows.

**Non-clustered Index:**
- Provides a separate structure for index storage, independent of the actual data order.
- The table can have multiple non-clustered indexes.
The leaf nodes of the non-clustered index contain a pointer to the actual data rows.

## Question 2: Which of the following statement is true about row locators in non-clustered indexes in MS SQL Server?

A. If the table does not have a clustered index, the row locator is the clustered index key for the row.

B. If the table has a clustered index, or the index is on an indexed view, the row locator is a pointer to the row.

C. If the table has a clustered index, or the index is on an indexed view, the row locator is the clustered index key for the row.

D. None of the above-mentioned statement is true.

**ANSWER:** C

**EXPLANATION:**

In Microsoft SQL Server, when a table has a clustered index or when a non-clustered index is created on an indexed view, the row locator in a non-clustered index for a particular row is the clustered index key for that row.

Here's a breakdown:

Clustered Index Presence:
- If the table has a clustered index, the data rows in the table are physically sorted and stored in the order of the clustered index key.

- In this case, the row locator in a non-clustered index on that table will be the clustered index key for the respective rows.

Indexed View:
- If the non-clustered index is on an indexed view (a view that has been indexed for better performance), the row locator in the non-clustered index will also be the clustered index key for the corresponding rows.

In summary, the statement is highlighting that when a clustered index is present on the table or when the non-clustered index is on an indexed view, the row locator in the non-clustered index points to the clustered index key for efficient retrieval of the actual data row.

## Question 2:  Consider the following two designs to store the data using clustered indexes in MS SQL Server:

- In the first design, the fill factor is 20% and the total number of free rows per page are A.

- In the second design, the fill factor is 40% and the total number of free rows per page are B.

Which the followings describes the relation between A and B:

A = 1.33B

B = 1.33A

A = 0.67B

B = 0.67A

**ANSWER:** A = 1.33B

**EXPLANATION:**

The fill factor is the percentage of space on each page that is filled with data, leaving the rest for future updates. If we compare the fill factors, we can use the following relationship:

A = 100% - 20% = 80%

B = 100% - 40% = 60%

<!-- A = $\frac{1}{\text{Fill Factor 1}}$

B = $\frac{1}{\text{Fill Factor 2}}$ -->

<!-- Given that the first design has a fill factor of 20% (or 0.2) and the second design has a fill factor of 40% (or 0.4):

A = $\frac{1}{\text{0.2}}$ = 5

B = $\frac{1}{\text{0.4}}$ = 2.5 -->

Therefore,  A=1.33B.

## Question 2:  The correct syntax for creating composite indexes in MS SQL Sever is:

A. `<p>CREATE INDEX index_name</p> <p>ON table_name(column1), table_name(column2);</p>`

B. `<p>CREATE INDEX index_name</p> <p>ON table_name(column1) and table_name(column2);</p>`

C. `<p>CREATE INDEX index_name</p> <p>ON table_name(column1, column2);</p>`

D. `<p>All the above-mentioned syntax are correct.</p>`

**ANSWER:** C


