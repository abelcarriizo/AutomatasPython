# Parte A: Autómatas Finitos No Deterministas mediante Construcción de Thompson

Este parte se centra en la construcción de autómatas finitos no deterministas (AFN) utilizando la técnica de "Construcción de Thompson". Cada parte del ejercicio corresponde a la creación de un AFN para reconocer una expresión regular específica.

## a. AFN para la expresión regular a* | b a

1) a ; b
![AFN para a* | b a](img/ejercicios/parteA/a/1.ayb.png)

2) b a
![AFN para a* | b a](img/ejercicios/parteA/a/2.ba.png)

3) a *
![AFN para a* | b a](img/ejercicios/parteA/a/3.a".png)

4) a * | b a (conclusion)
![AFN para a* | b a](img/ejercicios/parteA/a/4.a"-ba.png)

En este ejercicio, se ha creado un AFN que reconoce la expresión regular a* | b a mediante la técnica de Construcción de Thompson.

## b. AFN para la expresión regular (x | y x ) *

1) x ; y
![AFN para (x | y x ) *](img/ejercicios/parteA/b/1.x;y.png)

2) yx
![AFN para (x | y x ) *](img/ejercicios/parteA/b/2.yx.png)

3) x | yx
![AFN para (x | y x ) *](img/ejercicios/parteA/b/3.x-yx.png)

4) (x | yx)* (conclusion)
![AFN para (x | y x ) *](img/ejercicios/parteA/b/4.x-yx".png)

En este ejercicio, se presenta un AFN que reconoce la expresión regular (x | y x ) * utilizando la Construcción de Thompson.

## c. AFN para la expresión regular a* b | a

1) a ; b
![AFN para a* b | a](img/ejercicios/parteA/c/1.a;b.png)

2) a*
![AFN para a* b | a](img/ejercicios/parteA/c/2.a".png)

3) a*b
![AFN para a* b | a](img/ejercicios/parteA/c/3.a"b.png)

4) a*b | a
![AFN para a* b | a](img/ejercicios/parteA/c/4.a"b-a.png)

En este ultimo ejercicio de la primera parte, se ha construido un AFN para reconocer la expresión regular a* b | a.

# Parte B: Autómatas Finitos Deterministas
En esta parte, se llevará a cabo la conversión de autómatas finitos no deterministas (AFN) realizados en el ejercicio anterior en autómatas finitos deterministas (AFD). Se utilizará la técnica de "Construcción de Subconjuntos" para lograr esta conversión.

## a. AFD para la expresión regular a* | b a
![AFN para a* | b a](img/ejercicios/parteB/a.png)

## b. AFD para la expresión regular (x | y x ) *
![AFN para (x | y x ) *](img/ejercicios/parteB/b.png)

## c. AFD para la expresión regular a* b | a
![AFN para a* b | a](img/ejercicios/parteB/c.png)

## Conclusiones

Este ejercicio proporciona una introducción práctica a la construcción de autómatas finitos no deterministas y deterministas para expresiones regulares específicas.

¡Esperamos que esta documentación sea de utilidad! Si tienes alguna pregunta o comentario, no dudes en comunicarte.

