##import mysql.connector
import csv
##from mysql.connector import Error
from xml.dom import minidom
import xml.etree.ElementTree as ET

##def dbi():
##    dbi = mysql.connector.connect(host='localhost',
##                                       database='passinfodb',
##                                       user='root',
##                                       password='eieadmin')
##    return dbi
    
        
##def getGroupList():
##    db = dbi()
##    cur = db.cursor()    
##    cur.execute("select `GroupID`, `GroupName` from `tbl_group")
##    d = [item[0] for item in cur.fetchall()] 
##    return d
##
##def getPassInfoList():
##    db = dbi()
##    cur = db.cursor()    
##    cur.execute("select `PassInfoID`, `Title`, `UserName`, `Password`,`URL`, `Notes` from `tbl_passinfo` ")
##    d = [item[0] for item in cur.fetchall()] 
##    return d


def writeLineToCSV(ID,GroupName, Title, UserName, Password,URL, Notes ):
        
        
        data = [{'ID' : ID.strip() ,'GroupName' : GroupName.strip() , 'Title': Title.strip(), 'UserName' : UserName.strip(), 'Password' : Password.strip(), 'URL' : URL.strip(), 'Notes' : Notes.strip()}]                 
                        
                        
        with open('passInfo.csv', 'a') as csvFile:
                fields = ['ID','GroupName','Title','UserName','Password','URL','Notes']
                writer = csv.DictWriter(csvFile, fieldnames=fields)
##                writer.writeheader()
                writer.writerows(data)
                
       # print('Write Completed ...')

        csvFile.close()


def writeAllToCSV(ListPassData):
        
        data = []
        for j in ListPassData:
            data.append({'ID' : j.id ,'GroupName' : j.groupName , 'Title': j.title, 'UserName' : j.userName, 'Password' : j.password, 'URL' : j.url, 'Notes' : j.notes})
                         
                        
        with open('passInfo.csv', 'w') as csvFile:
                fields = ['ID','GroupName','Title','UserName','Password','URL','Notes']
                writer = csv.DictWriter(csvFile, fieldnames=fields)
##                writer.writeheader()
                writer.writerows(data)
                
      #  print('Write Completed ...')

        csvFile.close()


def getPassInfoList():
    with open('passInfo.tef') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        return 

def PopulateFromCsv():
    ListPassData = []
    with open('passInfo.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for j in readCSV:
            if any(j):
                ListPassData.append(PassData(j[0],j[1],j[2],j[3],j[4],j[5],j[6]))
    return  ListPassData            

def GetXmlFile():
        try:
             xmldoc = minidom.parse('Settings.xml')
             itemlist = xmldoc.getElementsByTagName('group')
             return itemlist 
        except IOError:
            print('Bad file')
            return
        except Exception as e:
            print('Really bad error')
            print(e)
            return

def GetMasterPassword():
        try:
             xmldoc = minidom.parse('Settings.xml')
             itemlist = xmldoc.getElementsByTagName('password')
             for s in itemlist:
                        psw = s.attributes['psw'].value
             return psw 
        except IOError:
            print('Bad file')
            return
        except Exception as e:
            print('Really bad error')
            print(e)
            return

def GetSelectedValue():
        try:
             xmldoc = minidom.parse('Settings.xml')
             itemlist = xmldoc.getElementsByTagName('SelectedValue')
             for s in itemlist:
                        val = s.attributes['val'].value
             return val 
             
        except IOError:
            print('Bad file')
            return
        except Exception as e:
            print('Really bad error')
            print(e)
            return
             
def SetSelectedValue(value):
        # try:
               
                d = minidom.parse('Settings.xml')
                elems = d.getElementsByTagName('SelectedValue')
                elems[0].setAttribute('val', value)
                with open('Settings.xml', 'w') as f:
                        d.writexml(f, addindent=' ')


                """ et = ET.parse('Settings.xml')

                # Append new tag: <a x='1' y='abc'>body text</a>
                new_tag = ET.SubElement(et.getroot(), 'SelectedValues')
                new_tag.attrib['val'] = value

                # Write back to file
                #et.write('file.xml')
                et.write('Settings.xml') """
            #  for s in itemlist:
            #             s.attributes['val'].SetSelectedValue(value)
         
        # except IOError:
        #     print('Bad file')
        #     return
        # except Exception as e:
        #     print('Really bad error')
        #     print(e)
        #     return

class PassData(object):
    def __init__(self, ID = None , GroupName = None , Title = None , UserName = None , Password = None , URL = None , Notes = None ) :
             self.id = ID
             self.groupName = GroupName
             self.title = Title
             self.userName = UserName
             self.password = Password
             self.url = URL
             self.notes = Notes
       

        
