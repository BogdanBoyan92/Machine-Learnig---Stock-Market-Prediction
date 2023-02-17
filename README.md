# Machine-Learnig---Stock-Market-Prediction

1. La intención del proyecto es dar un poco de luz sobre un tema como el de los mercados financieros. Este tema se puede ver desde distintos puntos de vista:
    * Por un lado están los que dicen que el mercado se mueve por emociones de los inversores.
    * Por otro lado están los que lo miran desde un punto de vista cuantitativo. Es en éste en el que nos vamos a centrar.

    * Otro objetivo es también hacer ver al pequeño inversor que es posible ser rentable en los mercados , no hay nada que haga milagros,
	 pero con la ayuda de los avances tecnológicos todo se ve un poco mas fácil.

2. El origen de los datos es directamente de yahoo finance. Fuente fiable y con largo historial de datos sobre muchisimas empresas. 
	Se han cogido datos desde el 1 de enero del 2012 hasta el 30 de diciembre de 2021. 
	El archivo viene con una estructura muy limpia. Los datos sobre la cotizacion son los siguientes : 
	Apertura(Open), Cierre(Close), Máximo(high), Mínimo(Low), Cierre ajustado(Adj. Close) y Volumen. 

3. En cuanto al procesamiento lo que vamos a hacer es lo siguiente: Al ser una serie temporal vamos a tener en cuenta solo Fecha y valor del Cierre del mercado.
	 Para un modelo inicial es suficiente. Se pueden agregar otros valores como el famoso RSI . 
	Tambien podemos tener en cuenta las Bandas de Bollinger, Media móvil exponencial o simple, parabolic SAR entre muchos otros.

4. El model elegido para realizar esta tarea es el LSTM (Long Short-Term Memory ) ya que está específicamente diseñado para tratar datos secuenciales,
	 en nuestro caso ( Time Series).

5. Dicho modelo mencionado anteriormente arroja unos resultados bastante buenos en la parte del test. 

6. El proyecto está enfocado desde un inicio con el modelo más recomendado para este tipo de análisis. 
	Es probable que si sacamos el modelo de su zona de confort(cotización de empresas), y probamos con datos de Forex (Intercambio de modena),
	Criptomonedas o Mercado de Futuros no rinda tan bien. Para su mejora optaría por seguir usando redes neuronales. 
	Aunque queda pendiente por probar modelo Arima o arboles de decisión. 
	Siempre y cuando el modelo cuente con muchas variables ya que creo que son la clave para conseguir un buen resultado.
