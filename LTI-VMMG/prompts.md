# prompt1
Eres un experto en producto, con experiencia en sistemas de reclutamiento ATS (Applicant-Tracking System). 

# prompt2
¿Qué funcionalidades básicas tiene un sistema de reclutamiento? Describelas en un listado, ordenado de mayor a menor prioridad

# prompt3
¿Que beneficios obtiene el cliente de un sistema de reclutamiento como este para considerar su uso?

# prompt4
Quiero desarrollar uno y para ello necesito previamente definir los siguientes puntos:
- Descripción breve del software LTI, valor añadido y ventajas competitivas. Explicación de las funciones principales. Añadir un diagrama Lean Canvas para entender el modelo de negocio  
- Descripción de los 3 casos de uso principales, con el diagrama asociado a cada uno  
- Modelo de datos que cubra entidades, atributos (nombre y tipo) y relaciones  
- Diseño del sistema a alto nivel, tanto explicado como diagrama adjunto  
- Diagrama C4 que llegue en profundidad a uno de los componentes del sistema, el que prefieras.  
Antes de hacer nada, quiero que me hagas todas las preguntas que necesites para resolver estos puntos.

# prompt5
Aqui van mis respuestas a tus preguntas:
- quiero diferenciar este ATS con la utilizacion de IA avanzada para mejorar el matching automatico y conseguir la mejor contratacion posible. El segmento de mercado es el IT y el canal de adquisición es directo.
- La gestion de candidatos, publicación de ofertas e integraciones con los principales portales de empleo son las funcionalidades imprescindibles para la primera version. Seria un SaaS en la nube con suscripción mensual. Las integraciones principales son Linkedin e Indeed.
- Los flujos mas criticos a modelar son la aplicacion de un candidato, evaluacion y seleccion y publicación de ofertas. La gestion tiene que poder ser multiempresa y con diferentes roles.
- El modelo de datos sera con CV en texto estructura y archivos adjuntos, con un seguimiento de interacciones con los candidatos (historial de entrevistas y feedback).
- Los datos clave para una oferta son los requisitos, ubicacion o modalidad de trabajo, salario, beneficios y expectativas del puesto.
- No tengo una arquitectura especifica, pero necesito que pueda ser escalabre para añadir mas integraciones o funcionalidades en el futuro.
- Tiene que incluir un proceso de autenticacion que maneje los distintos roles con sus permisos.
- El motor de matching es el componente que mas profundidad quiero en su analisis

# prompt6
Haz los diagramas en mermaid para poder exportarlos luego.