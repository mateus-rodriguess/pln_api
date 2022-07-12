# pln_api

### Como usar: 
  * Rodar comando docker
    ```bash
      docker-compose up --build
    ``` 
  * Sua API será executado em http://127.0.0.1:8090
  * Documentação da API http://127.0.0.1:8090/docs

## API
### Accuracy
* Endpoint: http://localhost:8090/accuracy
* HTTP Method: POST
* HTTP Success Response Code: CREATED (200)
  * Request payload
    ```json
        {
          "message": "I hate you",
          "save": false,
          "translate": false
        }
  * Response payload
    ```json
        {
          {
          "accuracy": 0.45894283056259155,
          "message": "Feedback"
          }
        }
