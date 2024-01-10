import os


f = open("guru99.txt","r+")
strInteger = f.readline()
f.close()
integer = int(strInteger)
# Absolute path of a file
old_name = r"C:\xampp\htdocs\assignment_3_sd4_helper.php"
new_name = r"C:\xampp\htdocs\assignment_3_sd4_helper.php.txt"

# Renaming the file
if integer%2==0:
    os.rename(old_name, new_name)
    os.system(f'pycharm64.exe {new_name}')
else:
    os.rename(new_name, old_name)

f = open('guru99.txt', 'w')
f.write(str(integer+1))
f.close()
