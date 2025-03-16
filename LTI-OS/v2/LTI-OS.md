# LTI Applicant Tracking System (LTI-ATS)

## Software Description

LTI-ATS is a comprehensive applicant tracking system designed to streamline and optimize the entire recruitment process from job posting to hire. This powerful platform centralizes candidate data management, automates repetitive tasks, and provides powerful analytics to make data-driven hiring decisions. LTI-ATS serves as the central hub for all recruitment activities, enabling organizations to efficiently identify, attract, evaluate, and hire top talent while maintaining compliance with hiring regulations.

## Benefits of Using LTI-ATS

- **Increased Efficiency**  
  Automates manual tasks such as resume parsing, candidate screening, and interview scheduling, reducing time-to-hire by up to 40%. Recruiters can focus on high-value activities rather than administrative work.

- **Improved Candidate Quality**  
  Advanced filtering and screening tools help identify the best candidates quickly. The system uses data-driven matching to connect the right talent with the right positions.

- **Enhanced Collaboration**  
  Facilitates seamless communication between recruiters, hiring managers, and interviewers. All stakeholders can access relevant information and provide feedback within a single platform.

- **Data-Driven Decision Making**  
  Comprehensive analytics and reporting provide insights into recruitment performance metrics. Organizations can continuously improve their hiring process based on actionable data.

- **Better Candidate Experience**  
  Streamlined application process and automated communications keep candidates informed at every stage. Positive experiences enhance employer brand and increase acceptance rates.

- **Cost Reduction**  
  Reduces cost-per-hire by optimizing job posting distribution and minimizing time-to-fill positions. Efficient processes lower recruitment expenses and minimize productivity loss from unfilled positions.

- **Compliance Management**  
  Ensures adherence to hiring regulations and documentation requirements. Reduces legal risks associated with recruitment processes.

- **Scalability**  
  Easily handles fluctuations in hiring volume without requiring additional resources. Supports organizations through growth phases and seasonal hiring demands.

## Core Functionalities

1. **Centralized Candidate Database & Data Management**  
   - Store and organize all candidate profiles and application data in one place.

2. **Resume Parsing & Data Extraction**  
   - Automatically extract key information (e.g., work history, skills, education) from submitted resumes.

3. **Job Posting & Distribution**  
   - Seamlessly post job openings across multiple job boards, social media channels, and your company careers page.

4. **Candidate Screening & Filtering**  
   - Apply keyword matching, predefined criteria, and automated filters to shortlist the best candidates.

5. **Candidate Tracking & Pipeline Management**  
   - Monitor candidate progress through each stage of the hiring process in a visual pipeline.

6. **Interview Scheduling & Coordination**  
   - Integrate with calendar systems and automate scheduling to streamline interview setups.

7. **Communication Tools**  
   - Automate emails, notifications, and candidate follow-ups to keep all parties informed.

8. **Reporting & Analytics**  
   - Generate insights and metrics (e.g., time-to-hire, cost-per-hire) to continuously optimize the recruitment process.

9. **Collaboration Features**  
   - Enable recruiters and hiring managers to share feedback, notes, and evaluations within the system.

10. **Integration & Compliance Management**  
    - Connect with HRIS, onboarding tools, background check services, and ensure compliance with hiring regulations.


### Lean Canvas: Tool used = Canvanizer
Result in the images repo called lean-canvas.png


## 3 main use cases

This document outlines the three main use cases for the LTI Applicant Tracking System, along with UML diagrams representing the interactions between different actors and the system.

### Use Case 1: Job Requisition and Posting Management

This use case covers the process of creating job requisitions, approving them, and posting them to various channels. It involves primarily HR managers and recruiters who collaborate to define job requirements and distribute postings.

#### Key Activities:
- Creating and defining job requisitions
- Approving job requisitions
- Posting jobs to internal/external job boards
- Managing job posting lifecycle

#### UML Diagram:

```
@startuml
left to right direction
actor "HR Manager" as HRM
actor "Recruiter" as REC
rectangle "LTI-ATS System" {
  usecase "Create Job Requisition" as UC1
  usecase "Review and Approve Requisition" as UC2
  usecase "Post Job to Channels" as UC3
  usecase "Monitor Job Posting Performance" as UC4
  usecase "Edit/Update Job Posting" as UC5
  usecase "Close Job Posting" as UC6
  
  UC3 ..> UC5 : includes
  UC4 ..> UC5 : may lead to
  UC4 ..> UC6 : may lead to
}

HRM --> UC1 : initiates
HRM --> UC2 : approves
HRM --> UC6 : decides

REC --> UC1 : creates
REC --> UC2 : submits for approval
REC --> UC3 : distributes
REC --> UC4 : analyzes
REC --> UC5 : modifies
REC --> UC6 : implements
@enduml
```

#### Image in images --> LTI_use_case1.png


### Use Case 2: Candidate Application and Screening Process

This use case covers the entire candidate journey from application submission through initial screening. It involves candidates submitting applications and recruiters reviewing and filtering candidates based on criteria.

#### Key Activities:
- Candidate profile creation and application submission
- Resume parsing and data extraction
- Initial screening and filtering of applications
- Moving candidates through preliminary stages of the pipeline

#### UML Diagram:

```
@startuml
left to right direction
actor "Candidate" as CAN
actor "Recruiter" as REC
actor "HR Manager" as HRM

rectangle "LTI-ATS System" {
  usecase "Create Profile/Account" as UC1
  usecase "Submit Application" as UC2
  usecase "Parse Resume/CV" as UC3
  usecase "Screen Applications" as UC4
  usecase "Filter Candidates" as UC5
  usecase "Request Additional Information" as UC6
  usecase "Move to Interview Stage" as UC7
  usecase "Reject Application" as UC8
  
  UC2 ..> UC3 : triggers
  UC3 ..> UC4 : enables
  UC4 ..> UC5 : includes
  UC5 ..> UC7 : leads to
  UC5 ..> UC8 : leads to
}

CAN --> UC1 : registers
CAN --> UC2 : applies
CAN --> UC6 : responds to

REC --> UC4 : reviews
REC --> UC5 : applies filters
REC --> UC6 : requests
REC --> UC7 : advances
REC --> UC8 : declines

HRM --> UC4 : reviews
HRM --> UC7 : approves
@enduml
```

#### Image in images --> LTI_use_case2.png

### Use Case 3: Interview Management and Candidate Evaluation

This use case covers the process of scheduling interviews, collecting feedback, and making hiring decisions. It involves recruiters, interviewers, and HR managers collaborating to evaluate candidates.

#### Key Activities:
- Interview scheduling and coordination
- Interview feedback collection
- Candidate evaluation and scoring
- Decision making and offer generation

#### UML Diagram:

```
@startuml
left to right direction
actor "Recruiter" as REC
actor "Interviewer" as INT
actor "HR Manager" as HRM
actor "Candidate" as CAN

rectangle "LTI-ATS System" {
  usecase "Schedule Interviews" as UC1
  usecase "Prepare Interview Kit" as UC2
  usecase "Conduct Interview" as UC3
  usecase "Submit Interview Feedback" as UC4
  usecase "Review All Feedback" as UC5
  usecase "Make Hiring Decision" as UC6
  usecase "Generate Offer" as UC7
  usecase "Reject Candidate" as UC8
  usecase "Communicate Decision" as UC9
  
  UC1 ..> UC2 : includes
  UC3 ..> UC4 : leads to
  UC4 ..> UC5 : aggregated in
  UC5 ..> UC6 : enables
  UC6 ..> UC7 : results in
  UC6 ..> UC8 : results in
  UC7 ..> UC9 : triggers
  UC8 ..> UC9 : triggers
}

REC --> UC1 : coordinates
REC --> UC2 : creates
REC --> UC5 : reviews
REC --> UC9 : implements

INT --> UC2 : receives
INT --> UC3 : performs
INT --> UC4 : provides

HRM --> UC3 : participates in
HRM --> UC5 : analyzes
HRM --> UC6 : approves
HRM --> UC7 : authorizes
HRM --> UC8 : decides on

CAN --> UC3 : participates in
CAN --> UC9 : receives
@enduml
```

