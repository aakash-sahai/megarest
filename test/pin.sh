curl --header "Content-Type: application/json" \
  --data '{"type":"digital","xmode":"output", "pin": "13" }' \
  http://localhost:8080/api/pin; echo

curl --header "Content-Type: application/json" \
  --data '{"type":"analog", "pin": "a0" }' \
  http://localhost:8080/api/pin; echo

curl --header "Content-Type: application/json" \
  http://localhost:8080/api/pin; echo

curl --header "Content-Type: application/json" \
  http://localhost:8080/api/pin/dp1; echo

curl --header "Content-Type: application/json" \
  http://localhost:8080/api/pin/ap1; echo

curl --header "Content-Type: application/json" \
  --request PUT \
  --data '{"value":"0" }' \
  http://localhost:8080/api/pin/dp1; echo

curl --header "Content-Type: application/json" \
  --request PUT \
  --data '{"value":"100" }' \
  http://localhost:8080/api/pin/ap1; echo

curl --header "Content-Type: application/json" \
  --request PUT \
  --data '{"value":"10" }' \
  http://localhost:8080/api/pin/dp1; echo

