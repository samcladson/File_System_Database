# FILE SYSTEM DATABASE

## Overview

This is a key-value based local storage file system application that offers basic CRD ( Create, Read, Delete) operations, This application is written in python and supports python version 3 and above.

## Installation

```
git clone https://github.com/samcladson/File_System_Database.git
```

## Folder Structure

- db.json (JSON File)
- Store.py (Python File)
- README.md (Help)

---

## Usage

```
#importing the class from the package
from Store import Store

#Instanciate the Object
dataSet = Store()
```

## Methods

The package contains three methods to work with the object created.

### create()

- create method takes two argument 1) Name Of key 2) JSON Object
- Key must be of length less than 32chars
- Value should be only in JSON format

  ```
  Key = "FirstData"

  Value = {
      "name":"Jhon Snow",
      "age":25,
  }

  dataset.create(Key,Value)
  ```

  ```
  #Output
  [DATA CREATED]...Data Created Successfuly.
  ```

### read()

- Read method will read all the data from the file and displays it.
- It takes key as an optional argument that will display a specific data.

  Read method without argument

  ```
  dataset.read()
  ```

  ```
  #Output
  [READING DATA]....

  {
      "FirstData":{
          "name":"Jhon Snow",
          "age":25,
      },
      "SecondData":{
          "name":"Henry",
          "age":32,
      }
  }
  ```

  Read method with argument

  ```
  args = 'FirstData'
  dataset.read(args)
  ```

  ```
  #Output
  [READING DATA]....

  {
      "FirstData":{
          "name":"Jhon Snow",
          "age":25,
      }
  }
  ```

### delete()

- Delete method takes single key as argument and deletes the data if the key is present.

  ```
  args = "FirstData"
  dataSet.delete(args)
  ```

  ```
  #Output
  [DELETED]....Deleted Successfuly
  ```

### Error Logs

- If File size exceeds 1GB

  ```
  [ERROR]....Store size exceeded 1GB.
  ```

- If Key already exixts
  ```
  [ERROR]....!Oops key already exist.
  ```
- If Key length is more than 32chars
  ```
  [ERROR]....Key must be of length less than 32!
  ```
- If Value is not in JSON format
  ```
  [ERROR]....Value must be is JSON format
  ```
- If Value size exceeds 16KB

  ```
  [ERROR]....Size of value must be below 16KB.
  ```

- If key does not exist, It throws the following error message
  ```
  [NOT FOUND]....key not found!
  ```
- If the Store is empty, It throws the following error message
  ```
  [NO DATA]....store is empty!
  ```
