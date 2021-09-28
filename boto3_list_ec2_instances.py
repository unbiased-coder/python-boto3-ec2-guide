import boto3_helper

print ('Getting boto3 session...')
session = boto3_helper.init_aws_session()
print ('Getting EC2 client object...')
ec2 = session.client('ec2')
instance_list = ec2.describe_instances()
for reservation in instance_list['Reservations']:
    for instance in reservation['Instances']:
        print ('Instance: %s, type: %s, '%(instance['InstanceId'], instance['InstanceType']), end='')
        for network_interface in instance['NetworkInterfaces']:
            print ('IP: %s'%network_interface['Association']['PublicIp'])
