import os
import sys
import re
def file_switch(path):
	file_array = []
	files= os.listdir(path)
	for file in files:
		file_path = path + '\\' + file
		if os.path.isfile(file_path):
			if(type(file) == str):
				if(re.match(r'.*ncm$', file,flags=0)):
					file_array.append(file_path)
		elif os.path.isdir(file_path):
			file = str(file)
			file_switch(f'{path}\\{file}')
	for i in file_array:
		now_path = os.path.dirname(os.path.realpath(sys.executable))
		os.system(f'{now_path}\\main.exe "{i}"')
		new_file1 = i[:-3] + 'mp3'
		new_file2 = i[:-3] + 'flac'
		if ((os.path.exists(new_file1)) | (os.path.exists(new_file2))):
			os.system(f'del "{i}"')
		else:
			print(f'文件:{i} 转换失败!')
print('请输入要转换的文件夹路径：')
path = input()
if(path):
	if ((os.path.exists(path))):
		try:
			file_switch(path)
		except Exception as e:
			print('路径有误，请重试！')
	else :
		print('路径不存在！')
else :
	print("未输入要转换的文件夹！请重试！")
input()