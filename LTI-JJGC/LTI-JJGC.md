# LTI Applicant-Tracking System (ATS) - Product Definition

## 1. Overview

### 1.1. Software Description

**LTI ATS** is an advanced Applicant-Tracking System designed to streamline the recruitment process for HR departments. It leverages cutting-edge AI to automate repetitive tasks, enhance real-time collaboration between recruiters and hiring managers, and provide actionable insights to improve hiring efficiency. The system is built to be intuitive, scalable, and customizable, catering to businesses of all sizes.

### 1.2. Value Proposition

- **Efficiency**: Automates manual tasks like resume screening, interview scheduling, and candidate communication.
- **Collaboration**: Enables real-time collaboration between recruiters and hiring managers.
- **AI Assistance**: Provides AI-driven insights for better decision-making, such as candidate matching and predictive analytics.
- **Scalability**: Adapts to the needs of small, medium, and large enterprises.
- **Integration**: Seamlessly integrates with existing HR tools and platforms.

### 1.3. Key Features

1. **AI-Powered Resume Screening**: Automatically ranks candidates based on job requirements.
2. **Real-Time Collaboration**: Shared dashboards and communication tools for recruiters and managers.
3. **Automated Interview Scheduling**: Syncs with calendars to schedule interviews without back-and-forth emails.
4. **Candidate Matching**: Uses AI to suggest the best-fit candidates for open roles.
5. **Analytics Dashboard**: Provides insights into recruitment metrics like time-to-hire, cost-per-hire, and candidate pipeline health.
6. **Customizable Workflows**: Allows HR teams to tailor the recruitment process to their specific needs.

### 1.4. Lean Canvas

```plaintext
| **Problem**                          | **Solution**                              | **Key Metrics**               |
|--------------------------------------|-------------------------------------------|-------------------------------|
| Manual recruitment processes are slow | Automate repetitive tasks with AI         | Time-to-hire, Cost-per-hire   |
| Poor collaboration between teams     | Real-time collaboration tools             | User engagement, Feedback      |
| Lack of actionable insights          | AI-driven analytics and reporting         | Candidate quality, Retention   |
| **Unique Value Proposition**         | **Unfair Advantage**                      | **Channels**                  |
| AI-powered recruitment efficiency    | Proprietary AI algorithms for matching    | Direct sales, Partnerships     |
| **Customer Segments**                | **Cost Structure**                        | **Revenue Streams**           |
| HR departments, Recruitment agencies | Development, Maintenance, Cloud hosting   | Subscription-based pricing     |
```

## 2. Use Cases

### Use Cases for LTI ATS

#### 1. Automated Candidate Screening

##### **Description**

The system automates the initial resume screening process using AI. Recruiters upload resumes, and the ATS analyzes qualifications, experience, and skills to shortlist candidates based on predefined criteria.

##### **Actors**

- **Recruiter**: Uploads resumes and reviews shortlisted candidates.
- **ATS System**: Performs AI screening and generates a shortlist.

##### **Flow**

1. Recruiter uploads a resume.
2. ATS performs AI-driven resume screening.
3. ATS generates a screening report with recommended candidates.
4. Recruiter reviews and shortlists candidates for the next step.

---

#### 2. Interview Scheduling & Coordination

##### **Description**

The system simplifies interview scheduling by allowing recruiters to select slots, invite candidates, and coordinate with hiring managers. The system ensures real-time availability updates and automated notifications.

##### **Actors**

- **Recruiter**: Selects interview slots and sends invitations.
- **Candidate**: Confirms availability.
- **Hiring Manager**: Confirms availability and attends interviews.
- **ATS System**: Manages scheduling and notifications.

##### **Flow**

1. Recruiter selects available interview slots.
2. ATS sends invitations to candidates and hiring managers.
3. Candidates and hiring managers confirm availability.
4. ATS schedules the interview and notifies all participants.

---

#### 3. Real-Time Feedback & Collaboration

##### **Description**

The system enables hiring managers and recruiters to provide structured feedback on candidates in real time. This enhances collaboration and speeds up decision-making.

##### **Actors**

- **Hiring Manager**: Provides interview feedback.
- **Recruiter**: Reviews feedback and updates candidate status.
- **ATS System**: Stores feedback and assists in decision-making.

##### **Flow**

1. Hiring manager submits structured feedback after an interview.
2. ATS stores feedback and shares it with the recruiter.
3. Recruiter reviews feedback and updates the candidate’s status.
4. Team members discuss and finalize hiring decisions within the ATS.

#### 4. Use Case Diagram

@startuml
left to right direction
skinparam packageStyle rectangle
skinparam actorStyle awesome

actor "Recruiter" as recruiter
actor "Candidate" as candidate
actor "Hiring Manager" as manager
actor "ATS System" as ats

