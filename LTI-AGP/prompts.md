# Prompts Used

## Step 1

### Prompt 1

```text

You are a senior CPO / CTO developing a new company based on the ATS (applicant-tracking-software).  I'd like you to help me refine the process step by step, in order to be able to: 
1. Define the whole process
2. Be able to divide the steps in smaller sections with the bojective to create a chain of responsability using Gen AI tools
3. At the end generate the documentation in markdown format with all the selected elements. 

This is my current step by step process i'm thinking: 
"Thought process: 

1. We want to build the best ATS (applicant tracking system) for the future

Context: What is a ATS: 
1. An application to track the lifecycle of a job an their applicants
 1. Create a Job offer with their job description and all the information related to the job. 
 2. Publish the Jobs to own website, jobs board, social media (linkedin / x) 
 3. Allow applicants to apply 
 4. Review the applications (Soft / Hard)
  Usually it is a cycle of: 
  1. Review the application details and the match to the company culture, and the requirements
  2. Create an initial Interview (schedule)
  3. Do online tests to validate hard skills
  4. Schedule and do an interview to validate the candidate willignes
 5. Select the applicants to make an ofer
 6. Track the offer status until the applicant is hired
 7. Unpublish the job offer

2. Identify the top 10 players and their pros and cons, try to idnetify what makes them different from the competition as their only special sauce.

3. Identify all the functionalitiles needed for a state of the art ATS system (USer login) 

4. Identify what could be a game changer for an ATS, specifically in the Gen-AI era. Give me a list of 10 game-changer unicorn cration features we could apply to our idea. (HR departments efficiency, better realtime collaboration, automations, Ai assitance) 

5. Identify some tools (Opensource of Paid) which we could use as a base to build our software

6. Then select with the information on point 3 / 4 which 3 features will be our main functions. 

7. create a Lean canvas and a Busines model Canvas to talk about why the opportunity is appealing. 

8. Define a name and a logo for an startup (Applicant-Tracking-System)

9. Create a description of our software, added value, advanteges, and "unfair advanteges". 

10. Describe the 3 selected main use cases
 1. Create a Use case diagram specific for each of them

11. Define what kind of data storage wea re going to use, docuemnt the resolution using the framework (Arqchitecturar Decision record)

11. Define a comlete data model with entities, attributes, name, types and relationships. 

12. Create more ADR, based on what we want to achieve with our selected use cases. 

13. Create a sofware acrhictecture systen design high level with text. 

14. Create a software architecture diagram

15. Create a C4 detailed diagram for one of the components. 

16. As a final output create a Markdown file with 
1. Name and logo of the software
2. Short Description
3. Added value and unfair advantages
4. how to compare with other solutions in the market. 
5. Explain and detailed description of top 3 use cases to develop

6. Data model diagram
7. High level system design (Explained with text and with a graphic diagram)
8. Detailed C4 Diagram with one of the funcioanlities. 
9. Add the ADR section with all the decision made during the design
12. Create a section on the 
with related links: 1. https://adr.github.io/
2. https://sst.dev/
3. Include the tools we will be using (chat gpt, mermaid, etc...)" 
```

**Thought process:**

1. Start with a complete definition of the flow, to be divided step by step. Use AI to help improve and materialized a good step by step process improving the process.

**Relevant Output Details:**

- A more structured initial process

**Personal Considerations:**

- Still, there is some additional considerations i would like to clean, so i create a 2nd iteration in the considerations.

## Step 2

### Prompt 2

