if __name__ == '__main__':
	content = ""
	print("Hello There!!!")
	print("1. Enter the text manually\
		2. Read from a file\n")
	if input() == '1':
		content = input("Enter the text\n")
	else:
		fileName = input("Enter the complete path")
		with open(fileName, "r") as fileName:
			content = fileName.read()
	import re
	content = re.sub("\s+"," ", content)
	print("The content is ready\n\
		Enter the name of the file to save")
	with open("/home/bpg168/TypeEm/"+input(), "w") as fileSave:
		fileSave.write(content)