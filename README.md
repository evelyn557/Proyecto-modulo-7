
# Alke Wallet - Proyecto Módulo 7

Aplicación web desarrollada en **Django** que simula una plataforma de billetera digital (Alke Wallet), permitiendo la gestión administrativa de clientes, el control de cuentas asociadas y el registro de movimientos financieros (ingresos y egresos). Este proyecto corresponde a las evaluaciones del Módulo 7.

---

## 📋 Características Principales

* **Autenticación y Seguridad:** Acceso exclusivo para usuarios administradores o personal autorizado (*staff*), protegiendo las vistas mediante Mixins de Django (`LoginRequiredMixin` y `UserPassesTestMixin`).
* **Gestión de Clientes (CRUD):** 
  * Listado completo con buscador integrado por nombre o correo electrónico.
  * Vista de detalles avanzada en dos columnas que incluye datos personales, número de cuenta, saldo actual y un historial detallado de transacciones.
  * Formularios estilizados para la creación, edición y eliminación de clientes.
* **Interfaz Moderna:** Diseñado con **Bootstrap 5**, tablas responsivas, tarjetas informativas (*cards*) y alertas dinámicas de retroalimentación para el usuario.
* **Manejo de Transacciones:** Visualización automática de movimientos financieros diferenciados por tipo (ingresos en verde, egresos en rojo).

---

## 🛠️ Tecnologías Utilizadas

* **Python** (Versión 3.14)
* **Django** (Versión 6.1.1)
* **Bootstrap** (Versión 5.0.2)
* **SQLite** (Base de datos por defecto para desarrollo)

---

## 📁 Estructura del Proyecto

* `alkewallet/`: Configuración general del proyecto Django (`settings.py`, `urls.py`, etc.).
* `gestion/`: Aplicación principal encargada de la lógica del negocio.
  * `models.py`: Modelos de datos (`Cliente`, `Cuenta`, `Transaccion`).
  * `views.py`: Vistas basadas en clases (CBVs) para la gestión y control de acceso.
  * `forms.py`: Formularios para el registro y actualización de clientes.
  * `templates/gestion/`: Archivos HTML con la interfaz de usuario (`base.html`, `lista_clientes.html`, `detalle_cliente.html`, etc.).

---

## 🗄️ 1. Configuración de la Base de Datos y Definición de Modelos

* **Configuración de la Base de Datos:** El proyecto utiliza **SQLite** como motor de base de datos relacional predeterminado mediante el archivo `settings.py`, permitiendo almacenar de manera local y ligera toda la información del sistema.
* **Definición de Modelos (`models.py`):** Se estructuraron tres modelos principales interconectados mediante relaciones relacionales (`ForeignKey` y `OneToOneField`):
  * **`Cliente`**: Almacena datos personales básicos (`nombre`, `email`, `telefono`).
  * **`Cuenta`**: Representa la billetera financiera del cliente, con su número de cuenta y saldo actual.
  * **`Transaccion`**: Registra cada movimiento vinculado a una cuenta (ingreso o egreso, monto, descripción y fecha/hora).

---

## 💡 2. Reflexiones sobre el ORM, Migraciones y Consultas

* **Uso del ORM de Django:** Simplificó la interacción con la base de datos permitiendo realizar operaciones CRUD a través de clases y métodos de Python de forma limpia y segura, evitando consultas SQL manuales.
* **Gestión de Migraciones:** Los comandos `makemigrations` y `migrate` aseguraron un control de versiones estructurado para reflejar de forma íntegra los cambios de los modelos en las tablas de la base de datos.
* **Consultas Personalizadas:** La integración de filtros avanzados y relaciones inversas demostró la alta eficiencia del ORM para calcular saldos y extraer historiales financieros de manera optimizada.

---

## 🚀 3. Instalación y Configuración Local

Sigue estos pasos para levantar el proyecto en tu entorno local:

1. Clonar el repositorio o descomprimir el proyecto:
   cd Proyecto-modulo-7

2. Crear y activar el entorno virtual:
   - En macOS / Linux:
     python -m venv venv
     source venv/bin/activate
   - En Windows:
     python -m venv venv
     venv\Scripts\activate

3. Instalar las dependencias:
   pip install django

4. Realizar las migraciones de la base de datos:
   python manage.py makemigrations
   python manage.py migrate

5. Crear un superusuario (necesario para acceder a las vistas protegidas y al panel de administración):
   python manage.py createsuperuser

6. Ejecutar el servidor de desarrollo:
   python manage.py runserver
---

## 📷 Evidencia de Funcionamiento (Capturas de Pantalla)

* **CLIENTES:**

<img width="1425" height="766" alt="clientes_AlkeWallet" src="https://github.com/user-attachments/assets/7dcecc12-add6-4359-9ad7-b011eeda0a0f" />



* **DETALLE Y ESTADO DE CUENTA:**

<img width="1425" height="766" alt="Detalle_estadocuenta" src="https://github.com/user-attachments/assets/eef0f7da-e438-40f7-8aa5-341775fcf8d3" />



* **CREAR REGISTROS (Desde la terminal):**

<img width="592" height="327" alt="crear_registros" src="https://github.com/user-attachments/assets/12e07629-8db4-4472-af76-0ab557499871" />



* **ACTUALIZAR REGISTROS (Desde la terminal):**
  
<img width="592" height="327" alt="actualizar_registros" src="https://github.com/user-attachments/assets/1a58d8bd-d578-4062-aa85-eeacbd356eb6" />



* **FILTRAR REGISTROS (Desde la terminal):**

<img width="592" height="327" alt="filtrar_registros" src="https://github.com/user-attachments/assets/5f9e1fa7-f19d-4cf3-8afc-ec4615e37da2" />




* **LEER REGISTROS (Desde la terminal):**

<img width="592" height="327" alt="leer_registros" src="https://github.com/user-attachments/assets/ebd7d7ba-75e7-4dc6-b5ad-e6c9998f2214" />



## 🎥 Demostración en video de las principales funcionalidades implementadas en el sistema:

---

 * **🛠️ Uso de panel de administración:**


https://github.com/user-attachments/assets/f3144e74-146a-41fa-b52e-566772bfcfb3


---

* ** 💳 Registro de  movimientos / transacción:**


https://github.com/user-attachments/assets/befdca1f-083f-4a30-93c5-115853bdad42



---

* **✏️ Editar y crear registros:**







https://github.com/user-attachments/assets/465755cd-780d-4d19-ade9-0a5b540fc5ce



---

* **VALIDACIÓN DE INTEGRIDAD REFERENCIAL (ProtectedError):**
 



https://github.com/user-attachments/assets/67e4c637-350b-4e5c-bf3f-7d7f62aaa808








