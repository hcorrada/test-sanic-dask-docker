from epivizfileserver import setup_app, MeasurementManager

mgr = MeasurementManager()
app = setup_app(mgr)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)