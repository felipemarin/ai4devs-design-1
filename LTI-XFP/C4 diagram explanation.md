# 📌 Arquitectura C4 para el ATS (LTI)

Este documento describe los primeros 3 niveles (Context, Container y Component) de la arquitectura del sistema ATS utilizando el estándar C4, específicamente enfocado en **API Gateway → AWS Lambda**.

---

## ✅ Nivel 1 – Contexto (System Context Diagram)

Visión global del sistema ATS, usuarios y sistemas externos con los que interactúa.

### Elementos clave:

- Sistema: ATS (Applicant Tracking System) LTI
- Usuarios: Recruiters internos, Hiring Managers
- Sistemas externos: LinkedIn, Calendarios externos (Google Calendar, Outlook)
- Interacciones destacadas:

    · Usuarios acceden al ATS para gestionar procesos de selección.
    · LinkedIn aporta candidatos externos.
    · Calendarios externos sincronizan entrevistas.


```plantuml
@startuml System_Context
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Context.puml

Person(recruiter, "Recruiter/Hiring Manager", "Gestiona procesos de selección")
System(ats, "ATS LTI", "Sistema inteligente de gestión del talento")
System_Ext(linkedin, "LinkedIn API", "Provee candidatos externos")
System_Ext(calendar, "Calendarios externos", "Gestiona entrevistas")

Rel(recruiter, ats, "Gestiona candidatos y entrevistas usando")
Rel(ats, linkedin, "Sincroniza vacantes y candidatos con")
Rel(ats, calendar, "Sincroniza entrevistas con")
@enduml
```

## ✅ Nivel 2 – Containers (Container Diagram)

En este nivel detallamos los contenedores principales dentro del sistema

### Elementos clave:

- Frontend: Next.js App alojada en AWS Amplify/S3+CloudFront
- API Gateway: Entrada principal al backend
- Backend (Serverless): Microservicios implementados con AWS Lambda
- Base de datos: AWS Aurora PostgreSQL (RDS)
- Almacenamiento de archivos: Amazon S3
- Servicios externos: LinkedIn, AWS Cognito (Auth)


```
@startuml Container_Diagram
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

System_Boundary(ats_boundary, "ATS LTI") {
    Container(frontend, "Next.js App", "Frontend", "React/Next.js")
    Container(api, "AWS API Gateway", "API pública", "REST/HTTP")
    Container(lambda, "AWS Lambda Functions", "Backend Serverless", "Node.js")
    Container(db, "Aurora PostgreSQL", "Base de datos relacional", "AWS Aurora Serverless (PostgreSQL)")
    Container(storage, "Amazon S3", "Almacenamiento seguro de archivos (CVs)", "AWS S3/KMS")
    Container(cognito, "AWS Cognito", "Autenticación y autorización", "AWS Managed Service")
}

System_Ext(linkedin, "LinkedIn API", "Integración externa")
System_Ext(calendar, "Calendarios externos", "Integración calendario")

Person(recruiter, "Recruiter")

Rel(recruiter, frontend, "Usa aplicación")
Rel(frontend, api, "Consume API")
Rel(api, lambda, "Envía solicitudes a")
Rel(lambda, db, "Lee/escribe en")
Rel(lambda, storage, "Almacena documentos en")
Rel(lambda, cognito, "Verifica autenticación vía")
Rel(lambda, linkedin, "Sincroniza candidatos con")
Rel(lambda, calendar, "Agenda entrevistas con")
@enduml
```

## ✅ Nivel 3 – Componentes (Component Diagram)

Finalmente, profundizamos en API Gateway → AWS Lambda

### Elementos clave:

- Candidate Service: gestión candidatos, scoring IA, almacenamiento de CVs.
- Vacancy Service: gestión de vacantes (crear/publicar/estados).
- Interview Scheduling Service: agenda entrevistas automáticamente.
- Authentication Service: integración con Cognito y manejo de JWT.
- Integration Service: conecta LinkedIn y calendarios externos.


```
@startuml Component_Diagram
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Component.puml

Container_Boundary(lambda, "AWS Lambda Functions") {
    Component(candidate_service, "Candidate Service", "Node.js", "Gestión candidatos, scoring IA, documentos en S3")
    Component(vacancy_service, "Vacancy Service", "Node.js", "Gestión creación y publicación vacantes")
    Component(interview_service, "Interview Scheduling Service", "Node.js", "Gestión automática entrevistas")
    Component(auth_service, "Authentication Service", "Node.js", "Gestión autenticación y autorización con Cognito")
    Component(integration_service, "Integration Service", "Node.js", "Integración LinkedIn y calendarios externos")
}

Container(api, "AWS API Gateway")

Rel(api, auth_service, "Verifica auth mediante JWT")
Rel(api, candidate_service, "Gestiona candidatos mediante")
Rel(api, vacancy_service, "Gestiona vacantes mediante")
Rel(api, interview_service, "Gestiona entrevistas mediante")
Rel(candidate_service, integration_service, "Sincroniza candidatos desde LinkedIn")
Rel(interview_service, integration_service, "Sincroniza eventos con calendarios")
@enduml

```

