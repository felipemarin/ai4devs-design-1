# Diseño de la Primera Versión del Sistema LTI

## 1. Descripción del Software

LTI es una plataforma innovadora de gestión del talento que optimiza los procesos de contratación y recursos humanos mediante automatización inteligente, colaboración en tiempo real y asistencia basada en IA. Su propuesta de valor se centra en reducir los tiempos de contratación, mejorar la toma de decisiones con análisis predictivo y garantizar una experiencia de usuario intuitiva y flexible. La diferenciación competitiva se basa en su integración fluida con sistemas existentes, escalabilidad modular y altos estándares de seguridad y cumplimiento normativo.

## 2. Funciones Principales

### a) Optimización de Procesos de HR

- Automatización de revisión de CVs y programación de entrevistas.
- Algoritmos de matching inteligente para candidatos y vacantes.
- Integración con sistemas RPA para reducir errores.

### b) Colaboración en Tiempo Real

- Plataforma unificada para interacción entre reclutadores y managers.
- Comunicación integrada (chat, comentarios en perfiles, notificaciones).
- Dashboards con métricas en tiempo real.

### c) Asistencia de IA en Decisiones

- Modelos de Machine Learning para predecir retención y tendencias.
- Chatbots impulsados por NLP para atención a candidatos y managers.
- Análisis de datos históricos para mejorar estrategias.

### d) Integración con Ecosistemas Existentes

- Compatibilidad con HRM y ATS del mercado.
- APIs abiertas para integración con ERP y CRM.
- Soporte para JSON y XML.

### e) Seguridad y Cumplimiento Normativo

- Encriptación de datos y autenticación multifactor.
- Cumplimiento con GDPR y CCPA.
- Auditorías de seguridad periódicas.

## 3. Lean Canvas

| Sección | Descripción |
| ------- | ----------- |
| **Problema** | Procesos de contratación largos, falta de colaboración, toma de decisiones basada en intuición. |
| **Segmento de Clientes** | Empresas de tamaño mediano y grande, industrias con alta rotación de talento. |
| **Propuesta de Valor** | Optimización de HR con IA, colaboración en tiempo real y automatización inteligente. |
| **Solución** | Automatización, matching inteligente, dashboards, IA para decisiones. |
| **Canales** | Ventas directas B2B, marketing digital, partnerships con HRM/ATS. |
| **Estructura de Costos** | Desarrollo, hosting, seguridad, marketing y soporte. |
| **Fuentes de Ingresos** | Suscripción SaaS, licencias on-premise, consultoría de implementación. |
| **Métricas Clave** | Tiempo medio de contratación, tasa de retención de candidatos, adopción de la plataforma. |

## 4. Casos de Uso

### Caso de Uso 1: Revisión Automática de CVs

**Actores:** Reclutador, Sistema LTI.

**Descripción:** El sistema analiza automáticamente los CVs de candidatos y los clasifica según el nivel de compatibilidad con la vacante.

### Caso de Uso 2: Comunicación en Tiempo Real

**Actores:** Reclutador, Manager.

**Descripción:** Los reclutadores y managers pueden dejar comentarios en perfiles de candidatos y recibir notificaciones en tiempo real.

### Caso de Uso 3: Predicción de Retención de Candidatos

**Actores:** Manager, Sistema LTI.

**Descripción:** Un modelo de IA analiza datos históricos y proporciona una probabilidad de retención para cada candidato preseleccionado.

## 5. Modelo de Datos

### Entidades Principales

- **Usuario** (id: int, nombre: string, email: string, rol: enum)
- **Candidato** (id: int, nombre: string, cv: text, experiencia: int)
- **Vacante** (id: int, título: string, requisitos: text, empresa: string)
- **Comentario** (id: int, usuario_id: int, candidato_id: int, contenido: text)
- **Evaluación IA** (id: int, candidato_id: int, score: float, recomendaciones: text)

## 6. Diseño del Sistema

El sistema LTI se basa en una arquitectura de microservicios desplegados en la nube con las siguientes capas:

1. **Capa de Presentación:** Aplicación web y móvil basada en React.
2. **Capa de Servicios:** API RESTful con Django REST Framework.
3. **Capa de Datos:** PostgreSQL para datos estructurados y Elasticsearch para búsqueda avanzada.
4. **Capa de IA:** Modelos de Machine Learning en Python (scikit-learn, TensorFlow).

**Diagrama de Arquitectura:**

+----------------+ +----------------+ +----------------+ | Frontend | ---> | Backend API | ---> | Base de Datos | +----------------+ +----------------+ +----------------+ | | | v v v +----------------+ +----------------+ +----------------+ | AI Engine | ---> | Notificaciones | ---> | Integraciones | +----------------+ +----------------+ +----------------+


## 7. Diagrama C4

Nivel 1 - **Contexto:** LTI como sistema central que interactúa con empresas, candidatos y sistemas externos.  
Nivel 2 - **Contenedores:** Descripción de los principales componentes del sistema (frontend, API, bases de datos, IA, notificaciones).

+------------------------------------+ | Sistema LTI | | +----------------------------+ | | | API de Reclutamiento | | | | | | | | +---------------------+ | | | | | Servicio de IA | | | | | | Predicciones ML | | | | | +---------------------+ | | | +----------------------------+ | +------------------------------------+


Este diseño provee una visión estructurada del sistema LTI, permitiendo futuras iteraciones y mejoras con base en retroalimentación del mercado y avances tecnológicos.
