# Diseño del Sistema ATS de LTI

## 1. Descripción del Software LTI

### Valor Añadido y Ventajas Competitivas
LTI es un sistema de rastreo de candidatos (ATS, Applicant Tracking System) de nueva generación que busca revolucionar el proceso de selección y contratación. Su enfoque se centra en la eficiencia, la colaboración en tiempo real y la automatización inteligente mediante IA. Sus ventajas principales incluyen:
- **Automatización inteligente:** Filtrado y clasificación de CVs con IA, programación automática de entrevistas y respuestas automatizadas a los candidatos.
- **Colaboración en tiempo real:** Espacios compartidos entre reclutadores y managers para evaluar candidatos y tomar decisiones conjuntas.
- **Integraciones fáciles:** Conectividad con plataformas como LinkedIn, Indeed y CRMs corporativos.
- **Análisis avanzado:** Informes personalizables sobre procesos de selección, tiempos de contratación y rendimiento de los candidatos.

### Funciones Principales
- **Publicación de ofertas de trabajo** en múltiples plataformas.
- **Recepción y gestión de aplicaciones** con IA para filtrar CVs.
- **Colaboración entre reclutadores y managers** mediante comentarios y evaluaciones conjuntas.
- **Automatización de entrevistas** con sugerencias de horarios y videollamadas integradas.
- **Seguimiento del candidato** desde la postulación hasta la contratación.
- **Reportes y análisis** con métricas clave para optimizar procesos de selección.

## 2. Lean Canvas (Modelo de Negocio)
(Se incluirá un diagrama Lean Canvas con los siguientes elementos: problema, solución, métricas clave, propuesta de valor, canales, segmentos de clientes, estructura de costos e ingresos.)

## 3. Casos de Uso Principales

### Caso de Uso 1: Publicación de una Oferta de Trabajo
**Actores:** Reclutador
**Flujo Principal:**
1. El reclutador inicia sesión en LTI.
2. Crea una nueva oferta de trabajo.
3. Define requisitos y criterios de selección.
4. Publica la oferta en múltiples plataformas integradas.
5. El sistema confirma la publicación y rastrea postulaciones.

(Diagrama de caso de uso asociado)

### Caso de Uso 2: Evaluación y Selección de Candidatos
**Actores:** Reclutador, Manager
**Flujo Principal:**
1. El sistema recibe postulaciones y aplica filtros automáticos.
2. Reclutadores y managers revisan perfiles recomendados.
3. Se califican y comentan los candidatos.
4. Se programa la entrevista automáticamente.
5. Se notifica al candidato y se realiza la entrevista.
6. Se toma la decisión final y se notifica al candidato seleccionado.

(Diagrama de caso de uso asociado)

### Caso de Uso 3: Reportes y Métricas de Selección
**Actores:** Gerente de RRHH
**Flujo Principal:**
1. El gerente accede a la sección de reportes.
2. Selecciona filtros para generar informes personalizados.
3. El sistema genera un dashboard con KPI clave.
4. El gerente exporta el reporte en formato deseado.

(Diagrama de caso de uso asociado)

## 4. Modelo de Datos
Se define el modelo de datos con entidades principales:

- **Usuarios (id, nombre, email, rol)**
- **Ofertas de Trabajo (id, título, descripción, requisitos, estado, fecha publicación)**
- **Candidatos (id, nombre, email, CV, estado, puntuación IA)**
- **Entrevistas (id, candidato_id, oferta_id, fecha, evaluación)**
- **Comentarios y Evaluaciones (id, usuario_id, candidato_id, puntuación, observaciones)**

(Diagrama de modelo de datos asociado)

## 5. Diseño de Alto Nivel
Se describen los módulos principales del sistema:
- **Módulo de Publicación de Ofertas**
- **Módulo de Gestión de Candidatos**
- **Módulo de Automatización y Programación de Entrevistas**
- **Módulo de Análisis y Reportes**
- **Módulo de Integraciones con Terceros**

(Diagrama del sistema a alto nivel adjunto)

## 6. Diagrama C4 (Componente Detallado)
Se elegirá un componente clave (ej. Gestión de Candidatos) para detallar su arquitectura interna según el modelo C4.

(Diagrama C4 adjunto)

---

Se incluirán todos los diagramas correspondientes en cada sección.

