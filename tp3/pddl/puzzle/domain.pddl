(define (domain puzzle)
  (:requirements :strips :typing)
  (:types ligne position numero)
  
  (:predicates
    (at ?d - ligne ?p - position)
    (empty ?p - position -n -numero)
    (adjacent ?p1 ?p2 - position)
  )

  (:action move
    :parameters (?d - ligne ?from ?to - position)
    :precondition (and (at ?d ?from) (empty ?to) (adjacent ?from ?to))
    :effect (and (at ?d ?to) (empty ?from) (not (at ?d ?from)) (not (empty ?to)))
  )
)