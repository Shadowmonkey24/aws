"""
Important: This Technology Module is broken down into 9 different sections:

Technology
Compute
Storage
Networking and Content Delivery
Databases
Analytics
Deploying/Managing Infrastructure
Monitoring
Support
At the beginning of each section you'll see a lesson like this one with a motivational (and completely real) Star Wars quote, along with resources that may come in handy for that section.

At the end of each section there is also a summary of the important points to remember.

Enjoy!

Resources you might find handy for this Technology section:

Official AWS Certified Cloud Practitioner Exam Guide: https://d1.awsstatic.com/training-and-certification/docs-cloud-practitioner/AWS-Certified-Cloud-Practitioner_Exam-Guide.pdf

AWS Shared Responsibility Model: https://aws.amazon.com/compliance/shared-responsibility-model

AWS Global Infrastructure Map (regions, availability zones): https://aws.amazon.com/about-aws/global-infrastructure

Edge Locations: https://aws.amazon.com/cloudfront/features/?whats-new-cloudfront.sort-by=item.additionalFields.postDateTime&whats-new-cloudfront.sort-order=desc
"""

"""Cloud Deployment

cloud ("public")
    - Cost savings
    - Scalability
    - Flexibility
    Infrastucture available to the genral public on the internet
    Ownd by an organization selling cloud services 

hybrid
    comprised of two or more clouds (private, public)
    Bound together to enable data and applications portability

on-premises ("private")
    - Privacy
    - Total control
    - Dedicated resources
    Infrastucture solely for one organization
    My be outsoursed or owned, on-premises or off-premises
    Ownd by an organization selling on-premises services
"""

"""AWS Connectivity Options

site-to-site VPN

cloud <------------------> on-premises
("public")                 ("private")

-Encrypted
-uses public internet
-fast to set up


AWS Direct Connect

cloud <------------------> on-premises
("public")                 ("private")

-Dedicated physical connection
- Bypasses publilc internet; uses dedicated privet network
(not encrypted by default)
-faster and more expensive
-takes longer to set up
"""

"""AWS Infrastructure Concepts

Availability Zone

A single data center or group of data centers within a region,
each with redundant power, networking and connectivity, housed in
separate facilities.

region (e.g., us-east-2)
has 3 Availability Zones ant the time of writing

Edge Location

A site that amazon coudfront uses to store cached copies of your
content closer to your customers for faster delivery.

"""

"""Important Points to Remember: Technology

WAYS TO WORK WITH AWS
    AWS Management Console (browser)
    Programmatic access
• From your local machine - both require access key IDs and secrets
• Software Developer Kit (SDK)
    Command Line Interface (CLI)
• AWS CloudShell
    Browser-based; doesn't require access key ID DEPLOYMENT MODELS
    Public cloud
    On-premises
    Hybrid
        Connectivity: Site-to-site VPN or direct connect

Availability Zone

A single data center or group of data centers within a region,
each with redundant power, networking and connectivity, housed in
separate facilities.

region (e.g., us-east-2)
has 3 Availability Zones ant the time of writing

Edge Location

A site that amazon coudfront uses to store cached copies of your
content closer to your customers for faster delivery.

- High availability = 2 or more AZs
- withstand environmental desaster = deploy to 2 or more regions

"""