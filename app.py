from flask import Flask,render_template,request,make_response,session
from contact import Contact
from db import dbHandler
from flask_session import Session
from controller import add_Contact,show_contacts,show_contact_name,get_user,insert_user,validatePasword,delete_contact,get_contact,update_contact
app = Flask(__name__)
app.config.from_object("config")
app.secret_key=app.config["SECRET_KEY"]
Session(app)

@app.route('/')
def FirstPage():
    return render_template("firstPage.html")


@app.route('/signup')
def Signup():
    return render_template("signup.html")
@app.route('/signupComplete', methods = ["POST","GET"])
def signupComplete():
    email = request.form["email"]
    password = request.form["password"]
    if(validatePasword(password)):
        insert_user(email,password)
        return render_template("login.html")
    else:
        return render_template("signup.html" ,msg = "Signup Failed")    



@app.route('/inputLogin')
def inputLogin():
    return render_template("login.html")
@app.route('/login', methods = ["GET","POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]
    data = get_user()
    for i in data:
        if(email == i[1] and password == i[2]):
            session["uemail"] = email
            session["upassword"] = password 
            return  render_template("index.html") 
    return render_template("login.html", msg = "User not found")
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/contact',methods = ["GET","POST"])
def contacts():
    return render_template("contact.html")  
@app.route('/addContact',methods = ["GET","POST"])
def addContact():
    name = request.form["name"]
    mobileNo= request.form["MobileNo"]
    cit = request.form["city"]
    profes= request.form["profession"]
    email = session.get("uemail")
    Con = Contact(name,mobileNo,cit,profes)
    add_Contact(Con)
    print("hello")
    response = make_response(render_template("addContact.html"))
    response.set_cookie("uname",name)
    response.set_cookie("ucity",cit)
    return response

@app.route('/showContact',methods = ["GET","POST"])
def showContact():
    name = request.cookies.get("uname")
    cit = request.cookies.get("ucity")
    data= show_contacts()
    #print(data)
    result = []
    n = len(data)
    for i in range(n):
        dic = {}
        dic.update(id = data[i][0])
        dic.update(name = data[i][2])
        dic.update(MobileNo = data[i][3])
        dic.update(city = data[i][4])
        dic.update(profession = data[i][5])
        result.append(dic)
    return render_template("showContact.html",context = result,name = name, city =cit)          

@app.route('/searchContact')
def searchContact():
    return render_template("searchContact.html")

@app.route('/searchComp', methods =["GET","POST"])
def searchComp():
    name = request.form["name"]
    dataOne = show_contacts()
    for i in dataOne:
        if(name == i[2]):
            data = show_contact_name(name)
            result = []
            dic = {}

            dic.update(id = data[0][0])
            dic.update(name = data[0][2])
            dic.update(MobileNo = data[0][3])
            dic.update(city = data[0][4])
            dic.update(profession = data[0][5])
            result.append(dic)
            return render_template("searchComp.html",context = result)

    return render_template("searchContact.html" , msg = "COntact NOt found")            

@app.route('/delete' , methods = ["GET","POST"])
def delete():
    data= show_contacts()
    result = []
    n = len(data)
    for i in range(n):
        dic = {}
        dic.update(id = data[i][0])
        dic.update(name = data[i][2])
        dic.update(MobileNo = data[i][3])
        dic.update(city = data[i][4])
        dic.update(profession = data[i][5])
        result.append(dic)
    return render_template("delete.html",context = result)


@app.route('/deleteComp' , methods = ["GET","POST"])
def deleteComp():   
    id = request.form["userid"] 
    delete_contact(id)
    return render_template("index.html")


@app.route('/showupdate')
def showUpdation():
    data= show_contacts()
    result = []
    n = len(data)
    for i in range(n):
        dic = {}
        dic.update(id = data[i][0])
        dic.update(name = data[i][2])
        dic.update(MobileNo = data[i][3])
        dic.update(city = data[i][4])
        dic.update(profession = data[i][5])
        result.append(dic)
    return render_template("update.html",context = result)

@app.route('/update',methods = ["GET","POST"])
def update():
    contactid = request.form["contactid"]
    
    data = get_contact(contactid)
    result = []
    dic = {}
    dic.update(id = data[0][0])
    dic.update(name = data[0][2])
    dic.update(MobileNo = data[0][3])
    dic.update(city = data[0][4])
    dic.update(profession = data[0][5])
    result.append(dic)
    response = make_response(render_template("inputUpdate.html",context = result,contact = contactid,uname= data[0][2],umobileNo =data[0][3],ucity=data[0][4],profession=data[0][5]))
    response.set_cookie("contactid",contactid)
    # response.set_cookie("name",data[0][2])
    # response.set_cookie("mobileNo",data[0][3])
    # response.set_cookie("city",data[0][4])
    # response.set_cookie("profession",data[0][5])
    return response
    #return render_template("inputUpdate.html",context = result,contact = contactid )
@app.route('/updated',methods = ["GET","POST"])
def updated():
    #contactid = request.form["contactid"]
    name = request.form["name"]
    mobileNo = request.form["MobileNo"]
    city = request.form["city"]
    profession = request.form["profession"]
    contactid = request.cookies.get("contactid")
    update_contact(contactid,name,mobileNo,city,profession)
    return render_template("index.html")



@app.route('/logout')
def logout():
    session.clear()
    return render_template("login.html")    


if __name__ == '__main__':
    app.debug=True
    app.run()    