# SISTEMA EXPERTO: RECOMENDACIÓN DE PELÍCULAS

## Indice:
- [Descripción](#descripción)
- [Consideraciones](#consideraciones)
    - [Sedes](#sedes)
    - [Géneros](#géneros)
    - [Estados de ánimo](#estados-de-ánimo)
    - [Año de Estreno](#año-de-estreno)
    - [Popularidad](#popularidad)
    - [Duración](#duración)
- [Instalación](#instalación)

## Descripción:
Este proyecto es un sistema de recomendación de películas basado en sistemas expertos. Utiliza Flask para el desarrollo del backend y JSON para el manejo de datos. El sistema experto se encarga de analizar las preferencias del usuario en términos de géneros y estados de ánimo para sugerir películas que se ajusten a sus gustos.

## Consideraciones para la base de conocimiento:
### Sedes:
**Comas**, **SJL** y **San Miguel**

### Géneros:
- **Acción**: Películas que enfatizan la adrenalina y el movimiento.
- **Aventura**: Historias que involucran exploraciones y experiencias emocionantes.
- **Comedia**: Diseñadas para provocar risa y entretenimiento.
- **Drama**: Se centra en conflictos emocionales y situaciones serias.
- **Terror**: Busca provocar miedo o inquietud en el espectador.
- **Ciencia Ficción**: Explora conceptos futuristas o fenómenos imaginarios.
- **Fantasía**: Incluye elementos mágicos o sobrenaturales.

### Estados de ánimo:
- **Intensa**: Películas que generan emociones fuertes y mantienen al espectador al borde de su asiento.
- **Intrigante**: Historias que despiertan curiosidad y mantienen el interés a través de giros inesperados.
- **Melancólica**: Narrativas que evocan nostalgia o tristeza, tocando temas profundos.
- **Inspiradora**: Películas que motivan y alientan a la superación personal.
- **Romántica**: Historias que exploran el amor y las relaciones personales de manera conmovedora.
- **Reflexiva**: Obras que invitan a la introspección y a pensar sobre la vida y las decisiones.

### Año de Estreno
De acuerdo a la época (los 90', 00' 10', etc)

### Popularidad
Se le coloca el puntaje que tiene la película en cuanto a popularidad (del 1 al 10)

### Duración
De acuerdo al tiempo disponible de los usuarios 

## Instalación

Para instalar y ejecutar el proyecto, sigue los siguientes pasos:

1. **Clonar el repositorio:**
    ```bash
    git clone git@github.com:JoArDiTo/sistemas-experto-peliculas.git
    cd sistemas-experto-peliculas
    ```

2. **Crear y activar un entorno virtual:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. **Instalar las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Ejecutar el programa:**
    ```bash
    flask run
    ```

Esto iniciará el servidor Flask y podrás acceder al sistema de recomendación de películas en tu navegador web.