(define (domain sokoban)
(:requirements :strips :typing)
(:types player box wall position)
(:predicates 
        (player-at ?px ?py)
        (box-at ?bx ?by)
        (wall-at ?wx ?wy)
        (adjacent ?px ?py ?px2 ?py2)
    )
    
    (:action move-right
        :parameters (?px ?py ?px2 ?py2)
        :precondition (and (player-at ?px ?py) 
                        (adjacent ?px ?py ?px2 ?py2) 
                        (not (wall-at ?px2 ?py2)) 
                        (not (box-at ?px2 ?py2)))
        :effect (and 
            (not (player-at ?px ?py)) 
            (player-at ?px2 ?py2)
        )
    )


    (:action push-up
        :parameters (?px ?py ?bx ?by ?bx2 ?by2)
        :precondition (and (player-at ?px ?py) (box-at ?bx ?by) (adjacent ?px ?py ?bx ?by) (adjacent ?bx ?by ?bx2 ?by2) (not (wall-at ?bx2 ?by2)) (not (box-at ?bx2 ?by2)))
        :effect (and (not (box-at ?bx ?by)) (box-at ?bx2 ?by2) (not (player-at ?px ?py)) (player-at ?bx ?by))
    )
    
    (:action push-down
        :parameters (?px ?py ?bx ?by ?bx2 ?by2)
        :precondition (and (player-at ?px ?py) (box-at ?bx ?by) (adjacent ?px ?py ?bx ?by) (adjacent ?bx ?by ?bx2 ?by2) (not (wall-at ?bx2 ?by2)) (not (box-at ?bx2 ?by2)))
        :effect (and (not (box-at ?bx ?by)) (box-at ?bx2 ?by2) (not (player-at ?px ?py)) (player-at ?bx ?by))
    )
    
    (:action push-left
        :parameters (?px ?py ?bx ?by ?bx2 ?by2)
        :precondition (and (player-at ?px ?py) (box-at ?bx ?by) (adjacent ?px ?py ?bx ?by) (adjacent ?bx ?by ?bx2 ?by2) (not (wall-at ?bx2 ?by2)) (not (box-at ?bx2 ?by2)))
        :effect (and (not (box-at ?bx ?by)) (box-at ?bx2 ?by2) (not (player-at ?px ?py)) (player-at ?bx ?by))
    )
    
    (:action push-right
        :parameters (?px ?py ?bx ?by ?bx2 ?by2)
        :precondition (and (player-at ?px ?py) (box-at ?bx ?by) (adjacent ?px ?py ?bx ?by) (adjacent ?bx ?by ?bx2 ?by2) (not (wall-at ?bx2 ?by2)) (not (box-at ?bx2 ?by2)))
        :effect (and (not (box-at ?bx ?by)) (box-at ?bx2 ?by2) (not (player-at ?px ?py)) (player-at ?bx ?by))
    )
)