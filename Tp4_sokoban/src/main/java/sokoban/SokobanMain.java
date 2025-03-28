package sokoban;

import com.codingame.gameengine.runner.SoloGameRunner;
import java.util.Scanner;
import java.io.IOException;

public class SokobanMain {
    public static void main(String[] args) {
        SoloGameRunner gameRunner = new SoloGameRunner();
        gameRunner.setAgent(Agent.class);
        //Entrer un non fichier test
        System.out.println("Enter the fichier testX.json:");
        Scanner in = new Scanner(System.in);
        String fichier = in.nextLine();
        gameRunner.setTestCase(fichier);

        int timeout=2;

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

            // Exécution du script Python parserToSeqMov.py qui transforme le fichier PDDL en séquence de mouvements
            String fichierPddl = "problemPDDL/" + fichier.replace(".json", ".pddl");
            System.out.println("Fichier PDDL généré : " + fichierPddl);
            ProcessBuilder pb2 = new ProcessBuilder("python3", "parserToSeqMov.py", "domain.pddl", fichierPddl, String.valueOf(timeout));
            pb2.redirectErrorStream(true); // Rediriger les erreurs vers la sortie standard
            Process process2 = pb2.start();
            
            // Lire la sortie du script Python
            Scanner outputScanner = new Scanner(process2.getInputStream());
            StringBuilder output = new StringBuilder();
            while (outputScanner.hasNextLine()) {
                output.append(outputScanner.nextLine()).append(System.lineSeparator());
            }
            outputScanner.close();
            
            int exitCode2 = process2.waitFor();
            if (exitCode2 != 0) {
                System.err.println("Erreur lors de l'exécution du script Python parserToSeqMov.py");
                return;
            }
            
            // Afficher la sortie du script Python
            System.out.println("Output du script parserToSeqMov.py:");
            System.out.println(output.toString());


        } catch (Exception e) {
            e.printStackTrace();
            return;
        }
        
        gameRunner.start(4200);
    }
}
