package fr.uga.pddl4j.yasp;

import fr.uga.pddl4j.plan.Plan;
import fr.uga.pddl4j.plan.SequentialPlan;
import fr.uga.pddl4j.problem.Fluent;
import fr.uga.pddl4j.problem.Problem;
import fr.uga.pddl4j.problem.operator.Action;
import fr.uga.pddl4j.util.BitVector;

import java.util.List;
import java.util.ArrayList;
import java.util.HashMap;


/**
 * This class implements a planning problem/domain encoding into DIMACS
 *
 * @author H. Fiorino
 * @version 0.1 - 30.03.2024
 */
public final class SATEncoding {
    /*
     * A SAT problem in dimacs format is a list of int list a.k.a clauses
     */
    private List<List<Integer>> initList = new ArrayList<List<Integer>>();

    /*
     * Goal
     */
    private List<Integer> goalList = new ArrayList<Integer>();

    /*
     * Actions
     */
    private List<List<Integer>> actionPreconditionList = new ArrayList<List<Integer>>();
    private List<List<Integer>> actionEffectList = new ArrayList<List<Integer>>();

    /*
     * State transistions
     */
    private HashMap<Integer, List<Integer>> addList = new HashMap<Integer, List<Integer>>();
    private HashMap<Integer, List<Integer>> delList = new HashMap<Integer, List<Integer>>();
    private List<List<Integer>> stateTransitionList = new ArrayList<List<Integer>>();

    /*
     * Action disjunctions
     */
    private List<List<Integer>> actionDisjunctionList = new ArrayList<List<Integer>>();

    /*
     * Current DIMACS encoding of the planning domain and problem for #steps steps
     * Contains the initial state, actions and action disjunction
     * Goal is no there!
     */
    public List<List<Integer>> currentDimacs = new ArrayList<List<Integer>>();

    /*
     * Current goal encoding
     */
    public List<Integer> currentGoal = new ArrayList<Integer>();

    /*
     * Current number of steps of the SAT encoding
     */
    private int steps;

    public SATEncoding(Problem problem, int steps) {

        this.steps = steps;

        // Encoding of init
        // Each fact is a unit clause
        // We get the initial state from the planning problem
        // State is a bit vector where the ith bit at 1 corresponds to the ith fluent being true
        final int nb_fluents = problem.getFluents().size();
        //System.out.println(" fluents = " + nb_fluents );
        final BitVector init = problem.getInitialState().getPositiveFluents();
        
        // TO BE DONE!

        //les clauses de l'init
        for (int i = 0; i < nb_fluents; i++) {
            //possible fluent
            if (init.get(i)) {
                List<Integer> clause = new ArrayList<Integer>();
                clause.add(pair(i + 1, 1));
                this.initList.add(clause);
            }
            else{
                //négatif fluent
                List<Integer> clause = new ArrayList<Integer>();
                clause.add(-pair(i + 1, 1));
                this.initList.add(clause);
            }
        }

        //goal on reucpère le bitvector de l'objectif
        final BitVector goal = problem.getGoal().getPositiveFluents();

        for(int i = 0; i < nb_fluents; i++){
            if (goal.get(i)) {
                this.goalList.add(pair(i + 1, steps));
            }
            else{
                this.goalList.add(-pair(i + 1, steps));
            }
        }
        

        // Actions : préconditions and effects
        for (int i = 0; i < problem.getActions().size(); i++) {
            Action action = problem.getActions().get(i);
            List<Integer> clause = new ArrayList<Integer>();
            List<Integer> effect = new ArrayList<Integer>();
            //System.out.println("action = " + action.toString());
            System.out.println("action precondition = " + action.getPrecondition().toString());
            System.out.println("action effect = " + action.getPrecondition().getPositiveFluents());
            if(action.getPrecondition().getPositiveFluents() != null){
                for (int j = 0; j < action.getPrecondition().getPositiveFluents().size(); j++) {
                    //System.out.println("fluent = " + action.getPrecondition().getPositiveFluents().get(j));
                    if (action.getPrecondition().getPositiveFluents().get(j)) {
                        clause.add(pair(j + 1, 1));
                    } else {
                        clause.add(-pair(j + 1, 1));
                    }
                }
            }

            this.actionPreconditionList.add(clause);
            this.actionEffectList.add(effect);
        }

        // State transitions

        for(int i=0; i< problem.getActions().size(); i++){
            Action action = problem.getActions().get(i);
            List<Integer> clause = new ArrayList<Integer>();
            List<Integer> add = new ArrayList<Integer>();
            List<Integer> del = new ArrayList<Integer>();

            this.addList.put(i, add);
            this.delList.put(i, del);
        }

        //actions disjunctions
        for (int i=0 ; i< problem.getActions().size(); i++){
            Action action = problem.getActions().get(i);
            List<Integer> clause = new ArrayList<Integer>();
            for (int j = 0; j < action.getConditionalEffects().size(); j++) {
    
            }
            this.actionDisjunctionList.add(clause);
        }



        //affchier les clauses

        System.out.println("init clauses = " + this.initList);
        System.out.println("goal clauses = " + this.goalList);
        System.out.println("action precondition clauses = " + this.actionPreconditionList);
        System.out.println("action effect clauses = " + this.actionEffectList);
        System.out.println("state transition clauses = " + this.stateTransitionList);
        System.out.println("action disjunction clauses = " + this.actionDisjunctionList);


        // Makes DIMACS encoding from 1 to steps
        encode(1, steps);
    }
    
