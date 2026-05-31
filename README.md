# AWS CDK Hello Exercise
## Overview
This repository contains a minimal AWS CDK project written in Python.

The purpose of this exercise was to:

- Deploy a simple AWS Lambda function using AWS CDK.
- Understand how CDK synthesizes CloudFormation templates.
- Practice clean infrastructure deployment and teardown.
- Reinforce credential hygiene and cost awareness.

This project is intentionally simple and focused on fundamentals.

## Architecture
The stack defines:

A single AWS Lambda function.
Required IAM permissions managed automatically by CDK.
CDK synthesizes the stack into CloudFormation templates before deployment.

Generated artifacts are stored locally in cdk.out/ and are not committed to this repository.

## Prerequisites
- Python 3.10+
- Node.js (compatible with current AWS CDK version)
- AWS CLI configured
- AWS CDK installed globally
  
Install CDK globally if needed:
`npm install -g aws-cdk`
## Setup

### Create and activate a virtual environment

```bash
python3 -m venv cdk-env
source cdk-env/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

If no requirements file exists, install manually:

```bash
pip install aws-cdk-lib constructs
```

### Synthesize the Stack

Generate the CloudFormation template locally:

```bash
cdk synth
```

This produces output inside:

`cdk.out/`

### Deploy

```bash
cdk deploy
```

### Destroy

```bash
cdk destroy
```

This prevents unintended charges.
