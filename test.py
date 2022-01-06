    if(facultypanel.tkslot.get()==""):
        facultypanel.fperror.config(text="Enter Slot!")
        return
    if(facultypanel.tkday.get()==""):
        facultypanel.fperror.config(text="Enter Day!")
        return
    if(facultypanel.tkmonth.get()==""):
        facultypanel.fperror.config(text="Enter Month!")
        return
    if(facultypanel.tkyear.get()==""):
        facultypanel.fperror.config(text="Enter Year!")
        return





        import cv2
 
img = cv2.imread('/home/img/python.png', cv2.IMREAD_UNCHANGED)
 
print('Original Dimensions : ',img.shape)
 
scale_percent = 60 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
  
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions : ',resized.shape)
 
cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()