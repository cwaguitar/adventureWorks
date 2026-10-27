Resumen: Conceptos Clave de Modelado de Datos (Modelo en Estrella)
Para estructurar una base de datos analítica de forma profesional, eficiente y rápida, dividimos la información en dos grandes tipos de tablas interconectadas:

1. Tablas de Dimensión (dim_) — El Contexto
¿Qué son? Tablas que almacenan los detalles descriptivos de los elementos de un negocio.

Preguntas que responden: ¿Quién?, ¿Qué?, ¿Dónde?, ¿Cuándo?

Qué contienen: Nombres, descripciones, categorías, colores, ubicaciones o fechas. Son datos estables que cambian muy poco.

Ejemplo: dim_product (contiene los atributos del producto, como su nombre, categoría y color).

2. Tablas de Hechos (fact_) — Los Números y Acciones
¿Qué son? Tablas centrales donde ocurren las transacciones o eventos medibles.

Preguntas que responden: ¿Cuánto se vendió?, ¿Cuántas unidades?, ¿Cuál fue el costo?

Qué contienen: Métricas numéricas (cantidades, montos de venta, descuentos) junto con los identificadores (claves) que apuntan a las tablas de dimensiones para darles contexto.

Ejemplo: fact_sales (registra cada venta realizada, vinculándola con el producto y la región correspondientes).

Ventaja principal: Al separar el contexto (dimensiones) de las transacciones (hechos), evitamos duplicar texto innecesariamente en la base de datos, optimizamos el espacio en disco y logramos que las consultas y reportes (en herramientas como Power BI o Tableau) vuelen.