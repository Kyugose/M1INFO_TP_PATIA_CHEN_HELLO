(define (domain puzzle)
  (:requirements :strips :typing)
  (:types ligne position numero)
  
  (:predicates
    (at ?d - ligne ?p - position ?n - numero)
    (empty ?p - position)
    (adjacent ?p1 ?p2 - position)
  )

  (:action move
    :parameters (?d - ligne ?from ?to - position ?fromnum -numero)
    :precondition (and 
                    (at ?d ?from ?fromnum) 
                    (empty ?to) 
                    (adjacent ?from ?to))
    :effect (and (at ?d ?to ?fromnum)
              (empty ?from) 
              (not (at ?d ?from ?fromnum)) 
              (not (empty ?to)))
  )
)