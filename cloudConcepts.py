""" Cloud Concepts
1.Compute
2.Database
3.Storage
4.Network
5.Security

Foundational Services

1. Compute Elastic Compute Cloud (EC2)
2. Database Relational Database Service (RDS) and DynamoDB
3. Storage Simple Storage Service (S3) 
4. Networking Virtual Private Cloud (VPC)
5. Security Identity and Access Management (IAM)

Term            Description                     Example

Elasticity      the ability to adapt to         Amazon.com handling a huge
                workload changes                spike in traffic on prime day
                (usually bynamic, short-term)

Scalability     the ability to handle           Scale up a data bace because the
                increased workload by adding    size has grown over time
                resources
                (usually more static, long-term)

Availability    the ability to continue         When a power outage causes one
                even if some comonents          data center to go down,
                fails                           traffic is routed to another

Reliability     the ability to function         99.99% uptime for EC2 
                consistently and corectly       instance during a given month
                when expected                   

Agility         the ability to rapidly          Launch a new business 
                develop, test and launch        application in days rather than
                applications to deliver         months
                business value

Global Reach    the ability to get closer       26 geographic regions around the
                to your costomers through       world
                a global infrastructure

Pay-as-you-     only pay for what you use       an EC2 instance only used for 2 hr;
go pricing      and only when you need it       only pay for 2 hrs

Economies of    Because of their size,          Amazon purchases servers at
scale           AWS can purchase things more    a fraction of the cost that
                cheaply than an individual      you could, and passes the 
                organization can                savings on to you

Cloud Archecture Design Principles

1. Design for failure
2. Decouple Componets  use loose coupling or micoservices (vs monilithic)
3. Impement elasticity
4. think parallel   example 1 system renning for 24 hrs vs 24 system running for 1hr


Cloud Adoption Framework (CAF)

Leverages AWS exerience and beat practices to transform and accelerate business
outcomes by using AWS

Six pillars

1. Business 
2. People
3. Governance
4. Paltform
5. Security
6. Operations

please look at the docs for better understanding of the CAF
https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/foundational-capabilities.html



Important Points to remember

Benefits
    - Globle reach: data senters around the world
    - High availability: continues functioning even when one componet 
    (server, data center, etc.) goes down
    - Cost savings: reduces up-front cost ("CapEX") and ongoinh costs ("OpEx")
        - Only pay for what you use
        - Right-sizing infrastructure means you dont't have to "guess" capacity
        - Managed services reduce your IT overhead/spend

Design Principles
    - Design for failure: assume things will fail, and architect for that
    - Loose coupling: reduse the dependency between components
    - Elasticity: components should be able to scale up and down based on needs
    - Reliability: perform an intended function correctly and consistently
        when expected to
    - Review the Well-Architected Framework:
    https://docs.aws.amazon.com/wellarchitected/latest/framework/definitions.html

Cloud Adoption Framework (CAF) 

    - Leverage AWS experience and best practices to transform and accelerate
    business outcomes by using AWS

    - Understand what makes up the Six pillars:
        1. Business
        2. People
        3. Governance
        4. Platform
        5. Security
        6. Operations
    - Please look at the docs for better understanding of the CAF
        https://docs.aws.amazon.com/wellarchitected/latest/framework/definitions.html


"""