These three use cases represent the core functionality of the LTI-ATS system, covering the entire recruitment lifecycle from job posting to candidate selection. 

#### Image in images --> LTI_use_case2.png


## The database png is in Images --> LTI_database.png


## High level system design

The LTI-ATS system will be implemented as a modern, cloud-native application utilizing a microservices architecture deployed on AWS. This approach provides scalability, resilience, and flexibility to accommodate changing business requirements. The architecture will consist of domain-driven microservices, each with its own database, communicating through well-defined APIs and event-driven patterns.

### Business Domains and Microservices

The microservices architecture is organized around the following core business domains:

1. **Identity and Access Management Domain**
   - **User Service**: Manages all user accounts, authentication, authorization, and role-based access control across the system. Handles user profiles for all system actors (HR Managers, Recruiters, Interviewers, and Candidates).
   - **Business Value**: Provides centralized security and personalized experiences while ensuring appropriate data access across the platform.

2. **Job Management Domain**
   - **Job Requisition Service**: Handles the creation, approval workflow, and management of internal job requisitions prior to publishing.
   - **Job Posting Service**: Manages the external publication of approved job requisitions, distribution to multiple channels, and monitoring of posting performance.
   - **Business Value**: Streamlines the job creation process and optimizes job visibility across multiple platforms.

3. **Candidate Management Domain**
   - **Candidate Profile Service**: Manages candidate core data, profile information, and search capabilities.
   - **Application Service**: Handles the application process, status tracking, and pipeline management.
   - **Resume Processing Service**: Specializes in resume parsing, data extraction, and skills identification using AI.
   - **Business Value**: Provides a comprehensive view of candidates and automates the initial screening process.

4. **Interview Management Domain**
   - **Interview Scheduling Service**: Coordinates interview scheduling, calendar integration, and notification management.
   - **Interview Kit Service**: Manages interview templates, questions, and evaluation criteria.
   - **Feedback Collection Service**: Gathers, aggregates, and analyzes interviewer feedback.
   - **Business Value**: Streamlines the interview process and standardizes evaluation approaches.

5. **Decision and Offer Domain**
   - **Hiring Decision Service**: Manages the decision-making workflow, approvals, and justification.
   - **Offer Management Service**: Handles offer generation, approval, tracking, and acceptance/rejection.
   - **Business Value**: Accelerates the final stages of hiring and improves offer acceptance rates.

6. **Communication Domain**
   - **Notification Service**: Manages all system notifications, templates, and delivery across multiple channels (email, in-app, SMS).
   - **Business Value**: Ensures consistent, timely communication with all stakeholders throughout the recruitment process.

7. **Analytics and Reporting Domain**
   - **Reporting Service**: Provides standard and custom reports on recruitment metrics.
   - **Analytics Service**: Delivers advanced insights, predictive analytics, and performance dashboards.
   - **Business Value**: Enables data-driven recruitment strategies and continuous process improvement.

8. **Integration Domain**
   - **External Systems Integration Service**: Handles connections to job boards, HRIS, background check services, and other third-party tools.
   - **Business Value**: Provides seamless data flow between LTI-ATS and the organization's existing technology ecosystem.

### Communication Patterns

The LTI-ATS system employs a strategic combination of synchronous and asynchronous communication patterns:

1. **Synchronous Communication (REST/GraphQL APIs)**
   - **Used For**: 
     - User-facing operations requiring immediate responses
     - Simple CRUD operations
     - Data queries where consistency is critical
     - Service-to-service communication within the same domain
   - **Implementation**: 
     - REST APIs for straightforward resource operations
     - GraphQL for complex, aggregated data queries from the frontend
     - API Gateway for management, security, and throttling

