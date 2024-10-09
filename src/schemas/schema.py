from datetime import datetime

from pydantic import BaseModel, Field


class DailyWeather(BaseModel):
    """Daily weather data model"""

    date: datetime = Field(default=None)
    temperature_2m_max: float = Field(default=None)
    temperature_2m_min: float = Field(default=None)
    precipitation_sum: float = Field(default=None)
    wind_speed_10m_max: float = Field(default=None)

    def __str__(self) -> str:
        return (
            f'ПОГОДА В МОСКВЕ на {self.date.date()} \n'
            f'Макс.темп: {round(self.temperature_2m_max,1)}°C\n'
            f'Мин.темп: {round(self.temperature_2m_min)}°C\n'
            f'Осадки: {round(self.precipitation_sum)} \n'
            f'Ветер: {round(self.wind_speed_10m_max)} м/с'
        )
