(define (problem sokoban-problem)
    (:domain sokoban)
    
    (:objects
        p1 p2 p3 p4 p5 p6 p7 p8 p9 p10 - position
        player1 - player
        box1 box2 - box
        wall1 wall2 wall3 wall4 - wall
    )
    
    (:init
        (player-at p1 p1)
        (box-at p2 p2)
        (box-at p3 p3)
        (wall-at p4 p4)
        (wall-at p5 p5)
        (adjacent p1 p1 p2 p2)
        (adjacent p2 p2 p3 p3)
        (adjacent p3 p3 p4 p4)
        (adjacent p4 p4 p5 p5)
        (adjacent p5 p5 p6 p6)
        (adjacent p6 p6 p7 p7)
        (adjacent p7 p7 p8 p8)
        (adjacent p8 p8 p9 p9)
        (adjacent p9 p9 p10 p10)
    )
    
    (:goal
        (and
            (box-at p6 p6)
            (box-at p7 p7)
        )
    )
)