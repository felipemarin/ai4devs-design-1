# Diseño del Sistema de Gestión de Candidatos - LTI

## 1. Descripción del Software

LTI es un Applicant-Tracking System (ATS) innovador diseñado para optimizar el proceso de contratación mediante automatización avanzada. Su valor añadido radica en la mejora de la eficiencia de los departamentos de Recursos Humanos, la colaboración en tiempo real entre reclutadores y managers, y la capacidad de automatizar tareas repetitivas.

### **Ventajas Competitivas**

- **Automatización inteligente**: Reducción del trabajo manual con flujos de trabajo automatizados.
- **Colaboración en tiempo real**: Espacio compartido entre reclutadores y managers con comentarios y evaluaciones.
- **Integraciones clave**: Conexión con LinkedIn, portales de empleo y herramientas de entrevista.
- **Análisis avanzado**: Generación de reportes con insights de contratación.

## 2. Funcionalidades Principales

1. **Publicación y gestión de ofertas de empleo**
2. **Seguimiento automatizado de candidatos**
3. **Colaboración en tiempo real**
4. **Integraciones con plataformas externas**
5. **Generación de reportes y análisis de datos**
6. **Manejo de entrevistas y pruebas automáticas**
7. **Retroalimentación estructurada entre equipos de reclutamiento**

## 3. Lean Canvas

```mermaid
graph TD;
    subgraph PROBLEMA [Problema]
        P1[Falta de automatización en RRHH]
        P2[Procesos de selección largos y costosos]
    end

    subgraph SOLUCIÓN [Solución]
        S1[ATS con automatización y análisis]
    end

    subgraph PROPUESTA_VALOR [Propuesta de Valor Única]
        PV1[Eficiencia y reducción de costos]
        PV2[Decisiones basadas en datos]
    end

    subgraph CLIENTES [Segmentos de Clientes]
        C1[Empresas medianas y grandes]
        C2[Startups en crecimiento]
    end

    subgraph CANALES [Canales]
        CH1[Integración con LinkedIn y portales de empleo]
        CH2[Marketing digital y referencias]
    end

    subgraph INGRESOS [Fuentes de Ingresos]
        I1[Suscripción SaaS]
        I2[Planes por usuario]
    end

    subgraph COSTOS [Estructura de Costos]
        CO1[Infraestructura cloud]
        CO2[Desarrollo y soporte]
    end

    subgraph MÉTRICAS [Métricas Clave]
        M1[Tasa de contratación exitosa]
        M2[Reducción del tiempo de selección]
        M3[Feedback positivo de usuarios]
    end

    subgraph VENTAJA [Ventaja Injusta]
        V1[Datos exclusivos y automatización avanzada]
        V2[IA para selección de candidatos]
    end

    P1 --> S1
    P2 --> S1
    S1 --> PV1
    S1 --> PV2
    PV1 --> C1
    PV1 --> C2
    PV2 --> C1
    PV2 --> C2
    C1 --> CH1
    C2 --> CH1
    CH1 --> I1
    CH2 --> I2
    I1 --> CO1
    I2 --> CO2
    CO1 --> M1
    CO1 --> M2
    CO2 --> M3
    M1 --> V1
    M2 --> V1
    M3 --> V2
```

## 4. Modelo de Datos Mejorado

```mermaid
classDiagram
    class Candidato {
        +ID
        +Nombre
        +Email
        +Experiencia
        +Skills
        +EstadoAplicacion
        +NotasEntrevista
        +ComentariosEvaluacion
    }
    class Oferta {
        +ID
        +Título
        +Descripción
        +FechaPublicacion
        +Estado
        +EmpresaID
    }
    class Reclutador {
        +ID
        +Nombre
        +Email
        +Rol
    }
    class Entrevista {
        +ID
        +Fecha
        +Estado
        +Notas
        +Evaluador
        +CandidatoID
    }
    class Prueba {
        +ID
        +Tipo
        +Puntuacion
        +CandidatoID
    }
    class Empresa {
        +ID
        +Nombre
        +Sector
        +Ubicacion
    }
    class ComentarioEvaluacion {
        +ID
        +CandidatoID
        +ReclutadorID
        +Texto
        +Fecha
    }
    Candidato --> Entrevista
    Candidato --> Prueba
    Candidato --> ComentarioEvaluacion
    Reclutador --> Oferta
    Reclutador --> ComentarioEvaluacion
    Oferta --> Empresa
```

## 5. Arquitectura del Sistema Mejorada

```mermaid
graph TD;
    UI[Frontend Web (React)] -->|API Requests| API[Backend (Node.js + Express)]
    API -->|Gestión de Datos| DB[PostgreSQL]
    API -->|Integración| EXT[LinkedIn, Portales de Empleo]
    API -->|Gestión de Entrevistas y Pruebas| TEST[Módulo de Evaluación]
    API -->|Generación de Reportes| REPORT[BI y Análisis]
    API -->|Microservicio de Notificaciones| NOTIF[Gestión de Notificaciones]
    API -->|Autenticación| AUTH[Microservicio de Autenticación]
```

## 6. Flujo de Procesos Mejorado

```mermaid
flowchart TD;
    Inicio --> PublicarOferta[Publicación de Oferta]
    PublicarOferta --> RecibirAplicaciones[Recepción de Aplicaciones]
    RecibirAplicaciones --> Evaluacion[Revisión y Evaluación]
    Evaluacion --> Entrevistas[Entrevistas Programadas]
    Evaluacion --> Pruebas[Pruebas Online]
    Pruebas --> Entrevistas
    Entrevistas --> DecisionFinal[Selección Final]
    DecisionFinal --> Contratacion[Proceso de Contratación]
    Contratacion --> Feedback[Evaluación del Proceso]
```