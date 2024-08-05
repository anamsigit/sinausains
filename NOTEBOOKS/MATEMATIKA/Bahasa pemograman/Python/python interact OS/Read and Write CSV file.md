HTML is a markup format which defines the content of a webpage. JSON is a data interchange format commonly used to pass data between computers on networks, especially the internet. CSV or comma separated values is a very common data format used to store data as segment of text separated by commas.

#### parsing

analsis konten struktur data dengan benar

CSV is a pretty simple format. contohnya
![c83727cf89998f23d8d94643542a4c3a.png](../../../../../_resources/c83727cf89998f23d8d94643542a4c3a.png)

### open CSV file

import csv
file = open('CSVFile.csv')
fileCSVFile = csv.readaer(file)
for row in fileCSVFile:
  name, phone, role = row; print('name:{}, phone:{}, role:{}'.format(name, phone,row)
  ![a18b67e8d2be7e4f4774e23b9df971de.png](../../../../../_resources/a18b67e8d2be7e4f4774e23b9df971de.png)
  
 you can use row[0]
 
 menulis
 ![06af91d05d40ef2a62f6300439c47b4c.png](../../../../../_resources/06af91d05d40ef2a62f6300439c47b4c.png)
 
 #### search by key
 the csv file:
 ![63b8c51758069f9f015c284c45fa7904.png](../../../../../_resources/63b8c51758069f9f015c284c45fa7904.png)
 
 how read it with dictreader
 ![586dc5941a03e96a850acbd775f08dd9.png](../../../../../_resources/586dc5941a03e96a850acbd775f08dd9.png)
 
 menulis dengan dictreader
 ![90dcdcea7b679bc6f8a657bb5420b31b.png](../../../../../_resources/90dcdcea7b679bc6f8a657bb5420b31b.png)
 
DictReader() allows us to convert the data in a CSV file into a standard dictionary. DictWriter() \ allows us to write data from a dictionary into a CSV file. What’s one parameter we must pass in order for DictWriter() to write our dictionary to CSV format?

for more : [*](https://docs.python.org/3/library/csv.html) [*](https://realpython.com/python-csv/)