**Rol**: Actúa como arquitecto de software con enfoque en producto. Analiza las necesidades de LTI y elabora la primera versión de su ATS.

---

## 1. Descripción del Software LTI

- **Objetivo**: Explica brevemente qué es LTI y cuál es su valor añadido (eficiencia en HR, automatizaciones, IA asistida, etc.).

- **Ventajas competitivas**: Incluye al menos 3 diferenciales frente a la competencia.

- **Funciones principales**: Menciona las capacidades esenciales del ATS (gestión de candidatos, evaluaciones colaborativas, notificaciones automatizadas, etc.).

- **Lean Canvas**: Crea un diagrama con los componentes clave (problema, propuesta de valor, segmentos de clientes, canales, estructura de costes, etc.) **utilizando plantUML**. Presenta el código en un bloque <code>```plantuml ... ```</code>.

## 2. Casos de Uso Principales

- **Descripción**: Detalla 3 escenarios de uso clave (ejemplo: registro de candidato, proceso de entrevista, feedback colaborativo).

- **Diagramas**: Para cada caso, describe un diagrama de flujo o de secuencia **usando plantUML**, mostrando la interacción entre usuarios y sistema. Utiliza la sintaxis `@startuml ... @enduml`.

---

## 3. Modelo de Datos

- **Entidades**: Lista entidades (p. ej., “Candidato”, “Vacante”, “Entrevista”) con una breve descripción.

- **Atributos**: Indica nombre y tipo (p. ej., “nombre: string”, “fechaAplicacion: date”).

- **Relaciones**: Explica cómo se vinculan las entidades (p. ej., “Un Candidato puede aplicar a muchas Vacantes”).

- **Diagrama de Entidades**: Genera un diagrama de relaciones entre entidades con plantUML (p. ej., `@startuml ... @enduml`).

---

## 4. Diseño de Sistema (Alto Nivel)

- **Descripción Global**: Explica, en un párrafo, la arquitectura general (por capas, microservicios, monolito, etc.).

- **Diagrama General**: Proporciona un diagrama en plantUML que muestre los componentes principales (API, base de datos, servicios de IA, etc.).

---

## 5. Diagrama C4 Detallado

- **Enfoque en un Componente**: Elige uno (por ejemplo, el motor de recomendación de candidatos).

- **Niveles del Diagrama**:

1. Context

2. Container

3. Component (más profundidad en el componente elegido)

4. (Opcional) Code (si se desea detallar aún más).

- **Presentación**: Para cada nivel, utiliza la sintaxis de plantUML y entrega el diagrama dentro de un bloque de código `@startuml ... @enduml`.

- **Justificación**: Explica brevemente por qué ese componente es crítico en la arquitectura.

---

### Instrucciones de Entrega

1. **Escribe** tu respuesta en texto continuo y en formato markdown.

2. **Incluye** cada diagrama en un bloque de código con sintaxis de plantUML (p. ej. `@startuml ... @enduml`).

3. **Mantén** un enfoque de producto y justifica cómo cada funcionalidad aporta valor a LTI.

¡Adelante! Diseña el ATS para LTI, incluye los diagramas en plantUML y entrega todos los puntos solicitados con detalle, creatividad y claridad.