```text
Objective

I am developing a next-generation Applicant Tracking System (ATS) that leverages AI and automation to redefine recruitment efficiency. I want to refine and structure the process step by step, ensuring:

A well-defined and documented ATS development process.

Breaking down each stage into smaller, well-defined sections to create a chain of responsibility using Gen AI tools.

Generating a final Markdown document that compiles all key elements in a structured and actionable format.

Step-by-Step Process to Define & Build the ATS

1. Define the ATS Purpose and Workflow

What is an ATS?

Core functionalities of a modern ATS including

Job lifecycle management (posting, tracking, closing).

Application management (review, AI filtering, interviews, selection).

Offer management and hiring process.

Post-hiring analytics and tracking.

2. Competitive Analysis

Identify the top 10 ATS solutions in the market.

List pros, cons, and differentiators (their “special sauce”).

Identify gaps and opportunities to create a better and superior system.

3. Functional Requirements

Identify core functionalities for a state-of-the-art ATS.

Explore integration possibilities (LinkedIn, Slack, AI models, etc.).

4. Differentiators

Identify 10 AI-driven or UX-driven game-changing features for an ATS.

Add a score to each of them and order it by the market impact. 

5. Technology Stack & Open-Source Tools

Identify open-source or commercial ATS tools.

List frameworks, AI tools, and APIs that could enhance development.

6. Define MVP

Define a minimum viable product (MVP) with the 3 most impactful features and the architectures selected from the previous point.

7. Generate Business Strategy & Market Validation

Lean Canvas: Problem, Solution, Key Metrics, Revenue Model.

Business Model Canvas: Value Proposition, Channels, Customer Segments.

8. Branding & Positioning

Define the name, logo, and unique positioning of our ATS.

Create a brand identity aligned with market needs.

9. Product Description & Unique Value

Define a short, compelling product description.

List value propositions and unfair advantages.

Identify how it compares with the competitors.

10. Use Case Definition

Select 3 primary use cases defined as game changers in the MVP definition.

Create use case diagrams with actors and workflows.

11. Data Storage Strategy

Define data storage approach (SQL, NoSQL, Hybrid) and tools.

Document the decision using Architectural Decision Records (ADR).

12. Complete Data Model

Define entities, attributes, and relationships.

Create an ERD (Entity-Relationship Diagram).

13. System Architecture & High-Level Design

Document software architecture in text and visuals.

Create a high-level architecture diagram.

Document additional ADR of top decisions (Event-Based Architecture, Controller, Services and Repository definitions, Entities, etc.).

14. Detailed System Design

Create a C4 diagram for a critical system component.

15. Final Documentation in Markdown

Structure a well-organized Markdown document with:

Software name & logo.

Short description & unique selling points.

Competitive comparison.

Use cases & diagrams.

Data model & ERD.

System architecture & diagrams.

C4 diagram of a core functionality.

ADR decisions.

Related tools & references.

Expected Outcome

A step-by-step development framework for the ATS.

A structured chain of responsibility using Gen AI tools.

A professional, well-documented roadmap for execution.

A final Markdown file containing all key project elements.
```

**Relevant Output Details:**

- A structured and repeateable process

## Step 3

### Prompt 3

```text
Continue as a Senior product Manager Defining the Purpose and Workflow of an ATS. 

The output will be an initial section for the final Markdown document, (Introduction). 

give me the markdown code directly, no instruction about how to use it. 
```

**Relevant Output Details:**
I was exepecting directly the markdown code, however, In the new ChatGPT clients it creates a "document" which was being edited continously.

I copied and pasted the response and added simple markdown format in my LTI-AGP.md page

## Step 4

### Prompt 4

```text
Now, you have a role of a senior consultant firm specialized in Competitive analysis, 
Identify the top 10 ATS solutions in the market, create a  visual SWOT diagram for each of them. (Use infromation from cusotmer, business, professional reviews and other users from their system). 

Define who would be our target, and the market size in europe (TAM / SAM / SOM) 

As a conclusion identify the gaps an opportunities to create a better and superior ATS system. 
```

**Thought process:**
**Relevant Output Details:**
I was using the deep research capabilities from Open AI, tool, ask me some confirmation questions before starting the analysis:

- Which region i want to focus on (I said Europe)
- Which capabilities want to be analyzed (balanced view, but with some focus on AI and UX)
**Personal Considerations:**
The analysis took (15 minutes) checking more tahn 50 relevant sources. It identify a long list of competitors, with their SWOT analysis.

## Step 5

### Prompt 5

