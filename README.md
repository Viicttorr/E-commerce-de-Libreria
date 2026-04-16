# 🛒 E-commerce de Librería
Aplicación web desarrollada en **Django** como parte de la Evaluación Sumativa 2 de Programación Back End.  
El proyecto consiste en un **sitio Ecommerce funcional** que permite visualizar productos, gestionarlos desde un panel administrativo y navegar por categorías y detalles.

---

## 🚀 Funcionalidades principales

### Estructura de datos
Cada producto incluye:
- Nombre
- Precio
- Stock
- Descripción
- Imagen

### Páginas del sitio
- **Página principal**: muestra todos los productos disponibles y un **navbar** para navegar entre categorías.
- **Página por categoría**: lista únicamente los productos de la categoría seleccionada.
- **Página de detalle del producto**: muestra información detallada (descripción, stock, precio e imagen ampliada).
- **Página de administrador**:
  - Inserción, modificación y eliminación de productos.
  - Visualización de modelos en columnas por atributos.

### Credenciales de administrador
- Usuario: **ES02**  
- Contraseña: **pbe-es-02**

---

## 🎯 Objetivos de aprendizaje

1. Construir un sitio Ecommerce funcional con **Django**.  
2. Implementar navegación por categorías y detalle de productos.  
3. Integrar base de datos para gestión de productos.  
4. Configurar y utilizar el **panel administrativo de Django**.  
5. Aplicar buenas prácticas de seguridad (uso de `.gitignore`).  

---

## 🛠️ Tecnologías utilizadas

- **Python 3.x**
- **Django**
- **Bootstrap**
- **SQLite (por defecto)**

---

## 📂 Estructura del proyecto

- `/project/` → Configuración principal de Django.  
- `/app/` → Aplicación con modelos, vistas y lógica de negocio.  
- `/templates/` → Archivos HTML para frontend.

---

## ⚙️ Instalación y ejecución

1. Clonar el repositorio.
2. Crear y activar entorno virtual:
   - python -m venv venv
   - venv\Scripts\activate.bat
3. Instalar dependencias:
   - pip install django
4. Ejecutar servidor:
   - python manage.py runserver
5. Abrir en navegador:
   - http://127.0.0.1:8000/

---

## 👨‍💻 Actividad demostrada
- Visualización de productos en página principal.
- Navegación por categorías.
- Detalle de producto con información completa.
- Gestión de productos desde el panel administrativo.
- Inserción, modificación y eliminación de registros en BD.

---

## 📜 Licencia
Este proyecto se distribuye bajo la licencia MIT.
Puedes usarlo, modificarlo y compartirlo libremente, siempre mencionando la autoría original.
