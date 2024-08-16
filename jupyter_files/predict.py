import os
import pickle
import polars as pl
import mlflow
from flask import Flask, request, jsonify


RUN_ID = os.getenv('RUN_ID','eba233b9ace241f99e07c3198dcf86db')

logged_model = f's3://ift-bucket-jafet/mlflow/0/eba233b9ace241f99e07c3198dcf86db/artifacts/model'
# logged_model = f'runs:/{RUN_ID}/model'
model = mlflow.pyfunc.load_model(logged_model)

def prepare_features(valores):
    recibe = pl.from_dict(valores)
    recibe.with_columns([pl.col('L_NO_ESPECIFICADO_E').cast(pl.Int64).fill_null(0),pl.col('L_POSPAGOC_E').cast(pl.Int64).fill_null(0),pl.col('L_PREPAGO_E').cast(pl.Int64).fill_null(0),pl.col('L_TOTAL_E').cast(pl.Int64).fill_null(0)])
    features = recibe.to_dicts()
    return features


def predict(features):
    preds = model.predict(features)
    return float(preds[0])


app = Flask('prediction')


@app.route('/predict', methods=['POST'])
def predict_endpoint():
    valores = request.get_json()

    features = prepare_features(valores)
    pred = predict(features)

    result = {
        'market_share_prediction': pred,
        'model_version': RUN_ID
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)