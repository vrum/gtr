"""
gtd 1.0: google translate server app
"""

import asyncio
import os
from fastapi import FastAPI
import multiprocessing as mp
from concurrent.futures.process import ProcessPoolExecutor
from google.cloud import translate_v2 as translate

from common import SUPPORTED_LANGUAGES

app = FastAPI()
translate_client = translate.Client()


def do_translate(language: str, text: str):
    # print("do_translate:", os.getpid())
    translation = translate_client.translate(text, target_language=language)
    return {"res": translation["translatedText"]}


@app.get("/translate/{language}")
async def translate(language: str, text: str):
    if language not in SUPPORTED_LANGUAGES or not text:
        return
    return await run_in_process(do_translate, language, text)


async def run_in_process(fn, *args):
    loop = asyncio.get_event_loop()
    # wait and return result
    return await loop.run_in_executor(app.state.executor, fn, *args)


@app.on_event("startup")
async def on_startup():
    app.state.executor = ProcessPoolExecutor()


@app.on_event("shutdown")
async def on_shutdown():
    app.state.executor.shutdown()