"""Security and Compliance

Resources to keep handy for this module:

Official AWS Certified Cloud Practitioner Exam Guide: https://d1.awsstatic.com/training-and-certification/docs-cloud-practitioner/AWS-Certified-Cloud-Practitioner_Exam-Guide.pdf

AWS Shared Responsibility Model: https://aws.amazon.com/compliance/shared-responsibility-model

AWS Security, Identity and Compliance Products: https://aws.amazon.com/products/security


AWS Shared Responsibility Model

Customer Responsibility
    - Responsible for Security "in" the Cloud
        - Customer Data
        - Platform, Applications, Identity & Access Management (IAM)
        - Operation System, Network & Firewall Configuration
            - Clent-side data, encryption & data integrity authentication
            - server-side encryption (file system and/or data)
            - Network Traffic Protection

AWS Responsibility
    - Responsible for Security "of" the Cloud
        - Compute
        - Storage
        - Networking
        - Database
        - AWS Global Infrastructure
            - Regoins
            - Availability Zones
            - Edge Locations

Inferucture as a Service (IaaS)
You manage
    - Applications
    - Data
    - Runtime
    - Middleware 
    - OS
AWS manages
    - Networking
    - Virtualization
    - Storage
    - Servers

Platform as a Service (PaaS)
You manage
    - Applications
    - Data
AWS manages
    - Runtime
    - Middleware
    - OS
    - Networking
    - Virtualization
    - Storage
    - Servers

Software as a Service (SaaS)
AWS manages
    - Applications
    - Data
    - Runtime
    - Middleware
    - OS
    - Networking
    - Virtualization
    - Storage
    - Servers

    
Identity and Access Management (IAM)
Service used to securely control access to your AWS resources
Controls authentication (who) and authorization (what they can do)


IAM Identity Center (formerly AWS Single Sign-on or SSO)

Provides a single sign-on (SSO) 
- All AWS accounts (leveraging AWS Organizations)
- Cloud-based applications like Salesforce, Box, Microsoft 365
- EC2 instaces running windows
- SAML 2.0-enabled applications 
- Can use mutiple identity providers, such as Active Directoy,
Okta, the built-in IAM store and more

with IAM
Manage identities and access in a single AWS account
Not using AWS Organizations

With IAM Identity Center
Manage identities and access across multiple AWS accounts and applications
Use with AWS Organizations
The recommended way to manage 
Console access, command line and programmatic access (i.e., access
keys IDs and secret access keys)


USERS

Root Users vs IAM Users
Root users 
- one per account
- Unrestricted access
- Difficult to restrict or revoke access
Can preform the following tasks:
    - close an AWS account
    - Change an AWS support plan
    - Changed AWS account settings

IAM users 
- Multiple per account
- Users can be deleted or disabled
- Easy to restrict access

Best Practices
- work in your IAM account,
not the  root account
    - Set up IMA users with least number of permissions needed
- Don't create access keys for the root account
(or delete them if you have them)
- Enable multi-factor authentication


USERS GROUPS

ROLES

An IAM role is an identity you can create that has specific permissions
with credentials that are valid for short durations. Roles can be
assumed by entities that you trust

roles similar to a user (an idntity with permissions)
Does not have credentials (password or keys)

example an EC2 instance trying to talk to E3 and cloudWatch

option 1 
- Create an IAM user for the app with appropriate permissions
- Hard-code user Credentials in the app or on EC2 instance file system
and retrieve them at runtime
 
Or
the only one you should be using
option 2
- Create an IAM role for the app with appropriate permissions
- When creating the EC2 instance, assign it this role
- No credentials required


IAM Policies

POLICY
Who can do what to which resources and when

"Allow IAM user to rotate their own credentials programmatically
and in the console."
or 
"Allow a user to start and stop EC2 instances."

this is the basic syntax of a policy
{
    "Statement": [
        {
            "Effect": "effect", (for effect there are 2 options are to allow or deny. deny is the default)
            "Action": "action" (this will correspond to the API calls to AWS services)
            "Resource": "arn"(amazon resource name. this is the resource that you want to apply the permisson to)
            "Condition": {
                "condition": {
                    "key": "value" (condition are optional, and they control when the policy should apply)
                    }
                }
            }
        ]
    }
}

example
{
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:StartInstances",
                "ec2:StopInstances"
                ],
            "Resource": "arn:aws:ec2:*:*:instance/*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/Owner": "${aws:username}"
                    }
            }
        },
        {
            "Effect": "Allow",
            "Action": "ec2:DescribeInstances",
            "Resource": "*"
        }
    ]
}


multi-factor authenitcation is needed
you can remove it needed in your IAM go to My security credentials

ACCESS KEYS

in your IAM go to users go to the user your want to make
a access key for in summary click "create access key " 
you can only have 2 at a time

in account settings you can change password policy
so you can make password expire after a certain amount of time
or you can make it expire after a certain amount of inactivity
and so on...

IAM Best practices
- Use an IAM user for day-to-day work, NOT the root user
- Use roles to give premissions to AWS services
(e.g., EC2 instances)
- Don't share credentials (user name,passwords and more ...)
- Assign permissions to groups (made up of users) rather than
individual users
- When assigning permissions (policies), give the least amount possible
- Enforce MFA and strong password polices 
- Use the IAM Credentials Report to audit permissions

AWS Security, Identity and Compliance Services

Security and Compliance Services

Infrastructure Protection: AWS Shield
Infrastructure Protection: AWS Web Application Firewall (WAF)
Data protection: AWS Key Management System (KMS) and CloudHSM
Data protection: AWS Certificate Manager (ACM)
Data protection: AWS Secrets Manager
Data protection: Amazon Macie
Detection: Amazon Inspector
Detection: Amazon GuardDuty
Detection: AWS Config
Detection: AWS Security Hub
Incident Response: Amazon Detective
Compliance: AWS Artifact



"""