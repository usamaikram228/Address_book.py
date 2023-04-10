import pymysql
from contact import Contact
class dbHandler:
    def __init__(self,host,user,passd,database):
        self.host = host
        self.user = user
        self.passwd = passd
        self.db = database

    def insertContact(self,contactObj):
        dbConnect = None
        curObj = None
        try:
            dbConnect = pymysql.connect(host =self.host,user =self.user,passwd =self.passwd,db=self.db)
            curObj = dbConnect.cursor()
            sqlQuery ="""insert into contacts(name,mobileNo,city,profession)
            values(%s,%s,%s,%s)"""
            agrc =(contactObj.name,contactObj.mobileNo,contactObj.city,contactObj.profession)
            curObj.execute(sqlQuery,agrc)
            print("Hello")
            dbConnect.commit()
            
        except Exception as e:
            print(e)
        finally:
            if dbConnect!= None:
                dbConnect.close()         

    def showAllContacts(self):
        dbConnect = None
        curObj = None
       
        try:
            dbConnect = pymysql.connect(host =self.host,user =self.user,passwd =self.passwd,db=self.db)
            curObj = dbConnect.cursor()
            sqlQuery = """Select * from contacts"""
            curObj.execute(sqlQuery)
            result = curObj.fetchall()
        except Exception as e:
            print(e)
        finally:
            if dbConnect!= None:
                dbConnect.close()
        return result       
    def showContactbyName(self,name):
        dbConnect = None
        curObj = None
        try:
            dbConnect = pymysql.connect(host =self.host,user =self.user,passwd =self.passwd,db=self.db)
            curObj = dbConnect.cursor()
            sqlQuery = """Select * from contacts
            where name = %s"""
            argc = (name)
            curObj.execute(sqlQuery,argc)
            result = curObj.fetchall()
        except Exception as e:
            print(e)
        finally:
            if dbConnect!= None:
                dbConnect.close()
        return result        

    def getUser(self):
        dbConnect = None
        curObj = None
        try:
            dbConnect = pymysql.connect(host =self.host,user =self.user,passwd =self.passwd,db=self.db)
            curObj = dbConnect.cursor()
            sql = "select * from user"
            curObj.execute(sql)
            result = curObj.fetchall()
            return result 
        except Exception as e:
            print(e)
        finally:
            if dbConnect!= None:
                dbConnect.close()
            


    def insertUser(self,email,password):
        dbConnect = None
        curObj = None
        try:
            dbConnect = pymysql.connect(host =self.host,user =self.user,passwd =self.passwd,db=self.db)
            curObj = dbConnect.cursor()
            sql = """insert into user(email,password)
            values(%s,%s)"""
            argc = (email,password)
            curObj.execute(sql,argc)
            dbConnect.commit()
        except Exception as e:
            print(e)
        finally:
            if dbConnect!= None:
                dbConnect.close()


    def deleteContact(self,id):
        dbConnect = None
        curObj = None
        try:
            dbConnect = pymysql.connect(host =self.host,user =self.user,passwd =self.passwd,db=self.db)
            curObj = dbConnect.cursor()
            sql = """delete from contacts
            where contact_id = %s"""
            argc = (id)
            curObj.execute(sql,argc)
            dbConnect.commit()
        except Exception as e:
            print(e)
        finally:
            if dbConnect!= None:
                dbConnect.close()

    def getContact(self,contactid):
        dbConnect = None
        curObj = None
        try:
            dbConnect = pymysql.connect(host =self.host,user =self.user,passwd =self.passwd,db=self.db)
            curObj = dbConnect.cursor()
            sql = """select * from contacts
            where contact_id = %s"""
            argc = (contactid)
            curObj.execute(sql,argc)
            result1 = curObj.fetchall()
            print(result1)
            return result1        
        except Exception as e:
            print(e)
        finally:
            if dbConnect!= None:
                dbConnect.close()    

    def updateContact(self,contactid,name,mb,city,pro):
        dbConnect = None
        curObj = None
        try:
            dbConnect = pymysql.connect(host =self.host,user =self.user,passwd =self.passwd,db=self.db)
            curObj = dbConnect.cursor()   
            sql = """update contacts
            set name = %s,mobileNo = %s,city = %s,profession = %s
            where contact_id = %s
            """
            argc = (name,mb,city,pro,contactid)
            curObj.execute(sql,argc)
            dbConnect.commit()
        except Exception as e:
            print(e)
        finally:
            if dbConnect!= None:
                dbConnect.close()    