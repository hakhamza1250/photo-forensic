print(''' 
#####################################################################
#     _____  ________   ______   _______   __       __  __      __  #
#    |     \|        \ /      \ |       \ |  \     /  \|  \    /  \ #
#     \$$$$$| $$$$$$$$|  $$$$$$\| $$$$$$$\| $$\   /  $$ \$$\  /  $$ #
#       | $$| $$__    | $$__| $$| $$__| $$| $$$\ /  $$$  \$$\/  $$  #
#  __   | $$| $$  \   | $$    $$| $$    $$| $$$$\  $$$$   \$$  $$   # 
# |  \  | $$| $$$$$   | $$$$$$$$| $$$$$$$\| $$\$$ $$ $$    \$$$$    #
# | $$__| $$| $$_____ | $$  | $$| $$  | $$| $$ \$$$| $$    | $$     #
#  \$$    $$| $$     \| $$  | $$| $$  | $$| $$  \$ | $$    | $$     #
#   \$$$$$$  \$$$$$$$$ \$$   \$$ \$$   \$$ \$$      \$$     \$$     #
#                                                                   #
#            Coded By : Alex            * photo forensic *          #
#####################################################################                                                               
                                                                 
''')

import sys
choice = raw_input("Select your choice \npress [1] to extract metadata. \npress [2] to delete metadata.\n[-]write (exit) to leave.\n>> ")
if choice =="1":
    from PIL import Image
    from PIL.ExifTags import TAGS
    path=raw_input("enter the path of image:")

    dict_dict = {}
    try:
        i = Image.open(path)
        info = i._getexif()
        for tag, value in (info.items()):
            decoded = TAGS.get(tag, tag)
            dict_dict[decoded] = value
        type_of_phone= dict_dict['Make']
        flash=dict_dict['Flash']
        GPSInfo=dict_dict['GPSInfo']
        DateTimeOriginal=dict_dict['DateTimeOriginal']
        Software=dict_dict['Software']
        Model=dict_dict['Model']
        print "[+]The type of camera or Phone :"+type_of_phone
        

        if flash!=0:
            print "[+]Flash is open"
        else:
            print "[+]Flash is not open"
        print"[+]GPSInfo:"+str(GPSInfo)
       
        print "[+]DateTimeOriginal:"+DateTimeOriginal
     

        print "[+]Software:"+Software
       

        print "[+]Model:"+Model


    except:
        print "\n [-] Ops!! sorry we cant find anything !"
elif choice =="2":
    import piexif

    path=raw_input("enter the path of image:")

    data = piexif.load(path)

    piexif.remove(path)
    empty = piexif.load(path)
    print "\n [+] Done ^__^ "

elif choice == "exit":
    sys.exit()
else :
    print " Wrong choice \n "
    
