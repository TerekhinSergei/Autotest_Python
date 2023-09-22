from zeep import Client, Settings
import yaml


with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)

settings = Settings(strict=False)
client = Client(wsdl=data['wsdl'], settings=settings)


def check_text(text: str):
    return client.service.checkText(text)[0]['s']