from instapy import InstaPy

session = InstaPy(username="<your username>", password="<your password>").login()
# session without open browser
# session = InstaPy(username="<your username>", password="<your password>", headless_browser=True)

session.login()

session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)

session.like_by_tags(["bmw", "mersedes"], amount=5)
session.set_dont_like(["naked", "nsfw"])
session.set_do_follow(True, percentage=50)
session.set_do_comment(True, percentage=50)
session.set_comments(["Nice!", "Sweet!", "Beautiful :heart_eyes:"])
session.end()