```text
Ok, now that you finished the Market research give me from it: 
- Our expected target description (applicants and SMEs) 
- market size (number of applicants and SMEs) and estimation of TAM / SOM / SAM. 
- Market size in $$$ poiint of view considering an standard fee from SMEs to use our services. 
A list of notable players. 
 A visual Simplified (visual SWOT diagram for them) just the concept. You can use Mermaid or UML to give me Diagram as a code for each of them. 

A compelled combined oportunities list form each of those players, with specific actions. 
Give me teh markdown file exported in .txt to facilitate teh integration with my curren repository. 
```

**Thought process:**
**Relevant Output Details:**
It modified teh active document and had several interesting outputs in the analysis.
**Personal Considerations:**

## Step 6

### Prompt 6

```text
Help me a little bit with formatting: 
"Combined Market Opportunities & Actions

Opportunity

Specific Action

UX Optimization

Develop an intuitive, recruiter-friendly UI to compete with legacy enterprise ATS.

AI-Powered Hiring

Offer AI-driven job matching, automated screening, and predictive analytics for better hiring decisions.

SME-Focused ATS

Build an affordable, easy-to-implement ATS with pay-as-you-go pricing for SMEs.

Seamless Integrations

Provide pre-built integrations with HRIS, Slack, and assessment tools for plug-and-play adoption.

Compliance & GDPR Support

Automate GDPR workflows and AI-driven candidate data compliance tools.

Recruitment Automation

Automate interview scheduling, candidate messaging, and follow-ups with AI.

Self-Service & No-Code Customization

Offer no-code ATS configuration so SMEs can tailor workflows easily.

Embedded Video & AI Chatbots

Integrate video interviewing and AI chatbots to engage candidates better.

Data-Driven Insights

Deliver real-time hiring metrics, diversity analytics, and recruiter efficiency reports.

Subscription Flexibility

Provide monthly and per-hire pricing models to appeal to different business sizes." 

Format it as a markdown .md format table. Give me the plain TXT version of the markdown. 

Do the same with The system functionalities and ther classification by need to have, nice to have
```

**Thought process:**
Close section 1 and formatting details.
**Relevant Output Details:**
The output was not what i was expecting, still notdelivering the md code but teh formatted in-app vision.

I needed to insist with two more commands
**Personal Considerations:**

## Step 7

### Prompt 7

```text
Based on must have features
"### **🔹 Must-Have Features (Core ATS Functionalities)**

| **Category** | **Functionality** |
|-------------|------------------|
| **User Management** | Authentication, Role-Based Access Control, GDPR Compliance |
| **Job Management** | Job Posting, Multi-Channel Distribution, Approval Workflows |
| **Candidate Management** | Resume Parsing, Candidate Status Tracking, Application Management |
| **Communication** | Automated Notifications, Email/SMS Integration, Interview Scheduling |
| **Interview & Assessment** | Video Interviews, AI Scoring, Skills Assessments |
| **Offer & Hiring** | Offer Letter Generation, E-signatures, Hiring Workflow Tracking |
| **Reporting & Compliance** | KPI Dashboards, Diversity Analytics, GDPR Data Management |" 

Which opensource tools or system could we use as a base instead of building it from scratch? 
```

**Thought process:**
Reduce Time to market with already existing tools
**Relevant Output Details:**
A list of opensource tools / packages which could help to develop faster the solution

## Step 8

### Prompt 8

```text
Ok, review with me the basic pplication diagram based on all the requirements we stated before. 
The user/recruiter will connect to the application throught a web app. 
Webapp will be connected to an API Gateway connecting to different services (following jobHunter) 
- Auth Service (Auth Database) 
- Applicant/Candidate
- Scheduler
- JobService
- OpenCats servcie. 

All the messages arriving to the API Gateway will be authorized (if needed) and publish an event before their integration with the downstreamed service. 

We use OpenCats as data source and exposed vie the API. 

As an output, give me a generate me a description and diagram in mermaid form the high level infrastructure
```

**Thought process:**
**Relevant Output Details:**
**Personal Considerations:**

## Step 9

### Prompt 9

