import json
import os
dir  =   os.getcwd()
jFile  = (os.getcwd ()+'\ASSETSDB.json')
print jFile

rFile = open(jFile).read()
jObj = json.loads(rFile)

print jObj["weapons"]['apar_scourgerailgun']['file_path']
print jObj["weapons"]['apar_scourgerailgun']['file_path']






input1 = '''
{
    "FirstName":"Bhairav",
    "MiddleName":"Sharma",
    "LastName":"Ram",
    "DateOfBirth":"09-01-1984",
    "Contact":{
        "Phone":9988776655,
        "Email":"bhairav@gmail.com"
    },
    "Address":[
        {
            "Type":"Office",
            "ZipNumber":560056,
            "Street":"Nagarbhavi Road",
            "City":"Bangalore",
            "Country":"India"
        },
        {
            "Type":"Home",
            "ZipNumber":560004,
            "Street":"Gandhi Bazaar Road",
            "City":"Bangalore",
            "Country":"India"
        }
    ]
}
        '''

input  = '''
{
    "name" : "Atri",
    "middleName" : "Dave",
    "Salary" : 60000,
    "Age" : 35,

    "color":
    [
      
    {"name": "Red",
      "type": "Bright",
      "signifies": ["energy", "war", "danger", "strength","power", "determination"]
    },
    
    {"name": "Yello",
      "type": "Bright",
      "signifies": ["freshness", "happiness", "positivity", "clarity", "energy", "optimism", "enlightenment", "remembrance", "intellect", "honor", "loyalty", "joy"]
    },
    
    {"name": "Blue",
      "type": "dull",
      "signifies": [ "trust", "loyalty", "wisdom", "confidence", "intelligence", "faith", "truth","heaven"]
    }
    
    ]

}
            '''
#print(type(input1))
#jsonObjectInfo = json.loads(input)
#print(type(jsonObjectInfo))
#print(jsonObjectInfo)
#print "total dictonary key are {0}".format(len(jsonObjectInfo))

#print jsonObjectInfo['name']
#print jsonObjectInfo['middleName']

#colorStr =  "Color {} Signifies {} "
#print colorStr.format((jsonObjectInfo['color'][0]['name']),(jsonObjectInfo['color'][0]['signifies']))


#for each in jsonObjectInfo['color']:
#    print each['signifies']


#for i in range(0,len(jsonObjectInfo['color'][2]['signifies'])):
#    print (jsonObjectInfo['color'][2]['signifies'])[i]




rFile = open(jFile).read()
jObj = json.loads(rFile)
#just for checking




#binders =  jObj['binders']
#groups  =  jObj['groups']
#group1 =   jObj[groups[0]] 


#print jObj[groups[2]] 


#for item in jObj['groups']:
#    print item['file_path']




#print list(group1.keys())


#for i in range(0,len(groups)):
#    innerGroups =  jObj[groups[i]]
#    print ('Group %s :: ' % groups[i])
#    print list(innerGroups.keys())





#print list(binders.keys())



#for i in range(0,len(jObj['groups'])):
#               print jObj['groups'][i]


    

#print("First Name is {0}".format(jsonObjectInfo['FirstName']))
#print("Email ID is is {0}".format(jsonObjectInfo['Contact']['Email']))
#print("-----------------**************---------------")

#for eachjsonobject in jsonobjectinfo['address']:
#    print("address type is {0}".format(eachjsonobject['type']))
#    print("zip number is {0}".format(eachjsonobject['zipnumber']))
#    print("street name is {0}".format(eachjsonobject['street']))
#    print("city name is {0}".format(eachjsonobject['city']))
#    print("country name is {0}".format(eachjsonobject['country']))
#    print("-----------------**************---------------")
