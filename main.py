from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.toast.kivytoast.kivytoast import toast
from kivy.lang.builder import Builder
import os
from scrape import Scraper


class MainWindow(MDScreen):
    def scrapeImages(self, text):
        if "fandom.com" not in self.ids.linkinput.text:
            toast("Invalid URL")
        else:
            toast("Scraping...")
            Scraper(self.ids.linkinput.text)
            toast("Finished Scraping!")


class WikiaScraper(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.root_widget = Builder.load_file("wikiascraper.kv")

    def on_start(self):
        try:
            os.mkdir("Saved Images")
        except:
            pass


if __name__ == '__main__':
    WikiaScraper().run()
