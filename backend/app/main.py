from fastapi import FastAPI

app = FastAPI(title="Issue Tracker API")


@app.get("/health")
def health() -> dict[str, str]:
    """Simple check that the server is up."""
    return {"status": "ok"}
