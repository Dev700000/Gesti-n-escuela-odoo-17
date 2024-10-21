# Módulo de Gestión Educativa para Odoo

## Objetivo

Este módulo tiene como propósito gestionar las inscripciones de alumnos en un sistema educativo. Permite a una institución educativa administrar eficientemente los recursos relacionados con alumnos, materias, cursos y profesores.

## Requisitos Funcionales

### Modelo de Alumnos
- Crear un modelo que herede de `res.partner` para gestionar los datos de los alumnos.
- Añadir un campo de fecha de nacimiento.
- Implementar un método que calcule y muestre automáticamente la edad del alumno basado en su fecha de nacimiento.

### Modelo de Inscripciones
- Crear un modelo para gestionar las inscripciones de los alumnos en diferentes cursos.
- Contener referencias a los alumnos, cursos y fecha de inscripción.
- Incluir un campo de estado para gestionar el flujo de inscripción (Ej. Pendiente, Confirmada, Cancelada).

### Modelo de Materias
- Crear un modelo para gestionar las materias que se impartirán en los cursos.
- Incluir campos como nombre de la materia, descripción y número de créditos.

### Modelo de Cursos
- Crear un modelo que herede de `product.template` para gestionar los cursos como productos consumibles.
- Incluir:
  - Profesores asignados.
  - Materias impartidas en el curso.
  - Duración y fecha de inicio del curso.
  - Capacidad máxima de alumnos por curso.

### Modelo de Profesores
- Crear un modelo que herede de `res.partner` para gestionar los datos de los profesores.
- Incluir referencias a las materias que imparten.

## Requisitos Técnicos

### Interfaz de Usuario
- Diseñar interfaces de usuario intuitivas para la gestión de alumnos, inscripciones, materias, cursos y profesores.
- Asegurar la consistencia y usabilidad en todas las vistas del módulo.

### Seguridad
- Implementar medidas de seguridad que restrinjan el acceso y modificación de los datos del módulo.
- Solo los administradores y usuarios autorizados podrán acceder y gestionar la información.
- Crear grupos de acceso para diferenciar roles de usuario (Ej. Administrador, Profesor, Coordinador).

### Documentación
- Instrucciones detalladas sobre la instalación, configuración y uso del módulo.
- Explicación clara de los modelos y su propósito dentro del sistema.
- Instrucciones para la administración y mantenimiento del sistema.
- Incluir comentarios en el código que faciliten su comprensión.

## Instalación

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/Dev700000/Gesti-n-escuela-odoo-17.git
