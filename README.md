# R7Converter

## Passerelles entre logiciels de présentation

Il s’agit de créer une ou des applications consommant une application d’un type A et donnant en sortie un type B.
La conversion doit se faire entre 3 frameworks de présentation :
* EAST;
* Reveal.js;
* Markdown. 
La sortie d’une conversion doit être la plus inclusive possible. 

Comme minimum on peut prendre Markdown: cette spécification se concentre uniquement sur les aspects présentation d’un document, laissant de côté toute intéraction.
La transformation Markdown -> Reveal.js -> EAST->Markdown doit donner le même fichier à la sortie. Ce comportement doit ressembler à une conversion en PDF. 
La transformation Reveal -> EAST ou EAST -> Reveal doit garder le maximum du contenu intéractif. 

### Markdown
Type : Un langage de balisage. 
Date : 2004
But : Formatage facilité d’un texte. 
La variante utilisée sera Github Flavored Markdown.

### Reveal.js
Type : Application javascript. 
Date : 2007
But : Création de slideshow dynamique avec du HTML.
Support des autres logiciels : Markdown.

### EAST
Type : Application XML 
Date : N/R
But : Création de slideshow dynamique en XML.
Support des autres logiciels : None. 
L’intégration avec markdown est possible si on inclue le pré-processeur de Markdown après la compilation en HTML. 


