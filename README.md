# Instituto Federal de Telecomunicaciones (IFT) Federal Institute of Telecom

<p align="center">
  <img src="images\ift_pict.png">
</p>

---

<p align="justify">
The Federal Telecommunications Institute (IFT) is an autonomous agency of the Mexican government responsible for regulating and promoting competition and efficient development of telecommunications and broadcasting in Mexico.
</p>

---
## Index
- 1.[Objective](#1-objective)
- 2.[Technologies](#2-technologies)
  - 2.1.[Alternative A - One host machine.](#21-alternative-a---one-host-machine)
  - 2.2.[Alternative B - User plus server machine.](#22-alternative-b---user-machine-plus-server-machine)
- 3.[Data Architecture](#3-data-architecture)
- 4.[Data description](#4-data-description)
- 6.[Instructions on how to replicate the project](#6-instructions-on-how-to-replicate-the-project)
  - 6.1.[Setting up Google Cloud Platform account](#61-setting-up-google-cloud-platform-account)
  - 6.2.[Creating a VM Instance on Google Compute Engine](#62-creating-a-vm-instance-on-google-compute-engine)
  - 6.3.[VM instance connection configuration](#63-vm-instance-connection-configuration)
  - 6.4.[Setting up VM instance](#64-setting-up-vm-instance)
- 7.[Alternative A - Local](#7-alternative-a---local)
  - 7.1.[Creating a docker-compose](#71-creating-a-docker-compose)
  - 7.2.[Running a docker-compose](#72-running-a-docker-compose)
  - 7.3.[Port Forwarding](#73-port-forwarding)
  - 7.4.[Testing the pipeline](#74-testing-the-pipeline)
  - 7.5.[Orchestrating with prefect](#75-orchestrating-with-prefect)
- 8.[Alternative B - Cloud](#8-alternative-b---cloud)
  - 8.1.[Creating service account](#81-creating-service-account)
  - 8.2.[Edit Permissions](#82-edit-permissions)
  - 8.3.[Installing Terraform](#83-installing-terraform)
  - 8.4.[Setting up Terraform files](#84-setting-up-terraform-files)
  - 8.5.[Orchestrating with prefect](#85-orchestrating-with-prefect)
  - 8.6.[Deployment with prefect](#86-deployment-with-prefect)
  - 8.7.[Running Prefect flows on docker containers](#87-running-prefect-flows-on-docker-containers)
  - 8.8.[Dbt](#88-dbt)
  - 8.9.[Looker Studio](#89-looker-studio)
- 9.[Future enhancements ](#9-future-enhancements)
- 10.[References](#10-references)
---

## 1. Objective
<p align="justify">
This project aims to create a Machine Learning Operations environment for processing and analyzing data from the Federal Telecommunications Institute of México. this environment also consider the ingestion and pre-processing of the information
</p>

You can take a look of the information about ift and the source of the files 
Source (Spanish):

> https://bit.ift.org.mx/BitWebApp/descargaDatos.xhtml
> https://www.ift.org.mx/

## 2. Technologies
For setting up the VM Instance or Local Machine please install these tools:

- Miniconda environment (Python=3.13)
- Docker
- Docker-compose
- AWS CLI
- Terraform

After installed Miniconda environment please install the requirements file 

### 2.1 Alternative A - One host machine

- <p align="justify">
  <b>Docker-compose</b> : for creating the airflow docker image, mlflow docker image and rdbms system (postgress) docker image.
  </p>

- <p align="justify">
  <b>Airflow</b>: is an open-source orchestration tool, which allows you to define, schedule and monitor your data pipelines.
  </p>

- <p align="justify">
  <b>Mlflow</b>:is an open-source framework designed to manage the entire machine learning lifecycle.
  </p>
  
- <p align="justify">
  <b>Terraform</b>:  is an open-source infrastructure-as-code software tool. Users define and provide data center infrastructure using a declarative configuration language known as HashiCorp Configuration Language, or optionally JSON.
  </p>

- <p align="justify">
  <b>Jupyter</b>:  is an open-source project that provides an interactive computing environment.
  </p>

- <p align="justify">
  <b>Polars</b>:  is a data manipulation library.
  </p>

- <p align="justify">
  <b>Sci-kit Learn</b>:  is a machine learning library.
  </p>
  
- <p align="justify">
  <b>s3fs</b>:  Library that provides a filesystem interface to Amazon S3.
  </p>
  
- <b>Amazon Web Service</b>:

  -	S3
    
- <p align="justify">
  <b>Looker Studio</b>: a free tool that turns your data into informative, easy to read, easy to share, and fully customizable dashboards and reports.
  </p>

### 2.2 Alternative B - user machine plus server machine 

- <p align="justify">
  <b>Docker-compose</b> : for creating the airflow docker image, mlflow docker image and rdbms system (postgress) docker image.
  </p>

- <p align="justify">
  <b>Airflow</b>: is an open-source orchestration tool, which allows you to define, schedule and monitor your data pipelines.
  </p>

- <p align="justify">
  <b>Mlflow</b>:is an open-source framework designed to manage the entire machine learning lifecycle.
  </p>
  
- <p align="justify">
  <b>Terraform</b>:  is an open-source infrastructure-as-code software tool. Users define and provide data center infrastructure using a declarative configuration language known as HashiCorp Configuration Language, or optionally JSON.
  </p>

- <p align="justify">
  <b>Jupyter</b>:  is an open-source project that provides an interactive computing environment.
  </p>

- <p align="justify">
  <b>Polars</b>:  is a data manipulation library.
  </p>

- <p align="justify">
  <b>Sci-kit Learn</b>:  is a machine learning library.
  </p>
  
- <p align="justify">
  <b>s3fs</b>:  Library that provides a filesystem interface to Amazon S3.
  </p>
  
- <b>Amazon Web Service</b>:

  -	S3
    
- <p align="justify">
  <b>Looker Studio</b>: a free tool that turns your data into informative, easy to read, easy to share, and fully customizable dashboards and reports.
  </p>
  
## 3. Data Architecture
Alternative A
<p align="center">
  <img src="images\diagram_v2.svg">
</p>

Alternative B
<p align="center">
  <img src="images\diagram_v3.svg">
</p>

## 4. Data description

<p align="justify">
The source of information is public, that means everyone has acces to this information. Also, this data is provided by the open data platform of IFT. 
</p>

<p align="justify">
 This information si provided in csv format, also I provide a google sheets document where is the original schema structure and data description of the tables. This information is uploaded monthly.
</p>

> https://docs.google.com/spreadsheets/d/176qSChhhpF43hzslsFscsAcBblJ0Wa_cyBHnzWTq1Eg/edit?usp=sharing

<b>Tables:</b>

- Lineas
- Tráfico de datos
- Indice de concentración
- Participacion de mercado

## 6. Instructions on how to replicate the project
### 6.1. Setting up alternative A
For this option need a host machine with Linux included, I used Debian distribution but is not necesary. You can use a virtual machine or your own computer, a good option if you don´t have a linux distribution instance yoou can use github codespace.

#### 6.1.1 Setting up instance.
Install the listed tools in your instance:

- Miniconda environment
- Docker
- Docker-Compose
- terraform
- git
- AWS
If you want steps for installing those tools, please check [`here`](./machine_configuration.md).

#### 6.1.2 Creating fyle system.

After finished point [6.1.1 Setting up instance.](#-setting-up-instance). Please copy this repository in a folder.

#### 6.1.3 Creating AWS S3 Bucket.
Inside of directory aws_infrastructure resides the tf files that allows to create a simple s3 bucket with standard configuration.
In order to run configuration you need to have your AWS credentials as environment variables after you have your credentials you can use the next command inside the directory /aws_infrastructure to initializate terraform and the setup of AWS. You can modify the variables.tf files if you want to change the bucket name and the region. 

```
terraform init 
```

Use the next command to create the AWS infrastructure with terraform.

```
terraform apply
```

You can always check if your bucket has beeen created using AWS cli. 

```
aws s3 ls
```

#### 6.1.3 Creating services with docker-compose

Inside of directory airflow_mlflow_files please create a .env file with these variables and fill then with your own choises. Be carefull the name you use in the POSTGRESS_DB variable because it is going to be the db used for airflow so maybe is better to leave it just like this but is up to you. The AIRFLOW_UID is only your user id you can see it using the command id -u. Also create these directories if they dont exists.

```
mkdir -p ./dags ./logs ./plugins ./config
```

```
AIRFLOW_UID=1001
POSTGRES_USER="user"
POSTGRES_PASSWORD="password"
POSTGRES_DB="airflow"
_AIRFLOW_WWW_USER_USERNAME="user"
_AIRFLOW_WWW_USER_PASSWORD="user"
BUCKET="s3://your_bucket_name/mlflow/"
```

Inside of directory airflow_mlflow_files resides a yaml file that have the configurations to install the images of airflow, mlflow and postgress. Please check if you´re inside the /airflow_mlflow_files directory and run the next command.

```
docker-compose up --build
```

Feel free to not use the --build command this is only to see the logs of the services.

You can check if the containers are up using 

```
docker ps
```
