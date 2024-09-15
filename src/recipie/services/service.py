import uuid
from src.recipie.model.model import Recipe


class RecipeService:
    @staticmethod
    def create(recipe,current_user,db):
        print(recipe)
        recipe.id = uuid.uuid4()
        new_recipe = Recipe(
            id = recipe.id,
        title=recipe.title,
        description=recipe.description,
        ingredients=recipe.ingredients,
        category=recipe.category,
        # image=recipe.image,
        user_id=current_user.id  # Assuming current_user has the user id
    )
        print("new_recipe")
        db.add(new_recipe)
        db.commit()
        db.refresh(new_recipe)
        return new_recipe