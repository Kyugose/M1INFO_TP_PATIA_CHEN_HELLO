(define (domain disk)
  (:requirements :strips :typing)
  (:types disk)
  (:predicates (on ?x - disk ?y - disk)
               (ontable ?x - disk)
               (clear ?x - disk)
               (handempty)
               (holding ?x - disk)
               (greater ?x - disk ?y - disk)
               (correctly-placed ?x - disk))

  (:action pick-up
           :parameters (?x - disk)
           :precondition (and (clear ?x) (ontable ?x) (handempty))
           :effect
           (and (not (ontable ?x))
                (not (clear ?x))
                (not (handempty))
                (holding ?x)))

  (:action put-down
           :parameters (?x - disk)
           :precondition (holding ?x)
           :effect
           (and (not (holding ?x))
                (clear ?x)
                (handempty)
                (ontable ?x)
                ))

  (:action stack
           :parameters (?x - disk ?y - disk)
           :precondition (and (holding ?x) (clear ?y) (greater ?y ?x))
           :effect
           (and (not (holding ?x))
                (not (clear ?y))
                (clear ?x)
                (handempty)
                (on ?x ?y)
                (correctly-placed ?x)))
)