    /*
     * SAT encoding for next step
     */
    public void next() {
        this.steps++;
        encode(this.steps, this.steps);
    }

    public String toString(final List<Integer> clause, final Problem problem) {
        final int nb_fluents = problem.getFluents().size();
        List<Integer> dejavu = new ArrayList<Integer>();
        String t = "[";
        String u = "";
        int tmp = 1;
        int [] couple;
        int bitnum;
        int step;
        for (Integer x : clause) {
            if (x > 0) {
                couple = unpair(x);
                bitnum = couple[0];
                step = couple[1];
            } else {
                couple = unpair(- x);
                bitnum = - couple[0];
                step = couple[1];
            }
            t = t + "(" + bitnum + ", " + step + ")";
            t = (tmp == clause.size()) ? t + "]\n" : t + " + ";
            tmp++;
            final int b = Math.abs(bitnum);
            if (!dejavu.contains(b)) {
                dejavu.add(b);
                u = u + b + " >> ";
                if (nb_fluents >= b) {
                    Fluent fluent = problem.getFluents().get(b - 1);
                    u = u + problem.toString(fluent)  + "\n";
                } else {
                    u = u + problem.toShortString(problem.getActions().get(b - nb_fluents - 1)) + "\n";
                }
            }
        }
        return t + u;
    }

    public Plan extractPlan(final List<Integer> solution, final Problem problem) {
        Plan plan = new SequentialPlan();
        HashMap<Integer, Action> sequence = new HashMap<Integer, Action>();
        final int nb_fluents = problem.getFluents().size();
        int[] couple;
        int bitnum;
        int step;
        for (Integer x : solution) {
            if (x > 0) {
                couple = unpair(x);
                bitnum = couple[0];
            } else {
                couple = unpair(-x);
                bitnum = -couple[0];
            }
            step = couple[1];
            // This is a positive (asserted) action
            if (bitnum > nb_fluents) {
                final Action action = problem.getActions().get(bitnum - nb_fluents - 1);
                sequence.put(step, action);
            }
        }
        for (int s = sequence.keySet().size(); s > 0 ; s--) {
            plan.add(0, sequence.get(s));
        }
        return plan;
    }
    
    // Cantor paring function generates unique numbers
    private static int pair(int num, int step) {
        return (int) (0.5 * (num + step) * (num + step + 1) + step);
    }

    private static int[] unpair(int z) {
        /*
        Cantor unpair function is the reverse of the pairing function. It takes a single input
        and returns the two corespoding values.
        */
        int t = (int) (Math.floor((Math.sqrt(8 * z + 1) - 1) / 2));
        int bitnum = t * (t + 3) / 2 - z;
        int step = z - t * (t + 1) / 2;
        return new int[]{bitnum, step}; //Returning an array containing the two numbers
    }

    private void encode(int from, int to) {
        this.currentDimacs.clear();
        
        // TO BE DONE!
        // Encoding of init

        for (List<Integer> clause : this.initList) {
            List<Integer> newClause = new ArrayList<Integer>();
            for (Integer x : clause) {
                newClause.add(x);
            }
            this.currentDimacs.add(newClause);
        }

        // Encoding of actions

        for (int i = 0; i < this.actionPreconditionList.size(); i++) {
            List<Integer> clause = new ArrayList<Integer>();
            for (Integer x : this.actionPreconditionList.get(i)) {
                clause.add(pair(x, from));
            }
            for (Integer x : this.actionEffectList.get(i)) {
                clause.add(pair(x, from + 1));
            }
            this.currentDimacs.add(clause);
        }

        // Encoding of action disjunctions
 
        for (List<Integer> clause : this.actionDisjunctionList) {
            List<Integer> newClause = new ArrayList<Integer>();
            for (Integer x : clause) {
                newClause.add(pair(x, from + 1));
            }
            this.currentDimacs.add(newClause);
        }

        // Encoding of state transitions
  
        for (int i = 0; i < this.stateTransitionList.size(); i++) {
            List<Integer> clause = new ArrayList<Integer>();
            for (Integer x : this.addList.get(i)) {
                clause.add(pair(x, from + 1));
            }
            for (Integer x : this.delList.get(i)) {
                clause.add(-pair(x, from + 1));
            }
            this.currentDimacs.add(clause);
        }

        // Encoding of goal

        for (Integer x : this.goalList) {
            this.currentGoal.add(pair(x, to));
        }



        System.out.println("Encoding : successfully done (" + (this.currentDimacs.size()
                + this.currentGoal.size()) + " clauses, " + to + " steps)");
    }

}
