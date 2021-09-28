import boto3_helper

print ('Getting boto3 session...')
session = boto3_helper.init_aws_session()
print ('Getting EC2 client object...')
ec2 = session.client('ec2')

instance_id_list = []

instance_list = ec2.describe_instances()
for reservation in instance_list['Reservations']:
    for instance in reservation['Instances']:
        instance_id_list.append(instance['InstanceId'])

ec2_resource = session.resource('ec2')
for instance_id in instance_id_list:
    instance = ec2_resource.Instance(instance_id)
    ret = instance.terminate()
    print ('Terminating: %s'%instance_id)
    print (ret)

print ('Process completed')
