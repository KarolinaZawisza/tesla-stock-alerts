import datetime as dt


class DateManager:

    @staticmethod
    def get_today_date_format_ymd():
        return dt.datetime.now().strftime('%Y-%m-%d')

    @staticmethod
    def get_today_date_format_dmy():
        return dt.datetime.now().strftime('%d.%m.%Y')
