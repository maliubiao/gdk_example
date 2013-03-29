#-*- encoding=utf-8-*-
import pygtk
import os.path
import gtk
import shlex
import subprocess

def set_current_path(button,ce,infobar,path):
	if not os.path.exists(ce.get_text()): 
		infobar.show()		
	else:
		path.insert(0,ce.get_text())
def exec_compile(button,cc,infobar,path): 
	if not os.path.exists(path[0]):
		infobar.show()	
	else:
		#os.environ['PWD'] = path[0]
		print path[0]
		if cc.get_text() is "":
			return
		args = ['/bin/sh','-c']
		args.append(cc.get_text())
		print args
		p = subprocess.Popen(args,cwd = path[0])
		del p
def close_infobar(infobar,response_id):
	infobar.hide()

def main():
	w = gtk.Window()
	f = gtk.Fixed()
	ce = gtk.Entry() 
	ce.set_width_chars(50)
	e = gtk.Button("环境目录")
	path = ["/data/project/py/github/gdk_example"]
	info = gtk.InfoBar()
	info_label1 = gtk.Label("环境目录不存在?")
	info_confirm = gtk.Button("去修改")
	#info.get_action_area().add(info_confirm)
	info.add_action_widget(info_confirm,1)
	info.get_content_area().add(info_label1)
	info.connect("response",close_infobar)
	e.connect("clicked",set_current_path,ce,info,path)
	cc = gtk.Entry() 
	cc.set_width_chars(50)
	c = gtk.Button("编译")
	c.connect("clicked",exec_compile,cc,info,path)	
	f.put(ce,0,0)
	f.put(e,400,0)
	f.put(cc,0,20)
	f.put(c,400,20)
	f.put(info,0,100)
	w.add(f)
	w.set_default_size(500,400)
	w.set_title("小配置工具")
	w.connect("delete-event",gtk.main_quit)
	w.show_all()
	info.hide()	
if __name__ =="__main__":
	main()
	gtk.main()
