"""
Resources you might find handy for this Compute section:

All Compute products: https://aws.amazon.com/products/compute
EC2 instance types: https://aws.amazon.com/ec2/instance-types
EC2 instance purchasing options: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-purchasing-options.html
PuTTY download (to SSH from Windows 8 or lower): https://www.putty.org
"""

"""EC2 (Elastic Compute Cloud)
All Compute products: https://aws.amazon.com/products/compute

EC2 instance types: https://aws.amazon.com/ec2/instance-types

EC2 instance purchasing options: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-purchasing-options.html

A virtual server that you rent in AWS called an "instance"

- easy to scale (auto scale)
- reliable
- use with other services
- only pay for what you use 

Shared Responsibility Model for EC2

AWS Responsibility
- Physical hardware and network
- Hypervisors (allows you to create Virtual machines)
- Elastic Block Store (EBS) storage system

Customer Responsibility
- Software running on the instance, including operating system and applications
(maintaence, patching, ect.)
- Security groups and network access control lists

type        | Descriptions
------------|------------------------------------
On-demand   |• Default option
Instances   |Pay by the second while instance is running (minimum 60 seconds)
            |
Reserved    |• Reserve instances for 1-3 years (e.g., database server)
Instances   |• Savings of up to 70%
            |
Spot        |• Bid on unused EC2 capacity
Instances   |• Savings up to 90%, but can lose instance at any time
            |
Dedicated   |• Book an entire physical server and bring your own licenses
Hosts       |• Can be purchased on-demand or reserved
            |
Dedicated   |• Ensures no other AWS customer shares your hardware
Instances   |• Pay by the hour ons
            |
Capacity    |• Reserve capacity for instances in a specific 
Reservations|   availability zone for any duration
"""

"""SSH (Secure Shell)

Protocal used to securely log into other computers and run commands from the 
command line.

Uses TCP protocol on Port 22

Options for Connecting to EC2 Instances

YOUR OPERATING SYSTEM   EC2 INSTANCE        OPTIONS TO CONNECT
                        OPERATING SYSTEM
Linux                   Linux               SSH client
Mac                     Linux               SSH client
Windows 10 or later     Linux               PowerShell or cmd
Windows 8 or earlier    Linux               PuTTY
Windows (any version)   Windows             Remote Desktop Protocol (RDP)
Any (uses browser)      Linux               EC2 Instance Connect
                                            Usually easiest option

"""

"""Elastic Load Balancing 

the elastic load balancer will direct traffic in a was to avoid a server over load
it will balance the load

Benefits of using elastic load balancing 

- Managed service
    - AWS guarantees up time 
    - AWS handles maintenance, upgrades, etc.
- Distributes the load across mutiple instances, and across availability zones
- Can handle instance failures by doing regular health checks
- Only exposes a single endpoint (DNS) to your appliction 

There are 3 types of load balancer 

- Application Load Balancer (ALB)
    - Handels HTTP/HTTPS  traffic 
    - Layer 7
- Network Load Balancer (NLB)
    - Handles TCP, UDP, TLS
    - Ultra-high performance, ultra-low latencies
    - Layer 4
- Gateway Load Balancer (GLB)
    -Used to deploy and manage third-party virual appliances such as firewalls,
    intruion detection and prevention systems
(there is a classic load balancer but this is a retired)

"""