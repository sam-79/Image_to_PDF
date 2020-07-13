from PIL import Image as UMP 
from PIL import ImageTk
import reportlab as rl
from reportlab.pdfgen import pdfimages , canvas
import tempfile
import time
from tkinter import *
from tkinter import filedialog
import os
import glob
from tkinter import simpledialog
from tkinter.simpledialog import Dialog
#Creating Class

class pdf():
	global file_names , file_dir
	file_dir=[]
	file_names=[]
	
	
	
	
	def get_files(self):
		file=filedialog.askopenfilename(filetypes=[("Image Files","*.jpg")])
		self.photo_show(file)
		
		
		

	def photo_show(self,file):
		global view
		view=Tk()
		view.geometry("800x800")
		
		img=UMP.open(file)
		img.thumbnail((700,600))
		pho=ImageTk.PhotoImage(img,master=view)
		
		canvo=Canvas(view,width = 800 ,height=700,background="white")
		canvo.pack()
		
		canvo.create_image(canvo.canvasx(400),canvo.canvasy(350),image=pho)
		
		sel_btn=Button(view,text="Select",command=lambda:self.add_file(file))
		sel_btn.pack(side=RIGHT, padx=40)
		
		
		cancel_btn=Button(view,text="Cancel",command=view.destroy)
		cancel_btn.pack(side=LEFT, padx=40)
		
		
		view.mainloop()
		
	def add_file(self,file):
		head,tail=os.path.split(file)
		file_names.append(tail)
		file_dir.append(file)
		file_listbox.insert(END,file_names[-1])
		
		view.destroy()
		
		
	#def askname(self):
#		global filename
#		Tk().withdraw()
#		simpledialog.Dialog.buttonbox()
#		simpledialog.Dialog.ok(event=pdf_convert)
#		filename=simpledialog.askstring("Name", "Enter File Name:")
#		
	
	
	
	def pdf_convert(self):
		
#		if(len(filename)>0):
#			pass
#		else:
#			filename="file"
				
		f= tempfile.TemporaryDirectory(dir = "C:/")
		dir=f.name
		
		for i in file_dir:
			img=UMP.open(i)
			img.thumbnail((500,500))
			head, tail=os.path.split(i)
			f_dir=dir+"/"+tail+".jpg"
			img.save(f_dir)
		
		new_pdf=canvas.Canvas("MyPdf.pdf",pagesize="letter")
		new_pdf.setAuthor("Sameer")
		
		for j in glob.glob(dir+"/*.jpg"):
			Img=UMP.open(j)
			x,y=Img.size
			x=(610-x)/2
			y=(800-y)/2
			new_pdf.drawImage(j,x,y)
			new_pdf.showPage()
		
		new_pdf.save()




obj=pdf()
#Create tkinter Window
global root
root=Tk()
root.title("Image to PDF ")
root.geometry("1300x900")
root.resizable(False,False)



scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT , fill = Y)

file_listbox=Listbox(root,width=25, yscrollcommand = scrollbar.set)
file_listbox.pack( side = RIGHT, fill =Y)

load_btn=Button(root,text="Load Files", width=11,command=obj.get_files)
load_btn.pack( anchor=W , padx=(60,0) , pady=(240,10))


create_btn=Button(root,text="Create",width=11 , command=obj.pdf_convert)
create_btn.pack(anchor = W , padx=(60,0) , pady=(300,100))




root.mainloop()
