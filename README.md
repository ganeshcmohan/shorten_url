# shorten_url
Shorten url is backend API for generating short url developed using flask.

# Installation steps
pip install -r requirements.txt

python3 app.y

# Api Documentation

1.Create Short url


URL    : http://127.0.0.1:5000/api/shortner/create

Method : POST

Payload: 
   
         {
           
            "url": <URL>  ## "https://github.com/ganeshcmohan/shorten_url"
            
          }


2.Getting website url

URL    : http://127.0.0.1:5000/api/shortner/<short-key>

METHOD : GET

RESPONSE :


     {
     
       "long": "https://github.com/ganeshcmohan/shorten_url",
     
       "short": "aHR0cH"
     
     }

