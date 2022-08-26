from ntpath import join
from os import access
import uuid
import boto3
import argparse
from pyparsing import empty
from requests import delete
from traitlets import default

################# Arguments ######################################################
myArgs = argparse.ArgumentParser(description="Upload file on specified S3 bucket \n")
myArgs.add_argument("-c","--create",help="create the new bucket \n",action="store_true")
myArgs.add_argument("-o","--option",help="enter the options\n" , action="store_true")
myArgs.add_argument("akey",help="enter the access key\n")
myArgs.add_argument("-u","--upload",help="choose upload option\n",action="store_true")
myArgs.add_argument("-d" , "--delete" , help="delete the specified bucket",action="store_true")
myArgs.add_argument("skey",help="enter the secreate key\n")
myArgs.add_argument("-obj","--objlist",help="to get the list of objects in bucket\n",action="store_true")
myArgs.add_argument("-l","--list",help="get the list of buckets\n",action="store_true")
myArgs.add_argument("-b","--bname",help="enter the buckate name\n")
myArgs.add_argument("-f","--fname",help="enter the file name\n")
args = myArgs.parse_args()
####################################################################################

s3_client = boto3.resource('s3',aws_access_key_id=args.akey ,
 aws_secret_access_key=args.skey)


################ Get the list of buckets ################

def getList():
    blist = s3_client.buckets.all()
    for buckets in blist:
        print(buckets.name)

############## Upload file to Bucket ####################
def uploadFile(bname,fname):
    s3_client.Bucket(bname).upload_file(Filename=fname,Key=fname)
    print(f"{fname} File is uploaded to {bname}")

############# to get the list of objects in specific bucket ##########
def getObject_list(bname):
    objls = s3_client.Bucket(name=bname)

    for objs in objls.objects.all():
        print(objs.key)

########### Create the bucket ##########
def bucketName(pfix):
    return ''.join([pfix,"-" , str(uuid.uuid4())])

def create_bucket(bname):
    bname = bucketName(bname)
    s3_client.create_bucket(Bucket=bname, CreateBucketConfiguration=
    {'LocationConstraint':'ap-south-1'})
    print(f"{bname} is created successfully !!!!!")
   
        
########### Delete the bucket ##########

def delete_bucket(bname):
   s3_client.Bucket(bname).delete()
   print(f"{bname} is deleted successfully !!!!!!!")
    

############# Switch Case ##############    
def mySwitchCase(option):
    
    match option:
        case args.delete:
            return delete_bucket(args.bname)
        case args.list:
            return getList()
        case args.create:
            create_bucket(bname=args.bname)
        case args.objlist:
            try:
                getObject_list(bname=args.bname)   
            except:
                print("Bucket name is need to specify , please enter it ")     
        case args.upload :
            try:
                if args.bname != empty & args.fname != empty:
                  uploadFile(bname=args.bname , fname= args.fname)
            except:
                print("You haven't entered correct bucket name or file name ")     
            
        
        case default:
            return "Please choose the options"    


mySwitchCase(args.option)




