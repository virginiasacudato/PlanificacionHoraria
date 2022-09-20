
<!-- PROJECT LOGO -->
<br />
<div>
  <a href="https://github.com/virginiasacudato/PlanificacionHoraria">
   
  </a>

<h3 align="center">Automatización de Planificación Horaria</h3>






<!-- ABOUT THE PROJECT -->
## Acerca del proyecto

Con este proyecto se busca automatizar pruebas para el módulo Planificación Horaria.

A continuación un detalle de los casos de prueba que realiza:

**1. Test Suite (Jornadas):**
- Caso 1: Seleccionar x empleados de la lista y clickear "Generar". Verifica la existencia de elemento traído.
- Caso 2: Cambio de jornada completa para todos los días generados. Verifica el cambio.
- Caso 3: Cambio de jornada en algunos de los días generados. Verifica el cambio.

**2. Test Suite (Filtros):**
[Antes de generar empleados]
- Caso 1: Selecciona x elemento del filtro Empresa y Sector. Verifica cambios en vista.
- Caso 2: Selecciona x fecha desde/hasta. Verifica cambios en vista.
- Caso 3: Selecciona Empresa. Verifica cambios en vista.
- Caso 4: Seleccionar Sector. Verifica cambios en vista.

[Déspues de generar empleados]
- Caso 5: Selecciona x empleados. Verifica cambios en check Sabados y Domingos.
- Caso 6: Selecciona x empleados. Selecciona x empresa y genera nuevamente. Verifica cambios.
- Caso 7: Selecciona x empleados. Selecciona x sector y genera. Verifica cambios.
- Caso 8: X sector y x empresa.

**3. Test Suite (Save):**
*Precondiciones: Tener seleccionados x empleados, haber realizado cambios en jornada.*
- Caso 1 (Happy Path): Guardar. Verifica leyenda de operación exitosa.
- Caso 2: No realiza ningún cambio en jornada. Verifica leyenda de error.

**4. Test Suite (Imprimir):**
*Precondiciones: Tener seleccionados x empleados y haberlos generado.*
- Caso 1 (Happy Path): Selecciona "Imprimir". Verifica la generación de la pantalla de impresión.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Construido

* Python - Pytest
* Selenium


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Empezando

El proyecto está construido en base al patrón de diseño Page Object Model(POM).

### Prerequisitos

v.Python >= 3.10

### Instalación

1. Clonar el repositorio.
   ```sh
   git clone https://github.com/virginiasacudato/PlanificacionHoraria.git
   ```
2. Crear un archivo .env con las siguientes variables de entorno:
   ```sh
   USER=example@mail.com
   PASSWORD=password
   URL=http://urlexample.com
   ```
3. Descargar ```chromedriver``` y ubicar en la raíz del proyecto. 
            https://chromedriver.chromium.org/downloads

   *Tener en cuenta la version del navegador web a la hora de descargar.*
4. En línea de comandos ejecutar (*El segundo comando es opcional, sirve para ver los mensajes print*):
   ```sh
   python -m pytest
   ```
   ```sh
   python -m pytest -s
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contacto

Virginia Sacudato

Project Link: [https://github.com/virginiasacudato/PlanificacionHoraria](https://github.com/virginiasacudato/PlanificacionHoraria)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


 