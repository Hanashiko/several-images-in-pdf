import img2pdf, os

path = ""
images_format = ".jpg"
result_file_name = "result.pdf"

images = [i for i in os.listdir(path) if i.endswith(images_format)]
pdf = img2pdf.convert(images)
with open(result_file_name, "wb") as result_file:
	result_file.write(pdf)
