# LTI - EPH

- Trae (Claude-3.7-Sonnet) 
- ChatGPT
- DiagramGPT

# Prompts

## Prompts para Investigación y análisis de requisitos

### Prompt 1

You are a product expert with experience in applicant tracking systems.
What are the basic functionalities of an applicant tracking system?
Describe them in a list, ordered from highest to lowest priority.

### Prompt 2

What benefits does the client derive from an applicant tracking system to consider using it?

### Prompt 3

What are the alternatives to using an applicant tracking system and when are they relevant?

### Prompt 4

What does the normal customer journey of a customer using an applicant tracking system look like? Describe to me step by step all interactions

### Prompt 5

Which open source applicant tracking systems are best known?

### Prompt 6

Which commercial applicant tracking systems are most popular? Compare them on the basis of Candidate Database Management, Job Posting and Distribution and Application Processing and assess which would be a better option.

### Prompt 7

Given all this information, suppose we are a startup called LTI, which wants to make an applicant tracking system of the future. I want you to help me perform the following task:

- Short description of the LTI software
- Added value and competitive advantages. 
- Explanation of the main functions. 
- Add a Lean Canvas diagram to understand the business model.


## Prompts para Definición de casos de uso

### Prompt 1

With all the information we have so far. You're an expert software analyst. As you know, I'm building LTI, an online applicant tracking system. List and briefly describe the most important use cases to be implemented to achieve basic functionality.

### Prompt 2

Right, let's narrow this down to the 3 most critical use cases, as I want to go into detail on them.

### Prompt 3

Represent these use cases in the most appropriate type of diagram using the plantUML format. According to UML syntax and best practices, define and describe what is necessary. Make a diagram for each use case.


## Prompts para Modelado de datos

### Prompt 1

With all the information we have so far. You are an expert software architect. What are the essential data model entities in my online applicant tracking system? Give me some essential fields of each and how they relate to each other.

### Prompt 2

Good work. You are now a brilliant software architect. You are able to design, explain and diagram the different aspects of a software system.

Generate me a mermaid diagram with the entities and relationships you have given me.


## Prompts para Diseño del sistema y arquitectura de alto nivel

### Prompt 1

With all the information we have so far. You're an expert software infrastructure. Think we want to use a microservices infrastructure. What architectural components do you think would be necessary?

### Prompt 2 (DiagramGPT)

(Response from previous prompt)
The cloud provider will be AWS, so use proper services.
Also, include a load balancer and CDN for files and images.

#### Questions from DiagramGPT

1. What specific AWS services do you envision using for the data storage layer, if any?
   - Amazon RDS
   - Amazon S3

2. Are there any specific security compliance standards or regulations that the architecture should adhere to, if any?
   - GDPR

3. What types of analytics and reporting features do you prioritize for the Analytics Service, if any?
   - None


## Prompts para Diagrama C4

### Prompt 1

With all the information we have so far. You're an expert software analyst. As you know, I'm building LTI, an online applicant tracking system. I want you that represent one of the component of the system using a C4 diagram, using the plantUML format. According to UML syntax and best practices, define and describe what is necessary.

Let's focus on the next component of the system:

#### User Service

- Handles user authentication, authorization, and profile management
- Manages role-based access control
- Integrates with SSO providers
- Stores user preferences and settings

Use the resources in this repository https://github.com/plantuml-stdlib/C4-PlantUML?ref=lukemerrett.com to generate the C4 diagram.
