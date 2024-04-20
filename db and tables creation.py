import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"

)
mycursor = db.cursor()

sql="USE DATABASE  library_management_system"
# mycursor.execute(sql)
# db.commit()
sql1 = ''' CREATE TABLE `library_management_system`.member (
  `Id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(45) NULL,
  `password` VARCHAR(45) NULL,
  `privilege` VARCHAR(45) NULL,
  PRIMARY KEY (`Id`));'''
mycursor.execute(sql1 )
db.commit()
sql2 ='''CREATE TABLE `library_management_system`.`bookRecord` (
  `Bno` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NULL,
  `author` VARCHAR(45) NULL,
  `year` VARCHAR(45) NULL,
  `school` VARCHAR(45) NULL,
  `type` VARCHAR(45) NULL,
  PRIMARY KEY (`Bno`));'''
mycursor.execute(sql2)
db.commit()
sql3='''CREATE TABLE `library_management_system`.`issue` (
  `Bno` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NULL,
  `author` VARCHAR(45) NULL,
  `year` VARCHAR(45) NULL,
  PRIMARY KEY (`Bno`));
'''
mycursor.execute(sql3)
db.commit()
