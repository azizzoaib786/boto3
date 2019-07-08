import boto3
import click

session = boto3.Session(profile_name='awsbot')
ec2 = session.resource('ec2')

@click.group()
def instances():
        "command for instances"

@instances.command('list')
def listinstances():
        "List EC2 instances"
        instances=[]
        for i in ec2.instances.all():
                print(', '.join((
                        i.id,
                        i.instance_type,
                        i.placement['AvailabilityZone'],
                        i.state['Name'],
                        i.private_ip_address,
                        )))
        return

@instances.command('stop')
def stopinstances():
        "Stop EC2 instances"
        for i in ec2.instances.all():
                print("stopping instance ....{0}".format(i.id))
                i.stop()

@instances.command('start')
def startinstance():
        "Start EC2 instances"
        for i in ec2.instances.all():
                print("start instance ....{0}".format(i.id))
                i.start()

if __name__ == '__main__':
        instances()
