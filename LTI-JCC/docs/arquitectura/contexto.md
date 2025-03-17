# Diagrama de Contexto

Este diagrama muestra la visión general del sistema ATS y su interacción con usuarios externos y sistemas.

```mermaid
C4Context
    title Sistema ATS - Diagrama de Contexto

    Person(candidato, "Candidato", "Usuario que busca empleo")
    Person(reclutador, "Reclutador", "Personal de RRHH")
    Person(admin, "Administrador", "Administrador del sistema")

    System(ats, "Sistema ATS", "Sistema de Seguimiento de Candidatos")

    System_Ext(email, "Servicio de Email", "Sistema de envío de correos")
    System_Ext(jobBoards, "Job Boards", "Portales de empleo externos")
    System_Ext(calendar, "Calendario", "Sistema de calendario")
    System_Ext(analytics, "Analytics", "Sistema de análisis de datos")

    Rel(candidato, ats, "Se registra, aplica a empleos, actualiza perfil")
    Rel(reclutador, ats, "Gestiona vacantes, evalúa candidatos")
    Rel(admin, ats, "Configura y administra el sistema")

    Rel(ats, email, "Envía notificaciones")
    Rel(ats, jobBoards, "Publica ofertas y recibe aplicaciones")
    Rel(ats, calendar, "Agenda entrevistas")
    Rel(ats, analytics, "Envía datos para análisis")
```

## Elementos Principales

### Usuarios
- **Candidatos**: Personas que buscan empleo y aplican a las vacantes
- **Reclutadores**: Personal de RRHH que gestiona el proceso de selección
- **Administradores**: Responsables de la configuración y gestión del sistema

### Sistemas Externos
- **Servicio de Email**: Manejo de comunicaciones por correo electrónico
- **Job Boards**: Integración con portales de empleo
- **Calendario**: Gestión de agenda y entrevistas
- **Analytics**: Análisis de datos y reportes

## Responsabilidades

### Sistema ATS
1. Gestión de perfiles de candidatos
2. Publicación y gestión de vacantes
3. Proceso de selección automatizado
4. Comunicación con candidatos
5. Reportes y análisis
6. Agenda de entrevistas
7. Evaluación de candidatos 