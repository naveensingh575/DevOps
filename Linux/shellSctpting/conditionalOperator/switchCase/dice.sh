#!/usr/bin/bash
echo "Input the type of dice"
read dice
case $dice in
       Tetrahedron )
                echo "$dice  is 4 face dice" ;;
        Cube )
                echo "$dice is 6 face dice" ;;
        Octahedron )
                echo "$dice is 8 face dice" ;;
        "Pentagonal trapezohedron" )
                echo "$dice is 10 face dice" ;;
        Dodecahedron )
                echo "$dice is 12 face dice" ;;
        Icosahedron )
                echo "$dice is 20 face dice" ;;

         *)
                echo "$dice is a invalid dice" ;;
esac


#learning
read variable -variable without $
"Pentagonal trapezohedron" - white space not allowed in pattern without "". it will give fatal giving fatal
Pentagonal trapezohedron ) - fatal

./rollADice.sh: line 11: syntax error near unexpected token `trapezohedron'
./rollADice.sh: line 11: `      Pentagonal trapezohedron )'
