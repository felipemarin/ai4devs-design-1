# Main Use Cases for LTI-ATS

This document outlines the three main use cases for the LTI Applicant Tracking System, along with UML diagrams representing the interactions between different actors and the system.

## Use Case 1: Job Requisition and Posting Management

This use case covers the process of creating job requisitions, approving them, and posting them to various channels. It involves primarily HR managers and recruiters who collaborate to define job requirements and distribute postings.

### Key Activities:
- Creating and defining job requisitions
- Approving job requisitions
- Posting jobs to internal/external job boards
- Managing job posting lifecycle

### UML Diagram:

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


## Use Case 2: Candidate Application and Screening Process

This use case covers the entire candidate journey from application submission through initial screening. It involves candidates submitting applications and recruiters reviewing and filtering candidates based on criteria.

### Key Activities:
- Candidate profile creation and application submission
- Resume parsing and data extraction
- Initial screening and filtering of applications
- Moving candidates through preliminary stages of the pipeline

### UML Diagram:

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

## Use Case 3: Interview Management and Candidate Evaluation

This use case covers the process of scheduling interviews, collecting feedback, and making hiring decisions. It involves recruiters, interviewers, and HR managers collaborating to evaluate candidates.

### Key Activities:
- Interview scheduling and coordination
- Interview feedback collection
- Candidate evaluation and scoring
- Decision making and offer generation

### UML Diagram:

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