rectangle "LTI ATS System" {
usecase "Automated Candidate Screening" as UC1
usecase "Interview Scheduling & Coordination" as UC2
usecase "Real-Time Feedback & Collaboration" as UC3

usecase "Upload Resumes" as UC1_1
usecase "Perform AI Screening" as UC1_2
usecase "Generate Screening Report" as UC1_3
usecase "Review Shortlisted Candidates" as UC1_4

usecase "Select Interview Slots" as UC2_1
usecase "Send Invitations" as UC2_2
usecase "Confirm Availability" as UC2_3
usecase "Schedule Interview" as UC2_4
usecase "Send Notifications" as UC2_5

usecase "Submit Interview Feedback" as UC3_1
usecase "Store & Share Feedback" as UC3_2
usecase "Update Candidate Status" as UC3_3
usecase "Collaborate on Hiring Decision" as UC3_4
}

' Main use case relationships
recruiter --> UC1
recruiter --> UC2
recruiter --> UC3
candidate --> UC2
manager --> UC2
manager --> UC3
ats --> UC1
ats --> UC2
ats --> UC3

' UC1 includes relationships
UC1 .> UC1_1 : includes
UC1 .> UC1_2 : includes
UC1 .> UC1_3 : includes
UC1 .> UC1_4 : includes
recruiter --> UC1_1
ats --> UC1_2
ats --> UC1_3
recruiter --> UC1_4

' UC2 includes relationships
UC2 .> UC2_1 : includes
UC2 .> UC2_2 : includes
UC2 .> UC2_3 : includes
UC2 .> UC2_4 : includes
UC2 .> UC2_5 : includes
recruiter --> UC2_1
ats --> UC2_2
candidate --> UC2_3
manager --> UC2_3
ats --> UC2_4
ats --> UC2_5

' UC3 includes relationships
UC3 .> UC3_1 : includes
UC3 .> UC3_2 : includes
UC3 .> UC3_3 : includes
UC3 .> UC3_4 : includes
manager --> UC3_1
ats --> UC3_2
recruiter --> UC3_3
recruiter --> UC3_4
manager --> UC3_4
@enduml

--

### Version 2:

flowchart TD
subgraph "LTI ATS System"
UC1["Automated Candidate Screening"]
UC2["Interview Scheduling & Coordination"]
UC3["Real-Time Feedback & Collaboration"]

        %% Subflows for UC1
        UC1_1["Upload Resumes"]
        UC1_2["Perform AI Screening"]
        UC1_3["Generate Screening Report"]
        UC1_4["Review Shortlisted Candidates"]

        %% Subflows for UC2
        UC2_1["Select Interview Slots"]
        UC2_2["Send Invitations"]
        UC2_3["Confirm Availability"]
        UC2_4["Schedule Interview"]
        UC2_5["Send Notifications"]

        %% Subflows for UC3
        UC3_1["Submit Interview Feedback"]
        UC3_2["Store & Share Feedback"]
        UC3_3["Update Candidate Status"]
        UC3_4["Collaborate on Hiring Decision"]

        %% Relationships between use cases and subflows
        UC1 -->|includes| UC1_1
        UC1 -->|includes| UC1_2
        UC1 -->|includes| UC1_3
        UC1 -->|includes| UC1_4

        UC2 -->|includes| UC2_1
        UC2 -->|includes| UC2_2
        UC2 -->|includes| UC2_3
        UC2 -->|includes| UC2_4
        UC2 -->|includes| UC2_5

        UC3 -->|includes| UC3_1
        UC3 -->|includes| UC3_2
        UC3 -->|includes| UC3_3
        UC3 -->|includes| UC3_4
    end

    %% Actors
    Recruiter((Recruiter))
    Candidate((Candidate))
    Manager((Hiring Manager))
    ATS((ATS System))

    %% Actor connections to use cases
    Recruiter --> UC1
    Recruiter --> UC2
    Recruiter --> UC3
    Candidate --> UC2
    Manager --> UC2
    Manager --> UC3
    ATS --> UC1
    ATS --> UC2
    ATS --> UC3

    %% Actor connections to specific subflows
    Recruiter --> UC1_1
    ATS --> UC1_2
    ATS --> UC1_3
    Recruiter --> UC1_4

    Recruiter --> UC2_1
    ATS --> UC2_2
    Candidate --> UC2_3
    Manager --> UC2_3
    ATS --> UC2_4
    ATS --> UC2_5

    Manager --> UC3_1
    ATS --> UC3_2
    Recruiter --> UC3_3
    Recruiter --> UC3_4
    Manager --> UC3_4

## 3 Lean Canvas Diagram Link

https://app.eraser.io/workspace/fnhMQ5FBb5KWHJWaOFHt?origin=share

## 4 Interview Scheduling and Coordinatioin Diagram Link

https://app.eraser.io/workspace/TxsIJFHE3HFmVTei8okk?origin=share

## 5 Data Model Diagram Link

https://app.eraser.io/workspace/1oGfcekgw4vjnmu7ieM2?origin=share
