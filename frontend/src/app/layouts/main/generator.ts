import { ICategory, RecipeCategory } from "src/app/models/models";

export const getCategories: ICategory[] = [
    { id: 3, category_id: 3, title: "Easy", imgURL: "./../../assets/salad.svg", category: RecipeCategory.salad },
    { id: 4, category_id: 4, title: "Middle", imgURL: "./../../assets/burger.svg", category: RecipeCategory.burger },
    { id: 5, category_id: 5, title: "Hard", imgURL: "./../../assets/pizza.svg", category: RecipeCategory.italian },
    { id: 6, category_id: 6, title: "Popular", imgURL: "./../../assets/soup.svg", category: RecipeCategory.soup },
    { id: 1, category_id: 1, title: "Other", imgURL: "./../../assets/meat.svg", category: RecipeCategory.meat },
]