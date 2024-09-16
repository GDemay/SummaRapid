# QuickSummarizer API

QuickSummarizer is a fast and efficient text summarization API that harnesses the power of cutting-edge NLP models to instantly condense lengthy content into concise summaries, all through an easy-to-use API powered by FastAPI. This is the API project, and it's designed to work alongside the ReactJS frontend available at [https://github.com/GDemay/SummaRapid-React](https://github.com/GDemay/SummaRapid-React). The application can be accessed at [https://www.quicksummarizer.com](https://www.quicksummarizer.com/).

## Installation

To get started, you will need to have Python 3.10 installed. You also need to install the necessary dependencies using [Poetry](https://python-poetry.org/):

```
poetry install
```

### Environment Variables

You will need to create a `.env` file at the root of the project with the following environment variables:

```
OPENAI_API_KEY="XXXX"
RECAPTCHA_SECRET_KEY="XXXX"
ENVIRONMENT="local" #
```

Replace "XXXX" with the appropriate values:

* `OPENAI_API_KEY`: Obtain an API key from [OpenAI](https://beta.openai.com/signup/).
* `RECAPTCHA_SECRET_KEY`: Obtain a reCAPTCHA secret key from the [Google reCAPTCHA admin console](https://www.google.com/recaptcha/admin/create).

For deployment to AWS Lambda, set the `ENVIRONMENT` variable to "production" within the Lambda function.

## Running the Application

To run the application locally, execute the following command:

```
make run
```

## Building and Deploying to AWS Lambda

You will need the [AWS SAM CLI](https://aws.amazon.com/serverless/sam/) installed to build and deploy the application to AWS Lambda.

1. Build the application:

```
make build-run
```

2. Deploy the application to AWS Lambda:

```
make build-deploy
```

The `template.yaml` file is used for deploying the API to AWS Lambda using the AWS SAM CLI. It contains the necessary configurations, including environment variable handling and resource allocation.

## API Usage

The main endpoint for text summarization is:

```
POST /summarize
```

Parameters:

* `text_to_summarize` (str): The input text to be summarized.
* `captcha` (str): The reCAPTCHA response provided from the [ReactJS app](https://github.com/GDemay/SummaRapid-React).

Response:

```
{
  "summarized_content": "This is a summarized text."
}
```

## Contributing

Please submit issues and pull requests for bug fixes, features, and improvements. Contributions are welcome and will be reviewed and incorporated as appropriate.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
