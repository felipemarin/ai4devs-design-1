🔖 Caso de Uso #3: **Coordinación automática de entrevistas**
---------------------------------------------------------

### 📌 **Descripción del Caso de Uso:**

| Campo                                  | Detalle del Caso de Uso                                                                                                                                                                                                                                                                                  |
|----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Nombre**                             | Coordinación automática de entrevistas                                                                                                                                                                                                                                                                  |
| **Actores principales**                | • Reclutador interno (Recruiter)<br>• Hiring Manager<br>• Candidato                                                                                                                                                                                                                                    |
| **Actores secundarios (sistemas externos)** | • Calendario externo (Google Calendar, Microsoft Outlook)                                                                                                                                                                                                                                          |
| **Precondiciones**                     | • Reclutador ha seleccionado candidatos para entrevistar.<br>• Integración con calendarios externos configurada.                                                                                                                                                                                           |
| **Triggers** (Disparador)              | • Reclutador selecciona opción "Agendar entrevista" en ATS.                                                                                                                                                                                                                                              |
| **Flujo Principal (Main Flow)**        | 1. Reclutador selecciona candidatos y opción "Agendar entrevista".<br>2. ATS consulta disponibilidad en calendarios del equipo interno (Recruiter, Hiring Manager).<br>3. ATS muestra fechas disponibles al reclutador.<br>4. Reclutador confirma la fecha propuesta.<br>5. ATS agenda automáticamente entrevista en calendarios del equipo y candidato.<br>6. ATS envía email automático al candidato con detalles.<br>7. ATS envía recordatorios automáticos antes de la entrevista. |
| **Alternative Flows** (Flujos alternativos)  | • Calendario externo no sincronizado (ATS avisa para reintentar conexión).<br>• Reclutador selecciona manualmente la fecha si no acepta sugerencia automática del ATS.<br>• El candidato solicita cambio de fecha (requiere nueva aprobación del recruiter).                                        |
| **Postcondiciones**                    | • Entrevista correctamente programada en calendario de recruiters, managers y candidato.                                                                                                                                                                                                                  |
| **Reglas de negocio**                  | • El ATS siempre verificará disponibilidad antes de agendar la entrevista.<br>• Todos los participantes reciben notificación automática con confirmación de entrevista.<br>• Los cambios o reprogramaciones requieren confirmación por parte del reclutador.                                                                                                |
                                                                         |


### 📌 **Diagrama UML:**

```mermaid
sequenceDiagram
    actor Reclutador
    participant ATS
    participant Calendario
    participant Hiring_Manager
    participant Candidato

    Reclutador ->> ATS: Solicita agendar entrevista
    ATS ->> Calendario: Consulta disponibilidad equipo interno
    Calendario -->> ATS: Devuelve disponibilidad
    ATS -->> Reclutador: Muestra opciones disponibles
    Reclutador ->> ATS: Confirma fecha propuesta
    ATS ->> Calendario: Agenda entrevista automáticamente
    ATS ->> Hiring_Manager: Notifica entrevista agendada
    ATS ->> Candidato: Envía email confirmando entrevista
```





