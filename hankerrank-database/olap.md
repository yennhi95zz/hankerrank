# HANKERRANK - OLAP

![Author](https://img.shields.io/badge/Author-Nhi%20Yen-brightgreen)
[![Medium](https://img.shields.io/badge/Medium-Follow%20Me-blue)](https://medium.com/@yennhi95zz/subscribe)
[![GitHub](https://img.shields.io/badge/GitHub-Follow%20Me-lightgrey)](https://github.com/yennhi95zz)
[![Kaggle](https://img.shields.io/badge/Kaggle-Follow%20Me-orange)](https://www.kaggle.com/nhiyen/code)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect%20with%20Me-informational)](https://www.linkedin.com/in/yennhi95zz/)

## Question 1: This OLAP operation involves computing all of the data relationships for one or more dimensions.

A. dice

B. slice

C. pivot

D. roll-up

**ANSWER:** roll-up

The OLAP operation that involves computing all of the data relationships for one or more dimensions is called "roll-up." 

In the context of OLAP (Online Analytical Processing), roll-up refers to the process of summarizing data at a higher level of aggregation. It involves moving from detailed data to more aggregated levels by eliminating one or more dimensions. This allows users to view data at different levels of granularity and analyze it from various perspectives.


**EXPLANATION:**

1. Dice:

- Definition: Dicing involves selecting a specific range of values along one or more dimensions to view a subset of data.

- Example: If you have a cube representing sales data with dimensions like Time, Product, and Region, dicing might involve selecting a specific time period, certain products, and particular regions to focus on a more detailed subset of the data.

2. Slice:

- Definition: Slicing involves viewing a two-dimensional cross-section of the multidimensional data cube by selecting a specific value for one dimension.

- Example: If you have a cube representing sales data, slicing might involve selecting a particular time period, and the resulting slice would show sales data for that specific time period across all products and regions.

3. Roll-Up:

- Definition: Rolling up involves aggregating data at a higher level of abstraction, reducing the level of detail in one or more dimensions.

- Example: If you have a cube representing sales data with dimensions like Time, Product, and Region, rolling up might involve aggregating sales data from daily to monthly or from a specific product category to a broader category.

In summary:

- Dice involves selecting specific values along one or more dimensions.

- Slice involves viewing a cross-section by fixing one dimension and observing the others.

- Pivot involves rearranging or rotating the dimensions to view data from different perspectives.

- Roll-Up involves aggregating data at a higher level to reduce detail.

## Question 2:  This OLAP Operation rotates the data, and delivers an alternative to the original presentation. 

A. pivot

B. slice

C. roll-up

D. dice


**ANSWER:** Pivot

## Question 3:  What is the source of the cube metadata for OLAP?

A. Star Schema

B. Snowflake Schema

C. Standard Database

D. Both star and snowflake schema(s)

**ANSWER:** D. Both star and snowflake schema(s)


The source of the cube metadata for OLAP (Online Analytical Processing) typically comes from both star and snowflake schemas. These schemas are designed to organize data in a way that facilitates efficient querying and analysis in OLAP systems.

- Star Schema: In a star schema, there is a central fact table containing the primary metrics of interest, surrounded by dimension tables. The fact table is connected to the dimension tables through foreign key relationships. This schema simplifies queries and makes them more efficient for analytical purposes.

- Snowflake Schema: The snowflake schema is an extension of the star schema where dimension tables are normalized into multiple related tables. This normalization can help reduce data redundancy and improve data integrity. Snowflake schemas are also used to organize data for OLAP analysis.

Both of these schema designs provide the necessary structure and relationships among data elements that are crucial for building OLAP cubes and enabling efficient multidimensional analysis. Therefore, the cube metadata in OLAP systems often originates from databases structured using star and snowflake schemas.

## Question 3:  Which of these are alternate names for an OLAP Cube? The options in the top row are a and b respecitvely and those in the bottom row are c and d.

A. Cube

B. Multidimensional Cube

C. HyperCube

D. Both (B) and (C)

**ANSWER:** D. Both (B) and (C)


## Question 3:  Which of these provides a total view of the organization?

A. OLAP

B. OLTP

C. Data Warehousing

D. Database

**ANSWER:** C. Data Warehousing

Data Warehousing provides a total view of the organization by consolidating and integrating data from various sources into a central repository. This repository, known as a data warehouse, contains historical and current data from different departments and systems within an organization.

In contrast:

- OLAP (Online Analytical Processing) focuses on analyzing multidimensional data for decision-making and business intelligence. OLAP is often used in conjunction with data warehousing to provide a more efficient way to analyze and navigate data.

- OLTP (Online Transaction Processing) is designed for transactional processing, dealing with day-to-day operations and transactions within an organization.

- A Database is a broader term that refers to the organized collection of data, and it may include OLAP, OLTP, or other types of databases. However, a standard database alone does not necessarily provide a total view of the organization in the way a data warehouse does.

## Question 3:   Consider a fact table DataPoints(D1,D2,D3,x), and the following three queries:

Q1: Select D1,D2,D3,Sum(x) From DataPoints Group By D1,D2,D3

Q2: Select D1,D2,D3,Sum(x) From DataPoints Group By D1,D2,D3 WITH CUBE

Q3: Select D1,D2,D3,Sum(x) From DataPoints Group By D1,D2,D3 WITH ROLLUP

Suppose attributes D1, D2, and D3 have n1, n2, and n3 different values respectively, and assume that each possible combination of values appears at least once in the table DataPoints. The number of tuples in the result of each of the three queries above can be specified as an arithmetic formula involving n1, n2, and n3. Pick the one tuple (a,b,c,d,e,f) in the list below such that when n1=a, n2=b, and n3=c, then the result sizes of queries Q1, Q2, and Q3 are d, e, and f respectively.

A. (2, 2, 2, 6, 18, 8)

B. (2, 2, 2, 8, 64, 15)

C. (5, 10, 10, 500, 1000, 550)

D. (4, 7, 3, 84, 160, 117)

**ANSWER:** D. (4, 7, 3, 84, 160, 117)

**EXPLANATION:** Incorrect, Need to check

Let's analyze each query to determine the result sizes in terms of n1, n2, and n3:

Q1: Select D1, D2, D3, Sum(x) From DataPoints Group By D1, D2, D3

- Result size = n1 * n2 * n3

Q2: Select D1, D2, D3, Sum(x) From DataPoints Group By D1, D2, D3 WITH CUBE

- Result size = (n1 + 1) * (n2 + 1) * (n3 + 1)

Q3: Select D1, D2, D3, Sum(x) From DataPoints Group By D1, D2, D3 WITH ROLLUP

- Result size = (n1 + 1) * (n2 + 1) * (n3 + 1) - 1

Now, let's match the result sizes with the given options:

For option A: (2, 2, 2, 6, 18, 8)

- Q1: 2 * 2 * 2 = 8
- Q2: (2 + 1) * (2 + 1) * (2 + 1) = 27
- Q3: (2 + 1) * (2 + 1) * (2 + 1) - 1 = 26

For option B: (2, 2, 2, 8, 64, 15)

- Q1: 2 * 2 * 2 = 8
- Q2: (2 + 1) * (2 + 1) * (2 + 1) = 27
- Q3: (2 + 1) * (2 + 1) * (2 + 1) - 1 = 26

For option C: (5, 10, 10, 500, 1000, 550)

- Q1: 5 * 10 * 10 = 500
- Q2: (5 + 1) * (10 + 1) * (10 + 1) = 726
- Q3: (5 + 1) * (10 + 1) * (10 + 1) - 1 = 725

For option D: (4, 7, 3, 84, 160, 117)

- Q1: 4 * 7 * 3 = 84
- Q2: (4 + 1) * (7 + 1) * (3 + 1) = 320
- Q3: (4 + 1) * (7 + 1) * (3 + 1) - 1 = 319

Among the options, option D matches the result sizes for Q1, Q2, and Q3 when n1=4, n2=7, and n3=3. Therefore, the correct answer is:

D. (4, 7, 3, 84, 160, 117)

## Question 3:  Which of these helps OLAP speed up queries, in terms of performance?

A. Dice

B. Aggregation

**ANSWER:** B. Aggregation

**EXPLANATION:** 

- Aggregation helps OLAP (Online Analytical Processing) speed up queries by pre-calculating and summarizing data, which reduces the amount of computation needed at query time. Aggregation involves combining data values from multiple sources and summarizing them into a single value. This process can significantly improve query performance by reducing the amount of data that needs to be processed during query execution.

- Dice, on the other hand, is a technique used in OLAP for selecting a subset of data from a cube by specifying certain dimensions and their members. While dice operations can help to focus queries on specific subsets of data, they may not directly contribute to overall query performance improvement in the same way that aggregation does.