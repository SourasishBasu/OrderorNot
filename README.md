# OrderOrNot
> Simple HTTP API that responds "yes/no/maybe"

# Introduction
I have trouble deciding on small matters in my day to day such as whether to order food so I decided to get an API to do it for me. 

I have been learning **AWS**, in particular AWS Lambda and API Gateway Integrations so I created a small python function which responds *"yes / no / maybe"*. This is sent as a reponse when the HTTP API is queried using a `GET` request.

# Prerequisites
- Create an [AWS](https://aws.amazon.com/) account and login.

# Setup

### AWS Lambda
- Go to AWS Console Home Page. Go to Services > Lambda.
- Choose `Create` function.
- For Function name, enter `my-function`. Choose Create function.
- Under Code Source copy the code within `lambda_function.py` in this repository. Click `Deploy` to save changes.

  ![image](https://github.com/SourasishBasu/OrderorNot/assets/89185962/30a5a43c-996b-4aa6-837a-0f01905893f0)

### API Gateway
- Go to Services > API Gateway.
- Choose `Build` under HTTP API.
- Under Integrations, choose `Add Integration > Lambda`. For Lambda function, enter `my-function.`
- For API name, enter `my-http-api`. Choose Next.
  
  ![image](https://github.com/SourasishBasu/OrderorNot/assets/89185962/b913eff1-4b46-4bfb-95b7-fe86b376db52)

- Under route settings select `GET` under Method since we will be making GET requests to receive the responses from the API.
- Let the stage settings be default and choose Next. Choose Create.
- Go to APIs > `my-http-api` > Deploy > Stages and copy the `Invoke URL`.
  
  ![image](https://github.com/SourasishBasu/OrderorNot/assets/89185962/67137a55-cd39-41cb-ae05-ab454f08c198)


## Usage

The API's `Invoke URL` will be used to query our API. Append the URL with the name of the lambda function `my-function` and enter it in a web browser to send a GET request.

### Request

`GET`
```bash
https://abcdef123.execute-api.us-east-2.amazonaws.com/my-function
```
### Response

```bash
yes
```

