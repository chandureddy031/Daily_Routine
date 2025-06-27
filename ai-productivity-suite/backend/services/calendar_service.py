from caldav import DAVClient
from utils.config import Config

def create_event(summary, start, end, description=""):
    config = Config()
    with DAVClient(
        url=config.CALDAV_URL,
        username=config.CALDAV_USER,
        password=config.CALDAV_PASSWORD
    ) as client:
        principal = client.principal()
        calendar = principal.calendars()[0]
        return calendar.save_event(
            dtstart=start,
            dtend=end,
            summary=summary,
            description=description
        )