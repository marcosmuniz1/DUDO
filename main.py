# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from game import Game
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()
game = Game()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def root():
    return FileResponse("static/index.html")


class BidInput(BaseModel):
    fv: int
    m: int

@app.post("/new")
def new_game():
    game.__init__()
    game.start_round()
    return {
        "round": game.rnum,
        "your_dice": game.d1,
        "remaining_dices": game.remaining_dices
    }

@app.post("/bid")
def place_bid(bid: BidInput):
    result = game.player_bid(bid.fv, bid.m)
    return result

@app.post("/challenge")
def challenge():
    return game.player_challenge()

@app.post("/next-round")
def next_round():
    if game.is_over():
        winner = 2 if game.remaining_dices[1] == 0 else 1
        return {"game_over": True, "winner": winner}
    game.start_round()
    return {
        "round": game.rnum,
        "your_dice": game.d1,
        "remaining_dices": game.remaining_dices
    }