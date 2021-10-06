import cv2
import dropbox
import time
import random

start_time=time.time()

def takesnapshot():
    number=random.randint(0,100)
    #initializing cv2
    videocaptureobject=cv2.VideoCapture(1)
    result=True
    while(result):
        #read the frames while the camera is on 
        ret,frame=videocaptureobject.read()
        #cv2.imwrite() method is used to save an image
        #to any storage device
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False    
    return img_name
    print("snapshot taken")    

    #release the camera
    videocaptureobject.release()
    #closes all the window that might be opened while this process
    cv2.destroyAllWindows()    

takesnapshot()    




def upload_file(img_name):

    access_token = 'c1gsHzegWOMAAAAAAAAAAReaYEVXAaeka_dwbLkimAHzWvJD07jGY9utBvoLI45u'
    file =img_name
    file_from=file
    file_to="/cp-102/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from,"rb") as f:
        dbx.files_upload(f.read(),file_to, mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")
    
def main():
    while(True):
        if((time.time()-start_time)>=15):
            name=takesnapshot()
            upload_file(name)


main()

