# pln_api

### how to use: 
  * install the [Docker](https://docs.docker.com/compose/install/)
  * Be sure to leave the door open
  * Run docker command in project root
    ```bash
      docker-compose up --build
    ``` 
  * Sua API será executado em http://127.0.0.1:8090
  * API documentation http://127.0.0.1:809/docs

## API
### Accuracy
* Endpoint: http://localhost:809/accuracy
* HTTP Method: POST
* HTTP Success Response Code: CREATED (200)
  * Request payload
    ```json
        {
        "message": "Feedback"
        }

  * Response payload
    ```json
        {
          {
          "accuracy": 0.45894283056259155,
          "message": "Feedback"
          }
        }
