import uvicorn
from fastapi import FastAPI
from typing import Union

from db.database import fetch_random_recipe, fetch_recipe_by_id
from models.recipe import Recipe, RecipeResponse
from models.error import NotFoundResponse


app = FastAPI()


@app.get("/", response_model=RecipeResponse, responses={200: {"model": RecipeResponse}})
def get_recipes() -> dict:
    """
    This function returns a random recipe from the database.
    ---
    Args: None
    Returns:
        dict: A dictionary containing status code and recipe. 
    """
    recipe: Recipe = fetch_random_recipe()
    return {"status": 200, "recipe": recipe}


@app.get("/{id}",
    response_model=Union[RecipeResponse, NotFoundResponse],
    responses={200: {"model": RecipeResponse}, 404: {"model": NotFoundResponse}},
)
def get_recipe_by_id(id: int) -> dict:
    """
    This function returns a recipe from the database by id.
    ---
    Args:
        id (int): id of the recipe passed as a path parameter.
    Returns:
        dict: A dictionary containing status code and a recipe.
    """
    recipe: Recipe = fetch_recipe_by_id(id)
    if recipe is not None:
        return {"status": 200, "recipe": recipe}
    return {"status": 404, "message": "recipe not found"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
