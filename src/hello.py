import area

# while running in file.py the "__name__" will be "__main__"
# if doesn't file directly run the "__name__" will be "module name"

print(f"IN Hello.py = {area.findArea(5, 6)}")

try :
    print(1/0)
except Exception as e :
    print(type(e).__name__)