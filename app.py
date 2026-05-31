#!/usr/bin/env python3

import aws_cdk as cdk
from aws_cdk import (
    Stack,
    Duration,
    aws_lambda as lambda_,
    aws_apigateway as apigw,
)
from constructs import Construct


class HelloStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        # Create Lambda
        hello_lambda = lambda_.Function(
            self,
            "HelloLambda",
            runtime=lambda_.Runtime.PYTHON_3_12,
            handler="handler.handler",
            code=lambda_.Code.from_asset("lambdas/hello_lambda"),
            timeout=Duration.seconds(10),
        )

        # Create API Gateway
        apigw.LambdaRestApi(
            self,
            "HelloApi",
            handler=hello_lambda
        )


app = cdk.App()
HelloStack(app, "HelloStack")
app.synth()