```text
Now, let's track ADR decissions. 
1. Define which Data storage are we using and why
2. Define which architecture and integration paradima we will be using. (Event Based platform with microservices, for custom functionalities + API Gateway with event publishing and integrating with openCats from most of the funcitonality) 
3. Track all ADR decision up to now (Database, using openCats, API definition compatible with JobHunt) in a valid ADR format. 
4. For the functionality 2, 3, and 4 of our MVP list, define a ERD model and draw it with Mermaid. IDentify attribute name, types and relationship between them. 

Everything should be on new .md downloadable document output. Don't reuse teh ATS market analysis document.
```

**Thought process:**
**Relevant Output Details:**
**Personal Considerations:**## Step 10

### Prompt 10

```text
Add two new ADR resoulition using API Gateway to controll trhottling and createan abstraction layer between servcies and OpenCATS 

The EVent based architecture EventBridge, SNS + SQS to generate a Event based architecture with a Fanout pattern with queues and DLQ for any services
```

**Thought process:**
**Relevant Output Details:**
**Personal Considerations:**

## Step 11

### Prompt 11

```text
Now, generate a complete autonomous prompt to pass to any GEN-AI tool to: 
1. Develop a full C4 model diagram for the **AI-Driven Resume & Candidate Matching** feature. 
It should generate a diagram for each level of the C4 model. Context, Containers, components and code. 
use and explain the architecture infrasctructure and ERD diagram we have defined so far during the process.

```

**Thought process:**
**Relevant Output Details:**
It gave me a complete output propmt process to deliver a c4 model diagram:

```text

# Task: Generate a Full C4 Model Diagram for AI-Driven Resume & Candidate Matching

## **Objective**
Develop a **complete C4 model** for the **AI-Driven Resume & Candidate Matching** feature in an **Applicant Tracking System (ATS)**. The model must include **all four levels**:
1. **Context Diagram (L1)**: High-level system overview, including interactions between users and external systems.
2. **Container Diagram (L2)**: Breakdown of the ATS system into main components (API Gateway, microservices, databases, and external services).
3. **Component Diagram (L3)**: In-depth look at how services interact internally within the **Resume Matching** feature.
4. **Code Diagram (L4)**: Focus on the internal structure of a key component, such as the **AI Matching Engine**.

## **Background & Architecture Overview**
We are building an **AI-powered ATS** with an **Event-Driven Microservices Architecture**. The **Resume Matching** feature automatically ranks candidates by comparing **job descriptions** with **resume data** using **Natural Language Processing (NLP) and AI models**.

### **Key Architecture Decisions (ADR)**
- **PostgreSQL** is used as the main relational database to store job postings, candidate data, and AI-generated scores.
- **OpenCATS** is used as the core ATS, and it is integrated via an **API Gateway** to expose functionalities.
- **API Gateway** handles **authentication, request routing, event publishing**, and **rate-limiting**.
- **AWS EventBridge, SNS, and SQS** enable an **event-driven fanout architecture**, ensuring **asynchronous processing** of AI-driven tasks.
- **Resume Matching AI** is a **dedicated microservice** using **pre-trained NLP models** (e.g., OpenAI, BERT) to compare job requirements with candidate resumes.

---

## **🔹 C4 Model Breakdown**

### **1️⃣ Context Diagram (L1) – High-Level Overview**
- **Actors**:
  - **Recruiters & Hiring Managers**: Upload job descriptions & search for candidates.
  - **Candidates**: Submit resumes.
  - **System Admins**: Manage configurations and security settings.
- **External Systems**:
  - **OpenCATS** (Existing ATS)
  - **Third-Party Job Boards (LinkedIn, Indeed, JobHunt API)**.
- **Flow**:
  - Recruiters create job postings.
  - Candidates apply with resumes.
  - The AI Matching service ranks candidates.
  - Matched candidates are sent to recruiters.

### **2️⃣ Container Diagram (L2) – System Components**
- **Web Application**: UI where recruiters/candidates interact.
- **API Gateway**: Controls authentication, routing, event publishing.
- **Microservices**:
  - **Auth Service** (User management & permissions)
  - **Job Service** (Manages job postings)
  - **Candidate Service** (Stores candidate profiles)
  - **AI Resume Matching Service** (Processes candidate-job ranking)
- **Data Storage**:
  - **PostgreSQL** (Job & candidate data)
  - **OpenCATS Database** (Existing ATS data)

### **3️⃣ Component Diagram (L3) – Resume Matching Microservice**
- **Components:**
  - **NLP Model Wrapper** (Pre-trained AI model for similarity scoring)
  - **Feature Extractor** (Extracts skills, experience, education)
  - **Ranking Engine** (Compares job descriptions & candidate profiles)
  - **Event Listener** (Consumes SQS events for new job applications)
  - **API Endpoint** (Exposes ranking results)

### **4️⃣ Code Diagram (L4) – Internal AI Matching Engine**
- **Classes & Functions:**
  - `ResumeParser()` → Extracts text from PDFs/Word files.
  - `FeatureVectorizer()` → Converts resume/job descriptions into embeddings.
  - `SimilarityScorer()` → Uses cosine similarity/BERT to compare text.
  - `RankingAlgorithm()` → Applies weight-based ranking.
  - `APIHandler()` → Exposes results via REST API.

---

## **🔹 Expected Output**
- **C4 Model Mermaid Diagrams** for **each level (L1-L4)**.
- **Annotations** explaining relationships between **services, databases, and external systems**.
- **Markdown-formatted output** for direct documentation integration.

---

## **Additional Notes**
- Ensure **proper event flow visualization** for asynchronous AI ranking.
- Highlight **how event-driven messaging** (SNS/SQS/EventBridge) integrates AI matching results back into the ATS.
- Optimize AI inference by **caching results** to reduce redundant processing.

---

## **Final Deliverable**
- **A complete C4 model with detailed explanations**.
- **Diagrams** in **Mermaid format**.
- **Fully structured Markdown output** for direct integration into ATS documentation.
```

