
"""
aws is in 33 regions and has 105 Availability zones


AWS Regions
separate
geographically distinct locations on the planet

Availability Zones
physical locations within a region
each zone have at least 2 AZs 
most have 3
some have 6
they are fully isolated from each other
for compleate redundancy, you need to have at least 2 AZs in each region
separate facilities redundent power and a dedicated 


Network
purpoese built
higly available
low-latency
fully redundent parallel fiber network

Point of prescence (POP)
PoP
edge location 
regional edge location
cahhe servers
that talk to data centers

Amazon CloudFront 
Globle content delivery network (CDN)


A elastic load balancer distributes traffic across multiple targets, such as EC2 instances, in one AZ
An Application Load Balancer distributes traffic across multiple targets, such as EC2 instances, across 
multiple AZs in one region

aws uses costom hardware that is only used for aws apps
"""

"""
Instance

an instance is a virtual server running on Amazon EC2
there are 6 difent types of instances
each type has a different level of performance and cost
general purpose cpu, memory and network
compute optimized cpu, memory and network
memory optimized cpu, memory and network
storage optimized cpu, memory and network
accelerated computing optimized cpu, memory and network
high performance computing optimized cpu, memory and network

and you can chose difent instance sizes


AMI amazon machine image

is a template that contains a software configuration and application software
you must chose an ami when you launch an instance
you can chose an ami when you launch an instance
you can create an ami from an instance
you can share an ami with other aws accounts

Storage

EC2 can access discs attached to the host comp this is called instance store 
temporary block levle storage
you can also attach a amazon elastic block storage (EBS) volume for
persistent block level storage that acts like a raw, unformated exteral block device
it can act like EBS snapshot and stored in Amazon S3
EC2 also uses S3 to stor images of your AMI
you can also make a Elastic File System (EFS) that acts like a network file system

apps that run on your EC2 can 

Networking 
Vitual Privet Cloud (VPC)
lets you logically isolate your own virtual network
you can also use a default VPC
you can also create a VPC and manage it through the console
you lanch your EC2 instances into a VPC that you difine

your aws account comes with a default vpc to launch your EC2 instances into
you can also create a VPC and manage it through the console
you lanch your EC2 instances into a VPC that you difine

Security
you can also use a default VPC
you can also create a VPC and manage it through the console
you lanch your EC2 instances into a VPC that you difine


Amazon EBS Elastic Volume

with cloudwatch and aws lambda you can do automatic volume changes


Amazon EBS-Optimized Instances
EBS-optimized instances are instances that are optimized for Amazon EBS I/O performance.

you can launch certain EC2s as EBS-optimized with dedicaitd throughput with speeds 500 - 19000 Mbps
this will help with trafic on your EC2 lanes

Amazon EBS Snapshots 
EBS snapshots are point-in-time copies of your EBS volumes.
snapshots are incremental backups of your EBS volumes
you can create a snapshot of your EBS volume and store it in Amazon S3

you can use EBS direct api to read and compare snapshots
you can make any EBS snapshots even if the data is on-premises


you can use Fast Snapshot Restores to restore a snapshot to an EBS volume
to immediately restore a snapshot to an EBS volume, you can use the Fast Snapshot Restore feature
you can use Fast Snapshot Restores to restore a snapshot to an EBS volume
and this will be immediatly copyed to other regions
if you delet anything only the unique data to that shapshot will be removed


Data lifecycle manager (DLM) for EBS stapshots 
will clean and take snapshots of your EBS volumes
you can use DLM to manage the lifecycle of your EBS snapshots
all you have to do is tag your EBS volumes and DLM will take care of the rest

"""


"""
AWS Systems manager overview

is for managing your aws cloud of on-premise data centers

helps with operation problems


you can automate common and repetitive tasks such as maintence and dev tasks 
and use it to automate password resets OS patches and compliance issues
"""