(define (domain sokoban)
    (:requirements :strips :typing)
    (:types position)
    (:predicates 
        (player-at ?p - position)
        (box-at ?p - position)
        (adjacentdroit ?p1 ?p2 - position)
        (adjacenthaut ?p1 ?p2 - position)
        (adjacentbas ?p1 ?p2 - position)
        (adjacentgauche ?p1 ?p2 - position)
        (clear ?p - position)
    )
    
    (:action moveup
        :parameters (?p1 ?p2 - position)
        :precondition 
            (and
                (player-at ?p1) 
                (clear ?p2)
                (adjacenthaut ?p1 ?p2)
            )
        :effect 
            (and
                (not (player-at ?p1)) 
                (player-at ?p2)
                (not (clear ?p2))
                (clear ?p1)
            )
    )

    (:action movedown
        :parameters (?p1 ?p2 - position)
        :precondition 
            (and
                (player-at ?p1) 
                (clear ?p2)
                (adjacentbas ?p1 ?p2)
            )
        :effect 
            (and
                (not (player-at ?p1)) 
                (player-at ?p2)
                (not (clear ?p2))
                (clear ?p1)
            )
    )

    (:action moveleft
        :parameters (?p1 ?p2 - position)
        :precondition 
            (and
                (player-at ?p1) 
                (clear ?p2)
                (adjacentgauche ?p1 ?p2)
            )
        :effect 
            (and
                (not (player-at ?p1)) 
                (player-at ?p2)
                (clear ?p1)
                (not (clear ?p2))
            )
    )

    (:action moveright
        :parameters (?p1 ?p2 - position)
        :precondition 
            (and
                (player-at ?p1) 
                (clear ?p2)
                (adjacentdroit ?p1 ?p2)
            )
        :effect 
            (and
                (not (player-at ?p1)) 
                (player-at ?p2)
                (clear ?p1)
                (not (clear ?p2))
            )
    )

    (:action pushup
        :parameters (?p1 ?p2 ?p3 - position)
        :precondition 
            (and 
                (player-at ?p1) 
                (box-at ?p2) 
                (adjacenthaut ?p1 ?p2) 
                (adjacenthaut ?p2 ?p3) 
                (clear ?p3)
            )
        :effect 
            (and 
                (not (box-at ?p2)) 
                (box-at ?p3) 
                (not (player-at ?p1)) 
                (player-at ?p2)
                (clear ?p1)
                (not (clear ?p3))
            )
    )

    (:action pushdown
        :parameters (?p1 ?p2 ?p3 - position)
        :precondition 
            (and 
                (player-at ?p1) 
                (box-at ?p2) 
                (adjacentbas ?p1 ?p2) 
                (adjacentbas ?p2 ?p3) 
                (clear ?p3)
            )
        :effect 
            (and 
                (not (box-at ?p2)) 
                (box-at ?p3) 
                (not (player-at ?p1)) 
                (player-at ?p2)
                (clear ?p1)
                (not (clear ?p3))
            )
    )

    (:action pushleft
        :parameters (?p1 ?p2 ?p3 - position)
        :precondition 
            (and 
                (player-at ?p1) 
                (box-at ?p2) 
                (adjacentgauche ?p1 ?p2) 
                (adjacentgauche ?p2 ?p3) 
                (clear ?p3)
            )
        :effect 
            (and 
                (not (box-at ?p2)) 
                (box-at ?p3) 
                (not (player-at ?p1)) 
                (player-at ?p2)
                (clear ?p1)
                (not (clear ?p3))
            )
    )

    (:action pushright
        :parameters (?p1 ?p2 ?p3 - position)
        :precondition 
            (and 
                (player-at ?p1) 
                (box-at ?p2) 
                (adjacentdroit ?p1 ?p2) 
                (adjacentdroit ?p2 ?p3) 
                (clear ?p3)
            )
        :effect 
            (and 
                (not (box-at ?p2)) 
                (box-at ?p3) 
                (not (player-at ?p1)) 
                (player-at ?p2)
                (clear ?p1)
                (not (clear ?p3))
            )
    )

)