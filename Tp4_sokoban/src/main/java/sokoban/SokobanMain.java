package sokoban;

import com.codingame.gameengine.runner.SoloGameRunner;

public class SokobanMain {
    public static void main(String[] args) {
        SoloGameRunner gameRunner = new SoloGameRunner();
        gameRunner.setAgent(Agent.class);
        //Entrer un non fichier test
        System.out.println("Enter the fichier testX.json:");
        Scanner in = new Scanner(System.in);
        String fichier = in.nextLine();
        gameRunner.setTestCase(fichier);

        
        
        gameRunner.start(4200);
    }
}
