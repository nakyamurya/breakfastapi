from pydantic import BaseModel


class Recipe(BaseModel):
    id: int
    name: str
    total_duration: int
    ingredients: list
    directions: str

    class Config:
        schema_extra = {
            "example": {
                "id": 5490,
                "name": "Tongue and Mustard Sandwiches Recipe",
                "total_duration": 150,
                "ingredients": ["salt", "onion", "mustard", "bread", "beef"],
                "directions": "Rinse beef tongue and place in a large pot. Cover with water and add the salt and chopped onion...",
            }
        }


class RecipeResponse(BaseModel):
    status: int
    recipe: Recipe
