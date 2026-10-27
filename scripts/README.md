# 📊 Sales Analytics & Star Schema Portfolio Project

## 📌 Descripción del Proyecto
Este proyecto demuestra el diseño e implementación de un pipeline de datos de ventas de extremo a extremo, estructurado mediante un **Modelo en Estrella (Star Schema)** e integrado en **Power BI** para la toma de decisiones estratégicas.

---

## 🏗️ Arquitectura del Modelo de Datos
El proyecto utiliza una arquitectura dimensional limpia cargada mediante scripts en Python para mantener la integridad relacional:

- **`fact_sales`**: Tabla de hechos con métricas de ventas (`Sales`) y volumen (`Quantity`).
- **`dim_product`**: Dimensión de productos conectada mediante `ProductKey`.
- **`dim_region`**: Dimensión geográfica/territorial conectada mediante `SalesTerritoryKey`.

![Modelo en Estrella](./dashboard/vista_modelo.jpeg) *(Reemplaza con la ruta de la captura de tu vista modelo)*

---

## 📈 Dashboard en Power BI
El informe final combina métricas de rendimiento y distribución de datos:
- **Distribución Regional:** Análisis visual de cuota de mercado por zona.
- **Rendimiento de Productos:** Análisis comparativo de ventas e ingresos por ítem.

![Power BI Dashboard](./dashboard/adventure.gif) *(Reemplaza con la ruta de la captura de tu reporte)*

---

## 🛠️ Tecnologías Utilizadas
- **Python / SQLite:** Ingesta y modelado dimensional.
- **Power BI Desktop:** Modelado relacional (DAX básicos) y visualización de datos.
- **Git / GitHub:** Control de versiones y documentación.