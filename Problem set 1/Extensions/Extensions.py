file_name = input("File name: ")
file, extension = file_name.split(".")
if extension == "gif" :
	print("image/gif")
elif extension =="jpg" or extension =="jpeg" :
	print ("image/jpeg")
elif extension =="png" :
	print ("image/png")
elif extension =="pdf" :
	print ("document/pdf")
elif extension =="txt" :
	print ("document/text")
elif extension =="zip" :
	print ("file/zip")
else:
	print("application/octet-stream")
