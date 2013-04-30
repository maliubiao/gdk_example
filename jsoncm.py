#! /usr/bin/python
#-*-encoding=utf-8-*-
#this is a very simple json config file manager, file format: [{},{},{}], available cli command: -a(add), -d(delete), -d(list_all)

import sys
import io
import json
import argparse 
from StringIO import StringIO

def main(): 
	args = init()
	f = io.FileIO("/home/richard_n/bin/alias_db","r+") 
	j = f.read() 
	db = list()
	#clear db if load failed
	if j != "":
		f.seek(0,io.SEEK_SET)
		try:
			db = json.load(f) 
		except ValueError:
			pass
		
	f.seek(0,io.SEEK_SET) 
	if args.add is not None: 
		addvalue = args.add[0] 
		if addvalue == "":
			print "need one json string"
		else:
			db.append(json.load(StringIO(addvalue)))
			print "added: " +str(db)
	if args.delete is not None:
		delvalue = args.delete[0]

		if delvalue == "":
			print "please specify the key to delete"
		else: 
			i = list()
			#don't del db[index] directly, list will shift automatically.
			for index,jitem in enumerate(db): 
				if delvalue in jitem:
					i.append(index)
					print "deleted: "+ str(delvalue)
			#reverse first
			for m in reversed(i):
				del db[m]
			del i	

	if args.list_all is False:
		print db

	f.truncate(0)
	f.write(json.dumps(db))		
	f.close()

	
def init():
	parser = argparse.ArgumentParser(description="json config manager",prefix_chars='-')
	parser.add_argument('-a',"--add",type=str,nargs=1,help="add one item")
	parser.add_argument("-d","--delete",type=str,nargs=1,help="delete one item")
	parser.add_argument("-l","--list_all",action="store_false",help="list all items")
	return parser.parse_args()
		

if __name__ == "__main__":
	main()
