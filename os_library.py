import os
	
#Get the current working directory (CWD)
cwd = os.getcwd()
print("Current working directory:", cwd)

#Change directory
os.chdir('/home/odoo/Desktop')
cwd = os.getcwd()
print('New directory:',cwd)
os.chdir('/home/odoo/Desktop/Virendra')
cwd = os.getcwd()

#Make new directory
directory = 'temp'
path = os.path.join(cwd, directory)
print(path)

os.mkdir(path)
os.mkdir('temp2') #if you wand to creat directory in CWD then no need to give 'path'.
print('Directory \'%s\' created' % directory)

#List directory
path_ = '/home/odoo/Desktop'
list = os.listdir(path_)
print(list)

#remove directory or file
os.rmdir(path) #path = /home/odoo/Desktop/Virendra/temp as above
print('Directory \'%s\' removed sucessfuly.' % directory)
os.remove('test.txt')