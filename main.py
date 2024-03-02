from fastapi import FastAPI
import os
import cProfile

PROFILING = os.getenv('PROFILE_APP') == 'true'

app = FastAPI()

if PROFILING:
    profiler = cProfile.Profile()

def compute_sum(n: int) -> int:
    return sum(range(1, n + 1))

@app.get("/sum/{n}")
async def read_sum(n: int):
    result = compute_sum(n)
    return {"n": n, "sum": result}

@app.on_event("startup")
async def start_profiler():
    print("Starting up...")
    if PROFILING:
        global profiler
        profiler.enable()
        print("Profiler enabled")

@app.on_event("shutdown")
async def stop_profiler_and_dump_stats():
    print("Shutting down...")
    global profiler
    profiler.disable()
    print("Profiler disabled, dumping stats...")
    profiler.dump_stats("/app/profiling_results/profiling_results.prof")


