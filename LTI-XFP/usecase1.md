🔖 Caso de Uso #1: **Creación y publicación de vacantes**
---------------------------------------------------------

### 📌 **Descripción del Caso de Uso:**

| Campo                | Detalle del Caso de Uso                                                                                                                                                                                                                                                                                                                                 |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Nombre**           | Creación y publicación de vacantes                                                                                                                                                                                                                                                                                                                      |
| **Actores**          | • Reclutador Interno (Recruiter)<br>• Plataforma ATS<br>• LinkedIn                                                                                                                                                                                                                                                                                      |
| **Precondiciones**   | • Reclutador autenticado en la plataforma ATS.<br>• El usuario tiene rol y permisos necesarios para crear y publicar vacantes.<br>• Integración previa con LinkedIn activada y configurada.                                                                                                                                                             |
| **Disparador**       | El reclutador pulsa el botón "**Nueva Vacante**".                                                                                                                                                                                                                                                                                                       |
| **Flujo Principal**  | 1. Reclutador accede al sistema.<br>2. Selecciona "Nueva Vacante".<br>3. Introduce título, descripción, requisitos, habilidades, salario y otra información clave.<br>4. Selecciona los canales externos de publicación (LinkedIn Jobs, web corporativa).<br>5. Publica la vacante.<br>6. ATS confirma la publicación y sincroniza con los canales externos automáticamente.<br>7. ATS recibe candidaturas automáticamente. |
| **Flujos Alternativos** | • **Vacante incompleta o error en datos:** ATS muestra alerta al usuario para corrección.<br>• **Fallo al publicar en canales externos:** ATS muestra notificación automática al usuario para corregir el error y volver a intentar la publicación.                                                                                                                                                    |
| **Postcondiciones**  | • La vacante queda publicada exitosamente en ATS y canales externos.<br>• ATS comienza automáticamente a recibir candidaturas.                                                                                                                                                                                                                          |
| **Reglas de negocio** | • Una vacante no puede publicarse sin título, descripción básica y requisitos mínimos.<br>• El usuario debe disponer de permisos específicos para publicar vacantes.<br>• La integración con LinkedIn debe estar activa para la publicación automática.                                                                                                 |

### 📌 **Diagrama UML:**

```mermaid
sequenceDiagram
    actor Reclutador
    participant ATS
    participant LinkedIn

    Reclutador ->> ATS: Inicia creación de vacante
    ATS -->> Reclutador: Formulario creación vacante
    Reclutador ->> ATS: Introduce detalles vacante
    ATS ->> LinkedIn: Publica vacante automáticamente
    LinkedIn -->> ATS: Confirma publicación
    ATS -->> Reclutador: Notifica éxito publicación
```


