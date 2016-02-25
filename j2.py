import json
from collections import OrderedDict

input = '''
[
  {
  "note":"This file contains the actual data for your assignment",
  "comments":[
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
    },
    {
      "name":"Arihant",
      "count":95
    },
    {
      "name":"Reis",
      "count":94
    },
    {
      "name":"Laiba",
      "count":94
    },
    {
      "name":"Tiylar",
      "count":88
    },
    {
      "name":"Shafia",
      "count":84
    },
    {
      "name":"Aytug",
      "count":76
    },
    {
      "name":"Hayden",
      "count":75
    },
    {
      "name":"Umer",
      "count":72
    },
    {
      "name":"Laci",
      "count":71
    },
    {
      "name":"Kelsie",
      "count":71
    },
    {
      "name":"Ingrid",
      "count":69
    },
    {
      "name":"Oluwalayomi",
      "count":69
    },
    {
      "name":"Keely",
      "count":68
    },
    {
      "name":"Steffie",
      "count":68
    },
    {
      "name":"Ellisha",
      "count":66
    },
    {
      "name":"Tait",
      "count":66
    },
    {
      "name":"Jaslyn",
      "count":63
    },
    {
      "name":"Marcie",
      "count":60
    },
    {
      "name":"Eboni",
      "count":53
    },
    {
      "name":"Jordy",
      "count":49
    },
    {
      "name":"Khai",
      "count":46
    },
    {
      "name":"Toni",
      "count":42
    },
    {
      "name":"Cameron",
      "count":41
    },
    {
      "name":"Shiloh",
      "count":37
    },
    {
      "name":"Arann",
      "count":36
    },
    {
      "name":"Bendeguz",
      "count":35
    },
    {
      "name":"Demetrius",
      "count":34
    },
    {
      "name":"Arunas",
      "count":31
    },
    {
      "name":"Emmajane",
      "count":29
    },
    {
      "name":"Zanab",
      "count":29
    },
    {
      "name":"Mira",
      "count":25
    },
    {
      "name":"Zacharie",
      "count":24
    },
    {
      "name":"Amaney",
      "count":23
    },
    {
      "name":"Kern",
      "count":23
    },
    {
      "name":"Samantha",
      "count":22
    },
    {
      "name":"Rosa",
      "count":21
    },
    {
      "name":"Keegan",
      "count":19
    },
    {
      "name":"Samual",
      "count":12
    },
    {
      "name":"Sera",
      "count":10
    },
    {
      "name":"Dua",
      "count":8
    },
    {
      "name":"Hazel",
      "count":8
    },
    {
      "name":"Kylah",
      "count":6
    },
    {
      "name":"Justin",
      "count":6
    },
    {
      "name":"Ally",
      "count":5
    },
    {
      "name":"Cuba",
      "count":5
    },
    {
      "name":"Wilson",
      "count":4
    },
    {
      "name":"Caitlynn",
      "count":1
    }
  ]
}
]'''


def parseIntegers(mixedList):
    newList = [i for i in mixedList if isinstance(i, int)]
    return newList


info = json.loads(input)
print 'Raw File\n', info
print '\nUser count:', len(input)
print type(info) is list
# print json.dumps(info, indent=4)

countsonly = parseIntegers(info)
print 'Counts only', countsonly


total = 0
for item in info:
    try:
        print '\n', item
    except (ValueError,KeyError, TypeError):
      print 'JSON format error'

print 'Total:', total
