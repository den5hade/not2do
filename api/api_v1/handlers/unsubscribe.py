from datetime import datetime
from fastapi import APIRouter
from fastapi.responses import HTMLResponse


unsubscribe_router = APIRouter()


@unsubscribe_router.get("/{name}", response_class=HTMLResponse)
async def unsubscribe_email(name: str):
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logg_row = f"{name} : {current_date}"
    showen_name = name.split('-')[1:]
    with open('emails.txt', 'a') as file:

        file.write(logg_row + '\n')
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>Unsubscribe Confirmation</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    margin: 0;
                    padding: 20px;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    min-height: 100vh;
                    background-color: #f5f5f5;
                }}
                .container {{
                    background-color: white;
                    padding: 40px;
                    border-radius: 10px;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                    text-align: center;
                    max-width: 600px;
                }}
                h1 {{
                    color: #333;
                    margin-bottom: 20px;
                }}
                p {{
                    color: #666;
                    margin-bottom: 20px;
                }}
                .email {{
                    font-weight: bold;
                    color: #444;
                }}
                .icon {{
                    font-size: 48px;
                    margin-bottom: 20px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="icon">✔️</div>
                <h1>Успешная отписка</h1>
                <p>Адрес <span class="email">{showen_name}</span> был успешно отписан от рассылки.</p>
                <p>Вы больше не будете получать наши уведомления.</p>
            </div>
        </body>
    </html>
    """
    return html_content
