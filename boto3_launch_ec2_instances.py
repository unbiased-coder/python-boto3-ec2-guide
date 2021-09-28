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

print ('Starting/Launching list of instances: ', instance_id_list)
ret = ec2.start_instances(InstanceIds=instance_id_list)
print ('All instances were signaled to launch/start')
print (ret)
