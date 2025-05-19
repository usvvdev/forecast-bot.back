# coding: utf-8

### <-- DEPENDIES --> ###

BASE_SETTINGS_DIR = "settings.json"

### <-- FORECASTS QUERIES --> ###

SELECT_FORECAST = "SELECT * FROM api_forecasts WHERE id = %s"
SELECT_PLANNED_FORECASTS = "SELECT * FROM api_planned_forecasts WHERE is_done = 0"
UPDATE_PLANNED_FORECASTS = "UPDATE api_planned_forecasts SET is_done = 1 WHERE id = %s"

### <-- USER QUERIES --> ###

SELECT_USER_IDS = "SELECT * FROM api_user_ids WHERE is_active = 1"
INSERT_USER_ID = "INSERT INTO api_user_ids (user_id, questionnaire_id) VALUES (%s, %s) ON DUPLICATE KEY UPDATE user_id = user_id"
DELETE_USER = "DELETE FROM api_user_ids WHERE user_id = %s"
UPDATE_USER_STATUS = "UPDATE api_user_ids SET is_active = 0 WHERE user_id = %s"

### <-- START MESSAGE TEMPLATE --> ###

START_MESSAGE_TEMPLATE = """
Приветствуем Вас! В данном боте будут присылаться прогнозы от Betify.ru
"""

### <-- FORECAST MESSAGE TEMPLATE --> ###

MESSAGE_TEMPLATE = """
🏆 <b>Новый прогноз</b>
🏟 Вид спорта: <b>{sport_type}</b>
🌟 Событие: <b>{event}</b>
📅 Дата и время: <b>{datetime}</b>

Ставим на: <b>{predicted_event}</b>
Коэффициент: <b>{event_ratio}</b>
Рекомендуемый процент от начального 🏦 банка: <b>{bet_percent}%</b>
"""

### <-- BUTTON OF FORECAST MESSAGES TEMPLATE --> ###

BUTTON_TEMPLATE = "Поставить на {title} {icon}"
BUTTON_ICONS = ("💎", "💥", "🔥", "🌟")

### <-- RABBIT PARAMETRS --> ###

EXCHANGE = "forecast_messages"
EXCHANGE_TYPE = "direct"
ROUTING_KEY = "forecast_message_handler"

### <-- RABBIT FUNCTION DEPENDIES --> ###

RABBIT_FUNCTIONS = ("_connect", "_channel")
