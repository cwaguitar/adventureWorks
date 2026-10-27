# 🚴‍♂️ AdventureWorks: Optimización de Ventas y Modelado Dimensional 

## 💼 Contexto del Negocio & Problema

**AdventureWorks** es un fabricante y distribuidor global de equipos de ciclismo y accesorios. La dirección comercial enfrentaba dificultades para tomar decisiones estratégicas debido a la falta de visibilidad unificada sobre el rendimiento de las ventas por región y la rotación de catálogo.

### Retos Clave:

- **Falta de consolidación:** Los datos de transacciones, regiones y productos se encontraban aislados, dificultando el análisis cruzado.
- **Toma de decisiones lenta:** El equipo comercial no podía identificar con rapidez los productos estrella frente a los de baja rotación en cada territorio.

---

## 🎯 Solución Implementada

Se diseñó un pipeline de inteligencia de negocios de extremo a extremo que transforma los registros transaccionales en un **modelo de datos relacional altamente optimizado** y un **dashboard interactivo** en Power BI para el nivel directivo.

### 1. Arquitectura de Datos (Modelo en Estrella)

Para garantizar consultas rápidas y escalabilidad ante volúmenes masivos de ventas, se estructuró un **Star Schema**:

- **`fact_sales`**: Registra los eventos transaccionales, ingresos ($) y volumen de unidades (`Quantity`).
- **`dim_product`**: Dimensión de catálogo que permite segmentar el rendimiento por artículo.
- **`dim_region`**: Dimensión geográfica para análisis de penetración de mercado.

![Modelo en Estrella](https://github.com/cwaguitar/adventureWorks/blob/main/dashboard/vista_modelo.jpeg)

---

## 📊 Demostración Interactiva & Impacto
El dashboard permite al equipo gerencial filtrar interactivamente el rendimiento por territorio, evaluar la concentración de ingresos y ajustar las estrategias de inventario según la demanda regional.

![Demo Dashboard](https://github.com/cwaguitar/adventureWorks/blob/main/dashboard/adventure.gif)

---

## 🛠️ Stack Tecnológico & Competencias Demostradas
- **Python / SQL:** Limpieza, procesamiento e ingesta de datos transaccionales.
- **Modelado Dimensional:** Diseño de arquitectura Star Schema (Fact & Dimensions).
- **Power BI Desktop:** Modelado de relaciones, filtrado cruzado y visualización de KPIs.
- **Documentación Técnica:** Control de versiones e integración en GitHub.
