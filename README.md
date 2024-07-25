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
  - 2.1.[Alternative A - Only one host machine.](#21-alternative-a---Only-one-host-machine)
  - 2.2.[Alternative B - User plus server machine.](#22-alternative-b---user-machine-plus-server-machine)
- 3.[Data Architecture](#3-data-architecture)
- 5.[Data description](#5-data-description)
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

### 2.1 Alternative A - Only one host machine

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

<p align="center">
  <img src="images\diagram_v2.svg">
</p>

<p align="center">
  <img src="images\diagram_v3.svg">
</p>
