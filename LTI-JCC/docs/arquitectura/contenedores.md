# Diagrama de Contenedores

Este diagrama muestra la arquitectura de alto nivel del sistema ATS y sus principales componentes.

```mermaid
C4Container
    title Sistema ATS - Diagrama de Contenedores

    Person(candidato, "Candidato", "Usuario que busca empleo")
    Person(reclutador, "Reclutador", "Personal de RRHH")

    System_Boundary(ats, "Sistema ATS") {
        Container(spa, "Single Page Application", "React, TypeScript, Material-UI", "Interfaz web para usuarios")
        Container(mobile, "Aplicación Móvil", "React Native, TypeScript", "App móvil para candidatos")
        
        Container(api, "API Gateway", "Node.js, Express.js", "Gateway principal de APIs")
        
        Container(auth, "Servicio de Autenticación", "Node.js, JWT, OAuth2", "Gestión de autenticación y autorización")
        Container(candidates, "Servicio de Candidatos", "Node.js, Express", "Gestión de perfiles y aplicaciones")
        Container(jobs, "Servicio de Empleos", "Node.js, Express", "Gestión de vacantes")
        Container(matching, "Servicio de Matching", "Node.js, Express", "Evaluación y matching de candidatos")
        
        ContainerDb(db, "Base de Datos", "PostgreSQL", "Almacenamiento principal")
        ContainerDb(cache, "Cache", "Redis", "Caché de datos frecuentes")
        
        Container(queue, "Cola de Mensajes", "RabbitMQ", "Gestión de eventos y mensajes")
        Container(notification, "Servicio de Notificaciones", "Node.js", "Gestión de notificaciones")
    }

    System_Ext(email, "Servicio de Email")
    System_Ext(jobBoards, "Job Boards")
    System_Ext(calendar, "Calendario")

    %% Relaciones Frontend
    Rel(candidato, spa, "Usa", "HTTPS")
    Rel(candidato, mobile, "Usa", "HTTPS")
    Rel(reclutador, spa, "Usa", "HTTPS")

    %% Relaciones API
    Rel(spa, api, "API Calls", "JSON/HTTPS")
    Rel(mobile, api, "API Calls", "JSON/HTTPS")

    %% Relaciones Servicios
    Rel(api, auth, "Valida", "JSON/HTTPS")
    Rel(api, candidates, "Usa", "JSON/HTTPS")
    Rel(api, jobs, "Usa", "JSON/HTTPS")
    Rel(api, matching, "Usa", "JSON/HTTPS")

    %% Relaciones Base de Datos
    Rel(candidates, db, "Lee/Escribe", "SQL")
    Rel(jobs, db, "Lee/Escribe", "SQL")
    Rel(matching, db, "Lee", "SQL")
    
    %% Relaciones Cache
    Rel(api, cache, "Lee/Escribe", "Redis Protocol")
    
    %% Relaciones Cola de Mensajes
    Rel(candidates, queue, "Publica", "AMQP")
    Rel(jobs, queue, "Publica", "AMQP")
    Rel(notification, queue, "Suscribe", "AMQP")
    
    %% Relaciones Sistemas Externos
    Rel(notification, email, "Envía", "SMTP")
    Rel(jobs, jobBoards, "Publica", "API")
    Rel(candidates, calendar, "Agenda", "API")
```

## Componentes Principales

### Frontend
- **Single Page Application**: Interfaz web principal
- **Aplicación Móvil**: Versión móvil para candidatos

### Backend
- **API Gateway**: Punto de entrada único para todas las peticiones
- **Servicios Core**:
  - Autenticación
  - Gestión de Candidatos
  - Gestión de Empleos
  - Sistema de Matching
  - Notificaciones

### Almacenamiento
- **PostgreSQL**: Base de datos principal
- **Redis**: Sistema de caché

### Mensajería
- **RabbitMQ**: Sistema de colas para eventos

## Patrones de Diseño Implementados

1. **API Gateway**
   - Punto único de entrada
   - Manejo de autenticación
   - Rate limiting
   - Logging centralizado

2. **Microservicios**
   - Servicios independientes
   - Bases de datos por servicio
   - Comunicación asíncrona

3. **Event-Driven**
   - Publicación/Suscripción de eventos
   - Procesamiento asíncrono
   - Desacoplamiento de servicios

4. **Caching**
   - Caché de datos frecuentes
   - Mejora de rendimiento
   - Reducción de carga en BD 