**Personal Considerations:**

## Step 12

### Prompt 12

```text
USed the prompt generated previously
```

**Thought process:**
**Relevant Output Details:**
**Personal Considerations:**

## Step 13

### Prompt 13

```text
Generate a name suggestion for my company and a logo. It should be designed for my target, be original and cool
```

**Thought process:**
**Relevant Output Details:**
**Personal Considerations:**## Step 14

### Prompt 14

```text
Give me a propmt to genereate a complete Busines Model canvas and a Lean Canvas for HiresPhere in any AI Generative Tool 
```

**Thought process:**
**Relevant Output Details:**
```text
# Task: Generate a Complete Business Model Canvas & Lean Canvas for "HireSphere"

## **Objective**
Develop a **detailed Business Model Canvas** and **Lean Canvas** for "HireSphere", an AI-driven Applicant Tracking System (ATS) designed to optimize recruitment efficiency for SMEs, mid-sized businesses, and enterprises.

The output should include:
1. **A complete Business Model Canvas** following the **9-block framework** (Customer Segments, Value Proposition, Channels, Revenue Streams, etc.).
2. **A Lean Canvas** tailored for startups, covering key problems, solutions, revenue models, and unfair advantages.
3. **Mermaid-formatted diagrams** for both canvases to allow direct documentation integration.

---

## **🛠 Context & Background**
**HireSphere** is an **AI-powered ATS** designed to **automate and optimize** hiring by integrating:
- **AI-driven resume & job matching** to streamline candidate selection.
- **Automated interview scheduling** to reduce recruiter workload.
- **AI-generated job descriptions** for better candidate engagement.

The business model focuses on **subscription-based pricing**, **API integrations**, and **pay-per-hire models**.

---

## **🔹 Business Model Canvas (BMC)**
### **Include the following details for HireSphere**:
1️⃣ **Customer Segments**:  
   - **Primary**: SMEs, Mid-sized companies, HR teams, recruiters.  
   - **Secondary**: Large enterprises needing automation & compliance tools.  
   - **Job Seekers**: Indirectly benefiting through improved hiring workflows.  

2️⃣ **Value Proposition**:  
   - **AI-driven automation** for candidate ranking.  
   - **Data-driven hiring decisions** to improve talent acquisition.  
   - **GDPR-compliant, easy-to-use ATS** for SMEs.  

3️⃣ **Channels**:  
   - **Direct sales** to HR teams & SMEs.  
   - **Partnerships** with HR Tech & Job Boards (LinkedIn, Indeed, JobHunt API).  
   - **Inbound marketing & SEO** for lead generation.  

4️⃣ **Revenue Streams**:  
   - **SaaS subscription model** (monthly/yearly pricing).  
   - **Per-hire fees** (SMEs pay based on hiring volume).  
   - **Enterprise API Licensing** for ATS integrations.  

5️⃣ **Key Resources**:  
   - AI-powered **Resume Matching Engine**.  
   - Scalable **Event-Driven ATS Infrastructure**.  
   - OpenCATS integration & API ecosystem.  

6️⃣ **Key Activities**:  
   - **AI Model Training & Optimization**.  
   - **Recruitment workflow automation**.  
   - **Compliance & GDPR enhancements**.  

7️⃣ **Key Partnerships**:  
   - **Job boards & HR Tech providers** (LinkedIn, Indeed).  
   - **AI technology providers** for NLP & Resume Matching.  

8️⃣ **Cost Structure**:  
   - AI development & cloud infrastructure.  
   - Sales, marketing & partnership costs.  
   - HR & compliance-related expenses.  

9️⃣ **Unfair Advantage**:  
   - **AI-first ATS for SMEs**, reducing hiring time drastically.  
   - **Automated resume parsing & matching** via advanced NLP.  
   - **GDPR & diversity compliance built-in** for European companies.  

---

## **🔹 Lean Canvas for HireSphere**
### **Key Sections to Cover**
1️⃣ **Problem Statement**:  
   - Hiring processes are inefficient & time-consuming.  
   - SMEs lack tools to attract top talent.  
   - AI-powered hiring solutions are mostly enterprise-focused.  

2️⃣ **Customer Segments**:  
   - SMEs, recruiters, hiring managers, and HR teams.  

3️⃣ **Unique Value Proposition**:  
   - **AI-powered talent matching** for **faster & fairer** hiring.  
   - **Seamless interview scheduling** for improved efficiency.  
   - **GDPR-compliant ATS tailored for SMEs**.  

4️⃣ **Solution**:  
   - AI-powered resume matching.  
   - Smart job description generator.  
   - Automated interview scheduling.  

5️⃣ **Revenue Streams**:  
   - SaaS subscription (monthly/yearly).  
   - Pay-per-hire model for SMEs.  
   - API monetization for enterprise HR integrations.  

6️⃣ **Cost Structure**:  
   - AI/NLP processing costs.  
   - Cloud & infrastructure maintenance.  
   - Sales, marketing, and regulatory compliance.  

7️⃣ **Channels**:  
   - Direct outreach to HR teams & SMEs.  
   - Partnerships with job boards & recruitment agencies.  
   - Organic inbound marketing & AI-generated hiring reports.  

8️⃣ **Key Metrics**:  
   - Time-to-hire improvement.  
   - AI matching accuracy & recruiter adoption.  
   - Revenue growth from enterprise licensing.  

9️⃣ **Unfair Advantage**:  
   - Proprietary **AI-powered job-candidate ranking**.  
   - **GDPR-compliant recruitment automation**.  
   - Optimized for **SMEs** (underserved by AI-powered ATS tools).  

---

## **📌 Expected Output**
- **A fully detailed Business Model Canvas** with structured descriptions.
- **A complete Lean Canvas** optimized for startups & ATS market needs.
- **Mermaid-formatted diagrams** for **both canvases**.
- **Clear explanations & documentation-ready Markdown output**.

---

## **🔹 Additional Notes**
- Ensure **AI, automation, and event-driven hiring** are highlighted.
- Structure the output in **Markdown** for **direct use in documentation**.
- Use **concise yet detailed explanations** for each canvas section.
- **Generate diagrams** that visually represent the business model & lean startup strategy.

---

## **Final Deliverable**
- **A complete Business Model Canvas & Lean Canvas** for HireSphere.
- **Mermaid-based diagrams** for structured documentation.
- **Formatted in Markdown for easy integration** into ATS project docs.
```