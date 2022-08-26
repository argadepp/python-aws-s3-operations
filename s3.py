from ast import arg
from genericpath import exists
import boto3
import argparse
from colorama import Fore, Back, Style
import colorama
from ipykernel import kernel_protocol_version
from pyparsing import empty

s3_arg_parser = argparse.ArgumentParser(description="This Module is used for AWS S3 service")
s3_arg_parser.add_argument("access_key",help="enter the vaules of aws_aacess_key_id")
s3_arg_parser.add_argument("secreate_key",help="enter the vaule of aws_secreate_access_key")
s3_arg_parser.add_argument("-l","--list",help="get the list of buckets",action="store_true")
s3_arg_parser.add_argument("-c","--colo",help="get color")
s3_arg_parser.add_argument("-b","--bucket_name",help="enter the bucket name ")
s3_arg_parser.add_argument("-f","--file_name" ,help="specify the name of file ")
args = s3_arg_parser.parse_args()



# s3_client = boto3.resource('s3',aws_access_key_id=aws_access_key ,
#  aws_secret_access_key=aws_secret)
a_key=''
s_key=''
###################### Get The List of all buckets #############
def getListof_Buckets(a_key , s_key ):
  s3_client = boto3.resource('s3',aws_access_key_id=args.access_key ,
 aws_secret_access_key=args.secreate_key)

  s3_list = s3_client.buckets.all()

  for name in s3_list:
    print("Bucket_Name="+name.name)
###################### Get the list of buckets with color ################
def getListof_Buckets_wc(a_key , s_key ):
  s3_client = boto3.resource('s3',aws_access_key_id=args.access_key ,
 aws_secret_access_key=args.secreate_key)

  s3_list = s3_client.buckets.all()

  for name in s3_list:
    print(Fore.RED+"Bucket_Name="+name.name)


################ Get the list of Objects in a buckets ###############
def getListof_Buckets_sp(a_key , s_key ,b_name ):
  s3_client = boto3.resource('s3',aws_access_key_id=args.access_key ,
  aws_secret_access_key=args.secreate_key)

  myBucket = b_name

  mb = s3_client.Bucket(name=myBucket)
  lists = []
  for objs in  mb.objects.all():
     lists.append(objs.key)
  
  print(lists)  



def uploadFile(a_key, s_key ,b_name ,f_name):
  s3_client = boto3.resource('s3',aws_access_key_id=args.access_key ,
  aws_secret_access_key=args.secreate_key)
  s3_client.Bucket(b_name).upload_file(Filename=f_name,Key=f_name)
  print("File is uploaded successfully !!!!!!!!!!!!!!")



if args.colo == 1 :
  getListof_Buckets_wc(a_key=args.access_key , s_key=args.secreate_key) 
elif args.list:
  getListof_Buckets(a_key=args.access_key , s_key=args.secreate_key)
elif args.access_key != empty & args.secreate_key != empty & args.bucket_name != empty:
  getListof_Buckets_sp(a_key=args.access_key,s_key=args.secreate_key,b_name=args.bucket_name)
elif args.access_key != empty & args.secreate_key != empty & args.bucket_name != empty & args.file_name != empty:
  uploadFile(a_key=args.access_key,s_key=args.secreate_key,b_name=args.bucket_name,f_name=args.file_name)
else:
  print("Not specified any thing")






