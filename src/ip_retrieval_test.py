import boto3
from moto import mock_ec2
from awsssh import AwsSSH

@mock_ec2
def test_ip_retreival_success():
  client = boto3.resource('ec2', region_name='us-east-1')
  client.create_instances(
      ImageId='test', 
      MinCount=1, MaxCount=1,
      NetworkInterfaces=[
          {
              'AssociatePublicIpAddress': True,
              'DeviceIndex': 0
          },
      ],
      TagSpecifications=[
          {
              'ResourceType': 'instance',
              'Tags': [
                  {
                      'Key': 'Name',
                      'Value': 'test1'
                  },
              ]
          },
      ])
  session = AwsSSH("test1")
  response = ""
  try:
    response = session.retrieve_ip()
  except Exception as e:
    response = str(e)

  assert response != "Host not found"
  print("test_ip_retreival_success\t\ttest\tpassed")

@mock_ec2
def test_ip_successful_retreival_fail():
  client = boto3.resource('ec2', region_name='us-east-1')
  client.create_instances(
      ImageId='test', 
      MinCount=1, MaxCount=1,
      NetworkInterfaces=[
          {
              'AssociatePublicIpAddress': True,
              'DeviceIndex': 0
          },
      ],
      TagSpecifications=[
          {
              'ResourceType': 'instance',
              'Tags': [
                  {
                      'Key': 'Name',
                      'Value': 'test1'
                  },
              ]
          },
      ])
  session = AwsSSH("invalid_tag")
  response = ""
  try:
    response = session.retrieve_ip()
  except Exception as e:
    response = str(e)

  assert response == "Host not found"
  print("test_ip_successful_retreival_fail\ttest\tpassed")

def main():
  print("Running tests...")
  test_ip_retreival_success()
  test_ip_successful_retreival_fail()

if __name__ == '__main__':
    main()