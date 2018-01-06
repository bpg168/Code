from io import BytesIO
import pyexcel
data = [
					[1, 2, 3],
					[4, 5, 6]
		] 
ioInstace = BytesIO()
sheet = pyexcel.Sheet(data)
sheet.save_to_memory("ods", ioInstace)
sheet.save_as("writeTest.ods")