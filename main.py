from apscheduler.schedulers.blocking import BlockingScheduler
from crawl import CrawlDmhy


def main():
    scheduler = BlockingScheduler()
    crawl = CrawlDmhy()
    crawl.crawl()
    scheduler.add_job(crawl.crawl, 'cron', minute=15, second=0)
    scheduler.start()


if __name__ == '__main__':
    main()
