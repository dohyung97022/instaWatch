from ..aws import AWS
from .instance import Instance


class EC2:
    image_id = 'ami-04876f29fd3a5e8ba'
    type = 't2.micro'
    security_group = 'default'
    region = AWS.Settings.region
    zone = region + 'a'
    key = 'vpc.pem'

    @classmethod
    def create_instance(cls, name: str) -> Instance:
        ec2 = AWS.session.resource('ec2', region_name=cls.region)
        instances = ec2.create_instances(
            ImageId=cls.image_id,
            KeyName=cls.key,
            MinCount=1,
            MaxCount=1,
            InstanceType=cls.type,
            SecurityGroups=[cls.security_group],
            TagSpecifications=[{
                'ResourceType': 'instance',
                'Tags': [{'Key': 'Name', 'Value': name}]
            }],
            Placement={'AvailabilityZone': cls.zone}
        )
        return Instance(instances[0])
