file_name = raw_input("What do you want to name your file?")
file_path = "/home/pi/Desktop/"+file_name + ".txt"

file_contents = raw_input("What do you want your file to contain?")

text_file = open(file_path, "w")
text_file.write(file_contents)
text_file.close()
