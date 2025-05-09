(define (problem Scoria-2---Level-9)
  (:domain sokoban)
  (:objects
    p0 p1 p2 p3 p4 p5 p6 p7 p8 p9 p10 p11 p12 p13 p14 p15 p16 p17 p18 p19 p20 p21 p22 p23 p24 p25 p26 p27 p28 p29 - position
  )
  (:init
    (clear p0)
    (clear p1)
    (clear p2)
    (clear p3)
    (clear p4)
    (clear p5)
    (clear p6)
    (clear p7)
    (clear p8)
    (clear p9)
    (box-at p10)
    (clear p11)
    (clear p12)
    (clear p13)
    (clear p14)
    (clear p15)
    (box-at p16)
    (clear p17)
    (box-at p18)
    (player-at p19)
    (clear p20)
    (clear p21)
    (box-at p22)
    (clear p23)
    (clear p24)
    (clear p25)
    (clear p26)
    (clear p27)
    (clear p28)
    (clear p29)
    (adjacentdroit p0 p1)
    (adjacentbas p0 p7)
    (adjacentdroit p1 p2)
    (adjacentgauche p1 p0)
    (adjacentdroit p2 p3)
    (adjacentgauche p2 p1)
    (adjacentbas p2 p8)
    (adjacentgauche p3 p2)
    (adjacentbas p3 p9)
    (adjacentdroit p4 p5)
    (adjacentbas p4 p11)
    (adjacentdroit p5 p6)
    (adjacentgauche p5 p4)
    (adjacentbas p5 p12)
    (adjacentgauche p6 p5)
    (adjacentbas p6 p13)
    (adjacentbas p7 p14)
    (adjacenthaut p7 p0)
    (adjacentdroit p8 p9)
    (adjacentbas p8 p16)
    (adjacenthaut p8 p2)
    (adjacentdroit p9 p10)
    (adjacentgauche p9 p8)
    (adjacentbas p9 p17)
    (adjacenthaut p9 p3)
    (adjacentdroit p10 p11)
    (adjacentgauche p10 p9)
    (adjacentbas p10 p18)
    (adjacentdroit p11 p12)
    (adjacentgauche p11 p10)
    (adjacentbas p11 p19)
    (adjacenthaut p11 p4)
    (adjacentdroit p12 p13)
    (adjacentgauche p12 p11)
    (adjacentbas p12 p20)
    (adjacenthaut p12 p5)
    (adjacentgauche p13 p12)
    (adjacentbas p13 p21)
    (adjacenthaut p13 p6)
    (adjacentdroit p14 p15)
    (adjacenthaut p14 p7)
    (adjacentdroit p15 p16)
    (adjacentgauche p15 p14)
    (adjacentdroit p16 p17)
    (adjacentgauche p16 p15)
    (adjacentbas p16 p22)
    (adjacenthaut p16 p8)
    (adjacentdroit p17 p18)
    (adjacentgauche p17 p16)
    (adjacentbas p17 p23)
    (adjacenthaut p17 p9)
    (adjacentdroit p18 p19)
    (adjacentgauche p18 p17)
    (adjacenthaut p18 p10)
    (adjacentdroit p19 p20)
    (adjacentgauche p19 p18)
    (adjacenthaut p19 p11)
    (adjacentdroit p20 p21)
    (adjacentgauche p20 p19)
    (adjacenthaut p20 p12)
    (adjacentgauche p21 p20)
    (adjacenthaut p21 p13)
    (adjacentdroit p22 p23)
    (adjacentbas p22 p26)
    (adjacenthaut p22 p16)
    (adjacentgauche p23 p22)
    (adjacentbas p23 p27)
    (adjacenthaut p23 p17)
    (adjacentdroit p24 p25)
    (adjacentbas p24 p28)
    (adjacentgauche p25 p24)
    (adjacentbas p25 p29)
    (adjacentdroit p26 p27)
    (adjacenthaut p26 p22)
    (adjacentgauche p27 p26)
    (adjacenthaut p27 p23)
    (adjacentdroit p28 p29)
    (adjacenthaut p28 p24)
    (adjacentgauche p29 p28)
    (adjacenthaut p29 p25)
  )
  (:goal
    (and
      (box-at p9)
      (box-at p10)
      (box-at p17)
      (box-at p18)
    )
  )
)