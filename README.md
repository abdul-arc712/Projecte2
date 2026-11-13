# Pràctica 02: Introducció a la programació amb Python

- **Alumne/a:** Abdul Ahad Mohammad
- **Curs:** 2n SMX 
- **Mòdul:** Projecte Intermodular

## Resum del projecte

### Exercici2

**Training2(2.1):**
He utilitzat float() en lloc de int() perquè la mida del costat d'un quadrat pot tenir decimals. Per calcular l'àrea he posat costat * costat i he guardat el resultat a la variable area abans d'imprimir-lo fent la multiplicació dins del print. Al print he posat la f davant de les cometes per ficar la variable dins del text de manera més senzilla.

**Training2(2.2):**
He utilitzat int() perquè l'exercici demana treballar en nombres enters. He guardat la suma, la resta i la multiplicació en variables separades abans d'imprimir. Per a la divisió he posat un if num2 != 0 abans de calcular per a que si l'usuari posa un 0 com a segon número el programa no peti amb un error matemàtic i ensenyi un avís per pantalla. Als print he gastat la f davant de les comes per poder ensenyar l'operació i el resultat en una mateixa línia.

**Training2(2.3):**
Aquí he gastat input() directament sense int() ni float() perquè estem demanant paraules (text) i input() ja les guarda com a text per defecte. Per ajuntar-les he utilitzat un f-string (f"{paraula1} {paraula2} {paraula3}") en lloc d'anar sumant textos i espais amb el signe +, perquè així queda molt més curt i es veu clarament l'espai entre cada paraula. Al final he guardat el resultat dins la variable frase abans de mostrar-lo amb el print.

**Training2(2.4):**
He gastat float() a les entrades perquè l'usuari pugui introduir decimals sense que el programa doni error. Primer he guardat la suma exacta a la variable suma_decimal i després li he convertit a enter amb int() dins d'una altra variable (resultat_enter)així mostro el resultat original i el numero arrodonit. Als print he posat la f davant de les cometes per inserir les variables directament dins del text.

### Exercici3

**Training3(3.1):**
He utilitzat int() perquè l'edat és un número sencer i sense decimals. A la condició he posat >= 18 i no només perquè si algú té 18 anys justos també conte com a major d'edat. Com que només hi ha 2 opcions possibles, en un if i un else es prou i no cal posar elif.

**Training3(3.2):**
Aqui he posat float() en lloc de int() per a que es pugui escriure en números decimals. He utilitzat and per assegurar que un número sigui més gran que els altres dos alhora. He triat elif en lloc de posar tres if separats perque si troba el més gran a la primera deixi de comprovar la resta i al final he posat un else directe perque si no són ni el primer ni el segon per descart ha de ser el tercer. Al print he posat la f davant de les cometes per ficar la variable dins del text de manera més fàcil.

**Training3(3.3):**
He posat >= 0 per a que el zero conte dins dels positius i així poder fer l'exercici només amb un if i un else sense afegir un elif només per al zero. Si el número no és 0 o més gran pos sera negatiu així que l'else ja cobreix tots els altres casos.

### Exercici4

**Training4(4.1):**
He triat un bucle for amb range() en lloc d'un while perquè ja ho se on comença i on acaba la seqüència i així m'estalvio de crear comptador manualment. Dins del range he posat (1, 201) i no (1, 200) perquè python se para un número abans del límit final que poses i d'aquesta manera m'asseguro que el 200 també quedi inclòs. Per quedar només amb els parells he utilitzat l'operador mòdul (i % 2 == 0) que comprova si el residu de dividir el número entre 2 és 0 i només quan es compleix ho mostra per pantalla.

**Training4(4.2):**
He utilitzat un bucle while True amb un break en lloc d'un bucle for perquè no sé quantes notes voldrà introduir l'usuari aixi  el programa va demanant dades indefinidament fins que s'escriu el -1 per sortir. A l'entrada he posat float() en lloc d'int() perquè les notes d'un examen poden tenir decimals. Per recordar si ha sortit algun 10 durant el procés he creat la variable num = False abans de començar i la canvio a True només quan s'introdueix un 10, no poso cap else per tornar a posar en False perquè si la següent nota és un 6 no vull que s'oblidi del 10 que ja havia sortit abans. Al final quan s'acaba el bucle miro si num s'ha quedat en True per mostrar tenia algun 10 o no.

**Training4(4.3):**
He fet servir un bucle for i in range(10) en lloc d'un while perquè ja sé des del principi que s'han de demanar exactament 10 números. A l'entrada he posat float() perquè l'usuari pugui escriure números amb decimals. Dins del bucle miro si el número és més petit que zero (num < 0) i si ho és mostro el missatge i poso un break per tallar el bucle al moment perquè si ja he trobat un de negatiu no cal demanar la resta de números. Al final he posat else alineat amb el for i no en if per a que aquest else només s'execute si el bucle acaba les 10 voltes senceres sense haver entrat mai al break així no cal crear una variable extra per recordar si ha sortit algun negatiu o no.

### Exercici5

**Training5(Exercici 1. Calculadora de preus):**
He creat una funció amb def que rep dos paràmetres (preu_peces i ma_obra) per poder reutilitzar la fórmula amb qualsevol reparació sense haver de repetir la suma cada vegada. Dins de la funció faig servir return preu en lloc d'un print perquè així el resultat es pot guardar en una variable i es pot aprofitar més endavant en altres càlculs.