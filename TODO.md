## Requirements

1. The goal is to integrate the data models that are created using the 'ModelToDB' class with the NoSQL databases
    - The databases to be supported are 1. MangoDB, 2. DynamoDB, 3. Cassandra
        - MangoDB will is integrated as a start

2. The following are mostly relavent to MangoDB
    - All the documents in a collections can be represented as ModelToDB data models
    - Create, Read, Update, Modify and Delete operations of a MangoDB document can be able to perform using the
      ModelToDB class instances.
    - Need for dynamic 'collection' classes has to be explored, it could contain the following features
        - Holds collection of data model objects in a MangoDB collection class.
        - Data read operarions on collections.
            - Aggregration
                - Filter
                - Sort
                - Group
                - Count
    - Dynamic datatype handling from python 'types' to database 'types'
