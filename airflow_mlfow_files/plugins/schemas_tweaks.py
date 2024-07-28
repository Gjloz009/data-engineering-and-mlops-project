import polars as pl
diccionario_datos = {
    "TD_LINEAS_INTMOVIL_ITE_VA":{
        "schema":{
            "FECHA": pl.Date,
            "ANIO": pl.Int16,
            "MES": pl.Int8,
            # "K_GRUPO": pl.Categorical,
            #"GRUPO": pl.Categorical,
            #"K_EMPRESA": pl.Categorical,
            #"EMPRESA": pl.Categorical,
            #"CONCESIONARIO": pl.Categorical,
            "L_PREPAGO_E": pl.Int32,
            "L_POSPAGO_E": pl.Int32,
            "L_POSPAGOC_E": pl.Int32,
            "L_POSPAGOL_E": pl.Int32,
            "L_NO_ESPECIFICADO_E": pl.Int64,
            "L_TOTAL_E": pl.Int32,
            #"FOLIO": pl.Categorical
          },
         "tweak_columns":[
            #pl.col( "L_PREPAGO_E" ).str.replace_all(",","").str.to_integer(base=10),
            #pl.col( "L_POSPAGO_E" ).str.replace_all(",","").str.to_integer(base=10),
            #pl.col( "L_POSPAGOC_E" ).str.replace_all(",","").str.to_integer(base=10),
            #pl.col( "L_POSPAGOL_E" ).str.replace_all(",","").str.to_integer(base=10),
            #pl.col( "L_NO_ESPECIFICADO_E" ).str.replace_all(",","").str.to_integer(base=10),
            #pl.col( "L_TOTAL_E" ).str.replace_all(",","").str.to_integer(base=10),
            pl.col("FECHA").str.to_date("%d/%m/%Y"),
            pl.col("FOLIO").cast(pl.Int32)
          ]
    },
    "TD_TRAF_INTMOVIL_ITE_VA":{
        "schema":{
            "ANIO":pl.Int16,
            "MES":pl.Int8,
            "FECHA":pl.Date,
            #"FOLIO":pl.Categorical,
            ## "K_GRUPO":pl.Categorical,
            #"GRUPO":pl.Categorical,
            #"K_EMPRESA":pl.Categorical,
            #"EMPRESA":pl.Categorical,
            #"CONCESIONARIO":pl.Categorical,
            "TRAF_TB_2G_E":pl.Float32,
            "TRAF_TB_3G_E":pl.Float32,
            "TRAF_TB_4G_E":pl.Float32,
            "TRAF_TB_NO_ESPECIFICADO_E":pl.Float32,
            "TRAF_TB_E":pl.Float32
        },
        "tweak_columns":[
            #pl.col('TRAF_TB_2G_E').cast(pl.Float32),
            #pl.col('TRAF_TB_3G_E').str.replace_all(",","").cast(pl.Float32),
            #pl.col('TRAF_TB_4G_E').str.replace_all(",","").cast(pl.Float32),
            #pl.col('TRAF_TB_NO_ESPECIFICADO_E').str.replace_all(",","").cast(pl.Float32),
            #pl.col('TRAF_TB_E').str.replace_all(",","").cast(pl.Float32),
            pl.col('FOLIO').cast(pl.Int32),
            pl.col("FECHA").str.to_date("%d/%m/%Y")
            #pl.coalesce(pl.col('FECHA').str.to_date(format="%d%b%Y",strict=False),pl.col('FECHA').str.to_date(format="%d-%b-%y",strict=False))
            ]
    },
    "TD_IHH_INTMOVIL_ITE_VA":{
        "schema":{
            "ANIO":pl.Int16,
            "MES":pl.Int8,
            "IHH_INTMOVIL_E":pl.Int16
        },
        "tweak_columns": [
            pl.col('IHH_INTMOVIL_E').str.replace_all(",",""),
            pl.col("FECHA").str.to_date("%d/%m/%Y")
        ]
    },
    "TD_MARKET_SHARE_INTMOVIL_ITE_VA":{
        "schema": {
            "ANIO":pl.Int16,
            "MES":pl.Int8,
            # "K_GRUPO":pl.Categorical,
            #"GRUPO":pl.Categorical
        },
        "tweak_columns":[
            pl.col('MARKET_SHARE').str.replace_all("%","").cast(pl.Float32),
            pl.col('FECHA').str.to_date(format="%d/%m/%Y")
        ]

    }
}