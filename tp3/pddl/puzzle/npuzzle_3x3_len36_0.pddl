(define (problem puzzle)
(:domain puzzle)
(:objects
p1 - position
p2 - position
p3 - position
p4 - position
p5 - position
p6 - position
p7 - position
p8 - position
p9 - position
n1 - numero
n2 - numero
n3 - numero
n4 - numero
n5 - numero
n6 - numero
n7 - numero
n8 - numero
)
(:init
(at p1 n3)
(at p2 n1)
(empty p3)
(at p4 n6)
(at p5 n5)
(at p6 n8)
(at p7 n7)
(at p8 n2)
(at p9 n4)
(adjacent p1 p2)
(adjacent p1 p4)
(adjacent p2 p3)
(adjacent p2 p5)
(adjacent p3 p6)
(adjacent p4 p5)
(adjacent p4 p7)
(adjacent p5 p6)
(adjacent p5 p8)
(adjacent p6 p9)
(adjacent p7 p8)
(adjacent p8 p9)
)
(:goal (and
(at p3 n2)
)))
