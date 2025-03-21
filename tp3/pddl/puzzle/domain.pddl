(define (domain puzzle)
  (:requirements :strips :typing)
  (:types position numero)
  
  (:predicates
    (at ?p - position ?n - numero)
    (empty ?p - position)
    (adjacent ?p1 ?p2 - position)
  )

  (:action move
    :parameters (?from ?to - position ?fromnum -numero)
    :precondition (and 
                    (at  ?from ?fromnum) 
                    (empty ?to) 
                    (adjacent ?from ?to))
    :effect (and (at ?to ?fromnum)
              (empty ?from) 
              (not (at ?from ?fromnum)) 
              (not (empty ?to)))
  )
)