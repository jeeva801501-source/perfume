#!C:\Python312\python.exe
import cgi
import mysql.connector
print("content-type:text\n\r\n\r")
print("<html>")
print("<body>")
data=cgi.FieldStorage()
first_name=data.getvalue("username")
last_name=data.getvalue("inisial")
mobile=data.getvalue("no")
gmail=data.getvalue("mail")
pwd=data.getvalue("pass")
age=data.getvalue("year")
date=data.getvalue("dob")
blood=data.getvalue("bg")
adress=data.getvalue("adrs")
pincode=data.getvalue("postalcode")
print("<center>")

print("<table>")
print(f"<tr><td><h1>First Name : <h1></td><td><h1>{first_name}</h1></td></tr></h1>")
print(f"<tr><td><h1>Last Name : <h1></td><td><h1>{last_name}</h1></td></tr></h1>")
print(f"<tr><td><h1>Mobile no : <h1></td><td><h1>{mobile}</h1></td></tr></h1>")
print(f"<tr><td><h1>Gmail : <h1></td><td><h1>{gmail}</h1></td></tr></h1>")
print(f"<tr><td><h1>Password : <h1></td><td><h1>{pwd}</h1></td></tr></h1>")
print(f"<tr><td><h1>Age : <h1></td><td><h1>{age}</h1></td></tr></h1>")
print(f"<tr><td><h1>Date of Birth : <h1></td><td><h1>{date}</h1></td></tr></h1>")
print(f"<tr><td><h1>Blood Group : <h1></td><td><h1>{blood}</h1></td></tr></h1>")
print(f"<tr><td><h1>Adress : <h1></td><td><h1>{adress}</h1></td></tr>")
print(f"<tr><td><h1>Pincode : <h1></td><td><h1>{pincode}</h1></td></tr>")

print("</table>")
print("</center>")
print("<center>")
print("<form>")
print("<button type='submit'><a href='./index.html'>Back</a></button>")
print("</form>")
print("</center>")
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="project"
)
cursor=db.cursor()
sql="INSERT INTO purchase(Firstname,Lastname,Mobilenumber,Gmailid,Password,Age,DOB,BloodGroup,Address,Pincode) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(first_name,last_name,mobile,gmail,pwd,age,date,blood,adress,pincode)
cursor.execute(sql,val)
db.commit()
print("</body>")
print("</html>")