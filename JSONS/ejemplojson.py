import ujson

#conf={'a list': [1, 42, 3.141, 1337, 'help', u'€'],
 #     'a string': 'bla',
  #    'another dict': {'foo': 'bar','key': 'value','the answer': 42}
   #   }
conf={}                        
conf["ssid"]={"foo":"bar"}
conf["pass"]="esp1"

print(conf)
with open('conf.json', 'w') as outfile:
    ujson.dump(conf, outfile)
