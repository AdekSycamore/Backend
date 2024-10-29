from fastapi import HTTPException, Body, APIRouter

from server.ai import prompt, model, parser
from server.models.recipe import Recipe

router = APIRouter()

@router.post('/generate_recipe', response_model=Recipe)
def generate_recipe(ingredients: str = Body(...), cuisine_type: str = Body(...)):
    print(type(ingredients), cuisine_type)
    try:
        # Invoke the chain
        chain = prompt | model | parser
        print(chain)
        response = chain.invoke({"ingredients": ingredients, "cuisine_type": cuisine_type})
        print(response)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate recipe: {str(e)}")