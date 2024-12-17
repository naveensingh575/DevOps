!#/usr/bin/bash
#Switch cases
echo Please input the day of week
read day
case  $day in
 Monday)
   echo "Today, I am in morning shift" ;;
 Tuesday)
   echo "Today, I am in morning shift" ;;
 Wednesday)
  echo "Today, I am in Normal shift" ;;
 Thursday)
  echo "Today, I am in Normal shift" ;;
 Friday)
  echo "Today, I am on weekly off" ;;
 Saturday)
  echo "Today, I am on weekly off" ;;
 Sunday)
  echo "Today,  I am in morning shift" ;;
 *)
  echo "Invalid input"
esac
