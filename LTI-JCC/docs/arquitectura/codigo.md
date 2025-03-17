# Diagrama de Código

Este diagrama muestra la estructura de clases y sus relaciones en los servicios principales.

```mermaid
classDiagram
    %% Interfaces Base
    class IController {
        <<interface>>
        +create(dto: CreateDTO)
        +update(id: string, dto: UpdateDTO)
        +delete(id: string)
        +findOne(id: string)
        +findAll(query: QueryDTO)
    }

    class IService {
        <<interface>>
        +create(data: any)
        +update(id: string, data: any)
        +delete(id: string)
        +findById(id: string)
        +findAll(query: any)
    }

    class IRepository {
        <<interface>>
        +create(entity: any)
        +update(id: string, entity: any)
        +delete(id: string)
        +findById(id: string)
        +findAll(filters: any)
    }

    %% Entidades Base
    class BaseEntity {
        +id: string
        +createdAt: Date
        +updatedAt: Date
        +deletedAt: Date
    }

    %% Entidades de Dominio
    class User {
        +email: string
        +password: string
        +role: UserRole
        +status: UserStatus
        +validate()
    }

    class Candidate {
        +userId: string
        +firstName: string
        +lastName: string
        +resume: string
        +skills: Skill[]
        +experience: Experience[]
        +education: Education[]
        +updateProfile()
        +addSkill()
        +addExperience()
        +addEducation()
    }

    class Job {
        +title: string
        +description: string
        +requirements: string[]
        +company: string
        +location: string
        +type: JobType
        +status: JobStatus
        +publish()
        +unpublish()
        +match(candidate: Candidate)
    }

    class Application {
        +candidateId: string
        +jobId: string
        +status: ApplicationStatus
        +score: number
        +notes: string
        +updateStatus()
        +evaluate()
    }

    class Test {
        +title: string
        +type: TestType
        +questions: Question[]
        +duration: number
        +passingScore: number
        +assignToCandidate()
        +grade()
        +generateReport()
    }

    class TestAttempt {
        +testId: string
        +candidateId: string
        +answers: Answer[]
        +score: number
        +startTime: Date
        +endTime: Date
        +status: TestStatus
        +submit()
        +grade()
    }

    class Interview {
        +applicationId: string
        +type: InterviewType
        +scheduledDate: Date
        +duration: number
        +location: string
        +interviewers: string[]
        +status: InterviewStatus
        +feedback: Feedback[]
        +schedule()
        +reschedule()
        +addFeedback()
    }

    class Hiring {
        +applicationId: string
        +status: HiringStatus
        +offerDetails: Offer
        +documents: Document[]
        +startDate: Date
        +createOffer()
        +acceptOffer()
        +initiateOnboarding()
    }

    %% Servicios
    class AuthService {
        +login(credentials: LoginDTO)
        +register(userData: RegisterDTO)
        +validateToken(token: string)
        +refreshToken(token: string)
    }

    class CandidateService {
        +createProfile(data: CreateProfileDTO)
        +updateProfile(id: string, data: UpdateProfileDTO)
        +uploadResume(id: string, file: File)
        +searchCandidates(filters: SearchDTO)
    }

    class JobService {
        +createJob(data: CreateJobDTO)
        +updateJob(id: string, data: UpdateJobDTO)
        +publishJob(id: string)
        +searchJobs(filters: SearchDTO)
    }

    class MatchingService {
        +matchCandidateToJobs(candidateId: string)
        +matchJobToCandidates(jobId: string)
        +calculateScore(candidate: Candidate, job: Job)
    }

    %% Relaciones
    BaseEntity <|-- User
    BaseEntity <|-- Candidate
    BaseEntity <|-- Job
    BaseEntity <|-- Application
    BaseEntity <|-- Test
    BaseEntity <|-- TestAttempt
    BaseEntity <|-- Interview
    BaseEntity <|-- Hiring

    User "1" -- "1" Candidate
    Candidate "1" -- "*" Application
    Job "1" -- "*" Application
    Application "1" -- "*" TestAttempt
    Test "1" -- "*" TestAttempt
    Application "1" -- "*" Interview
    Application "1" -- "1" Hiring

    AuthService -- User
    CandidateService -- Candidate
    JobService -- Job
    MatchingService -- Application

    %% Enums
    class TestType {
        <<enumeration>>
        TECHNICAL
        PSYCHOMETRIC
        LANGUAGE
        SKILLS
    }

    class TestStatus {
        <<enumeration>>
        PENDING
        IN_PROGRESS
        COMPLETED
        EXPIRED
    }

    class InterviewType {
        <<enumeration>>
        TECHNICAL
        HR
        CULTURAL_FIT
        FINAL
    }

    class InterviewStatus {
        <<enumeration>>
        SCHEDULED
        COMPLETED
        CANCELLED
        RESCHEDULED
    }

    class HiringStatus {
        <<enumeration>>
        OFFER_PENDING
        OFFER_SENT
        ACCEPTED
        REJECTED
        ONBOARDING
    }
```

## Estructura de Clases

### Entidades Base
- **BaseEntity**: Clase base con campos comunes
- **IController**: Interfaz base para controladores
- **IService**: Interfaz base para servicios
- **IRepository**: Interfaz base para repositorios

### Entidades de Dominio
- **User**: Gestión de usuarios y autenticación
- **Candidate**: Información de candidatos
- **Job**: Información de empleos
- **Application**: Gestión de postulaciones

### Entidades de Evaluación
- **Test**: Definición de pruebas
- **TestAttempt**: Intentos de pruebas
- **Interview**: Gestión de entrevistas
- **Hiring**: Proceso de contratación

### Servicios Principales
- **AuthService**: Lógica de autenticación
- **CandidateService**: Gestión de candidatos
- **JobService**: Gestión de empleos
- **MatchingService**: Lógica de matching

## Patrones de Diseño

1. **Domain-Driven Design**
   - Entidades ricas en comportamiento
   - Agregados bien definidos
   - Servicios de dominio

2. **Repository Pattern**
   - Abstracción de persistencia
   - Operaciones CRUD base
   - Queries especializadas

3. **Factory Pattern**
   - Creación de entidades
   - Validación de datos
   - Inicialización consistente

4. **Strategy Pattern**
   - Algoritmos de evaluación
   - Procesos de matching
   - Flujos de trabajo
