from fastapi import Depends, FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from models import Todos

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def index(request: Request, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Todos).order_by(Todos.created_at))
    todos = result.scalars().all()
    return templates.TemplateResponse(request, "base.html", {"todos": todos})


@app.post("/todos")
async def create_todo(
    request: Request,
    content: str = Form(...),
    db: AsyncSession = Depends(get_db),
):
    todo = Todos(content=content)
    db.add(todo)
    await db.commit()
    await db.refresh(todo)
    return templates.TemplateResponse(
        request, "partials/todo_list.html", {"todos": [todo]}
    )


@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: str, db: AsyncSession = Depends(get_db)):
    todo = await db.get(Todos, todo_id)
    if todo:
        await db.delete(todo)
        await db.commit()
    return ""  # empty response — HTMX swaps this in place of the <li>, removing it