curl --header "Content-Type: application/json" \
  --data '{"type":"digital","mode":"output", "pin": "13" }' \
  http://localhost:8080/api/pin; echo

curl --header "Content-Type: application/json" \
  --data '{"type":"analog", "pin": "a0" }' \
  http://localhost:8080/api/pin; echo

curl --header "Content-Type: application/json" \
  http://localhost:8080/api/pin; echo

curl --header "Content-Type: application/json" \
  http://localhost:8080/api/pin/dp1/value; echo

curl --header "Content-Type: application/json" \
  http://localhost:8080/api/pin/dp1/pin; echo

curl --header "Content-Type: application/json" \
  http://localhost:8080/api/pin/dp1/mode; echo

curl --header "Content-Type: application/json" \
  http://localhost:8080/api/pin/dp1/value/1; echo

curl --header "Content-Type: application/json" \
  http://localhost:8080/api/pin/dp1; echo

curl --header "Content-Type: application/json" \
  http://localhost:8080/api/pin/ap1/value; echo

curl --header "Content-Type: application/json" \
  http://localhost:8080/api/pin/dp1/value/0; echo

curl --header "Content-Type: application/json" \
  http://localhost:8080/api/pin/ap1/value/100; echo

curl --header "Content-Type: application/json" \
  http://localhost:8080/api/pin/dp1/value/100; echo

