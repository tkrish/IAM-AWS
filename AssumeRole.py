import json
import boto.s3.connection
import boto3


client = boto3.client('sts')

RoleSessionNameOption = input('Which role would you like to assume \n'+ 
	'1 Developer,\n'+
	'2 X-IAMAdmin,\n'+
	'3 X-AdminAccess\n'+
	'Please enter the number for your selection: ')

RoleSessionName = 'Developer'

if RoleSessionNameOption == '2':
    RoleSessionName = 'X-IAMAdmin'
elif RoleSessionNameOption == '3':
    RoleSessionName = 'X-AdminAccess'

TokenCode = input('Current MFA token (6 digits) from: ')
# print(RoleSessionName)

response = client.assume_role(
    RoleSessionName = RoleSessionName,
	RoleArn=('arn:aws:iam::477275408388:role/'+RoleSessionName),
    SerialNumber='arn:aws:iam::477275408388:mfa/srikrishna.tadinada@xero.com',
    TokenCode = TokenCode
)

#  print(RoleSessionName + ' ' + TokenCode)

 print(response)