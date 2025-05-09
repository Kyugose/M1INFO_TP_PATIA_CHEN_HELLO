(define (problem Scoria---Level-3)
  (:domain sokoban)
  (:objects
    p0 p1 p2 p3 p4 p5 p6 p7 p8 p9 p10 p11 p12 p13 p14 p15 p16 p17 p18 p19 p20 p21 - position
  )
  (:init
    (clear p0)
    (clear p1)
    (player-at p2)
    (box-at p3)
    (box-at p4)
    (clear p5)
    (clear p6)
    (clear p7)
    (clear p8)
    (clear p9)
    (clear p10)
    (clear p11)
    (clear p12)
    (clear p13)
    (clear p14)
    (box-at p15)
    (clear p16)
    (clear p17)
    (clear p18)
    (clear p19)
    (clear p20)
    (clear p21)
    (adjacentdroit p1 p2)
    (adjacentbas p1 p3)
    (adjacentgauche p2 p1)
    (adjacentbas p2 p4)
    (adjacentdroit p3 p4)
    (adjacentbas p3 p6)
    (adjacenthaut p3 p1)
    (adjacentgauche p4 p3)
    (adjacentbas p4 p7)
    (adjacenthaut p4 p2)
    (adjacentdroit p5 p6)
    (adjacentbas p5 p10)
    (adjacentdroit p6 p7)
    (adjacentgauche p6 p5)
    (adjacenthaut p6 p3)
    (adjacentdroit p7 p8)
    (adjacentgauche p7 p6)
    (adjacentbas p7 p11)
    (adjacenthaut p7 p4)
    (adjacentdroit p8 p9)
    (adjacentgauche p8 p7)
    (adjacentbas p8 p12)
    (adjacentgauche p9 p8)
    (adjacentbas p9 p13)
    (adjacentbas p10 p14)
    (adjacenthaut p10 p5)
    (adjacentdroit p11 p12)
    (adjacentbas p11 p16)
    (adjacenthaut p11 p7)
    (adjacentdroit p12 p13)
    (adjacentgauche p12 p11)
    (adjacentbas p12 p17)
    (adjacenthaut p12 p8)
    (adjacentgauche p13 p12)
    (adjacenthaut p13 p9)
    (adjacentdroit p14 p15)
    (adjacenthaut p14 p10)
    (adjacentdroit p15 p16)
    (adjacentgauche p15 p14)
    (adjacentdroit p16 p17)
    (adjacentgauche p16 p15)
    (adjacentbas p16 p18)
    (adjacenthaut p16 p11)
    (adjacentgauche p17 p16)
    (adjacentbas p17 p19)
    (adjacenthaut p17 p12)
    (adjacentdroit p18 p19)
    (adjacenthaut p18 p16)
    (adjacentgauche p19 p18)
    (adjacenthaut p19 p17)
    (adjacentdroit p20 p21)
    (adjacentgauche p21 p20)
  )
  (:goal
    (and
      (box-at p4)
      (box-at p7)
      (box-at p11)
    )
  )
)