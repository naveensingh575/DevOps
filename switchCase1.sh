case is used when we have the limited known choices and it is a coindtional operator like if else.
#syntax
case expression in
  pattern1)
    statement;;
  patern2)
    statement;;
  pattern3)
    statement;;
  .
  .
  .
  *)
    statement;;

for e.g

#!/usr/bin/bash
echo "Input the type of dice"
read dice
case $dice in
        "Tetrahedron" )
                echo "$dice  is 4 face dice" ;;
        "Cube" )
                echo "$dice is 6 face dice" ;;
        "Octahedron" )
                echo "$dice is 8 face dice" ;;
        "Pentagonal trapezohedron" )
                echo "$dice is 10 face dice" ;;
        "Dodecahedron" )
                echo "$dice is 12 face dice" ;;
        "Icosahedron" )
                echo "$dice is 20 face dice" ;;

        *)
                echo "$dice is a invalid dice" ;;
esac    

#learning
read variable -variable without $
"Tetrahedron" - string in "" withot "" giving fatal