2. **Asynchronous Communication (Event-Driven)**
   - **Used For**:
     - Cross-domain business processes (e.g., when a candidate is hired, notify HRIS)
     - Long-running operations (e.g., resume parsing, background checks)
     - System notifications and alerts
     - Operations that can tolerate eventual consistency
     - Loosely coupling services for better resilience
   - **Implementation**:
     - EventBridge for publishing domain events and orchestrating event-driven workflows
     - SQS for reliable, persistent message queuing and workload distribution
     - SNS for pub/sub messaging and broadcasting to multiple consumers
     - Step Functions for complex, stateful workflows (e.g., interview process, offer approval)

3. **Hybrid Patterns**
   - **CQRS (Command Query Responsibility Segregation)**:
     - Commands (write operations) often use synchronous communication
     - Queries (read operations) may use cached or denormalized data views updated asynchronously
   - **Saga Pattern**:
     - For distributed transactions across multiple services
     - Implemented via choreography (events) or orchestration (Step Functions)

### Database Technologies

Each microservice utilizes database technology aligned with its specific data requirements:

1. **Document Databases (Amazon DocumentDB)**
   - **Used By**: User Service, Interview Kit Service
   - **Rationale**: Well-suited for storing semi-structured, flexible user profiles and interview templates with varying attributes.

2. **Relational Databases (Amazon Aurora PostgreSQL)**
   - **Used By**: Candidate Profile Service, Application Service, Offer Management Service
   - **Rationale**: Provides ACID compliance for critical candidate data, supports complex queries for candidate filtering, and maintains referential integrity for application status tracking.

3. **NoSQL Key-Value Stores (Amazon DynamoDB)**
   - **Used By**: Job Posting Service, Interview Scheduling Service, Notification Service
   - **Rationale**: Offers high throughput and low latency for frequently accessed data like job postings and schedules, with flexible schema evolution.

4. **In-Memory Databases (Amazon ElastiCache)**
   - **Used By**: All services for caching frequently accessed data
   - **Rationale**: Reduces database load and improves response times for common queries, search results, and user sessions.

5. **Time-Series Database (Amazon Timestream)**
   - **Used By**: Analytics Service
   - **Rationale**: Efficiently stores and queries time-series metrics like application rates, time-to-hire, and recruitment funnel analytics.

6. **Data Warehouse (Amazon Redshift)**
   - **Used By**: Reporting Service, Analytics Service
   - **Rationale**: Supports complex analytical queries and data aggregation across the entire recruitment process.

7. **Object Storage (Amazon S3)**
   - **Used By**: Resume Processing Service, Document Management
   - **Rationale**: Cost-effective storage for documents, resumes, and attachments with strong durability and lifecycle management.

This domain-driven approach with specialized databases and strategic communication patterns enables the LTI-ATS system to maintain high performance, scalability, and resilience while addressing the specific needs of each recruitment function.

### Architecture Overview

The LTI-ATS is built on AWS using a domain-driven microservices approach where each microservice focuses on a specific business capability. Key components include:

1. **Frontend Layer**
   - React/Next.js single-page application hosted on S3
   - CloudFront CDN for global content delivery
   - Route 53 for DNS management
   - Backend-for-Frontend (BFF) pattern using API Gateway and Lambda

2. **Core Infrastructure**
   - AWS Cognito for authentication and user management
   - EventBridge for event-driven communication between services
   - AWS App Mesh for service discovery and traffic management
   - CloudWatch, X-Ray, and CloudTrail for monitoring and observability

3. **Microservices**
   - **User Service**: Manages user accounts, roles, and profiles (ECS Fargate + DocumentDB)
   - **Job Service**: Handles job requisitions and postings (ECS Fargate + DynamoDB)
   - **Candidate Service**: Manages candidate profiles and applications (EKS + Aurora PostgreSQL)
   - **Interview Service**: Coordinates interview scheduling and feedback (Lambda + DynamoDB)
   - **Communication Service**: Handles notifications and messaging (Lambda + SES/SNS)
   - **Analytics Service**: Provides reporting and insights (Redshift + QuickSight)
   - **Integration Service**: Connects with external systems (AppFlow + Lambda)
   - **Document Processing Service**: Handles resume parsing and document management (Lambda + Textract + S3)

