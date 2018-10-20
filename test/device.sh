curl --header "Content-Type: application/json" \
  http://localhost:8080/api/device; echo

curl --header "Content-Type: application/json" \
  --data '{"device": "/dev/ttyUSB1" }' \
  http://localhost:8080/api/device; echo

curl --header "Content-Type: application/json" \
  --data '{"device": "/dev/ttyUSB0" }' \
  http://localhost:8080/api/device; echo
