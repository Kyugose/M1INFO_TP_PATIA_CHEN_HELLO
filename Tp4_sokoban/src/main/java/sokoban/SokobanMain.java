package sokoban;

import com.codingame.gameengine.runner.SoloGameRunner;
import java.util.Scanner;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class SokobanMain {
    public static void main(String[] args) {
        SoloGameRunner gameRunner = new SoloGameRunner();
        //Entrer un non fichier test
        System.out.println("Enter the fichier testX.json:");
        Scanner in = new Scanner(System.in);
        String fichier = in.nextLine();
        gameRunner.setTestCase(fichier);

        String timeout="600";

       try {
            // Exécution du script Python parserToPddl.py qui génère le fichier PDDL
            String fichieravecpath = "config/" + fichier;
            ProcessBuilder pb = new ProcessBuilder("python3", "parserToPddl.py", fichieravecpath);
            pb.inheritIO(); // Pour afficher les sorties du script Python dans la console
            Process process = pb.start();
            int exitCode = process.waitFor();
            if (exitCode != 0) {
                System.err.println("Erreur lors de l'exécution du script Python parserToPddl.py");
                return; 
            }

        } catch (Exception e) {
            e.printStackTrace();
            return;
        }
        
        try {
            String command = "python3 parserToSeqMov.py domain.pddl problemPDDL/" + fichier.replace(".json", ".pddl") + " " + timeout;
            ProcessBuilder pb = new ProcessBuilder(command.split(" "));
            pb.inheritIO(); // Pour afficher les sorties du script Python dans la console
            Process process = pb.start();
            int exitCode = process.waitFor();
            if (exitCode != 0) {
            System.err.println("Erreur lors de l'exécution du script Python parserToSeqMov.py");
            return;
            }
        } catch (Exception e) {
            e.printStackTrace();
            return;
        }

        gameRunner.setAgent("python3 afficheSeq.py SeqMov/" + fichier.replace(".json", ""));
        
        gameRunner.start(4200);
    }
}
