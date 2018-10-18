curl --header "Content-Type: application/json" \
  --data '{"pin": "20" }' \
  http://localhost:8080/api/pushbutton; echo

curl --header "Content-Type: application/json" \
  http://localhost:8080/api/pushbutton/pb20; echo

curl --header "Content-Type: application/json" \
  http://localhost:8080/api/pushbutton/pb20/state; echo

curl --header "Content-Type: application/json" \
  http://localhost:8080/api/pushbutton/pb20/pin; echo

curl --header "Content-Type: application/json" \
  http://localhost:8080/api/pushbutton/pb20/clicks; echo

curl --header "Content-Type: application/json" \
  http://localhost:8080/api/pushbutton/pb20/enable; echo

curl --header "Content-Type: application/json" \
  http://localhost:8080/api/pushbutton/pb20/disable; echo

curl --header "Content-Type: application/json" \
  http://localhost:8080/api/pushbutton/pb20/reset; echo

curl --header "Content-Type: application/json" \
  http://localhost:8080/api/pushbutton/pb20/junk; echo

curl --header "Content-Type: application/json" \
  http://localhost:8080/api/pushbutton/pb0; echo

