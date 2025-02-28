(define (problem n-puzzle-problem)
  (:domain n-puzzle)
  
  (:objects
    tile1 tile2 tile3 tile4 tile5 tile6 tile7 tile8 tile9 tile10 tile11 tile12 tile13 tile14 tile15 - tile
    pos1 pos2 pos3 pos4 pos5 pos6 pos7 pos8 pos9 pos10 pos11 pos12 pos13 pos14 pos15 pos16 - position
  )
  
  (:init
    (at tile1 pos1) (at tile2 pos2) (at tile3 pos3) (at tile4 pos4)
    (at tile5 pos5) (at tile6 pos6) (at tile7 pos7) (at tile8 pos8)
    (at tile9 pos9) (at tile10 pos10) (at tile11 pos11) (at tile12 pos12)
    (at tile13 pos13) (at tile14 pos14) (at tile15 pos15) (empty pos16)
    
    (adjacent pos1 pos2) (adjacent pos2 pos1) (adjacent pos2 pos3) (adjacent pos3 pos2)
    (adjacent pos3 pos4) (adjacent pos4 pos3) (adjacent pos1 pos5) (adjacent pos5 pos1)
    (adjacent pos2 pos6) (adjacent pos6 pos2) (adjacent pos3 pos7) (adjacent pos7 pos3)
    (adjacent pos4 pos8) (adjacent pos8 pos4) (adjacent pos5 pos6) (adjacent pos6 pos5)
    (adjacent pos6 pos7) (adjacent pos7 pos6) (adjacent pos7 pos8) (adjacent pos8 pos7)
    (adjacent pos5 pos9) (adjacent pos9 pos5) (adjacent pos6 pos10) (adjacent pos10 pos6)
    (adjacent pos7 pos11) (adjacent pos11 pos7) (adjacent pos8 pos12) (adjacent pos12 pos8)
    (adjacent pos9 pos10) (adjacent pos10 pos9) (adjacent pos10 pos11) (adjacent pos11 pos10)
    (adjacent pos11 pos12) (adjacent pos12 pos11) (adjacent pos9 pos13) (adjacent pos13 pos9)
    (adjacent pos10 pos14) (adjacent pos14 pos10) (adjacent pos11 pos15) (adjacent pos15 pos11)
    (adjacent pos12 pos16) (adjacent pos16 pos12) (adjacent pos13 pos14) (adjacent pos14 pos13)
    (adjacent pos14 pos15) (adjacent pos15 pos14) (adjacent pos15 pos16) (adjacent pos16 pos15)
  )
  
  (:goal
    (and
      (at tile1 pos1) (at tile2 pos2) (at tile3 pos3) (at tile4 pos4)
      (at tile5 pos5) (at tile6 pos6) (at tile7 pos7) (at tile8 pos8)
      (at tile9 pos9) (at tile10 pos10) (at tile11 pos11) (at tile12 pos12)
      (at tile13 pos13) (at tile14 pos14) (at tile15 pos15) (empty pos16)
    )
  )
)