""" Cloud Concepts
Resources to keep handy for this module:

Official AWS Certified Cloud Practitioner Exam Guide: https://d1.awsstatic.com/training-and-certification/docs-cloud-practitioner/AWS-Certified-Cloud-Practitioner_Exam-Guide.pdf

AWS Well-Architected Framework: https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html

Cloud Adoption Framework:

Home page with assessment: https://aws.amazon.com/cloud-adoption-framework/
Pillars: https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/foundational-capabilities.html


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
