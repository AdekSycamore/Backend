from pydantic import BaseModel, Field

class Recipe(BaseModel):
    name: str = Field(description="The name of the recipe")
    ingredients: list[str] = Field(description="The list of ingredients for the recipe with quantity and unit")
    instructions: list[str] = Field(description="The list of instructions to make the recipe")
    cooking_time: str = Field(description="The cooking time for the recipe")
    serving_size: str = Field(description="The serving size for the recipe")