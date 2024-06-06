# WorkBioFasta

Este es un paquete de Python diseñado para trabajar con secuencias de ADN y ARN. Proporciona diversas funcionalidades para leer, procesar, y analizar secuencias genéticas. Este paquete  facilita la lectura y extraccion de informacion contenida en archivos FASTA, la obtencion del complemento  de secuencias de nucleotidos,  la realizacion de transcripcion y traduccion de secuencias de ADN en ARN y peptidos  respectivamente, y la separacion de codones de acuerdo al marco de lectura.

## Uso

El paquete provee funcionalidades para:
    - Leer y extraer la informacion contenida en archivos FASTA de manera estructurada 
    - Obtener el complemento de una secuencia de nucleotidos de ARN o DNA
    - Realizar la transcripcion y traduccion de una secuencia de ADN en una secuencia de ARN, y luego en una secuencia de peptidos
    
En general el paquete busca simular algunas de las funcionalidades presentes en la libreria de Biopython como: 
    - Leer, Escribir e indexar (En este caso unicamente en formato FASTA) 
    - Obtener el complemento de una secuencia de DNA y RNA 
    - Transcribir y Traducir una secuencia
    
Tambien implementa nuevas funcionalidades relacionadas a los marcos de lectura como:
    - Crear 6 archivos con los codones de sus secuencias separados por espacios segun sea su marco de lectura
    -  Transcribir y traducir secuencias de DNA en secuencias de RNA y proteinas respectivamente, segun el 
    marco de lectura.

## Instalacion

Se puede instalar el paquete desde el repositorio de codigo fuente clonando el repositorio  en la maquina local:
```
git clone https://github.com/ArmandoTrapaga/Proyecto_Biopython_Armando_Melissa
# Cambia al directorio del repositorio clonado:
cd repositorio
# Instala el paquete utilizando pip:
pip install 
```
Para verificar que el paquete se haya instalado correctamente, abre una terminal o consola de Python e intenta importar el paquete

## Control de errores

El paquete contiene mecanismos para el control de errores como la validacion de argumentos, manejo de excepciones, validacion de datos, y mensajes de error informativos.

## Pruebas
El paquete cuenta con pruebas para los modulos que componen el paquete.

### Modulo "complemento.py"
```
python test_complemento.py
```
### Modulo "ids_seq.py"
```
python test_ids_seq.py
```
### Modulo "dogma.py"
```
python test_dogma.py
```
## Datos

El script está disenado para operar con datos en formato FASTA. No hay restricciones en el numero de li­neas en el archivo.

## Metadatos y documentacion

Este README ofrece informacion de uso basico. Para obtener informacion mas detallada sobre el diseno y la implementacion del script, se le invita a consultar la documentacion de los modulos del paquete.

## Codigo fuente

El codigo fuente se encuentra disponible en este repositorio. Se acoge con satisfaccion cualquier contribucion o sugerencia a traves de solicitudes pull request.

## Terminos de uso

Este script esta disponible bajo la licencia APACHE. Consulte el archivo LICENSE para obtener mas detalles.

## Como citar

Si utiliza este script en su trabajo, por favor cite: <email:aggonzal@lcg.unam.mx> y <email:melissap@lcg.unam.mx>

## Contactenos 

Si tiene problemas o preguntas, por favor abra un problema en este repositorio o pongase en contacto con nosotros en: <email:aggonzal@lcg.unam.mx> y <email:melissap@lcg.unam.mx>