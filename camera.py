import cv2
import dropbox
import time
import random

startTime=time.time()
def take_snapshot():
    try:
        number=random.randint(0,100)
        vCO=cv2.VideoCapture(0)
        result=True
        while(result):
            ret,frame=vCO.read()
            imageName='Img'+str(number)+'.png'
            cv2.imwrite(imageName,frame)
            startTime=time.time()
            result=False
        return imageName
        print("Snapshot taken")
        vCO.release()
        cv2.destroyAllWindows()
    except:
        pass

def upload_files(imgN):
    accessToken="hlgwiXFNwooAAAAAAAAAAUMMMsBlrLIlMaym8sSCyBD7sllEwdkPO6TIMbP9vkm3"
    file_from=imgN
    file_to='/Py/'+(imgN)
    dbx=dropbox.Dropbox(accessToken)
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print('File uploaded')
def main():
    while(True):
        if((time.time()-startTime)>=1):
            name=take_snapshot()
            if(name):
                 upload_files(name)
           
main()