# Payslip Technical Challenge


## Challenge 1

### File is of type excel

* In this challenge, I check the extentsion of the file.

* To pass the test the file must be of type <code>.xlsx</code>. I pass it files with <code>.xlsx</code> from the pass_data folder and the tests pass.

* To fail this test I pass it a file with a type of <code>.txt</code> from the fail_data folder and the tests fail.

## Challenge 2

### GTN file contains line breaks

* In this challenge I use the <code>dropna</code> pandas method with the how param to find any empty row in the file, and then count the rows before and after it.

* To pass the tests, if the rows count are equal then there were no empty rows.

* To fail the tests, if the rows count are not equal then there was at least one empty row.

## Challenge 3

### GTN file header structure has changed

* In this challenge I use the <code>dtype</code> method to get the amount of different data types.

* To Pass,  if there is just one object type, this mean the column contains a string. I also, used the header param to remove each header row until there were more than one data type.

* To fail, I added a file with two headers in the fail_data folder, this will fail as there is more than one header.

## Challenge 4

### Employees present in Payrun and missing in GTN

* In this challenge I extracted the "employee_id" from GNT and the "Employee ID" from Payrun as a Series and compared to eachother. I had to change the Payrun Series from float and to int32.

* To pass, I compared both series of data and made sure they were equal.

* To fail, I altered some of the data to add different number for the employee_id in GTN and added the file to the fail_data folder. It fails as "Employee ID" in payrun is not in GTN.

## Challenge 5

### Employees present in GTN and missing in Payrun

* In this challenge I extracted the "employee_id" from GNT and the "Employee ID" from Payrun as a Series and compared to eachother. I had to change the Payrun Series from float and to int32.

* To pass, I compared both series of data and made sure they were equal.

* To fail, I altered some of the data to add different number for the employee id in Payrun and added the file to the fail_data folder. It fails as "employee_id" in GTN is not in payrun.

## Challenge 6

### Pay elements in GTN file do not map to Payrun file

* In this challege I extracted columns with the pay elements in both files to a dataframe.

* To pass, I used the equals method to check both dataframes and to pass I tested that the dataframes did not match.

* To fail, I used the equals method to check both dataframes and to fail I tested that the dataframes did match.

## Challenge 7

### Pay elements in Payrun file do not map to GTN file

* In this challege I extracted columns with the pay elements in both files to a dataframe.

* To pass, I used the equals method to check both dataframes and to pass I tested that the dataframes did not match.

* To fail, I used the equals method to check both dataframes and to fail I tested that the dataframes did match.

## Challenge 8

### Pay elements in GTN file are numeric

* In this challege I extracted the pay elements in the GTN file. I then used the <code>dtype</code> to get a Series of the different types of data in the columns. I then used a helper method to loop through the Series and check each  data type.

* To pass, the helper method will loop through all of the data as long as it is of type "int64" or "float64" and the test will pass.

* To fail, I altered some data to add non numeric fields to the columns of data , I added the file to the fail_data folder. To fail, the helper method will immediately return false when there is a data type other than "int64" or "float64" and the loop will stop, failing the test.

