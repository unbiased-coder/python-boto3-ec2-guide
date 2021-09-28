import boto3_helper

print ('Getting boto3 session...')
session = boto3_helper.init_aws_session()
print ('Getting EC2 resource object...')
ec2 = session.resource('ec2')
print ('Provisioning EC2 instance...')
ret = ec2.create_instances(ImageId='ami-05f7491af5eef733a', MinCount=1, MaxCount=5)
print ('Process completed')
print (ret)