
## Configuration MVN

```bash
mvn clean 
```

```bash
mvn install:install-file \
   -Dfile=pddl4j-4.0.0.jar \
   -DgroupId=fr.uga \
   -DartifactId=pddl4j \
   -Dversion=4.0.0 \
   -Dpackaging=jar \
   -DgeneratePom=true
 ```  

```bash
mvn compile
```


## Lancer un test

# lancer avec la comande suivant pour tester il demandera un fichier testX.json qui représente le niveau que l'on veut présent dans le répertoire config

```bash
java --add-opens java.base/java.lang=ALL-UNNAMED \
      -server -Xms2048m -Xmx2048m \
      -cp "$(mvn dependency:build-classpath -Dmdep.outputFile=/dev/stdout -q):target/test-classes/:target/classes" \
      sokoban.SokobanMain
```

## Explication de comment on a fait pour le sokoban

# Parser parserToPddl.py

Nous avons utilisé un premier parser qui parse un probleme sokoban décrit par le fichier json en pddl.

# Parser parserToSeqMov.py

Nous avons utilisé un second parser qui nous a permis de parser le résultat de l'éxecution de pddl4j sur le un problème sokoban pddl et de le transformer en une séquence de mouvement.
Il lance le pddl4j sur le fichier pddl et parse le résultat en seqmov (R,U,D,L).

# SokobanMain.java

Et nous avons aussi afficheSeq.py qui permet d'afficher correctement la séquence de mouvement pour l'utiliser avec le setagent du sokoban .

gameRunner.setAgent("python3 afficheSeq.py SeqMov/" + fichier.replace(".json", ""));

Ainsi avec les 2 parser dans SokobanMain.java on demande un fichier json puis on le lance parserToPddl sur ce fichier et on enregistre le fichier pddl dans le répertoire problemPDDL. 
Puis on le deuxieme parser sur le fichier pddl qui va lancer le pddl4j dessus et parser le résultat en séquence de mouvement dans le répertoire SeqMov.

Et enfin on donne à l'agent gameRunner en éxecutant afficheSeq.py sur le fichier SeqMov qui contient la séquence de mouvement.
