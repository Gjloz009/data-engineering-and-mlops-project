from airflow import DAG
from airflow.decorators import task
from airflow.utils.log.logging_mixin import LoggingMixin
from airflow.models.param import Param
from datetime import datetime
from schemas_tweaks import diccionario_datos
import functions_ift as f

with DAG(
    dag_id="ift_etl",
    dag_display_name="ETL IFT TABLES",
    schedule=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=["ift","etl"],
    params={
        "tabla_lineas": Param(
            "TD_LINEAS_INTMOVIL_ITE_VA",
            type="string",
            title="Name of the table that is going to be used for table lineas",
            description_md = ""
        ),
        "tabla_tdd": Param(
            "TD_TRAF_INTMOVIL_ITE_VA",
            type="string",
            title="Name of the table that is going to be used for data traffic",
            description_md = ""
        ),
        "tabla_ihh": Param(
            "TD_IHH_INTMOVIL_ITE_VA",
            type="string",
            title="Name of the table that is going to be used for concentration flag",
            description_md = ""
        ),
        "tabla_sm": Param(
            "TD_MARKET_SHARE_INTMOVIL_ITE_VA",
            type="string",
            title="Name of the table that is going to be used for market share",
            description_md = ""
        ),
        "bucket": Param(
            "ift-bucket-jafet",
            type="string",
            title="Name of the s3 bucket",
            description_md = ""
        )        
    }
) as dag:

    @task(task_id="Download files")
    def task_1(parametro_name):
        try:
            nombre = parametro_name
            
            prueba = f.download_files(nombre)
        
            LoggingMixin().log.info("Download process in time")

            return prueba.to_dict(as_series=False)

        except Exception as e:
            LoggingMixin().log.error(f"Error in task_1: {str(e)}")
            raise


    @task(task_id="Transformations")
    def task_2(task_1_result,parametro_name):
        try:
            task_transformed = f.dict_to_df(task_1_result)

            prueba_tweaked = f.tweak_df(task_transformed,diccionario_datos[parametro_name]['tweak_columns'],diccionario_datos[parametro_name]['schema'])
    
            LoggingMixin().log.info("Transformation of DataTypes in time")
    
            return prueba_tweaked.to_dict(as_series=False)
   
        except Exception as e:
            LoggingMixin().log.error(f"Error in task_2: {str(e)}")
            raise


    @task(task_id="Upload files")
    def task_3(task_2_result,parametro_name,bucket_name):
        try:
            task_transformed_2 = f.dict_to_df(task_2_result)

            LoggingMixin().log.info("Loading of file in time")
            
            f.upload_df(task_transformed_2,bucket_name,parametro_name)
        
        except Exception as e:
            LoggingMixin().log.error(f"Error in task_3: {str(e)}")
            raise 

    primer_paso = [
        task_1(dag.params['tabla_lineas']),
        task_1(dag.params['tabla_tdd']),
        task_1(dag.params['tabla_ihh']),
        task_1(dag.params['tabla_sm'])]

    segundo_paso = [
        task_2(primer_paso[0],dag.params['tabla_lineas']),
        task_2(primer_paso[1],dag.params['tabla_tdd']),
        task_2(primer_paso[2],dag.params['tabla_ihh']),
        task_2(primer_paso[3],dag.params['tabla_sm']),]
        
    tercer_paso = [
        task_3(segundo_paso[0],dag.params['tabla_lineas'],dag.params['bucket']),
        task_3(segundo_paso[1],dag.params['tabla_tdd'],dag.params['bucket']),
        task_3(segundo_paso[2],dag.params['tabla_ihh'],dag.params['bucket']),
        task_3(segundo_paso[3],dag.params['tabla_sm'],dag.params['bucket'])]