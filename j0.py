import json

data = '''
{
    "name":"Kahlya",
    "count":96
},
{
   	"name":"Hopkin",
    "count":96
},
{
    "name":"Eugene",
    "count":96
}'''

data2 = '''
[
  { "count" : "2",
    "name" : "Chuck"
  } ,
  { "count" : "7",
    "name" : "Chuck"
  } 
]'''

info = json.loads(data2)

for item in info:
	print 'Name:',info["name"]
	print 'Count:',info["count"]