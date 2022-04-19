from deta import app


@app.lib.cron()
def cron_job(event):
    return "Hello, cron!"
