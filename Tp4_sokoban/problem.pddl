(define (problem Scoria-3---Level-1)
  (:domain sokoban)
  (:objects
    p1 p2 p3 -position
  )
  (:init
  
    (player-at p1)
    (box-at p2)
    (adjacentdroit p1 p2)
    (adjacentdroit p2 p3)
    (clear p3)
  
  )
  (:goal
    (and
      (box-at p3)
    )
  )
)