4. **Data Storage Strategy**
   - Polyglot persistence approach with specialized databases for different services
   - Data consistency maintained through event-driven architecture
   - S3 for document storage with versioning and lifecycle policies
   - Redshift for analytics data warehouse

5. **Security**
   - Multi-layered security approach (network, application, data)
   - VPC isolation with security groups and NACLs
   - WAF for application protection
   - KMS for encryption and key management

### Design Principles

This architecture follows several key principles:

1. **Scalability**: Auto-scaling at all levels allows the system to handle varying loads efficiently
2. **Resilience**: Multi-AZ deployments and circuit breakers create a fault-tolerant system
3. **Maintainability**: CI/CD pipelines and infrastructure as code for consistent deployments
4. **Performance**: Caching strategies and read replicas for optimized response times
5. **Security**: Defense-in-depth approach with encryption at rest and in transit
6. **Cost-effectiveness**: Right-sizing resources and leveraging serverless where appropriate

The microservices architecture enables independent scaling and deployment of different components, allowing the system to evolve and adapt to changing business requirements while maintaining high availability and performance.





### Diagram


                                  +------------------+
                                  |    CloudFront    |
                                  |      (CDN)       |
                                  +--------+---------+
                                           |
                                  +--------+---------+
                                  |  Application     |
                                  |  Load Balancer   |
                                  +--------+---------+
                                           |
              +----------------------------|----------------------------+
              |                            |                            |
    +---------+----------+     +-----------+----------+     +-----------+----------+
    |  API Gateway &     |     |   Web Application    |     |  Authentication &     |
    |  BFF Layer         |     |   (React/Next.js)    |     |  Authorization        |
    +--------------------+     +----------------------+     +----------------------+
              |                            |                            |
    +--------------------+     +----------------------+     +----------------------+
    |                    |     |                      |     |                      |
    |   Service Mesh     |     |   Event Bus         |     |  Observability       |
    |   (AWS App Mesh)   |     |   (EventBridge)     |     |  Stack              |
    |                    |     |                      |     |                      |
    +--------------------+     +----------------------+     +----------------------+
              |                            |                            |
+--------------------------------------------------------------------------+
|                                                                          |
|                        Microservices Layer                               |
|                                                                          |
+---|------------|------------|------------|------------|----------------|-+
    |            |            |            |            |                |
+---+----+  +----+---+  +-----+--+  +------+-+  +-------+-+  +---------++
| User   |  | Job    |  |Candidate|  |Interview|  |Analytics|  |Integration|
|Service |  |Service |  |Service  |  |Service  |  |Service  |  |Service    |
+--------+  +--------+  +---------+  +---------+  +---------+  +----------+
    |            |            |            |            |                |
+---+----+  +----+---+  +-----+--+  +------+-+  +-------+-+  +---------++
|DocumentDB| |DynamoDB|  | Aurora  |  |DynamoDB|  |Redshift |  |Elasticache|
|  (User)  |  | (Job) |  |(Candidate)||(Interview)| |(Analytics)| |(Integration)|
+--------+  +--------+  +---------+  +---------+  +---------+  +----------+


### Image created entering all these previous details (without the diagram) inside DiagramGPT. Result in Images --> LTI-high-level-diagram.png

## multi-level C4 diagram
It has been generated with the local version of c4-PlantUML and Cursor Claude 3.7-sonnet model.

The result is Images --> job_service_multilevel.png

GENERAL CONCLUSION OF THIS WEEK EXERCISE ===========================

This is not a satisfaisant result for me in all the steps of this exercise. Unfortunately I was not able to provide a better result during the imparted time. It has enlighten that I need to continue working on this all session 4 week work to improve my skills in these related domains. I look forward the session of Tuesday.