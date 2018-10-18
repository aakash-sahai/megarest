curl --header "Content-Type: application/json" \
  --data '{"number": "1" }' \
  http://localhost:8080/api/stepper; echo

curl --header "Content-Type: application/json" \
  --data '{"number": "10" }' \
  http://localhost:8080/api/stepper; echo

curl --header "Content-Type: application/json" \
  http://localhost:8080/api/stepper/stpr1; echo

curl --header "Content-Type: application/json" \
  http://localhost:8080/api/stepper/stpr1/rpm; echo

curl --header "Content-Type: application/json" \
    http://localhost:8080/api/stepper/stpr1/rpm/100; echo

curl --header "Content-Type: application/json" \
  http://localhost:8080/api/stepper/stpr1/microsteps; echo

curl --header "Content-Type: application/json" \
    http://localhost:8080/api/stepper/stpr1/microsteps/16; echo

curl --header "Content-Type: application/json" \
  http://localhost:8080/api/stepper/stpr1/dir; echo

curl --header "Content-Type: application/json" \
    http://localhost:8080/api/stepper/stpr1/dir/0; echo

curl --header "Content-Type: application/json" \
  http://localhost:8080/api/stepper/stpr1/stepsperrev; echo

curl --header "Content-Type: application/json" \
    http://localhost:8080/api/stepper/stpr1/stepsperrev/100; echo

curl --header "Content-Type: application/json" \
  http://localhost:8080/api/stepper/stpr1/stepsremaining; echo

curl --header "Content-Type: application/json" \
  http://localhost:8080/api/stepper/stpr1/disable; echo

curl --header "Content-Type: application/json" \
  http://localhost:8080/api/stepper/stpr1/enable; echo

curl --header "Content-Type: application/json" \
  http://localhost:8080/api/stepper/stpr1/stop; echo

curl --header "Content-Type: application/json" \
    http://localhost:8080/api/stepper/stpr1/rotate; echo

curl --header "Content-Type: application/json" \
    http://localhost:8080/api/stepper/stpr1/rotate/240; echo

curl --header "Content-Type: application/json" \
    http://localhost:8080/api/stepper/stpr1/step; echo

curl --header "Content-Type: application/json" \
    http://localhost:8080/api/stepper/stpr1/step/1000; echo

curl --header "Content-Type: application/json" \
  http://localhost:8080/api/stepper/stpr1/junk; echo

curl --header "Content-Type: application/json" \
  http://localhost:8080/api/stepper/stpr2; echo
