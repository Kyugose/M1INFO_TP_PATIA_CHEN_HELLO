(define (problem tower-of-hanoi)
  (:domain disk)
  (:objects
    disk1 disk2 disk3 disk4 - disk)
  (:init
    (ontable disk1)
    (ontable disk2)
    (ontable disk3)
    (ontable disk4)
    (clear disk1)
    (clear disk2)
    (clear disk3)
    (clear disk4)
    (handempty)
    (greater disk4 disk3)
    (greater disk3 disk2)
    (greater disk2 disk1))
  (:goal
    (and
      (correctly-placed disk1)
      (correctly-placed disk2)
      (correctly-placed disk3)
      (clear disk1)
      (handempty))))