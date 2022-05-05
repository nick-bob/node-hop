#!/usr/bin/env python3

import boto3
import sys
import json
import subprocess

class AwsSSH:
  target = ""    

  def __init__(self, _target):
    self.target = _target

  def retrieve_ip(self):
    ec2 = boto3.client('ec2')
    instance = ec2.describe_instances(
      Filters = [
        {
          'Name': 'tag:Name',
          'Values': [f'{self.target}']
        }
      ]
    )
    if len(instance["Reservations"]) == 0:
      raise Exception("Host not found")
    
    public_ip = json.loads(json.dumps(instance["Reservations"][0]["Instances"][0]["PublicIpAddress"], indent=2, default=str))
    return public_ip
  
  def start_sesstion(self):
    try:
      public_ip = self.retrieve_ip()
      subprocess.call(f'ssh ec2-user@{public_ip}', shell=True)
    except Exception as e:
      print(str(e))


def main():
    try:
        aws_ssh = AwsSSH(sys.argv[1])
        aws_ssh.start_sesstion()
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    main()